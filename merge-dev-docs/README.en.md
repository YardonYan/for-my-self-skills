# merge-dev-docs — Merge Two Sets of Development Documents

> Merging is conflict adjudication, not summarization.

## What it solves

Hand two sets of development documents to a model and ask it to "blend them", and the result is always vaguer and less binding than either input — and a vague spec is no spec at all.

The premise of this skill is blunt: merging is not fusing two paragraphs into one. It means extracting claims, finding the real conflicts, adjudicating each with evidence, and writing something people can actually follow.

At folder scale there are three extra traps, each of which breaks a naive merge:

1. **Contamination** — read A then B and B's wording gets reshaped by A's framing, so the conflict matrix fills with "A's claim vs B as rewritten by A"
2. **Internal inconsistency** — one set can contradict itself; align within each set before aligning across sets
3. **Mixed tense** — one set describes the old design, the other the new one; merging directly promotes a deprecated architecture to current state, and readers follow it

## When to use it

```
Merge these two sets of development documents into one executable spec.
Align these two architecture docs and adjudicate the conflicts.
Take the best of both and produce one team standard.
```

## Not for

- Merging code → use diff / rebase
- A single set of documents that needs writing or review → edit directly
- Two sets that barely overlap → no adjudication needed, just unify the structure

## The phases

| Phase | What happens |
|---|---|
| 0 | Settle four things: which set is the base, whether a codebase or live environment can serve as evidence, one volume or two, and where the merged doc lives and who maintains it |
| 1 | Inventory both folders: bytes, section counts, item counts, tense signals, topic coverage |
| 2 | Profile each set independently — **no cross-referencing**; reverse the order and everything downstream is contaminated |
| 3 | Extract atomic claims and build the conflict matrix, each claim with a stable ID and source line number |
| 4 | Adjudicate real conflicts; with no evidence, every architecture-level conflict goes to a human — never decide by document length or seniority |
| 5 | **Hard gate**: stop and wait for the user's sign-off before writing anything |
| 6 | Write the volumes (architecture doc and dev spec have different skeletons; mixing them yields a hybrid nobody can use) |
| 7 | Record decisions and shared blind spots |

## The script

`scripts/claim-index.cjs` handles the mechanical work: inventory, independent profiles, atomic claim extraction, cross-folder overlap scoring and coverage-gap detection. Node 20+, zero dependencies.

```bash
node scripts/claim-index.cjs inventory <folderA> <folderB>
node scripts/claim-index.cjs profile <folderA> --tag A
node scripts/claim-index.cjs index <folderA> --tag A
node scripts/claim-index.cjs compare <folderA> <folderB> --min 0.18
```

The script only locates; the judgement has to come from reading the source. Three rules for reading its output live in `SKILL.md`; the critical one: `SAME TOPIC` is only a candidate list — real conflicts with different wording drop into `ONLY IN`, so every `ONLY IN` block needs a pass through the original text.

## What's inside

- The phase flow and the output template for each phase
- `references/judgment-rules.md`: conflict taxonomy and adjudication criteria
- `assets/`: six templates — document profile, conflict matrix, ADR, deprecation list, merged architecture doc, merged dev spec
- Coverage-gap detection — the real value of a merge is not A+B, it's exposing the blind spots both sets share

## Install

```bash
git clone https://github.com/YardonYan/for-my-self-skills.git
cp -r for-my-self-skills/merge-dev-docs <your-agent-skills-dir>/
```

## License

Apache-2.0, see [LICENSE](./LICENSE).
