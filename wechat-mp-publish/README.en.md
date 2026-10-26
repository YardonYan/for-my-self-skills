# wechat-mp-publish — Markdown in, WeChat draft out

> Take an article from Markdown all the way to a WeChat Official Account draft, and fix the problem that keeps biting: images vanish after pasting.

## What it solves

Posting to WeChat Official Account rarely fails on layout. It fails on images.

Write `![cover](images/cover.png)` in Markdown, paste into the editor, and every image is gone. Hosting them on Gitee or OSS does not help either — WeChat filters images from any domain but its own, and adds Referer hotlink protection on top.

The only images that render live on `mmbiz.qpic.cn`. So the pipeline needs a step that uploads each image to WeChat's own CDN. Most layout tools skip that step, which is why images break.

This skill closes the gap and separates what the machine does from what the human does:

```
AI writes ──► [human reviews] ──► AI lays out + uploads images ──► [human publishes]
                  gate 1                                              gate 2
```

## When to use it

```
Publish this markdown to our WeChat account.
Lay this out for WeChat, and don't lose the images.
Push it into the WeChat draft box.
Why do my images disappear after uploading?
```

## Two exits

| Situation | Command | Output |
|---|---|---|
| Account not verified, or you won't hand over AppSecret | `convert` | Paste-ready HTML, manual paste |
| Verified account, want to skip manual pasting | `push` | Written straight into the draft box |

`convert` does not upload anything — images travel through the clipboard when you paste. `push` uploads every image first and writes the draft, so styling survives untouched.

## Commands

Python 3.8+ standard library only. No pip install, and `convert` works offline.

```bash
# Layout preview (offline, no credentials)
python scripts/wmp.py convert article.md -o wechat.html --theme qing
python scripts/wmp.py check wechat.html

# Dry run: verify title, length and images without any network call
python scripts/wmp.py push article.md --cover cover.png --author Yardon --dry-run

# Real push into the draft box
python scripts/wmp.py push article.md --cover cover.png --author Yardon --digest "one-line summary"

# Credential and connectivity check
python scripts/wmp.py doctor
```

`convert` prints the body character count, image warnings and compliance issues. Only `RESULT: PASS` means it is ready.

## Three themes

`assets/themes.json` ships `qing` (bamboo teal), `ink` (mono black) and `blue` (classic blue). Add a theme by editing the JSON — no code change.

Themes only change colour and type sizes, never structure.

## Markdown rules

Markdown is rendered the way WeChat likes it, so you never write HTML:

- Headings, paragraphs, bold, inline code, code blocks, quotes, lists, tables, rules and images all supported
- A paragraph that is entirely bold becomes a pull-quote block (left rule + tinted background)
- Code blocks use `<section>` plus `<br>` instead of `<pre>` — `pre-wrap` gets stripped
- Images carry a caption built from the alt text
- Tables wider than 3 columns trigger a warning; they do not fit on phones
- mermaid blocks fail the check immediately, since WeChat does not render them

## Field limits

| Field | Limit |
|---|---|
| Title | 32 characters |
| Author | 16 characters |
| Digest | 128 characters |
| Body | 20,000 characters |
| Body image | 1 MB, jpg or png only |
| Cover | 10 MB, 2.35:1 recommended (900×383) |

The script enforces all of these before calling the API.

## Credentials

Get AppID and AppSecret from the account console (设置与开发 → 基本配置) and put them in a `.env` file at the project root:

```
WECHAT_APPID=wx...
WECHAT_APPSECRET=...
```

`.env` is already in `.gitignore`. Secrets are never printed to logs or output.

## Known limits

**The draft API needs a verified account.** Unverified personal accounts get `48001` from `draft/add`. Use `convert` and paste instead — the layout is identical.

**The publish API is closed to personal accounts.** Since July 2025, `freepublish/submit` is no longer available to personal or unverified business accounts. That is why this skill stops at the draft box and leaves the final click to a human.

**IP allowlist required.** The account console must list the caller's public IP, otherwise `40164`. Home broadband IPs change, so either run it on a fixed-IP host or run `doctor` before publishing.

## Boundaries

- Never clicks publish, never schedules mass sends
- No layout for Xiaohongshu or Zhihu — every platform filters differently
- Does not write the article; use a writing skill for that
- No pushing before review — a human must look at the `convert` output first

## Install

```bash
git clone https://github.com/YardonYan/for-my-self-skills.git
cp -r for-my-self-skills/wechat-mp-publish <your-agent-skills-dir>/
```

Or let the agent install it:

```
Install this skill: https://github.com/YardonYan/for-my-self-skills/tree/main/wechat-mp-publish
```

## License

Apache-2.0, see [LICENSE](./LICENSE).
