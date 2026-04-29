# Checklist — Delegation Suitability Matrix (Deliverable #2)

> Use this **after** generating your Delegation Suitability Matrix to verify completeness.

## Completeness check

### Assumption Log

- [ ] Appears at top of document
- [ ] Every `[ASSUMED]` tag in the body has a matching numbered entry

### Suitability gate (pre-filter)

- [ ] Each candidate checked against the 4 suitability gate criteria from `atx-scoring.md` § Step 1
- [ ] Tasks solvable with static rules / RPA flagged as "not an agent" — don't force them into an archetype
- [ ] Tasks with hard blocks on data/system access flagged as "blocked" with a path-to-unblock noted

### Suitability scoring table

- [ ] Every micro-task / JtD cluster from Deliverable #1 appears
- [ ] Scored on all 7 dimensions: Input structure, Decision determinism, Tool coverage, Context complexity, Exception rate, Latency constraint, Risk/compliance
- [ ] Each score is H/M/L with a short justification (not just a letter)
- [ ] Scores reference evidence from the scenario or Deliverable #1, not generic reasoning

### Archetype assignment

- [ ] Each task cluster assigned one of: Human Only / Human-led + Automation Support / Human-led + Agent Support / Agent-led + Human Oversight / Fully Agentic
- [ ] **At least 2 different archetypes** appear across all task clusters
- [ ] Each assignment has a **written rationale** citing which dimensions drove the decision
- [ ] Boundary cases (tasks near the edge between two archetypes) are flagged with the tension explained

### Anti-pattern check

| Anti-pattern | How to detect | Fix |
|---|---|---|
| **Everything is fully agentic** | Only one archetype in the matrix | Re-examine risk/compliance and exception rate dimensions — some tasks need human oversight |
| **No rationale** | Archetype column filled but no explanation | Add 1–2 sentences per row citing the key dimensions |
| **Ignoring tool/API gaps** | Task scored as agentic but the required system has no API (e.g. Saba LMS) | Score Tool coverage honestly; flag as a constraint on the archetype |
| **Conflating automation with agentic** | Deterministic rule-following tasks scored as "fully agentic" | Route to "Human-led + Automation Support" or RPA — agents are for non-determinism |

## Feed-forward

- Archetype assignments feed directly into **Deliverable #3** (Volume × Value — which work stream is the primary agentic target)
- The highest-value "Agent-led" or "Fully Agentic" cluster becomes the focus of **Deliverable #4** (Agent Purpose Document)

