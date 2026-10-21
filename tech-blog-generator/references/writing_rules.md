# Writing Rules Reference — Full 21 Rules

Adapted from agent-style (yzhao062) and classic writing authorities.
Each rule includes: source citation, severity, directive, BAD→GOOD examples, and rationale.

## Severity Scale
- **Critical**: Reader cannot understand or trust the prose if violated.
- **High**: Externally visible AI-tell, or recurring clarity failure.
- **Medium**: Local readability cost, felt by reader but not a trust issue.
- **Low**: Polish or preference; flagged for consistency.

## Escape Hatch (Orwell 1946 Rule 6)
"Break any of these rules sooner than say anything outright barbarous."
Rules are guides to clarity, not ends in themselves.

---

## Canonical Rules (01-12)

### RULE-01: Curse of Knowledge
- **Source**: Pinker 2014, Ch. 3
- **Severity**: Critical
- **Directive**: Do not use technical terms or acronyms that have not been established for the reader's background level. Do not launch into mechanics before naming the purpose. Before writing, name the intended reader.
- **BAD**: We use contrastive learning with InfoNCE and a momentum encoder.
- **GOOD**: Our method uses contrastive learning — a technique that trains representations to distinguish similar from dissimilar pairs. InfoNCE serves as the loss function, and a slowly-updating momentum encoder stabilizes training.
- **Rationale**: LLMs default to expert-register from training distributions. The failure mode is invisible to the writer but glaring to the wrong-audience reader.

### RULE-02: Active Voice When Agent Matters
- **Source**: Orwell 1946 Rule 3; S&W §II.14
- **Severity**: High
- **Directive**: Do not write "X was done by Y" when "Y did X" fits. When the agent is genuinely unknown (scientific attribution, observation of phenomena), passive is correct — use deliberately, not by default.
- **BAD**: The experiments were conducted on eight NVIDIA A100 GPUs.
- **GOOD**: We ran the experiments on eight NVIDIA A100 GPUs.
- **BAD**: Errors are logged to /var/log/app.log.
- **GOOD**: The service logs errors to /var/log/app.log on restart.
- **Rationale**: Passive hides the agent, drops responsibility, and forces readers to reconstruct who did what.

### RULE-03: Concrete over Abstract
- **Source**: S&W §II.16; Pinker 2014 Ch. 3
- **Severity**: High
- **Directive**: Replace category words (factors, aspects, considerations, issues, elements) with the specific items they refer to. If you reach for a category word, ask: what exactly?
- **BAD**: Several architectural considerations influenced our design decisions.
- **GOOD**: We chose a two-tower retrieval architecture because (1) the query-side embedding caches across sessions, and (2) the document-side index updates nightly without re-running inference.
- **Rationale**: Generic nouns are an AI-tell — the model names a category without naming what the category contains.

### RULE-04: Cut Needless Words
- **Source**: S&W §II.17; Orwell 1946 Rule 3
- **Severity**: High
- **Directive**: "In order to" → "to"; "due to the fact that" → "because"; "at this point in time" → "now"; "it is important to note that" → delete and state the fact; "may potentially" → "may".
- **BAD**: It is important to note that the learning rate was reduced in order to prevent divergence.
- **GOOD**: We reduced the learning rate to prevent divergence.
- **Rationale**: Every filler phrase signals that substance is about to arrive; delete the phrase and let the substance arrive directly.

### RULE-05: No Dying Metaphors
- **Source**: Orwell 1946 Rule 1
- **Severity**: Medium
- **Directive**: Do not use prefabricated phrases: "game-changer", "cutting-edge", "in today's digital landscape", "unlock the power of". Write what you actually mean.
- **BAD**: This framework unlocks the power of reactive programming.
- **GOOD**: This framework provides a declarative API for composing asynchronous data streams.

### RULE-06: No Unnecessary Jargon
- **Source**: Orwell 1946 Rule 5; Pinker 2014 Ch. 2
- **Severity**: Medium
- **Directive**: "Utilize" → "use"; "leverage" → "use (or explain the leverage)"; "facilitate" → "help/enable"; "commence" → "start".
- **BAD**: We leverage Kubernetes to facilitate container orchestration.
- **GOOD**: We use Kubernetes to manage container deployment, scaling, and networking.

### RULE-07: Affirmative Form
- **Source**: S&W §II.15
- **Severity**: Medium
- **Directive**: Make affirmative claims in affirmative form. "Not insignificant" → "significant"; "did not remember" → "forgot".
- **BAD**: The impact on latency was not insignificant.
- **GOOD**: The change reduced p95 latency by 40ms.

### RULE-08: Claim-Evidence Alignment
- **Source**: Pinker 2014 Ch. 6; Gopen & Swan 1990
- **Severity**: Medium
- **Directive**: Do not overstate or understate claims relative to evidence. "Dramatically improved" without numbers is dishonest.
- **BAD**: The optimization dramatically improved throughput.
- **GOOD**: The optimization increased throughput from 850 to 1200 req/s on our benchmark workload.

### RULE-09: Parallel Structure
- **Source**: S&W §II.19
- **Severity**: Medium
- **Directive**: Express coordinate ideas in similar form. All items in a list should match grammatically.
- **BAD**: The system handles authentication, processing requests, and logs management.
- **GOOD**: The system handles authentication, processes requests, and manages logs.

### RULE-10: Keep Related Words Together
- **Source**: S&W §II.20; Gopen & Swan 1990
- **Severity**: Medium
- **Directive**: Keep subject-verb-object close. Don't bury the action between long modifiers.
- **BAD**: An announcement, after much deliberation and consultation with stakeholders across all teams, was made that the service would restart.
- **GOOD**: After consulting stakeholders across all teams, the team announced the service restart.

### RULE-11: Stress Position
- **Source**: Gopen & Swan 1990
- **Severity**: Medium
- **Directive**: Place new or important information at the end of the sentence. The stress position is where readers expect the payload.
- **BAD**: We fixed the bug that caused production downtime last Tuesday.
- **GOOD**: Last Tuesday's production downtime traced back to a single bug: a nil pointer in the session handler.

### RULE-12: Vary Sentence Length
- **Source**: S&W §II.18; Pinker 2014 Ch. 4
- **Severity**: Medium
- **Directive**: Break sentences over 30 words. Alternate short and long for rhythm. Combine adjacent thoughts that share a tight relationship; split them when the break does useful work.

---

## Field-Observed Rules (A-I)

### RULE-A: No Bullet-Point Abuse
- **Severity**: High
- **Directive**: Do not convert prose into bullet points unless the content is genuinely a list. Two items or a single sentence rarely justify bullet formatting. Three-item parallel lists still count as list work.

### RULE-B: No Em-Dash Default
- **Severity**: Low
- **Directive**: Do not use em dashes as casual sentence punctuation. Prefer commas, colons, conjunctions, or full stops unless the dash clearly earns its keep.

### RULE-C: Vary Sentence Openings
- **Severity**: Medium
- **Directive**: Do not start consecutive sentences with the same word or phrase.

### RULE-D: No Transition-Word Overuse
- **Severity**: Medium
- **Directive**: "Additionally", "Furthermore", "Moreover" — justify, don't default. Let adjacent paragraphs share continuity without signpost openers.

### RULE-E: No Paragraph-Closing Summaries
- **Severity**: Medium
- **Directive**: Do not close every paragraph with a summary sentence. Trust the reader to follow the argument.

### RULE-F: Consistent Terminology
- **Severity**: High
- **Directive**: Use consistent terms; do not redefine abbreviations mid-document. Pick one term per concept and stick to it.

### RULE-G: Title Case for Headings
- **Severity**: Low
- **Directive**: Use title case for section and subsection headings. Articles, short prepositions, and coordinating conjunctions stay lowercase.

### RULE-H: Citation Discipline (Critical)
- **Severity**: Critical
- **Directive**: Support factual claims with citation or concrete evidence. Every assertion about performance, behavior, or design must be backed by a specific number, code reference, or documented decision.

### RULE-I: Full Forms in Formal Prose
- **Severity**: Low
- **Directive**: Prefer full forms over contractions in formal technical prose. "it is" over "it's", "cannot" over "can't". This does not apply to tutorials or casual formats.
