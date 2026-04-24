# Prompt — Capability Specification (Week 1 Deliverable 3)

This prompt produces **Deliverable 3** of the Week 1 task, as defined in `SupportingDocs/README-Participants-Week1-Scenarios.md` § *How to work with your chosen scenario*:

> *A first-draft capability specification for the agentic part: purpose, scope, inputs/outputs, decision logic, escalation triggers, integration points. Target 6–10 requirements minimum. Precise enough that an AI coding agent could start building from it.*

It is intentionally scoped to that one deliverable. It does **not** produce the problem statement, delegation analysis, validation design, or the full assumptions register — those are separate prompts under `Week1/Prompts/`.

The bar this deliverable must clear is **buildability**: an AI coding agent reading the capability spec should not need to ask a clarifying question to start building. That bar is codified in `SupportingDocs/production-spec-checklist.md`; this prompt treats it as non-negotiable.

---

## Inputs

- **Scenario file (required):** a prompt-scoped scenario file in the same `Prompts/` folder — e.g. `Week1/Prompts/scenario-1.md`. Contains the scenario text verbatim plus HUMAN assumptions with Assumption / Hypothesis / Test / Confidence.
- **Upstream deliverables (strongly preferred):** the most recent runs of
  - `Week1/Output/Scenario{M}/problem-statement-*.md` (Deliverable 1 — success metrics the spec must serve),
  - `Week1/Output/Scenario{M}/delegation-analysis-*.md` (Deliverable 2 — the boundary the spec must not cross).
  If either exists, load it and treat its work inventory, hard constraints, and boundary-respect metric as authoritative. If it does not exist, flag the gap in the Assumption Log rather than silently re-deriving the boundary.
- **Standing sources** inherited per `CLAUDE.md` § *Prompt Authoring Conventions* (applied automatically, not restated):
  - `CLAUDE.md` — repository structure, Core Entities, diagram rules.
  - `SupportingDocs/Week1-Thinking-Discipline-Primer.md` — reasoning and documentation style.
  - `SupportingDocs/README-Participants-Week1-Scenarios.md` — Week 1 expectations.
  - `SupportingDocs/production-spec-checklist.md` — **the buildability bar this deliverable must clear line-by-line.**
  - `SupportingDocs/spec-ambiguity-vs-builder-mistakes.md` — diagnostic taxonomy used when the build loop surfaces a mismatch.
  - `SupportingDocs/the-fde.md` — FDE Level 1 framing; entity / state-machine / bounded-context discipline.

If the scenario file is not specified at run time, default to `Week1/Prompts/scenario-1.md`.

## Output

Write a new file at:

```
Week1/Output/Scenario{M}/capability-specification-{{scenario-slug}}-{random-3-digits}.md
```

where `{{scenario-slug}}` is the scenario filename without the `.md` extension and `{M}` matches the scenario number. Do not overwrite a previous run — always create a new file so iterations remain auditable.

## Required structure of the output

The output file must contain, in order:

### 1. Front-matter block

- Submission ID (filename without extension).
- Source scenario file path (relative link).
- Links to the upstream problem-statement and delegation-analysis files used, with their run suffixes. If either was not used, say so explicitly.
- Date produced (`DD.MM.YYYY`).
- Status line — e.g. *"first draft, pre-build-loop"* or *"second draft, post-build-loop-1"*.

### 2. Assumption Log (at the top, per primer)

Same shape as in `build-spec.md` Prompt 1, scoped to assumptions that load-bear on the capability spec itself — chiefly feasibility (API shapes, rate limits, integration auth) and viability (retention, audit, governance).

- **Scan table** — one row per assumption: `#`, source (HUMAN / AGENT), one-line assumption, Cagan risk attacked, confidence, which rule / integration / entity is at risk if wrong.
- **Coach-session priority queue** — ordered, highest-leverage first. An assumption that *blocks a capability from being buildable* ranks above one that only shifts a threshold.
- **Update protocol** — standard "update in place, do not silently delete" language from the primer.
- **Full entries** — Assumption / Hypothesis / How I'd test it / Confidence for each numbered entry.

Rules inherited from `CLAUDE.md` § *Prompt Authoring Conventions* apply verbatim:

- Every non-trivial claim is **[CITED]** or **[ASSUMED]** (numbered Assumption Log entry).
- **High** confidence requires coach-session validation.
- Unknowns are marked `[UNKNOWN]` and raised in the Assumption Log — never silently filled in. LMS vendor, tenant URLs, auth flavours, and rate limits are the usual suspects.

### 3. Capability Set Overview

A short paragraph naming the 1–3 capabilities this spec covers and why that decomposition was chosen. Each capability is a bounded context per `SupportingDocs/the-fde.md` — it has its own purpose, its own inputs and outputs, and a named seam with the others.

Name each capability in one line:

1. **Capability 1 — <name>** — one-line purpose.
2. **Capability 2 — <name>** — one-line purpose.
3. **Capability 3 — <name>** — one-line purpose.

If the delegation analysis has more than three capability seams, pick the 1–3 that together cover the routine portion named in the problem statement plus every FULL / HUMAN-IN-LOOP row in the work inventory. Capabilities fully downstream of a HUMAN-LED decision (e.g. "execute after classification is set") stay in scope; capabilities that *make* a HUMAN-LED decision do not.

### 4. Entity Model

One subsection per entity. At minimum include every entity named in the work inventory or hard constraints (typically `Onboarding`, `Task`, `HumanDecision`; scenario-dependent additions as needed).

For each entity, a Markdown table with columns:

| Attribute | Type | Required | Constraints | Notes |
|---|---|---|---|---|

Plus, beneath the table:

- **State machine** (if the entity is stateful) — either a fenced text block listing `from → to : trigger / guard` or a Mermaid `stateDiagram-v2` if triggers in `CLAUDE.md` § *Diagrams* fire (> 3 states or non-linear graph). Always mark `[*]` initial and `-->[*]` terminal.
- **Immutability** — which attributes cannot change after creation.
- **Delete behaviour** — soft vs. hard; retention period (link back to the audit-trail retention cited in the delegation analysis hard-constraints table).

Every state, enum value, and FK named in the entity model must be used in §5 business rules. If it is not used, remove it — unused structure is noise per the production-spec-checklist.

### 5. Capability Specification — one subsection per capability

Repeat the following shape for each capability identified in §3. This is the section the AI coding agent will read most closely; precision wins over prose.

#### 5.n.1 Purpose
One or two sentences. What business outcome does this capability own? What does "done" look like from a human perspective?

#### 5.n.2 Scope

- **In scope:** bullet list of what this capability owns.
- **Out of scope:** bullet list of what it deliberately does not own — particularly anything HUMAN-LED in the delegation analysis. State the *reason* out-of-scope items are out of scope (e.g. *"Setting `employment_class` — HUMAN-LED per §2.2 hard constraint."*).

#### 5.n.3 Inputs

A table:

| Input | Type | Required / Optional | Validation | Source |
|---|---|---|---|---|

Types must be specific — `Workday employee UUID`, `ISO 8601 date`, `enum [A, B, C]`. No `string` without an enum or regex; no `number` without units and bounds.

#### 5.n.4 Outputs

A table:

| Output | Type | Condition | Destination |
|---|---|---|---|

Outputs include entity writes, notifications, webhooks fired, and reports emitted. If the output is a notification, the destination is a role (e.g. *"HR Ops distribution"*) — not a placeholder address.

#### 5.n.5 Business Rules

Numbered, 6–10 minimum per the Week 1 brief — and often more for the orchestrating capability. Each rule uses **must / will / cannot** (checklist requirement). Every numeric threshold is explicit — no *"reasonable time"*, no *"a few days"*. Every conditional is IF/THEN, optionally with ELSE.

Rules must cover, at minimum:
1. **Creation / instantiation** — what creates the entity, uniqueness guard, duplicate handling.
2. **State transitions** — who can move what to what, under which guard.
3. **Deadline computation** — how `due_at` or equivalent is calculated; whether it is immutable after set.
4. **Derived vs. stored state** — e.g. OVERDUE is derived, do not store.
5. **Regulatory / compliance-specific rule** where one applies — e.g. I-9 3-business-day window [CITED IRCA].
6. **Scheduled / time-triggered action** — e.g. day-10 handoff, day-14 audit.
7. **Idempotency** — every external-system write must be idempotent against a named deterministic key.
8. **Boundary guard** — an explicit rule forbidding the agent from taking any HUMAN-LED decision (cite the §2.2 hard constraint by number).

Where a rule depends on a HUMAN assumption, cite it inline (e.g. *"per H4"*). Where a rule depends on an AGENT assumption, cite the number (e.g. *"per A10"*).

#### 5.n.6 Escalation Triggers

A table:

| Trigger code | Condition | Who is notified | What the human must do | SLA |
|---|---|---|---|---|

Every escalation must have a named code (`ESC-<SHORT>` — e.g. `ESC-CLASS`, `ESC-I9`, `ESC-BUDDY-UNAVAILABLE`), a condition stated in terms of state and time (not in terms of intent), a role-level recipient, a specific required action, and a numeric SLA in business days or hours.

An escalation without a specific required human action is a notification, not an escalation — label it accordingly.

#### 5.n.7 Decision Log

A table:

| Decision point | Fields logged | Storage location | Retention |
|---|---|---|---|

Every state transition, every escalation raised, every human decision, and every external-system write must have a log row. Retention aligns with the audit-trail retention cited in the delegation analysis hard constraints (typically 7 years for employment records; 1 year for integration audit).

### 6. Integration Contracts

One subsection per external system named in the scenario or added by a HUMAN assumption (typically Workday, ServiceNow, LMS, Email, plus the two unnamed systems if a HUMAN assumption has identified them — e.g. Benefits, Payroll/Time).

For each:

| Property | Value |
|---|---|
| Purpose | one-line description |
| Endpoint | specific path(s); `[UNKNOWN]` if tenant-specific with an Assumption Log entry |
| Authentication | OAuth flow / API key / service account; secret name in the secrets manager |
| Timeout | seconds |
| Retry logic | 5xx / timeout retry count and backoff pattern; 4xx handling |
| Rate limit | if known; else `[UNKNOWN]` with Assumption Log link |

Plus:

- **Fallback** — what happens when the system is unavailable beyond the retry budget. Never *"we'll retry forever"*; always a specific escalation trigger and a named queue or dead-letter.
- **Data mapping** — a table mapping internal attributes to external fields, with direction arrows (`←` read, `→` write).

A `[UNKNOWN]` in this section that blocks building (e.g. LMS vendor unknown → cannot define completion webhook) must be flagged in the Assumption Log as **build-blocking** and raised to the top of the coach-session priority queue.

### 7. Diagrams (conditional)

Include Mermaid diagrams iff the triggers in `CLAUDE.md` § *Diagrams* fire. For a capability specification the usual candidates are:

- **Sequence / orchestration flow** — the day-N timeline for the orchestrating capability, when it touches four or more external systems with distinct auth, retry, and fallback profiles.
- **State machine** — any entity with more than three states or a non-linear transition graph (typically `Task`).
- **Integration topology** — where four or more external systems interact. Use subgraphs per system.

Follow `CLAUDE.md` § *Diagrams* verbatim: Mermaid only, `classDef agent` / `classDef human`, dashed escalation edges with `ESC-*` labels, human-led node labels suffixed with `(human)`, external systems in named subgraphs, captions cross-referenced from prose.

A diagram must not introduce a state, escalation, or integration that is not already named in §4–§6. If a diagram would need to do so, update the text first.

If no trigger fires, state explicitly: *"No diagram — prose + tables carry the structure for this draft."*

### 8. Self-audit (aligned to `production-spec-checklist.md`)

A checklist the draft must pass before the file is declared complete. Check each box as `[x]` only if it is honestly true of the draft — unchecked boxes are build-blocking and must be resolved before the closed build loop.

- [ ] Every business rule uses **must / will / cannot**.
- [ ] Every numeric threshold is explicit (timeouts, deadlines, SLAs, counts, max sizes) — no *"a few"*, *"quick"*, *"reasonable"*.
- [ ] Every conditional has an explicit IF / THEN (and ELSE where it exists).
- [ ] Every entity has a PK, `created_at`, `updated_at`, and a state machine where stateful.
- [ ] Every integration has endpoint, auth, timeout, retry policy, rate limit, fallback, and data mapping — or an explicit `[UNKNOWN]` traced to an Assumption Log entry.
- [ ] The delegation boundary from Deliverable 2 is respected in full — every HUMAN-LED row is out-of-scope for its capability *and* has a boundary-guard rule in §5.n.5.
- [ ] Every escalation trigger has a code, a state-based condition, a role recipient, a specific required human action, and a numeric SLA.
- [ ] Every external-system write is idempotent on a named deterministic key.
- [ ] Every `[ASSUMED]` or `[UNKNOWN]` in the body has a matching numbered entry in the Assumption Log.
- [ ] No `[TODO]` markers remain open.
- [ ] The Week 1 minimum of 6–10 business rules per capability is met (and an orchestrator capability typically exceeds it).
- [ ] The spec is consistent with the latest problem-statement success metrics and the latest delegation-analysis work inventory — any divergence is called out explicitly.

Close §8 with a one-paragraph **overall buildability read** — which capabilities are buildable now, which are pending a specific Assumption Log entry, and what the recommended next coach-session probe is.

### 9. Out of scope for this deliverable

One short paragraph naming what this file deliberately does *not* cover:

- Problem statement and success metrics (Deliverable 1).
- Delegation analysis — work inventory, hard-constraint rationale (Deliverable 2).
- Validation design — happy path, edge cases, failure modes, boundary tests (Deliverable 4).
- The full assumptions / unknowns register (Deliverable 5).

Cross-link to the companion prompts so a reviewer knows where the rest of the picture lives.

## Self-audit before declaring the output complete

(This is the prompt-level audit, distinct from the in-document §8 buildability audit. Both must pass.)

- [ ] The output sits under `Week1/Output/Scenario{M}/` with the naming convention above, and does not overwrite a prior run.
- [ ] The upstream problem-statement and delegation-analysis files (if present) were loaded and are cross-linked in the front-matter.
- [ ] No row in the delegation analysis has been silently re-classified in this deliverable — if a reclassification is needed, it is flagged in the Assumption Log and the delegation-analysis prompt is re-run instead.
- [ ] The boundary-respect metric from Deliverable 2 is honoured by a concrete boundary-guard rule in every capability's §5.n.5.
- [ ] No validation-design content (happy-path walkthroughs, failure-mode tables, edge-case catalogues) has leaked in from Deliverable 4 — the closest this file comes to validation is specifying *what* is logged and *when* it is escalated, not *how* we would prove the system correct.
- [ ] `SupportingDocs/the-fde.md` was not modified.
- [ ] Every diagram (if any) follows `CLAUDE.md` § *Diagrams* and introduces no new facts.

## Regeneration

If the scenario file or either upstream deliverable changes — especially the delegation analysis's work inventory or hard-constraint table, or the problem statement's success metrics table — regenerate this deliverable rather than hand-editing it. A divergence between the capability spec and the upstream deliverables is a defect, diagnosed the same way a divergence between spec and built software is diagnosed in the closed build loop per `SupportingDocs/spec-ambiguity-vs-builder-mistakes.md`.

