# prompt-optimizer — Four Ways to Rewrite a Prompt

> Feed in a rough draft, get four finished prompts using different strategies, then pick one.

## What it solves

"the model didn't understand me" is almost never the model. The prompt is missing what the model needs: audience, output format, constraints, and a definition of done.

This skill does not do gentle polishing. It rewrites the same request four different ways so you can see how the organization of a prompt changes the result:

| Strategy | Core idea | Best for |
|---|---|---|
| A — Detailed expansion | Add context, constraints, boundaries, output format, success criteria | Clear task, missing detail, need deterministic output |
| B — Role-play | Expert persona plus chain-of-thought guidance | Deep analysis, ideation, strategy |
| C — Structured decomposition | Split into 3–7 subtasks, each with inputs, outputs and a check | Multi-step work where the model skips steps |
| D — Reverse-engineered | Infer the real goal from a vague request, put the goal first | Exploratory work where you aren't sure what you want |

## When to use it

```
Optimize this prompt and give me a few versions to compare.
How should I word this prompt better?
The model keeps missing my point — rewrite this request clearly.
```

It should also fire when you never say "prompt" but clearly want an instruction to be clearer or more effective.

## Workflow

1. **Restate the intent** in one sentence so it doesn't invent requirements
2. **Ask** one or two key questions when critical information is missing, instead of guessing
3. **Generate four versions**, one per strategy
4. **Present for comparison** in a uniform format with a strategy table at the end

## Output shape

```
## Understanding
[one-sentence restatement]

## Rewrites
### A — Detailed expansion
[complete, copy-pasteable prompt]
### B / C / D …

## Quick comparison
| Strategy | Character | Best for |
```

Every version is a finished, independently usable prompt — copy it and run, no extra explanation needed.

## Principles

- Never change the user's intent — this is about clarity, not new requirements
- Match the input language: Chinese in, Chinese out
- If the original prompt is already good, don't wrap it for the sake of it

## Install

```bash
git clone https://github.com/YardonYan/for-my-self-skills.git
cp -r for-my-self-skills/prompt-optimizer <your-agent-skills-dir>/
```

## License

Apache-2.0, see [LICENSE](./LICENSE).
