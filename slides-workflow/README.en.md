# slides-workflow — From Raw Material to Finished Slides

> Content first, format second. Nail down what the deck says, then what it looks like, and only then decide whether it becomes HTML, image pages or an editable PPTX.

## What it solves

The usual AI deck failure isn't "it can't produce one" — it's discovering halfway through that the direction was wrong:

- The model paginates on its own, writes its own copy, and the finished draft has the wrong page order and the wrong emphasis, so you throw it away
- Without a style spec every page is designed separately, and by page seven the deck looks like three decks
- The wrong format gets chosen: you only needed something to read, but ended up needing an editable PPTX — or the opposite, you'll revise it ten times but produced flat images

Time looks like it goes into layout. What actually decides how many rewrites you do is whether the content was settled, the style was unified, and the format was chosen correctly. This skill splits the work into four stages, with hard gates after the first two.

## When to use it

```
Turn these materials into a report deck.
I need a 20-minute training deck; the material is ready.
This deck will be revised repeatedly — how do I get an editable version out of AI?
I have a deck as images and want a PPTX I can edit.
These pages never come out right; help me find why.
```

## The four stages

| Stage | What happens | Output |
|---|---|---|
| 1 — Gather and script | Six questions answered, material split into three folders, seven fields per page | `page-script.md` |
| 2 — Style spec | Reference images decomposed into color, type and layout; pick one direction | `style-spec.md` |
| 3 — Choose format and build | HTML Slides, image pages or editable PPTX | Deck plus a PDF backup |
| 4 — Targeted polish | Five-part revision requests, one page at a time | Final version |

Stages 1 and 2 end at a hard gate. Skipping a gate doesn't save time; it multiplies rework.

## Choosing a format

| Your situation | Pick |
|---|---|
| Live presentation, needs motion or interaction | HTML Slides |
| Just want to see the result, or only send it to read | Image pages |
| Will be revised often, or handed to a colleague | Editable PPTX |
| A brand template must be followed | Editable PPTX on the original master |
| Cover needs impact, content pages need editing | Mixed |

Each format has its own constraints, build prompt and acceptance checklist: `references/mode-html.md`, `references/mode-image.md`, `references/mode-pptx.md`.

## What's inside

- **Working method for all four stages**: two brief types (simple and detailed), the seven-field page script, the style spec template, the five-part revision request
- **Three build prompts**: HTML Slides, image pages and editable PPTX, taken from real projects, acceptance criteria included
- **Image-to-PPTX reconstruction**: hybrid reconstruction, clearing original text from backgrounds, and how to report the parts that can't be split cleanly
- **Nine known failure modes**: from "the model paginates on its own" to "two rounds with no improvement and still regenerating"
- **Two verification scripts**: project scaffolding plus page-script and asset integrity checks, standard library only

## Scripts

```bash
python scripts/scaffold.py <project> --full   # scaffold brief, page script, style spec, asset folders
python scripts/verify.py script <project>      # page numbering, all seven fields, open gaps
python scripts/verify.py assets <project>      # referenced images exist, unreferenced files, numbering
```

`verify.py` prints `RESULT: PASS` or lists every problem with page number and field name. Field names must match `references/page-script.md` exactly — writing `布局` instead of `建议布局` reports a missing field.

## Boundaries

- **No decks from thin air.** If material is missing, ask for it instead of inventing content
- **No pixel-perfect brand template reproduction.** When a template must be followed strictly, a human is faster
- **No deliverables that require a network connection to present**
- **"The image looks right" is not "the content is right."** Numbers and units go back to the source material

## How it relates to the rest of the repo

- Plain document conversion isn't this skill: use `md-to-docx` for Markdown to Word, `html-to-pdf` for HTML to PDF
- Single-file HTML artifacts (reports, dashboards) belong to `html-skill-effectiveness`; this skill's HTML mode targets 16:9 slide-by-slide presentation
- For the writing stage, `tech-blog-generator` or `yardon-writer` can straighten out the text before it becomes a page script

## Install

```bash
git clone https://github.com/YardonYan/for-my-self-skills.git
cp -r for-my-self-skills/slides-workflow <your-agent-skills-dir>/
```

Or let the agent install it:

```
Install this skill: https://github.com/YardonYan/for-my-self-skills/tree/main/slides-workflow
```

## Dependencies

None. Both scripts use the Python standard library only and run on Python 3.8+.

The external skills used during production (frontend-slides, huashu-design, visual-explainer and ppt-master-class tools) are not part of this repo. Use whichever you have; the prompts work without them if you swap the name.

## License

Apache-2.0, see [LICENSE](./LICENSE).
