# html-to-pdf — Print-Optimized HTML to PDF

> CSS is the typesetting language; `@page` controls the paper. CJK text stays intact, tables stay whole, images are inlined.

## What it solves

Turning Markdown or web content into a deliverable PDF leaves few options:

- **weasyprint**: needs GTK on Windows, heavy dependency
- **reportlab / fpdf**: CJK fonts registered by hand, table layout written in code
- **Word → PDF**: depends on the Office version and local fonts, plus a docx detour
- **Headless Chrome**: already there if Chrome or Edge is installed, consumes CSS directly

This skill wires headless Chrome into a fixed three-step flow: write print-optimized HTML → inline every image as base64 → convert, then verify page count and keywords and render pages to PNG for a visual check.

## When to use it

```
Turn this manual into a PDF for delivery.
Give me a PDF version of this proposal, not markdown.
This handbook goes to non-technical colleagues — make it a PDF.
```

## The three steps

1. **Write print-optimized HTML**: `@page { size: A4; margin: 16mm 14mm }`, `page-break-after: avoid` on headings, `page-break-inside: avoid` on table rows; 12.5pt body at 1.75 line height reads well on A4 in Chinese
2. **Inline images as base64**: leave `{{FIG1}}` placeholders and substitute `data:image/png;base64,...` at build time — avoids local-path sandbox issues and keeps the intermediate HTML portable as a single file
3. **Convert with headless Chrome**: `--headless=new --print-to-pdf=...`, with the input path converted to a `file:///` URI

## Verification is not optional

Saying "it's generated" without checking is the most common failure here. All three checks:

- Page count matches the content volume
- Every keyword is found in the extracted text (title, body fragment, English fragment)
- Render to PNG and look: tables split in half, dropped images, orphaned table headers at the page bottom

## Pitfalls

1. **CJK paths**: the output path may contain Chinese, but the input HTML must be converted with `Path(x).as_uri()` — otherwise it fails silently
2. **Target PDF locked**: if a reader has the PDF open, Chrome reports no error, exit code is still 0, and the file is untouched. Compare source and PDF modification times to catch it
3. **Never delete the source**: keep the HTML so a one-line change re-emits the PDF; a PDF without its source means rewriting from scratch
4. **Duplicate figure titles**: if the diagram image already contains "Figure 5", the `<figcaption>` should only carry explanatory text
5. **CJK in Pillow**: use a system CJK font, never emoji (they render as tofu boxes); draw colored dots with `draw.ellipse()`
6. **Re-read the figures after copy edits**: text changed from five steps to four while the diagram still shows five — a render check catches this fastest

## Also included

When the same material needs both a PDF and a web version, share one source HTML: the print path uses `@page` and page breaks, the screen path uses sticky navigation and a wide container. `SKILL.md` carries the rest — inter-page navigation, rendering archived Markdown, and a minimal tab-switching pattern for parallel content.

## Dependencies

- Chrome or Edge (the script resolves it with `shutil.which`; fall back to a hardcoded path per the comment)
- Python: `fitz` (PyMuPDF) for page-count and keyword verification

## Install

```bash
git clone https://github.com/YardonYan/for-my-self-skills.git
cp -r for-my-self-skills/html-to-pdf <your-agent-skills-dir>/
```

## License

Apache-2.0, see [LICENSE](./LICENSE).
