# wechat-mp-publish — Markdown 进，公众号草稿箱出

> 把文章从 Markdown 一路送到公众号草稿箱，顺手解决那个老问题：图片粘过去就没了。

## 解决什么

发公众号卡人的不是排版，是图片。

Markdown 里写 `![封面](images/cover.png)`，粘进编辑器，图全丢。挂到 Gitee、OSS 上也一样——微信会过滤非自家域名的图片，还有 Referer 防盗链。

真正能显示的，只有 `mmbiz.qpic.cn` 上的图。所以流程里必须有一道「把图传到微信图床」的工序，市面上的排版工具大多只做排版，不做这一步，图就断了。

这个 Skill 把链路补全，并且把 AI 该干的、人该干的分清楚：

```
AI 写稿 ──► [人审稿] ──► AI 排版+传图 ──► [人发布]
              闸门一                       闸门二
```

## 什么时候用

```
把这篇 md 发到公众号。
公众号排版一下，图片别丢。
推送到公众号草稿箱。
为什么图片上传后不显示？
```

## 两条出口

| 情况 | 用法 | 产出 |
|---|---|---|
| 账号未认证，或不想给程序 AppSecret | `convert` | 可粘贴 HTML，人工粘贴 |
| 账号已认证，想省掉手工粘 | `push` | 直接写进草稿箱 |

`convert` 不会上传图片，图片靠浏览器剪贴板带过去；`push` 会先把每张图换成微信地址，再写草稿，样式不会被打折。

## 命令

只依赖 Python 3.8+ 标准库。不用 pip install，不联网也能跑 `convert`。

```bash
# 排版预览（不联网，不需要凭据）
python scripts/wmp.py convert article.md -o 公众号版.html --theme qing
python scripts/wmp.py check 公众号版.html

# 只搬图片：把 md / html / 目录里的图全换到微信图床，并生成替换版
python scripts/wmp.py upload article.md --rewrite

# 干跑，确认标题、字数、图片都对，不发任何请求
python scripts/wmp.py push article.md --cover cover.png --author Yardon --dry-run

# 真推草稿箱
python scripts/wmp.py push article.md --cover cover.png --author Yardon --digest "一句话摘要"

# 凭据与连通性自检
python scripts/wmp.py doctor
```

`convert` 会打印正文中文字数、图片提示和合规问题，末行 `RESULT: PASS` 才算能发。

## 三个主题

`assets/themes.json` 里带 `qing`（青竹）、`ink`（墨黑）、`blue`（经典蓝）。改 JSON 加新主题，不用动代码。

换主题只影响配色和字号，不影响结构。

## 排版规则

Markdown 按微信公众号的脾气来渲染，不需要你写 HTML：

- 标题、段落、加粗、行内代码、代码块、引用、列表、表格、分割线、图片全部支持
- 整段只有一句加粗时，自动变成金句块（左竖线 + 浅底）
- 代码块用 `<section>` + `<br>` 分行，不用 `<pre>`——`pre-wrap` 会被微信吃掉
- 图片自带图注（用 alt 文字）
- 表格超过 3 列会提示你改结构，手机上放不下
- 遇到 mermaid 代码块直接报错拦住，微信不渲染它

## 字段上限

| 字段 | 上限 |
|---|---|
| 标题 | 32 字 |
| 作者 | 16 字 |
| 摘要 | 128 字 |
| 正文 | 20000 字 |
| 正文图 | 1MB，仅 jpg/png |
| 封面 | 10MB，建议 2.35:1（900×383） |

脚本推送前会逐项卡住，不会等接口报错。

## 凭据

在公众号后台「设置与开发 → 基本配置」拿 AppID 和 AppSecret，写进项目根目录的 `.env`：

```
WECHAT_APPID=wx...
WECHAT_APPSECRET=...
```

`.env` 已在 `.gitignore` 里。脚本不会把密钥打进日志或输出。

## 图片怎么保证一定在微信图床

三处卡口，缺一处都不算完成：

| 卡口 | 做什么 | 在哪 |
|---|---|---|
| 上传 | 逐张调 `media/uploadimg`，本地路径和外链都换成 `mmbiz.qpic.cn` 地址 | `push` 内置；单独用 `upload` |
| 校验 | 扫每个 `<img src>`，不是 mmbiz 域名就报警告 | `convert` / `check` 每次跑 |
| 落盘 | `--rewrite` 生成替换版，原文件不动 | `upload --rewrite` |

只要图、不发文章，就单跑 `upload`。它支持 md、html、图片目录三种输入：

```bash
python scripts/wmp.py upload article.md --rewrite --json
```

输出「原地址 → mmbiz 地址」的清单，加 `--rewrite` 会写一份 `article.wechat.md`，原文件保持原样，核对无误后拿副本去发布。

## 已知限制

**账号权限因类型而异，先实测再下结论。** 网上常说「个人号没接口权限」，这个说法不准。有实测报告显示，个人未认证号的 token、`media/uploadimg`、`material/add_material`、`draft/add` 都能调通，只有 `freepublish/submit` 需要企业认证。也有说法称未认证号调 `draft/add` 会返回 `48001`。两种说法冲突，脚本不预设结论：先跑 `doctor` 验 token，再跑 `push --dry-run`，通了就真推，报 48001 再回退到 `convert` 粘贴。

**发布接口对个人号已关闭。** 2025 年 7 月起，`freepublish/submit` 的权限对个人主体和未认证企业号被回收。所以本 Skill 只做到草稿箱，最后那一下由人点。

**IP 白名单。** 后台必须把调用方的公网 IP 加进去，否则 `40164`。家里宽带是动态 IP，建议跑在固定 IP 的机器上，或者每次发布前先跑 `doctor`。

## 边界

- 不代替用户点发布，也不做定时群发
- 不做小红书、知乎等平台的排版，各家过滤规则不同
- 不写稿。写稿交给写作类 Skill
- 没审稿就不推。`push` 前人必须看过 `convert` 的产物

## 安装

```bash
git clone https://github.com/YardonYan/for-my-self-skills.git
cp -r for-my-self-skills/wechat-mp-publish <your-agent-skills-dir>/
```

或让 Agent 自己装：

```
帮我安装这个 skill：https://github.com/YardonYan/for-my-self-skills/tree/main/wechat-mp-publish
```

## 许可

Apache-2.0，见 [LICENSE](./LICENSE)。
