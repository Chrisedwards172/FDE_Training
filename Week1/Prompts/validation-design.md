# Prompt — Validation Design (Week 1 Deliverable 4)

This prompt produces **Deliverable 4** of the Week 1 task, as defined in `SupportingDocs/README-Participants-Week1-Scenarios.md` § *How to work with your chosen scenario*:

> *A first-draft validation design with at least 3 scenarios spanning happy path, edge case, and failure mode — including at least one failure scenario that tests the delegation boundary itself.*

It is intentionally scoped to that one deliverable. It does **not** produce the problem statement, delegation analysis, capability spec, or the full assumptions register — those are separate prompts under `Week1/Prompts/`.

The bar this deliverable must clear: every scenario names *what "working" looks like in testable terms* and ties each failure mode to a specific decision in the capability spec — per the primer anti-pattern to avoid, *"'we'll write tests' without specifying what behaviour they'd defend"*.

---

## Inputs

- **Scenario file (required):** a prompt-scoped scenario file in the same `Prompts/` folder — e.g. `Week1/Prompts/scenario-1.md`. Contains the scenario text verbatim plus HUMAN assumptions with Assumption / Hypothesis / Test / Confidence.
- **Upstream deliverables (strongly preferred):** the most recent runs of
  - `Week1/Output/Scenario{M}/problem-statement-*.md` (Deliverable 1 — metrics the validation must exercise),
  - `Week1/Output/Scenario{M}/delegation-analysis-*.md` (Deliverable 2 — the boundary the failure scenarios must probe),
  - `Week1/Output/Scenario{M}/capability-specification-*.md` (Deliverable 3 — business rules, state machines, escalation triggers, and integration contracts the scenarios exercise).

  If any are missing, flag the gap in the Assumption Log rather than silently re-deriving the spec. Validation that does not trace to specific spec rules is not validation — it is decoration.

- **Standing sources** inherited per `CLAUDE.md` § *Prompt Authoring Conventions* (applied automatically, not restated):
  - `CLAUDE.md` — repository structure, Core Entities, diagram rules.
  - `SupportingDocs/Week1-Thinking-Discipline-Primer.md` — reasoning and documentation style; specifically the *"failure modes tied to specific decisions in the spec"* standard.
  - `SupportingDocs/README-Participants-Week1-Scenarios.md` — Week 1 expectations.
  - `SupportingDocs/production-spec-checklist.md` — quality bar; a scenario that does not reference a specific rule or state transition is a sign the underlying spec is under-specified, not that the validation needs softening.
  - `SupportingDocs/spec-ambiguity-vs-builder-mistakes.md` — the diagnostic taxonomy this deliverable is built to feed during the closed build loop.
  - `SupportingDocs/the-fde.md` — FDE Level 1 framing.

If the scenario file is not specified at run time, default to `Week1/Prompts/scenario-1.md`.

## Output

Write a new file at:

```
Week1/Output/Scenario{M}/validation-design-{{scenario-slug}}-{random-3-digits}.md
```

where `{{scenario-slug}}` is the scenario filename without the `.md` extension and `{M}` matches the scenario number. Do not overwrite a previous run — always create a new file so iterations remain auditable.

## Required structure of the output

The output file must contain, in order:

### 1. Front-matter block

- Submission ID (filename without extension).
- Source scenario file path (relative link).
- Links to the upstream problem-statement, delegation-analysis, and capability-specification files used, with their run suffixes. If any were not used, say so explicitly and raise the gap in the Assumption Log.
- Date produced (`DD.MM.YYYY`).
- Status line — e.g. *"first draft, pre-build-loop"* or *"second draft, post-build-loop-1 (FM-3 added after builder misread rule 7)"*.

### 2. Assumption Log (at the top, per primer)

Same shape as in `build-spec.md` Prompt 1, scoped to assumptions that load-bear on validation itself — chiefly, assumptions about what the scenario's baseline behaviour actually is today, what "correct" looks like for judgment cases, and whether the synthetic data that will drive the tests is representative.

- **Scan table** — one row per assumption: `#`, source (HUMAN / AGENT), one-line assumption, Cagan risk attacked (Value / Usability / Feasibility / Viability), confidence, which test scenario is at risk if wrong.
- **Coach-session priority queue** — highest-leverage first. An assumption that would change a scenario's expected outcome ranks above one that only changes the test data shape.
- **Update protocol** — standard "update in place, do not silently delete" language.
- **Full entries** — Assumption / Hypothesis / How I'd test it / Confidence.

Rules inherited from `CLAUDE.md` § *Prompt Authoring Conventions* apply verbatim.

### 3. Validation Strategy (brief)

Three to five sentences naming the shape of the validation:

- The deliverable produces **scenario-level** validation, not unit-test cases. Each scenario is a named situation with a named expected outcome, traceable to one or more rules in the capability spec.
- Each scenario carries a **P / F / E** marker: **P** (positive — must pass on happy-path implementation), **F** (failure — exercises a failure mode the design must absorb), **E** (edge — tests a non-obvious boundary case).
- The **delegation-boundary test(s) in §7 are the load-bearing piece of this deliverable** — they are the closest Week 1 comes to proving the FDE skill is real.

### 4. Happy Path (≥ 1)

A single, concrete happy-path scenario walking a typical case end-to-end through the orchestrating capability. Use the scenario's own numbers (hire volume, task count, systems) as the backdrop; specify one concrete input set.

Structure per happy-path scenario:

- **Scenario name + P/F/E tag.**
- **Input state** — every input field from the capability spec's §5.n.3 set to a specific value. No placeholders; if the scenario file gives a named role / location, use one.
- **Timeline** — numbered steps by day / time, each step naming the rule it exercises (e.g. *"Day 0: agent creates Onboarding per rule 1; instantiates ~40 tasks per rule 2."*). This is the point where the validation stops being prose and becomes a walk-through of the spec.
- **Expected output** — final state of every entity touched, count of escalations raised (should be zero in the happy path), count of human decisions logged (zero or one, depending on the scenario).
- **Success criteria** — explicit list of what must be true for the scenario to pass. Each criterion references a specific rule, log table, or state.

### 5. Edge Cases (≥ 3)

A table covering non-obvious boundary cases. Each row must trace to a business rule, a state transition, or a hard constraint in the capability spec or delegation analysis.

| # | Scenario | Input / trigger | Expected outcome | Rule(s) exercised | P/F/E |
|---|---|---|---|---|---|

Rules for the table:

- Include at minimum a **duplicate input** case (e.g. same webhook delivered twice — exercises idempotency rule), a **missing-but-permitted input** case (e.g. `employment_class = UNSET` at event), a **race / ordering** case (e.g. concurrent state change mid-write), and a **boundary-value** case (e.g. task processed at exactly `due_at + 1s`).
- Expected outcome names the end state, not the intent. *"Second event logged `duplicate_ignored`"* is acceptable; *"system handles duplicate"* is not.
- Every row cites the specific rule number or escalation code from the capability spec. A row without a citation is a sign the underlying spec is silent — raise it as an Assumption Log entry.

### 6. Failure Modes (≥ 3)

A table of failure modes the system must absorb. Each row names a specific failure and the spec-defined response.

| # | Failure | Agent response | Recovery path | Rule(s) / escalation | Detection signal |
|---|---|---|---|---|---|

Rules for the table:

- Include at minimum: an **integration outage** (external system returns 5xx beyond the retry budget), a **missing webhook / silent dependency** (a completion signal that never arrives), an **agent misread** (the agent took a routine path on an input that should have been treated as non-standard — the recovery path must involve a logged `HumanDecision` correction), and a **stale / out-of-order data** case (e.g. `start_date` shifts after `Onboarding` creation).
- **Agent response** names a specific mechanism (queue, nag cadence, ESC-* code, idempotency guard) — never *"we'll handle it"*.
- **Recovery path** names who acts, what they do, and which decision-log entry it produces.
- **Detection signal** names the observable — a log row, a metric, or a dashboard state — that tells operators the failure happened. Per the primer, a failure mode with no detection signal is not absorbed, it is hidden.

### 7. Delegation Boundary Test(s) (≥ 1 — required)

This is the load-bearing scenario. Produce at least one, and where the delegation analysis surfaces more than one open tension, produce one per tension.

Structure per boundary test:

- **Scenario name + F tag.**
- **Set-up** — a concrete input that *looks* to a naive agent like it should cross the boundary. Draw from the scenario text or HUMAN assumptions — e.g. a hire labelled `FULL_EMPLOYEE` in Workday with an attached engagement letter that reads like an SOW-style contractor structure.
- **Expected agent behaviour** — a short paragraph stating what the agent must do *and must not do*. Cite the §2.2 hard constraint number and the §5.n.5 boundary-guard rule from the capability spec.
- **Failure shapes** — a bullet list of the specific mis-behaviours that would count as boundary violations, each tied to the rule they would break. Include at least:
  - *Agent infers or derives the human-led decision and flips its processing path* → boundary violation.
  - *Agent blocks the workflow demanding reclassification / reconsideration* → boundary violation (the decision is HUMAN-LED, not agent-blocked).
  - *Agent passes through and the discrepancy is caught downstream by the named human role* → acceptable; the boundary held.
- **Success criteria** — the assertion set that would prove the boundary held: no state transition was taken that depends on the human-led input; an ESC-* was raised iff the condition for it was met; the decision log contains the human decision, not an agent decision, as the actor.

Where a HUMAN assumption has shifted a row from HUMAN-LED to FULL DELEGATION (e.g. the buddy three-factor filter under H4), add a **second** boundary test exercising the new fully-delegated path — e.g. a case where the filter yields a valid match but HR exercises their post-hoc override within the override window. The point is to prove the *new* boundary also holds, not only the old one.

### 8. Trace Matrix — scenarios ↔ spec rules

A compact matrix mapping each scenario to the capability-spec rules it exercises. This is how a reviewer sees at a glance whether every load-bearing rule has at least one scenario, and whether any scenario has been included without a rule to defend.

| Scenario ID | Capability | Rules / escalations exercised | Metric(s) defended |
|---|---|---|---|

- Every business rule in every capability's §5.n.5 must appear in the *Rules exercised* column of at least one scenario. A rule with zero scenarios is either dead code or a validation gap — call it out explicitly under the matrix.
- Every metric in the problem-statement success-metrics table must appear in the *Metric defended* column of at least one scenario. The boundary-respect non-negotiable metric must be defended by at least one §7 test.

Below the matrix, a short paragraph naming:

- Rules not yet covered by any scenario — and why (e.g. *"rule 9 idempotency is covered transitively by EC-2; no standalone scenario"*).
- Scenarios that exercise a rule the spec does not yet contain — these are spec gaps, raised as Assumption Log entries.

### 9. Diagrams (conditional)

Include Mermaid only when `CLAUDE.md` § *Diagrams* triggers fire. For a validation design, the realistic candidates are:

- A **sequence diagram** for the happy path or the boundary test, when timing + external calls + escalation branches interact in ways prose cannot carry in a glance.
- A **state diagram** of a `Task` lifecycle annotated with which scenario drives each transition, if the state graph is non-linear.

Follow `CLAUDE.md` § *Diagrams* verbatim: Mermaid only; `classDef agent` / `classDef human`; dashed escalation edges with `ESC-*` labels; human-led node labels suffixed with `(human)`; captions `*Figure N — …*` cross-referenced from prose.

A diagram in this deliverable must not introduce a state, escalation, or rule that is not already named in the capability spec. If it would, fix the capability spec first and regenerate.

If no trigger fires, state explicitly: *"No diagram — tables carry the structure for this draft."*

### 10. Self-audit

A checklist the draft must pass before the file is declared complete. Tick `[x]` only if honestly true.

- [ ] At least one happy path, three edge cases, three failure modes, and one delegation-boundary test are present.
- [ ] Every scenario carries a P / F / E marker.
- [ ] Every scenario cites at least one specific rule, escalation code, or hard constraint from the upstream capability spec / delegation analysis.
- [ ] Every failure mode has a named detection signal (log row, metric, dashboard state).
- [ ] Every boundary test names the specific mis-behaviours that would count as violations, each tied to the rule they would break.
- [ ] The trace matrix shows every §5.n.5 business rule exercised by at least one scenario, and flags any that are not.
- [ ] The trace matrix shows every success metric defended by at least one scenario, including the non-negotiable boundary-respect metric.
- [ ] No new business rules, states, escalations, or integrations have been introduced in this deliverable — if one was needed, it was raised as a spec gap in the Assumption Log and the capability-spec prompt is re-run instead.
- [ ] Every `[ASSUMED]` or `[UNKNOWN]` in the body has a matching numbered entry in the Assumption Log.
- [ ] No `[TODO]` markers remain open.
- [ ] Diagrams (if any) follow `CLAUDE.md` § *Diagrams* and introduce no new facts.

Close §10 with a one-paragraph **overall validation read** — whether the design, as drafted, would surface a boundary violation if the builder produced one, and which scenario is recommended as the first to run in the closed build loop.

### 11. Out of scope for this deliverable

One short paragraph naming what this file deliberately does *not* cover:

- Problem statement and success metrics (Deliverable 1).
- Delegation analysis (Deliverable 2).
- Capability specification — new rules, entities, escalations, integrations (Deliverable 3).
- The full assumptions / unknowns register (Deliverable 5).

Cross-link to the companion prompts under `Week1/Prompts/` so a reviewer knows where the rest of the picture lives.

## Self-audit before declaring the output complete

(Prompt-level audit, distinct from the in-document §10 audit. Both must pass.)

- [ ] The output sits under `Week1/Output/Scenario{M}/` with the naming convention above, and does not overwrite a prior run.
- [ ] The upstream problem-statement, delegation-analysis, and capability-specification files (where present) were loaded and are cross-linked in the front-matter.
- [ ] No row in the delegation analysis or capability spec has been silently re-classified or re-scoped in this deliverable — if a change is needed, it is flagged in the Assumption Log and the upstream prompt is re-run instead.
- [ ] The deliverable's scenario count clears the Week 1 minimum (≥ 1 happy + ≥ 3 edge + ≥ 3 failure + ≥ 1 boundary) and the coverage is substantive, not filler.
- [ ] `SupportingDocs/the-fde.md` was not modified.

## Regeneration

If the scenario file or any upstream deliverable changes — especially when the capability spec adds or removes a rule, escalation code, or state transition — regenerate this deliverable rather than hand-editing it. The trace matrix is the cheapest place in the programme to notice drift between spec and validation, and the closed build loop depends on it staying honest. A validation design that does not mirror the current capability spec is a defect, diagnosed the same way per `SupportingDocs/spec-ambiguity-vs-builder-mistakes.md`.

