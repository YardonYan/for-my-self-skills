#!/usr/bin/env node
/* Folder-level claim extraction, per-doc profiling, and cross-folder overlap scoring. */
const fs = require('fs');
const path = require('path');

function die(msg) { console.log('ERROR: ' + msg); process.exit(1); }

const EXT = new Set(['.md', '.markdown', '.mdx', '.txt', '.rst']);

function walk(dir, base, out) {
  let ents;
  try { ents = fs.readdirSync(dir, { withFileTypes: true }); }
  catch (e) { die('cannot read dir: ' + dir + ' (' + e.message + ')'); }
  ents.sort((a, b) => a.name.localeCompare(b.name, 'zh'));
  for (const ent of ents) {
    const full = path.join(dir, ent.name);
    if (ent.isDirectory()) {
      if (/^(\.|node_modules|dist|build)$/.test(ent.name)) continue;
      walk(full, base, out);
    } else if (ent.isFile()) {
      if (!EXT.has(path.extname(ent.name).toLowerCase())) continue;
      if (/(^|\.)(README|CHANGELOG|LICENSE|CONTRIBUTING)$/i.test(path.basename(ent.name, path.extname(ent.name)))) continue;
      out.push({ abs: full, rel: path.relative(base, full).split(path.sep).join('/') });
    }
  }
  return out;
}

function listDocs(target, tag) {
  const abs = path.resolve(target);
  if (!fs.existsSync(abs)) die('path not found: ' + abs);
  if (fs.statSync(abs).isFile()) return [{ abs, rel: path.basename(abs) }];
  const found = walk(abs, abs, []);
  if (!found.length) {
    const all = [];
    (function collect(dir) {
      let ents;
      try { ents = fs.readdirSync(dir, { withFileTypes: true }); } catch (e) { return; }
      ents.forEach(ent => {
        const full = path.join(dir, ent.name);
        if (ent.isDirectory()) { if (!/^(\.|node_modules|dist|build)$/.test(ent.name)) collect(full); }
        else if (ent.isFile()) all.push(path.relative(abs, full).split(path.sep).join('/'));
      });
    })(abs);
    const byExt = {};
    all.forEach(f => {
      const e = path.extname(f).toLowerCase() || '(no ext)';
      byExt[e] = (byExt[e] || 0) + 1;
    });
    const summary = Object.entries(byExt).map(([e, n]) => e + ' x' + n).join(', ');
    die('no readable docs under: ' + abs
      + '\nFound ' + all.length + ' file(s) but none are markdown/text: ' + (summary || 'empty dir')
      + '\nSupported: ' + [...EXT].join(', ')
      + '\nIf these are .docx/.pdf/.xlsx, convert them to markdown first (e.g. pandoc -t gfm) or extract the text, then re-run. Do NOT summarize them by reading the binaries.');
  }
  return found;
}

function parse(raw) {
  const lines = raw.split('\n');
  const out = [];
  const stack = [];
  let inCode = false, inFm = false, ord = 0;
  if (lines[0] === '---') inFm = true;
  for (let i = 0; i < lines.length; i++) {
    const line = lines[i];
    if (inFm) { if (line === '---' && i > 0) inFm = false; continue; }
    if (/^\s*(```|~~~)/.test(line)) { inCode = !inCode; continue; }
    if (inCode) continue;
    const h = line.match(/^(#{1,6})\s+(.*)$/);
    if (h) {
      const level = h[1].length;
      stack.length = level - 1;
      stack[level - 1] = h[2].trim();
      continue;
    }
    let text = null, kind = 'p';
    const li = line.match(/^(\s*)([-*+]|\d+[.)])\s+(.+)$/);
    const tr = line.match(/^\s*\|(.+)\|\s*$/);
    const bq = line.match(/^\s*>\s?(.+)$/);
    if (li) { kind = 'li'; text = li[3]; }
    else if (tr) {
      if (/^[\s|:-]+$/.test(tr[1])) continue;
      kind = 'row'; text = tr[1];
    }
    else if (bq) { kind = 'quote'; text = bq[1]; }
    else if (line.trim() === '' || /^\s*([-*_]\s*){3,}$/.test(line)) continue;
    else text = line;
    if (!text) continue;
    text = text.replace(/`/g, '').replace(/\*\*/g, '').replace(/\s+/g, ' ').trim();
    if (!text) continue;
    ord++;
    out.push({ id: ord, line: i + 1, kind, section: stack.filter(Boolean).join(' > ') || '(top)', text });
  }
  return out;
}

function readDoc(file, tag) {
  const raw = fs.readFileSync(file.abs, 'utf8').replace(/\r\n/g, '\n');
  return { tag, file: file.abs, rel: file.rel, name: path.basename(file.abs), raw, claims: parse(raw) };
}

function cid(doc, c) { return doc.tag + '/' + (c._rel || doc.rel) + ':' + c.id; }

const STOP = new Set(('a an the and or of to in for on with by is are be this that it as at from if then else using use used not no all any each must should can will would its'.split(' ')));

function tokens(text) {
  const set = new Set();
  const low = text.toLowerCase();
  (low.match(/[a-z0-9_][a-z0-9_.\/\-]{1,}/g) || []).forEach(w => { if (!STOP.has(w)) set.add(w); });
  const cjk = low.match(/[㐀-鿿぀-ヿ]+/g) || [];
  cjk.forEach(run => { for (let i = 0; i + 1 < run.length; i++) set.add(run.slice(i, i + 2)); });
  return set;
}

function bySection(doc) {
  const map = new Map();
  doc.claims.forEach(c => {
    if (!map.has(c.section)) map.set(c.section, { section: c.section, ids: [], toks: new Set(), chars: 0 });
    const s = map.get(c.section);
    s.ids.push(cid(doc, c));
    tokens(c.text).forEach(t => s.toks.add(t));
    s.chars += c.text.length;
  });
  return [...map.values()];
}

function score(a, b) {
  let inter = 0;
  a.toks.forEach(t => { if (b.toks.has(t)) inter++; });
  const denom = Math.min(a.toks.size, b.toks.size) || 1;
  return inter / denom;
}

function loadFolder(target, tag) {
  const files = listDocs(target, tag);
  if (!files.length) die('no readable docs under: ' + path.resolve(target));
  return files.map(f => readDoc(f, tag));
}

const TOPICS = [
  ['architecture / layering', /architecture|layering|dependenc/i, /架构|分层|落位|依赖方向|模块划分|组件划分/],
  ['domain terms', /domain|ubiquitous|glossary/i, /术语|领域模型|名词/],
  ['data ownership', /ownership|authoritative|source of truth/i, /所有权|权威|主数据|数据源/],
  ['consistency & idempotency', /consistency|idempot|transaction|eventual/i, /一致|事务|幂等|最终一致|去重/],
  ['error handling', /error handling|failure/i, /错误|异常|失败/],
  ['logging & observability', /logging|observab|metrics|alert|trace/i, /日志|监控|指标|告警|链路/],
  ['testing', /testing|coverage|test case/i, /测试|用例|覆盖率/],
  ['migration', /migration|schema change/i, /迁移|变更脚本|expand.contract|删列/],
  ['security & auth', /security|authz|authn|permission/i, /鉴权|权限|安全|认证|授权/],
  ['secrets & config', /secret|credential|config/i, /密钥|凭证|配置项|环境变量/],
  ['deploy & rollback', /deploy|release|rollback/i, /部署|发布|上线|回滚/],
  ['backfill & reconciliation', /backfill|reconcil|repair/i, /回填|对账|补偿|兜底/],
  ['naming', /naming|convention/i, /命名/],
  ['deployment topology', /topology|cluster|node|replica|shard/i, /拓扑|集群|节点|副本|分片|多活/],
  ['tech selection & rationale', /rationale|trade-?off|why.*choos/i, /选型|取舍|为什么选|权衡|技术决策/],
  ['interface & contract', /api|contract|schema|interface/i, /接口|契约|协议|报文/],
  ['capacity & performance', /capacity|latency|throughput|qps|sla/i, /容量|延迟|吞吐|性能指标|可用性/],
  ['versioning & release', /version|release|changelog/i, /版本|发版|变更记录/]
];

const TEMPORAL = [
  ['deprecate marker', /deprecat|obsolete|legacy|no longer|废弃|下线|不再使用|历史遗留|已废弃/],
  ['future marker', /plan|roadmap|will |next (quarter|phase)|todo|规划|计划|将来|下一步|待实施|拟/],
  ['as-built marker', /current(ly)? |as-?is|现状|目前|已经|已上线|现已/]
];

function argv(args) {
  const pos = [], opt = { top: 40, min: 0.18, limit: 0, offset: 0, width: 160, tag: 'A', depth: 2 };
  for (let i = 0; i < args.length; i++) {
    if (args[i] === '--top') opt.top = +args[++i];
    else if (args[i] === '--min') opt.min = +args[++i];
    else if (args[i] === '--limit') opt.limit = +args[++i];
    else if (args[i] === '--offset') opt.offset = +args[++i];
    else if (args[i] === '--width') opt.width = +args[++i];
    else if (args[i] === '--depth') opt.depth = +args[++i];
    else if (args[i] === '--tag') { const t = args[++i]; opt.tag = t.length <= 2 ? t.toUpperCase() : t.toUpperCase()[0]; }
    else pos.push(args[i]);
  }
  return { pos, opt };
}

function clip(s, n) { return s.length > n ? s.slice(0, n - 1) + '…' : s; }

/* inventory: list docs, sizes, section counts, temporal density, topic coverage */
function cmdInventory(pos, opt) {
  if (!pos.length) die('usage: claim-index.cjs inventory <dirA> <dirB> [--depth 2]');
  pos.forEach((p, k) => {
    const tag = k === 0 ? opt.tag : String.fromCharCode(opt.tag.charCodeAt(0) + k);
    const docs = loadFolder(p, tag);
    console.log('# FOLDER ' + tag + ' = ' + path.resolve(p) + '   docs=' + docs.length + '   claims=' + docs.reduce((s, d) => s + d.claims.length, 0));
    docs.forEach(d => {
      console.log('  ' + clip(d.rel, 64).padEnd(64) + String(d.raw.length).padStart(7) + 'B  sec=' + String(bySection(d).length).padStart(3) + '  claim=' + String(d.claims.length).padStart(4));
    });
    console.log('\n## temporal signal in ' + tag + ' (candidate 已废弃/待实施 lines — verify by reading, not by regex alone)');
    let shown = 0;
    docs.forEach(d => d.claims.forEach(c => {
      const label = TEMPORAL.find(([, re]) => re.test(c.text));
      if (!label || shown >= 25) return;
      shown++;
      console.log('  [' + label[0] + '] ' + cid(d, c) + ' :: ' + clip(c.text, opt.width - 20));
    }));
    if (!shown) console.log('  (no temporal markers detected)');
    console.log('\n## topic coverage in ' + tag);
    TOPICS.forEach(([label, en, zh]) => {
      const hits = [];
      docs.forEach(d => d.claims.forEach(c => {
        const hay = c.section + ' ' + c.text;
        if (en.test(hay) || zh.test(hay)) hits.push(cid(d, c));
      }));
      console.log('  ' + (hits.length ? String(hits.length).padStart(4) : '   0') + '  ' + label + (hits.length ? '   e.g. ' + hits.slice(0, 3).join(' ') : ''));
    });
    console.log('');
  });
}

/* index: enumerate claims inside a folder, file by file */
function cmdIndex(pos, opt) {
  if (!pos.length) die('usage: claim-index.cjs index <dir> [--tag A --offset N --limit N --width N]');
  const docs = loadFolder(pos[0], opt.tag);
  const all = [];
  docs.forEach(d => d.claims.forEach(c => all.push({ doc: d, c })));
  const slice = opt.limit ? all.slice(opt.offset, opt.offset + opt.limit) : all.slice(opt.offset);
  console.log('# folder=' + path.resolve(pos[0]) + '  docs=' + docs.length + '  claims=' + all.length + '  showing=' + slice.length + '  from=' + (opt.offset + 1));
  let last = null;
  slice.forEach(({ doc, c }) => {
    if (doc.rel !== last) { last = doc.rel; console.log('\n--- ' + doc.rel + ' ---'); }
    console.log(cid(doc, c) + ' [L' + c.line + '] ' + clip(c.section, 60) + ' :: ' + clip(c.text, opt.width));
  });
  if (opt.offset + slice.length < all.length) console.log('... remaining ' + (all.length - opt.offset - slice.length) + '  (--offset ' + (opt.offset + slice.length) + ')');
}

/* compare: section-level overlap across two folders */
function cmdCompare(pos, opt) {
  if (pos.length < 2) die('usage: claim-index.cjs compare <dirA> <dirB> [--min 0.18 --top 40]');
  const A = loadFolder(pos[0], 'A'), B = loadFolder(pos[1], 'B');
  const sa = bySection({ tag: 'A', rel: '(folder)', claims: A.flatMap(d => d.claims.map(c => ({ ...c, _rel: d.rel }))) })
    .map(s => ({ ...s, rel: '(folder)' }));
  const sb = bySection({ tag: 'B', rel: '(folder)', claims: B.flatMap(d => d.claims.map(c => ({ ...c, _rel: d.rel }))) });
  const pairs = [];
  sa.forEach(a => sb.forEach(b => {
    const s = score(a, b);
    if (s >= opt.min) pairs.push({ a, b, s });
  }));
  pairs.sort((x, y) => y.s - x.s);
  const claimTotal = A.reduce((s, d) => s + d.claims.length, 0) + B.reduce((s, d) => s + d.claims.length, 0);
  console.log('# A=' + path.resolve(pos[0]) + ' docs=' + A.length + ' claims=' + A.reduce((s, d) => s + d.claims.length, 0)
    + '  |  B=' + path.resolve(pos[1]) + ' docs=' + B.length + ' claims=' + B.reduce((s, d) => s + d.claims.length, 0)
    + '  |  total-claims=' + claimTotal);

  const strong = pairs.filter(p => p.s >= 0.35);
  const mid = pairs.filter(p => p.s >= opt.min && p.s < 0.35).slice(0, opt.top);

  console.log('\n## SAME TOPIC (adjudicate — must resolve, never keep both)  n=' + strong.length);
  console.log('   section names only; find the real conflict by reading the claim IDs listed here.');
  strong.slice(0, opt.top).forEach(p => {
    console.log('  ' + p.s.toFixed(2) + '  A[' + clip(p.a.section, 46) + '] ' + p.a.ids.length + '  <->  B[' + clip(p.b.section, 46) + '] ' + p.b.ids.length);
    console.log('        A ' + p.a.ids.slice(0, 4).join(',') + '  |  B ' + p.b.ids.slice(0, 4).join(','));
  });

  console.log('\n## RELATED (likely complementary — merge into one rule)  n=' + mid.length);
  mid.forEach(p => {
    console.log('  ' + p.s.toFixed(2) + '  A[' + clip(p.a.section, 46) + ']  <->  B[' + clip(p.b.section, 46) + ']');
  });

  const hitA = new Set(strong.concat(mid).map(p => p.a.section));
  const hitB = new Set(strong.concat(mid).map(p => p.b.section));
  const onlyA = sa.filter(s => !hitA.has(s.section));
  const onlyB = sb.filter(s => !hitB.has(s.section));

  console.log('\n## DOC-LEVEL asymmetry (check whether one side covers a topic the other never mentions at all)');
  const topicOfDoc = (docs) => {
    const m = new Map();
    docs.forEach(d => {
      const set = new Set();
      d.claims.forEach(c => {
        const hay = c.section + ' ' + c.text;
        TOPICS.forEach(([label, en, zh]) => { if (en.test(hay) || zh.test(hay)) set.add(label); });
      });
      m.set(d.rel, set);
    });
    return m;
  };
  const ta = topicOfDoc(A), tb = topicOfDoc(B);
  ta.forEach((set, rel) => {
    const other = new Set();
    tb.forEach(s => s.forEach(x => other.add(x)));
    const missing = [...set].filter(x => !other.has(x));
    if (missing.length) console.log('  ONLY IN A: ' + clip(rel, 44) + '  ->  ' + missing.join(', '));
  });
  tb.forEach((set, rel) => {
    const other = new Set();
    ta.forEach(s => s.forEach(x => other.add(x)));
    const missing = [...set].filter(x => !other.has(x));
    if (missing.length) console.log('  ONLY IN B: ' + clip(rel, 44) + '  ->  ' + missing.join(', '));
  });

  console.log('\n## ONLY IN A sections (candidate 优点 — check it is not dead weight)  n=' + onlyA.length);
  onlyA.slice(0, opt.top).forEach(s => console.log('  ' + clip(s.section, 80) + '  [' + s.ids.length + ' claims]  ' + clip(s.ids.join(','), 60)));
  console.log('\n## ONLY IN B sections  n=' + onlyB.length);
  onlyB.slice(0, opt.top).forEach(s => console.log('  ' + clip(s.section, 80) + '  [' + s.ids.length + ' claims]  ' + clip(s.ids.join(','), 60)));

  console.log('\n## COVERAGE GAPS (neither side covers — the real value of merging)');
  const hay = (docs) => docs.some(d => d.claims.some(c => {
    const s = c.section + ' ' + c.text;
    return TOPICS.find(([, en, zh]) => en.test(s) || zh.test(s));
  }));
  const hitTopic = (docs, en, zh) => docs.some(d => d.claims.some(c => {
    const s = c.section + ' ' + c.text;
    return en.test(s) || zh.test(s);
  }));
  TOPICS.forEach(([label, en, zh]) => {
    if (!hitTopic(A, en, zh) && !hitTopic(B, en, zh)) console.log('  MISSING IN BOTH: ' + label);
    else if (!hitTopic(A, en, zh)) console.log('  only in B: ' + label);
    else if (!hitTopic(B, en, zh)) console.log('  only in A: ' + label);
  });
  void hay;
}

/* profile: per-doc structural summary used to build the independent dossier (Phase 1) */
function cmdProfile(pos, opt) {
  if (!pos.length) die('usage: claim-index.cjs profile <dir> [--tag A]');
  const docs = loadFolder(pos[0], opt.tag);
  console.log('# PROFILE ' + opt.tag + ' = ' + path.resolve(pos[0]) + '   docs=' + docs.length);
  console.log('# Read the raw text yourself for judgement. This output only orients you; do not conclude from it alone.\n');
  docs.forEach(d => {
    const secs = bySection({ tag: d.tag, rel: d.rel, claims: d.claims });
    console.log('=== ' + d.rel + '  (' + d.raw.length + 'B, ' + secs.length + ' sections, ' + d.claims.length + ' claims)');
    const dated = d.raw.match(/(20\d{2}[-/年]\d{1,2}([-/月]\d{1,2})?)|(最后核对|更新时间|版本[:：]?\s*v?[\d.]+)/g);
    if (dated) console.log('  date/version markers: ' + [...new Set(dated)].slice(0, 6).join('  |  '));
    secs.forEach(s => console.log('  ' + clip(s.section, 76).padEnd(76) + String(s.ids.length).padStart(4) + ' claims  ' + String(s.chars).padStart(6) + 'ch'));
    console.log('  first claims:');
    d.claims.slice(0, 3).forEach(c => console.log('    ' + cid(d, c) + ' :: ' + clip(c.text, opt.width - 12)));
    console.log('');
  });
}

try {
  const [, , cmd, ...rest] = process.argv;
  const { pos, opt } = argv(rest);
  if (cmd === 'inventory') cmdInventory(pos, opt);
  else if (cmd === 'index') cmdIndex(pos, opt);
  else if (cmd === 'compare') cmdCompare(pos, opt);
  else if (cmd === 'profile') cmdProfile(pos, opt);
  else console.log('usage:\n  claim-index.cjs inventory <dirA> <dirB>\n  claim-index.cjs profile <dir> [--tag A]\n  claim-index.cjs index <dir> [--tag A --offset N --limit N --width N]\n  claim-index.cjs compare <dirA> <dirB> [--min 0.18 --top 40]');
} catch (e) { die((e && e.message) || 'unknown failure'); }