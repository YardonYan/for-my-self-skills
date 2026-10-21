# Self-Review Checklist

Run this checklist on every draft before final output. No skipping passes.

## Pass 1: Structure Audit

### Opening
- [ ] Does the first paragraph tell the reader what problem this solves? (Not "what this article is about")
- [ ] Is there a concrete detail in the first 100 words?
- [ ] Does the title match the actual content? (Read both and check)

### Body
- [ ] Is genre-appropriate structure followed? (Tutorial ≠ Deep Dive ≠ Comparison)
- [ ] Does every section have a clear purpose? (Could you title each section as a question it answers?)
- [ ] Are there abstract sections without diagrams or concrete examples? → Add one or cut
- [ ] Is there a 500+ word section without a code block, diagram, or table? → Break it up
- [ ] For tutorials: can the reader follow steps without jumping between sections?
- [ ] For deep dives: is the core mechanism explained before edge cases?

### Closing
- [ ] Does the conclusion match what was promised in the introduction?
- [ ] Is the conclusion a summary of facts, or a ceremonial wrap-up? → Cut the ceremony
- [ ] Is the last sentence substantive? (If you can delete it without losing information, delete it)

## Pass 2: Sentence-Level Audit

### Kill List (Ctrl+F and destroy)
- [ ] "in today's" → 0 occurrences
- [ ] "unlock the power" → 0 occurrences
- [ ] "game-changer" / "cutting-edge" → 0 occurrences
- [ ] "let's" (used pedagogically) → 0 occurrences
- [ ] "dive in" / "dive deep" → 0 occurrences
- [ ] "it is important to note" → 0 occurrences
- [ ] "in order to" → 0 occurrences (replace with "to")
- [ ] "due to the fact that" → 0 occurrences (replace with "because")
- [ ] "may potentially" → 0 occurrences
- [ ] "leverage" (without explanation) → 0 occurrences (replace with "use")
- [ ] "utilize" → 0 occurrences (replace with "use")
- [ ] "I hope this helps" / "Feel free to reach out" / "Stay tuned" → 0 occurrences

### Concrete Anchor Check
- [ ] Paragraph 1: has at least one proper noun, number, quote, or checkable detail? □
- [ ] Paragraph 2: same check □
- [ ] Paragraph 3: same check □
- [ ] ... (every paragraph) □

### Sentence Variety
- [ ] Any 3+ consecutive sentences starting with the same word? → Vary
- [ ] Any sentence over 40 words? → Split
- [ ] Any 5+ consecutive sentences under 8 words? → Combine some

### Code Blocks
- [ ] Every code block has a file reference? (file.go:line)
- [ ] Every code block has a "What / Why / I/O" explanation immediately after?
- [ ] No code block exceeds 30 lines without being broken into logical sections?
- [ ] All code fences have language tags?

### Vague Language
- [ ] "efficient" → quantified or replaced
- [ ] "robust" → mechanism explained or replaced
- [ ] "optimized" → before/after numbers or replaced
- [ ] "powerful" → specific capability listed or replaced
- [ ] "significant" → number given or replaced
- [ ] "various" / "multiple" → items listed or replaced

### Passive Voice
- [ ] Count passive constructions where agent is known: if >5 for the whole article, rewrite active
- [ ] Scientific/observation passives (agent genuinely unknown): leave as-is

## Pass 3: Reader Perspective Audit

### The "New Reader" Test
Read the first 3 paragraphs as if you have:
- Never seen this codebase
- Never used this technology in production
- 2 years of general programming experience

- [ ] Can you follow the argument without external knowledge?
- [ ] Every acronym is either defined or common enough not to need definition?
- [ ] The code examples build on each other, not random snippets?

### The "Peer Review" Test
Imagine a senior engineer reading this:
- [ ] Would they find it condescending? → Remove any "teaching" tone
- [ ] Would they challenge any unsupported claims? → Add evidence
- [ ] Would they find the code examples useful or trivial? → Increase complexity or cut

### The "Busy Reader" Test
Imagine someone with 2 minutes to decide whether to read this:
- [ ] Does the first paragraph make them want to continue?
- [ ] Can they scan headings and get the main argument?
- [ ] Does the conclusion stand alone as a useful takeaway?

### The "Chinese Reader" Test (if applicable)
- [ ] Any 「主持人」口吻 (host tone) sentences → deleted
- [ ] Any buzzwords from the blocklist → replaced with concrete actions
- [ ] Chinese quotation marks consistent: 「」
- [ ] No "不是...而是..." oppositional syntax
- [ ] No empty evaluation words: 很顺/很清楚/很现实

## Final Sanity Checks

- [ ] File references are correct (verify against actual uploaded files)
- [ ] Code snippets compile/run (spot-check critical paths)
- [ ] No hallucinated API parameters or function names
- [ ] All external claims have citations or are flagged as interpretation
- [ ] Tags and frontmatter are present and accurate

## Quality Gate

- ✅ All 3 passes complete? → Ready to emit
- ❌ Any critical rule violated? → Rewrite affected sections, re-run audit
- ⚠️ Only medium/low issues? → Fix them and emit
