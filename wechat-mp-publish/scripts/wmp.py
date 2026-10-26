#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""wmp — 公众号文章排版与草稿箱推送。只依赖 Python 标准库。

四个子命令:
    convert   Markdown → 公众号可粘贴 HTML（本地路径保留，用于手动粘贴）
    check     检查 HTML 是否符合微信过滤规则
    push      Markdown → 上传正文图 → 上传封面 → 推送到草稿箱
    doctor    检查凭据配置与接口连通性

正文图的关键：微信只认 mmbiz.qpic.cn 域名的图片，外链会被直接过滤。
所以 push 会先把每张本地图上传到 media/uploadimg，再把 src 换成返回的
微信图床地址。封面另走 material/add_material 拿 thumb_media_id。

凭据从环境变量或同目录 .env 读取：
    WECHAT_APPID / WECHAT_APPSECRET
"""
import argparse
import hashlib
import html as htmllib
import json
import mimetypes
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

API = "https://api.weixin.qq.com/cgi-bin"

# 微信侧硬限制
LIMIT_CONTENT_IMG = 1 * 1024 * 1024      # media/uploadimg 正文图 1MB 以下
LIMIT_COVER_IMG = 10 * 1024 * 1024       # material/add_material 封面 10MB
LIMIT_TITLE = 32
LIMIT_AUTHOR = 16
LIMIT_DIGEST = 128
LIMIT_BODY_CHARS = 20000

SKILL_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
THEMES = os.path.join(SKILL_DIR, "assets", "themes.json")

ERR_HINTS = {
    40001: "access_token 失效，重新执行即可（脚本会自动刷新）",
    40007: "media_id 无效。封面必须用永久素材接口 material/add_material，不能用 media/upload",
    40164: "调用 IP 不在白名单。去 公众号后台 → 设置与开发 → 基本配置 → IP白名单 添加当前公网 IP",
    45004: "摘要超长，控制在 128 字以内",
    45009: "接口调用超频，稍等再试",
    48001: "接口未授权。草稿箱接口需要公众号完成微信认证，未认证的个人订阅号无法调用",
    40009: "图片尺寸或大小不合规，正文图必须 jpg/png 且小于 1MB",
}


def out(msg=""):
    print(msg, flush=True)


def die(msg, code=1):
    print("错误：" + msg, file=sys.stderr, flush=True)
    sys.exit(code)


# ---------------------------------------------------------------- 主题

def load_theme(name):
    if not os.path.isfile(THEMES):
        die("找不到主题文件：" + THEMES)
    data = json.load(open(THEMES, encoding="utf-8"))
    data.pop("_readme", None)
    if name is None:
        name = next(iter(data))
    if name not in data:
        die("没有这个主题：%s（可选：%s）" % (name, "、".join(data)))
    t = dict(data[name])
    t["key"] = name
    return t


# ---------------------------------------------------------------- Markdown 渲染

RE_H = re.compile(r"^(#{1,6})\s+(.*)$")
RE_IMG_ONLY = re.compile(r"^!\[([^\]]*)\]\(([^)\s]+)\)$")
RE_IMG = re.compile(r"!\[([^\]]*)\]\(([^)\s]+)\)")
RE_UL = re.compile(r"^[-*+]\s+(.*)$")
RE_OL = re.compile(r"^(\d+)[.)]\s+(.*)$")
RE_TABLE_SEP = re.compile(r"^\|[\s:\-|]+\|?\s*$")


def esc(s):
    return htmllib.escape(s, quote=False)


def inline(text, t):
    """行内格式。外链只保留文字，因为微信正文不允许可点外链。"""
    text = esc(text)
    text = re.sub(r"\*\*(.+?)\*\*", lambda m: '<strong style="color:%s;font-weight:700;">%s</strong>' % (t["strong"], m.group(1)), text)
    text = re.sub(r"`([^`]+)`", lambda m: '<code style="background:%s;padding:1px 5px;border-radius:3px;font-family:Menlo,Consolas,monospace;font-size:14px;color:%s;">%s</code>' % (t["codeBg"], t["inlineCodeText"], m.group(1)), text)
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    return text


def p_style(t, extra=""):
    return ("margin:0 0 22px;font-size:%s;line-height:%s;color:%s;letter-spacing:%s;%s"
            % (t["fontSize"], t["lineHeight"], t["text"], t["letterSpacing"], extra))


def render(md, t):
    lines = md.replace("\r\n", "\n").replace("\r", "\n").split("\n")
    body = []
    i, n = 0, len(lines)
    title = None

    while i < n:
        line = lines[i]
        s = line.strip()

        # 代码块
        if s.startswith("```"):
            lang = s[3:].strip()
            i += 1
            buf = []
            while i < n and not lines[i].strip().startswith("```"):
                buf.append(lines[i])
                i += 1
            i += 1
            code = "\n".join(buf) if buf else " "
            label = ('<p style="margin:0 0 8px;font-size:12px;color:%s;letter-spacing:1px;">%s</p>'
                     % (t["muted"], esc(lang))) if lang else ""
            body.append(
                '<section style="margin:0 0 22px;padding:16px 18px;background:%s;border-radius:6px;'
                'font-family:Menlo,Consolas,monospace;font-size:13px;line-height:1.75;color:%s;word-break:break-all;">'
                '%s%s</section>' % (t["codeBg"], t["codeText"], label,
                                    "<br>".join(esc(x) if x.strip() else "&nbsp;" for x in code.split("\n")))
            )
            continue

        # 图片独占一行
        m = RE_IMG_ONLY.match(s)
        if m:
            alt, src = m.group(1), m.group(2)
            cap = ('<p style="margin:10px 0 0;font-size:12.5px;color:%s;text-align:center;letter-spacing:0.2px;">%s</p>'
                   % (t["muted"], esc(alt))) if alt else ""
            body.append('<section style="margin:0 0 26px;">'
                        '<img src="%s" style="width:100%%;display:block;border-radius:4px;">%s</section>'
                        % (esc(src), cap))
            i += 1
            continue

        # 标题
        m = RE_H.match(s)
        if m:
            level, text = len(m.group(1)), m.group(2).strip()
            if level == 1:
                title = title or text
                body.append('<section style="margin:0 0 26px;"><p style="margin:0;font-size:23px;'
                            'line-height:1.45;font-weight:700;color:%s;letter-spacing:-0.2px;">%s</p></section>'
                            % (t["strong"], inline(text, t)))
            elif level == 2:
                body.append('<section style="margin:46px 0 20px;padding-left:12px;border-left:4px solid %s;">'
                            '<p style="margin:0;font-size:19px;font-weight:700;color:%s;letter-spacing:0;">%s</p></section>'
                            % (t["accent"], t["strong"], inline(text, t)))
            else:
                body.append('<p style="margin:34px 0 16px;font-size:17px;font-weight:700;color:%s;">%s</p>'
                            % (t["strong"], inline(text, t)))
            i += 1
            continue

        # 分割线
        if re.match(r"^(-{3,}|\*{3,}|_{3,})$", s):
            body.append('<section style="margin:38px 0;height:1px;background:%s;"></section>' % t["border"])
            i += 1
            continue

        # 引用
        if s.startswith(">"):
            buf = []
            while i < n and lines[i].strip().startswith(">"):
                buf.append(lines[i].strip()[1:].strip())
                i += 1
            para = inline(" ".join(x for x in buf if x), t)
            body.append('<section style="margin:0 0 24px;padding:16px 20px;background:%s;border-left:3px solid %s;'
                        'border-radius:0 4px 4px 0;"><p style="margin:0;font-size:16.5px;line-height:1.85;color:%s;">%s</p></section>'
                        % (t["quoteBg"], t["accent"], t["strong"], para))
            continue

        # 表格
        if s.startswith("|") and i + 1 < n and RE_TABLE_SEP.match(lines[i + 1].strip()):
            header = [c.strip() for c in s.strip("|").split("|")]
            i += 2
            rows = []
            while i < n and lines[i].strip().startswith("|"):
                rows.append([c.strip() for c in lines[i].strip().strip("|").split("|")])
                i += 1
            th = "".join('<th style="padding:10px 12px;border-bottom:2px solid %s;font-size:13.5px;'
                         'text-align:left;color:%s;">%s</th>' % (t["border"], t["strong"], inline(c, t)) for c in header)
            trs = ""
            for r in rows:
                tds = "".join('<td style="padding:10px 12px;border-bottom:1px solid %s;font-size:13.5px;'
                              'color:%s;">%s</td>' % (t["border"], t["text"], inline(c, t)) for c in r)
                trs += "<tr>" + tds + "</tr>"
            body.append('<section style="margin:0 0 24px;overflow-x:auto;"><table style="width:100%%;'
                        'border-collapse:collapse;font-size:13.5px;"><thead><tr>%s</tr></thead><tbody>%s</tbody></table></section>'
                        % (th, trs))
            if len(header) > 3:
                body.append('<p style="margin:0 0 22px;font-size:13px;color:%s;">（这张表 %d 列，手机上可能偏挤，建议改成 3 列以内或拆成卡片）</p>'
                            % (t["muted"], len(header)))
            continue

        # 无序列表
        m = RE_UL.match(s)
        if m:
            body.append('<p style="%s">· %s</p>' % (p_style(t, "padding-left:2px;"), inline(m.group(1), t)))
            i += 1
            continue

        # 有序列表
        m = RE_OL.match(s)
        if m:
            body.append('<p style="%s">%s. %s</p>' % (p_style(t, "padding-left:2px;"), m.group(1), inline(m.group(2), t)))
            i += 1
            continue

        # 空行
        if not s:
            i += 1
            continue

        # 普通段落（连续行合并）
        buf = [s]
        i += 1
        while i < n:
            nxt = lines[i].strip()
            if (not nxt or nxt.startswith(("#", "```", ">", "|")) or RE_UL.match(nxt)
                    or RE_OL.match(nxt) or RE_IMG_ONLY.match(nxt) or re.match(r"^(-{3,}|\*{3,}|_{3,})$", nxt)):
                break
            buf.append(nxt)
            i += 1
        text = " ".join(buf)
        # 整段只有一句加粗 → 当成金句块，这是公众号最常见的强调写法
        m_gold = re.fullmatch(r"\*\*(.+?)\*\*", text.strip())
        if m_gold:
            body.append('<section style="margin:0 0 24px;padding:16px 20px;background:%s;border-left:3px solid %s;'
                        'border-radius:0 4px 4px 0;"><p style="margin:0;font-size:17px;line-height:1.7;'
                        'color:%s;font-weight:700;">%s</p></section>'
                        % (t["quoteBg"], t["accent"], t["strong"], inline(m_gold.group(1), t)))
        else:
            body.append('<p style="%s">%s</p>' % (p_style(t), inline(text, t)))

    page = ('<section style="max-width:677px;margin:0 auto;padding:8px 6px 40px;'
            'font-family:-apple-system,BlinkMacSystemFont,\'PingFang SC\',\'Hiragino Sans GB\',\'Microsoft YaHei\',sans-serif;'
            'font-size:%s;line-height:%s;color:%s;letter-spacing:%s;">\n%s\n</section>'
            % (t["fontSize"], t["lineHeight"], t["text"], t["letterSpacing"], "\n".join(body)))
    return page, title


def wrap_document(page, title):
    return ('<!doctype html>\n<html lang="zh-CN">\n<head>\n<meta charset="utf-8">\n'
            '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
            '<title>%s</title>\n</head>\n<body style="margin:0;padding:0;background:#ffffff;">\n'
            '%s\n</body>\n</html>\n' % (esc(title or "公众号文章"), page))


# ---------------------------------------------------------------- 检查

def scan_md(md):
    """发布前扫 Markdown 层面的坑。微信不吃的东西在这里拦下来。"""
    issues = []
    for idx, line in enumerate(md.split("\n"), 1):
        s = line.strip().lower()
        if s.startswith("```mermaid"):
            issues.append("第 %d 行是 mermaid 代码块，微信不渲染。先导出成 png，再用 ![](图) 引用" % idx)
    return issues


def check(page_html):
    issues, warns = [], []

    for tag in ("<style", "<script", "<link"):
        if tag in page_html.lower():
            issues.append("出现 %s 标签，微信会剥离，必须删掉" % tag)

    if re.search(r"\sclass=", page_html):
        issues.append("出现 class 属性，微信只认内联 style")
    if re.search(r"\sid=", page_html):
        issues.append("出现 id 属性，微信会剥离")

    tags = re.findall(r"<([a-z0-9]+)([^>]*)>", page_html)
    skip = {"html", "head", "body", "meta", "title", "br", "strong", "tr", "th", "td", "thead", "tbody", "table"}
    bare = {}
    for name, attrs in tags:
        if name in skip or name.startswith("!"):
            continue
        if "style=" not in attrs:
            bare[name] = bare.get(name, 0) + 1
    if bare:
        issues.append("以下标签缺内联样式：" + "、".join("%s×%d" % (k, v) for k, v in bare.items()))

    for src in re.findall(r'<img[^>]+src="([^"]+)"', page_html):
        if src.startswith("//"):
            src = "https:" + src
        if src.startswith("http"):
            if "mmbiz.qpic.cn" not in src:
                warns.append("图片不是微信图床，粘贴或推送后可能不显示：" + src[:60])
        else:
            if not os.path.isfile(src):
                issues.append("本地图片不存在：" + src)

    body_only = re.sub(r"<head[\s\S]*?</head>", "", page_html, flags=re.I)
    text_only = re.sub(r"<[^>]+>", "", body_only)
    chars = len(re.findall(r"[\u4e00-\u9fa5]", text_only))
    if chars > LIMIT_BODY_CHARS:
        issues.append("正文 %d 个中文字，超过微信 20000 字上限" % chars)
    elif chars > LIMIT_BODY_CHARS * 0.9:
        warns.append("正文 %d 字，已接近 20000 上限" % chars)

    return issues, warns, chars


# ---------------------------------------------------------------- 微信接口

def _load_env():
    appid = os.environ.get("WECHAT_APPID", "").strip()
    secret = os.environ.get("WECHAT_APPSECRET", "").strip()
    if appid and secret:
        return appid, secret
    for path in (".env", os.path.join(os.getcwd(), ".env")):
        if os.path.isfile(path):
            for line in open(path, encoding="utf-8"):
                line = line.strip()
                if not line or line.startswith("#") or "=" not in line:
                    continue
                k, v = line.split("=", 1)
                k, v = k.strip(), v.strip().strip('"').strip("'")
                if k == "WECHAT_APPID" and not appid:
                    appid = v
                if k == "WECHAT_APPSECRET" and not secret:
                    secret = v
            if appid and secret:
                return appid, secret
    return appid, secret


def _token_cache_path(appid):
    import tempfile
    tag = hashlib.md5(appid.encode()).hexdigest()[:12]
    return os.path.join(tempfile.gettempdir(), ".wmp_token_%s.json" % tag)


def get_token(appid, secret, force=False):
    cache = _token_cache_path(appid)
    if not force and os.path.isfile(cache):
        try:
            c = json.load(open(cache, encoding="utf-8"))
            if c.get("appid") == appid and c.get("expire_at", 0) - time.time() > 300:
                return c["access_token"]
        except Exception:
            pass
    payload = json.dumps({"grant_type": "client_credential", "appid": appid,
                          "secret": secret, "force_refresh": False}).encode("utf-8")
    req = urllib.request.Request(API + "/stable_token", data=payload,
                                 headers={"Content-Type": "application/json"}, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            data = json.loads(r.read().decode("utf-8"))
    except urllib.error.URLError as e:
        die("连不上微信接口：%s" % e)
    if "access_token" not in data:
        # 旧接口兜底（部分老账号 stable_token 未开通）
        q = urllib.parse.urlencode({"grant_type": "client_credential", "appid": appid, "secret": secret})
        try:
            with urllib.request.urlopen(API + "/token?" + q, timeout=20) as r:
                data = json.loads(r.read().decode("utf-8"))
        except urllib.error.URLError as e:
            die("连不上微信接口：%s" % e)
    if "access_token" not in data:
        raise ApiError(data)
    json.dump({"appid": appid, "access_token": data["access_token"],
               "expire_at": time.time() + int(data.get("expires_in", 7200))},
              open(cache, "w", encoding="utf-8"))
    try:
        os.chmod(cache, 0o600)
    except Exception:
        pass
    return data["access_token"]


class ApiError(Exception):
    def __init__(self, data):
        self.data = data
        self.code = data.get("errcode")
        self.msg = data.get("errmsg", "")
        super().__init__("errcode=%s errmsg=%s" % (self.code, self.msg))

    def hint(self):
        return ERR_HINTS.get(self.code, "对照 references/api.md 的错误码表排查")


def _post_multipart(url, filename, data, field="media", mime=None):
    boundary = "----wmp" + hashlib.md5(os.urandom(8)).hexdigest()
    mime = mime or mimetypes.guess_type(filename)[0] or "application/octet-stream"
    body = b"".join([
        ("--%s\r\n" % boundary).encode(),
        ('Content-Disposition: form-data; name="%s"; filename="%s"\r\n' % (field, os.path.basename(filename))).encode("utf-8"),
        ("Content-Type: %s\r\n\r\n" % mime).encode(),
        data, b"\r\n", ("--%s--\r\n" % boundary).encode(),
    ])
    req = urllib.request.Request(url, data=body, method="POST",
                                 headers={"Content-Type": "multipart/form-data; boundary=" + boundary})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read().decode("utf-8"))


def upload_content_image(token, path):
    url = "%s/media/uploadimg?access_token=%s" % (API, urllib.parse.quote(token))
    data = _post_multipart(url, path, open(path, "rb").read())
    if "url" not in data:
        raise ApiError(data)
    return data["url"]


def upload_cover(token, path):
    url = "%s/material/add_material?access_token=%s&type=image" % (API, urllib.parse.quote(token))
    data = _post_multipart(url, path, open(path, "rb").read())
    if "media_id" not in data:
        raise ApiError(data)
    return data["media_id"]


def add_draft(token, article):
    url = "%s/draft/add?access_token=%s" % (API, urllib.parse.quote(token))
    payload = json.dumps({"articles": [article]}, ensure_ascii=False).encode("utf-8")
    req = urllib.request.Request(url, data=payload, method="POST",
                                 headers={"Content-Type": "application/json; charset=utf-8"})
    with urllib.request.urlopen(req, timeout=30) as r:
        data = json.loads(r.read().decode("utf-8"))
    if data.get("errcode"):
        raise ApiError(data)
    return data.get("media_id")


# ---------------------------------------------------------------- 图片处理

def shrink_if_needed(path, limit):
    """超限时尝试压缩。优先 Pillow，其次 ImageMagick，都没有就返回原路径。"""
    if os.path.getsize(path) <= limit:
        return path
    base, ext = os.path.splitext(path)
    dst = base + ".wmp" + ext
    try:
        from PIL import Image
        im = Image.open(path)
        if im.mode in ("RGBA", "P", "LA"):
            im = im.convert("RGB")
        w, h = im.size
        scale = min(1.0, (limit * 0.85 / os.path.getsize(path)) ** 0.5)
        im = im.resize((max(1, int(w * scale)), max(1, int(h * scale))), Image.LANCZOS)
        im.save(dst, quality=85, optimize=True)
        if os.path.getsize(dst) <= limit:
            return dst
    except Exception:
        pass
    for exe in ("magick", "convert"):
        try:
            import subprocess
            subprocess.run([exe, path, "-resize", "1600x1600>", "-quality", "85", dst],
                           check=True, capture_output=True)
            if os.path.getsize(dst) <= limit:
                return dst
        except Exception:
            continue
    return path


def download_image(url):
    """远程图先落到本地临时文件，再走 uploadimg。外链直接写进正文会被微信过滤。"""
    import tempfile
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (wmp)"})
    with urllib.request.urlopen(req, timeout=30) as r:
        data = r.read()
    ext = os.path.splitext(urllib.parse.urlparse(url).path)[1].lower()
    if ext not in (".jpg", ".jpeg", ".png"):
        ext = ".png"
    fd, path = tempfile.mkstemp(suffix=ext, prefix="wmp_img_")
    with os.fdopen(fd, "wb") as f:
        f.write(data)
    return path


def collect_images(page_html):
    return re.findall(r'<img[^>]+src="([^"]+)"', page_html)


def replace_src(page_html, mapping):
    for old, new in mapping.items():
        page_html = page_html.replace('src="%s"' % old, 'src="%s"' % new)
    return page_html


# ---------------------------------------------------------------- 子命令

def cmd_convert(args):
    md = open(args.md, encoding="utf-8").read()
    theme = load_theme(args.theme)
    page, title = render(md, theme)
    doc = wrap_document(page, title)
    out_path = args.out or "公众号版.html"
    open(out_path, "w", encoding="utf-8", newline="\n").write(doc)
    issues, warns, chars = check(page)
    issues = scan_md(md) + issues
    out("已生成：%s" % out_path)
    out("主题：%s（%s）  正文 %d 字" % (theme["name"], theme["key"], chars))
    for w in warns:
        out("  提示：" + w)
    for it in issues:
        out("  问题：" + it)
    out("RESULT: " + ("PASS" if not issues else "FAIL"))
    return 0 if not issues else 1


def cmd_check(args):
    doc = open(args.html, encoding="utf-8").read()
    issues, warns, chars = check(doc)
    out("文件：%s" % args.html)
    out("正文 %d 字" % chars)
    for w in warns:
        out("  提示：" + w)
    for it in issues:
        out("  问题：" + it)
    out("RESULT: " + ("PASS" if not issues else "FAIL"))
    return 0 if not issues else 1


def cmd_doctor(args):
    appid, secret = _load_env()
    out("凭据：")
    out("  WECHAT_APPID     %s" % (appid[:6] + "***" + appid[-4:] if len(appid) > 10 else ("已配置" if appid else "未配置")))
    out("  WECHAT_APPSECRET %s" % ("已配置（%d 位）" % len(secret) if secret else "未配置"))
    if not (appid and secret):
        out("\n去公众号后台 → 设置与开发 → 基本配置 拿 AppID 和 AppSecret，")
        out("写进当前目录的 .env：WECHAT_APPID=xxx / WECHAT_APPSECRET=xxx")
        out("RESULT: FAIL")
        return 1
    try:
        token = get_token(appid, secret, force=True)
        out("\n接口连通：access_token 获取成功（%s…）" % token[:8])
        out("RESULT: PASS")
        return 0
    except ApiError as e:
        out("\n接口报错：%s" % e)
        out("  原因：%s" % e.hint())
        out("RESULT: FAIL")
        return 1


def cmd_push(args):
    md = open(args.md, encoding="utf-8").read()
    theme = load_theme(args.theme)
    page, auto_title = render(md, theme)
    title = args.title or auto_title
    if not title:
        die("没有标题。用 --title 指定，或在 Markdown 里写一个 # 一级标题")
    if len(title) > LIMIT_TITLE:
        die("标题 %d 字，微信上限 %d 字" % (len(title), LIMIT_TITLE))
    if args.author and len(args.author) > LIMIT_AUTHOR:
        die("作者 %d 字，微信上限 %d 字" % (len(args.author), LIMIT_AUTHOR))
    if args.digest and len(args.digest) > LIMIT_DIGEST:
        die("摘要 %d 字，微信上限 %d 字" % (len(args.digest), LIMIT_DIGEST))

    if not args.cover:
        die("必须用 --cover 指定封面图（建议 2.35:1，900×383）")

    issues, warns, chars = check(page)
    issues = scan_md(md) + issues
    if issues:
        out("排版检查未通过，先修这些：")
        for it in issues:
            out("  " + it)
        return 1

    # 收集并预处理图片
    mapping, plan = {}, []
    for src in collect_images(page):
        if src.startswith("http") or src.startswith("//"):
            if "mmbiz.qpic.cn" in src:
                continue
            if args.dry_run:
                plan.append(("远程外链", src, "待下载后上传到微信图床"))
                continue
            try:
                local = download_image(src if not src.startswith("//") else "https:" + src)
            except Exception as e:
                die("远程图片下载失败：%s（%s）。先存到本地再引用更稳" % (src, e))
            fixed = shrink_if_needed(local, LIMIT_CONTENT_IMG)
            if os.path.getsize(fixed) > LIMIT_CONTENT_IMG:
                die("远程图片压不到 1MB 以下：%s" % src)
            mapping[src] = fixed
            plan.append(("远程外链", src, "已下载，待上传"))
            continue
        if not os.path.isfile(src):
            die("正文图片不存在：" + src)
        fixed = shrink_if_needed(src, LIMIT_CONTENT_IMG)
        if os.path.getsize(fixed) > LIMIT_CONTENT_IMG:
            die("图片超过 1MB 且压不下来：%s（正文图上限 1MB）" % src)
        mapping[src] = fixed
        plan.append(("本地图片", src, "%.0f KB" % (os.path.getsize(fixed) / 1024)))

    out("标题：%s（%d 字）" % (title, len(title)))
    out("正文：%d 字，%d 张图" % (chars, len(mapping)))
    out("封面：%s" % args.cover)
    for kind, src, note in plan:
        out("  %s  %s  %s" % (kind, src, note))
    for w in warns:
        out("  提示：" + w)

    if args.dry_run:
        out("\n--dry-run：不做任何网络请求。真实执行会依次：")
        out("  1) 取 access_token")
        out("  2) 每张正文图走 media/uploadimg 换成 mmbiz.qpic.cn 地址")
        out("  3) 封面走 material/add_material 拿 thumb_media_id")
        out("  4) draft/add 写入草稿箱")
        out("RESULT: DRY-RUN")
        return 0

    appid, secret = _load_env()
    if not (appid and secret):
        die("没有凭据。先跑 `python scripts/wmp.py doctor` 按提示配置 .env")

    if not os.path.isfile(args.cover):
        die("封面文件不存在：" + args.cover)
    if os.path.getsize(args.cover) > LIMIT_COVER_IMG:
        die("封面超过 10MB")

    token = get_token(appid, secret)

    try:
        for old, fixed in mapping.items():
            url = upload_content_image(token, fixed)
            mapping[old] = url
            out("  已上传正文图 → %s" % url.split("/")[-1][:16])
        page = replace_src(page, {k: v for k, v in mapping.items() if v.startswith("http")})

        thumb = upload_cover(token, args.cover)
        out("  已上传封面 → media_id %s" % thumb[:12])

        draft_id = add_draft(token, {
            "title": title,
            "author": args.author or "",
            "digest": args.digest or "",
            "content": page,
            "thumb_media_id": thumb,
            "need_open_comment": 0,
            "only_fans_can_comment": 0,
        })
    except ApiError as e:
        out("\n接口报错：%s" % e)
        out("  原因：%s" % e.hint())
        return 1

    out("\n草稿已创建，media_id：%s" % draft_id)
    out("下一步（必须人工）：打开 mp.weixin.qq.com → 草稿箱 → 预览 → 自己点发布。")
    out("RESULT: PASS")
    return 0


def main():
    ap = argparse.ArgumentParser(description="公众号文章排版与草稿箱推送")
    sub = ap.add_subparsers(dest="cmd", required=True)

    c = sub.add_parser("convert", help="Markdown 转公众号可粘贴 HTML")
    c.add_argument("md")
    c.add_argument("-o", "--out")
    c.add_argument("--theme")
    c.set_defaults(func=cmd_convert)

    k = sub.add_parser("check", help="检查 HTML 是否符合微信过滤规则")
    k.add_argument("html")
    k.set_defaults(func=cmd_check)

    p = sub.add_parser("push", help="推送到公众号草稿箱")
    p.add_argument("md")
    p.add_argument("--cover", required=False)
    p.add_argument("--title")
    p.add_argument("--author")
    p.add_argument("--digest")
    p.add_argument("--theme")
    p.add_argument("--dry-run", action="store_true")
    p.set_defaults(func=cmd_push)

    d = sub.add_parser("doctor", help="检查凭据与接口连通性")
    d.set_defaults(func=cmd_doctor)

    args = ap.parse_args()
    sys.exit(args.func(args))


if __name__ == "__main__":
    main()
