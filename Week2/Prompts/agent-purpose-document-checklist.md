# Checklist — Agent Purpose Document (Deliverable #4)

> Use this **after** generating your Agent Purpose Document and **before** the closed build loop.

## Completeness check

### Assumption Log

- [ ] Appears at top of document — this is the **single consolidated log** for the entire deliverable set
- [ ] KPI targets and cost-per-case estimates logged as assumptions where not scenario-given
- [ ] All assumptions from other deliverables (D1–D3, D5–D7) are consolidated here with unique IDs

### Agent identity

- [ ] **Agent Name** — descriptive, not generic (e.g. "Onboarding Coordination Agent" not "HR Agent")
- [ ] **Job to be Done** — a cognitive contract, not a feature list. States the outcome the agent produces.
- [ ] **Business context** — which department, process, and customer/user journey step

### Primary objectives and KPIs

- [ ] At least 2 primary objectives (what success looks like)
- [ ] KPIs include all 5: Accuracy, Coverage, Throughput, Cost per case, HITL rate
- [ ] Each KPI has a **target** and an **acceptable ceiling/floor** (not just a single number)
- [ ] KPI targets are plausible given scenario volumes — tag speculative targets as `[ASSUMED]`

### Failure modes

- [ ] At least 2 failure modes named
- [ ] Each includes: what bad output looks like, consequence, recovery path
- [ ] At least one failure mode addresses the delegation boundary (agent acts when it should escalate)

### Delegation archetype

- [ ] One archetype named with written rationale referencing Deliverable #2 scores
- [ ] Rationale explains why adjacent archetypes were rejected (e.g. "not fully agentic because Risk/Compliance dimension scored H on compliance path selection")

### Escalation triggers

- [ ] At least 3 escalation triggers
- [ ] Each has: condition → target role (who gets escalated to)
- [ ] At least one trigger covers confidence/ambiguity (not just hard rules)

### Autonomy matrix

- [ ] 4 tiers present: Decides alone / Acts then notifies / Proposes for approval / Human takes over
- [ ] **At least 3 tiers populated** — if only "decides alone" has entries, the delegation thinking is incomplete
- [ ] Each entry specifies the decision or action (not just categories)
- [ ] Monetary or risk thresholds are explicit where applicable

## Build loop readiness check

Before handing to Claude Code, verify:

- [ ] Could a developer read this and know what to build without asking clarifying questions?
- [ ] Are system interfaces named (not just "the HR system")?
- [ ] Are input/output formats specified or at least described?
- [ ] Are edge cases from the scenario addressed (not hand-waved)?

## Anti-pattern check

| Anti-pattern | How to detect | Fix |
|---|---|---|
| **Purpose is a feature list** | "The agent will: create records, send emails, update statuses…" | Rewrite as a cognitive contract: what outcome does the agent produce? |
| **Autonomy matrix is all "decides alone"** | Only one tier populated | Move high-risk and high-exception items to oversight tiers |
| **No delegation boundary in failure modes** | Failures are all technical (API down, model hallucination) | Add a failure mode for the agent acting beyond its delegation authority |
| **KPIs without targets** | "Accuracy: measure %" with no number | Set a target and an acceptable floor, even if assumed |

## Feed-forward

- System interfaces named here become the input for **Deliverable #5** (System/Data Inventory)
- Escalation triggers inform **Deliverable #6** (Discovery Questions — what would change the escalation design?)
- This document is the artefact for the **closed build loop** and the **Thursday peer review submission**

