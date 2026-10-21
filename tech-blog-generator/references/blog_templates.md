# Blog Structure Templates

Use these templates as starting points. Adapt to the specific content, don't copy blindly.

## 1. Tutorial

```
---
title: "How to [Achieve Goal] with [Technology]"
description: "A practical guide to [goal], covering [key topics]."
tags: [tutorial, technology, language]
genre: tutorial
---

## Prerequisites
- [Tool/Knowledge needed]
- [Version requirement]

## Setup
[Step-by-step setup, with commands]

## Step 1: [Action]
[Code + explanation]

## Step 2: [Action]
[Code + explanation]

...

## Result
[What the reader built/accomplished]

## Gotchas
- [Common pitfall 1]
- [Common pitfall 2]

## Next Steps
- [What to learn next]
- [Related topics]
```

## 2. Deep Dive

```
---
title: "[Concept]: How [Technology] [Does Something] Under the Hood"
description: "An in-depth analysis of [mechanism], with benchmarks and source code walkthrough."
tags: [deep-dive, technology, internals]
genre: deep-dive
---

## The Problem
[What problem does this mechanism solve? Concrete example.]

## Architecture Overview
```text
[ASCII diagram of the system/mechanism]
```

## How It Works
### Core Algorithm
[Code + line-by-line explanation]

### Data Flow
[Step-by-step flow with diagram]

### Edge Cases
- [Edge case 1]: [how it's handled]
- [Edge case 2]: [how it's handled]

## Benchmarks
| Scenario | Before | After | Delta |
|----------|--------|-------|-------|
| [Case 1] | [number] | [number] | [Δ] |

## When Not to Use
[List scenarios where this approach fails]

## References
- [Source code link]
- [Related paper/docs]
```

## 3. Comparison

```
---
title: "[Technology A] vs [Technology B]: Which One Should You Use?"
description: "A data-driven comparison of [A] and [B] across performance, DX, ecosystem, and real-world use cases."
tags: [comparison, technology-a, technology-b]
genre: comparison
---

## Context
[Why this comparison matters. What decision it helps with.]

## At a Glance
| Criterion | A | B |
|-----------|---|---|
| First release | | |
| License | | |
| Performance | (number) | (number) |
| Learning curve | | |
| Ecosystem | | |

## Deep Comparison
### Performance
[Concrete benchmarks, not opinions]

### Developer Experience
[Specific examples: API design, error messages, tooling]

### Real-World Use Cases
[Companies/projects using each, success stories, failure stories]

## When to Choose A
- [Scenario]

## When to Choose B
- [Scenario]

## Recommendation
[Specific, context-dependent guidance, not a one-size-fits-all verdict]
```

## 4. Postmortem / Retrospective

```
---
title: "Postmortem: [Incident Name] — [Date]"
description: "Root cause analysis and prevention plan for [incident]."
tags: [postmortem, incident, reliability]
genre: postmortem
---

## Timeline
| Time (UTC) | Event |
|------------|-------|
| 14:00 | [Initial trigger] |
| 14:05 | [Detection] |
| 14:12 | [Mitigation started] |
| 14:30 | [Resolution] |

## Impact
- Duration: [X minutes]
- Affected users: [Y%]
- Business impact: [concrete description]

## Root Cause
[Specific line of code, config change, or external event that caused the failure]

## Why It Wasn't Caught
- [Missing test]
- [Missing alert]
- [Missing documentation]

## Fixes
### Immediate
- [What was done during the incident]

### Long-term
- [Systemic improvements]

## Prevention Plan
| Action | Owner | Timeline |
|--------|-------|----------|
| [Add integration test] | [Name] | [Date] |
```

## 5. Quick Tip

```
---
title: "[One-Line Problem → Solution]"
description: "[Solution] — a quick pattern for [use case]."
tags: [quick-tip, technology]
genre: quick-tip
---

## The Problem
[One sentence: what you want to do, and why the obvious way fails]

## The Solution
```language
// Code showing the pattern
```

## How It Works
[2-3 sentences explaining the key insight]

## One Gotcha
[Single, specific thing to watch out for]

## When to Use / When Not to Use
- Use when: [1-2 scenarios]
- Avoid when: [1-2 scenarios]
```

## 6. Architecture Overview

```
---
title: "[System Name]: Architecture and Design Decisions"
description: "How [system] is structured, why those choices were made, and what constraints shaped them."
tags: [architecture, system-design, technology]
genre: architecture
---

## Context
[What this system does. Who uses it. What constraints exist.]

## Design Goals
1. [Goal 1]: [why it matters]
2. [Goal 2]: [why it matters]

## System Architecture
```text
[ASCII or Mermaid diagram of components and data flow]
```

## Key Design Decisions
### Decision 1: [What we chose]
- **Alternatives considered**: [A, B, C]
- **Why we chose X**: [specific reasons with trade-offs]
- **Trade-offs**: [what we gave up]

### Decision 2: [What we chose]
...

## Data Flow
### Read Path
[Step-by-step with diagram]

### Write Path
[Step-by-step with diagram]

## Observability
- Metrics: [key metrics exposed]
- Alerts: [what triggers an alert]
- Dashboards: [where to see system health]

## Future Work
- [Planned improvements]
- [Known limitations]
```
