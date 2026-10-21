# Style Guide - Technical Writing Anti-Patterns (v2.0)

## Forbidden Phrases (DO NOT USE)

### Pedagogical Tone
- "Let's learn..."
- "I hope this helps"
- "As you know..."
- "Beginners often..."
- "Teacher" / "Student" / "Tutor"
- "Follow along"
- "Step-by-step" (use numbered steps without the word)
- "You might be wondering..."
- "In this article, we will..." (just do it, don't announce it)
- "Without further ado..."

### AI Fluff (The Dead List)
- "In today's digital landscape..."
- "In today's fast-paced world..."
- "Unlock the power of..."
- "The future is bright..."
- "Welcome to..."
- "Exciting journey..."
- "Keep coding!"
- "Happy learning!"
- "Stay tuned!"
- "Let's dive in!" / "Let's dive deep!"
- "Buckle up!"
- "Game-changer"
- "Cutting-edge"
- "Revolutionary" (without evidence)
- "World-class"
- "Best-in-class"
- "Industry-leading" (without evidence)

### Filler Phrases (Replace Immediately)
| Don't Use | Use Instead |
|-----------|------------|
| It is important to note that | (Delete, state the fact) |
| It is worth mentioning that | (Delete, state the fact) |
| In order to | to |
| Due to the fact that | because |
| At this point in time | now |
| In the event that | if |
| May potentially | may |
| Could possibly | could |
| It may be necessary to | (State what's needed) |
| A number of | several / many (or give the number) |
| The vast majority of | most |
| In close proximity to | near |
| With the exception of | except |

### Vague Descriptions (Quantify or Delete)
| Vague | Replace With |
|-------|-------------|
| efficient | (Number: p95 latency, throughput, memory usage) |
| robust | (Mechanism: retry logic? circuit breaker? validation?) |
| optimized | (Metric: before vs after numbers) |
| powerful | (Capability: what can it do that alternatives can't?) |
| significantly improved | (How much? 3%? 3x? On what metric?) |
| various factors | (List the factors) |
| multiple scenarios | (Name the scenarios) |
| meaningful impact | (Describe the impact with numbers) |

## Required Patterns

### Code Block → Explanation
Every code block MUST be followed by:
1. **File reference** (e.g., `handler.go:45-78`)
2. **What it does** (one sentence)
3. **Why it's designed that way** (one sentence)
4. **Input/Output** specifics
5. **Gotcha** (one non-obvious pitfall, if applicable)

### Comparisons
When comparing A vs B, always include:
| Aspect | A | B |
|--------|---|---|
| Definition | | |
| Mechanism | | |
| When to use | | |
| When to avoid | | |
| Performance | (concrete numbers) | (concrete numbers) |

### Concrete Anchors (per WRITING.md)
Each substantial paragraph must carry at least one:
- A proper noun the reader could look up
- A specific number that is not just a date or version
- A direct quote
- A named decision, moment, or thread
- A checkable detail

Does NOT count:
- many, various, several, a lot of
- in ways that mattered, meaningful changes, broad implications
- milestone names or dates standing alone

## Voice Guidelines

- Use imperative mood: "Use X instead of Y"
- Avoid passive: "The function returns" not "The value is returned by the function"
- Address as peer: "The reader should..." not "You should..." (tutorials can use direct "you")
- Start where the answer starts, stop where the answer stops
- No keynote cadence, no ceremonial wrap-ups
- No service-desk tone: no "Great question!", "Absolutely!", "Feel free to reach out"

## Structural Patterns

### Good Paragraph Shape
```
Claim → Evidence → Implication
```
Not:
```
Setup → Claim → Restatement → Closing thought
```

### Good Opening
"The `jobChan` (main.go:45) is a buffered channel with capacity 100."
Not:
"Concurrency is a fundamental concept in modern software development..."

### Good Closing
"Swap `Mutex` for `RWMutex` when reads outnumber writes by more than 5:1."
Not:
"I hope this article has helped you understand concurrency in Go. Happy coding!"
