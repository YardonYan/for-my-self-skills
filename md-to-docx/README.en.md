# md-to-docx — Lossless Markdown to Word

> Each Markdown element maps to a Word element, then a verification pass proves nothing was dropped. `RESULT: PASS` or it isn't done.

## What it solves

The usual ways to get Markdown into Word each cost something:

- **pandoc**: another install, CJK styling needs tuning, table shading, code block background and quote rules all need work
- **Online converters**: your document gets uploaded — not an option for internal archives
- **Copy-paste into Word**: formatting collapses, tables misalign, code blocks turn into paragraphs

This skill maps Markdown to `.docx` element by element with `python-docx`, then verifies the result character by character. The check is strict: every content line in the Markdown (headings, table cells, code lines, quotes, list items, body text) must be findable verbatim in the docx, and the counts of headings, tables and code blocks must match.

## When to use it

```
Convert this md to Word — it has to be lossless.
Turn this weekly report into a docx for archiving.
This manual goes to non-technical colleagues; give me a Word file.
```

## Element mapping

| Markdown | Word |
|---|---|
| `#` ~ `######` headings | Heading 1~6, bold, outline structure preserved, navigable in the Navigation Pane |
| `\| a \| b \|` tables | Table Grid, bold header row with light blue shading, 9pt cells, rows never split across pages |
| Fenced code blocks | Per-line monospace (Consolas + CJK fallback), light grey shading, single line spacing |
| `>` blockquotes | Left rule + light background + indent |
| `- ` / `1. ` lists | Nested indentation; ordered lists keep their original numbers to avoid Word's list renumbering |
| `---` horizontal rules | Thin grey bottom border on a paragraph |
| Inline `code` / `**bold**` / `*italic*` | Matching run formatting |

## Pitfalls already handled

1. The italic regex needs negative lookarounds, or `111*84*30cm` gets its `*84*` treated as italics
2. A table separator row `| --- |` must not be parsed as a horizontal rule — take the table branch first
3. `python-docx` defaults to Letter; CJK documents need A4
4. Setting `run.font.name` alone does not change East Asian glyphs — `rFonts` `w:eastAsia` is required
5. Do not use Word's built-in List Number style; multiple lists continue each other's numbering
6. Box-drawing characters in code blocks (│ ↓ ┌ ┐ └ ┘ →) align closest to the original ASCII art with a CJK font beside Consolas

## Dependency

```
pip install python-docx
```

That is the only third-party package. Both scripts are parameterised CLI tools and work on any Markdown file.

## Known limitation

Images (`![](path)`) are not embedded yet; add an image-paragraph step before `add_body` when needed.

## Install

```bash
git clone https://github.com/YardonYan/for-my-self-skills.git
cp -r for-my-self-skills/md-to-docx <your-agent-skills-dir>/
pip install python-docx
```

## Usage

```bash
python scripts/md2docx.py <src.md> [dst.docx]
python scripts/md2docx_verify.py <src.md> <dst.docx>   # must be PASS
```

## License

Apache-2.0, see [LICENSE](./LICENSE).
