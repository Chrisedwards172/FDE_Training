# Prompt — Agent Specification (Gate 1 Deliverable 3)

This prompt produces **Deliverable 3** of the Gate 1 timed exercise, as defined in [`Week1/Gate1/SupportingDocs/Gate1-Participant-Pack.md`](../SupportingDocs/Gate1-Participant-Pack.md) §4:

> **Agent specification** — *Purpose, scope, inputs/outputs, decision logic, escalation triggers, integration contracts, state model, error handling. Precise enough that Claude Code could begin building from it. This is the largest deliverable — expect to spend the most time here.*

It is intentionally scoped to that one deliverable. It does **not** produce the problem statement, delegation analysis, validation design, or the full assumptions & unknowns register — those are separate prompts under `Week1/Gate1/Prompts/`.

The bar this deliverable must clear is **buildability**, against Pack §6.3 verbatim:

> *Would an AI coding agent need to guess at intent? Entities defined, state machines named, integration contracts explicit (endpoint / auth / request / response / timeout / retry / fallback), decision logic with concrete thresholds.*

That bar is reinforced by `SupportingDocs/production-spec-checklist.md`; this prompt treats it as non-negotiable. Pack §7 calls out three anti-patterns that bite this deliverable in particular: *Hand-waving verbs*, *Implicit state*, and *Integration hand-wave*. The self-audit explicitly checks for all three.

---

## Inputs

- **Scenario file (required):** [`Week1/Gate1/gate-scenario.md`](../gate-scenario.md). Contains the §3 scenario text verbatim plus any HUMAN assumptions captured during the timed exercise. **There is no coach session inside the Gate 1 window** (Pack §2 — 2.5 hours, scenario unseen, submission closes before the Live Walkthrough). Treat everything that is not directly cited from the scenario or the Pack as an **assumption**. No assumption in this deliverable can carry **High** confidence.
- **Gate 1 Participant Pack (authoritative):** [`Week1/Gate1/SupportingDocs/Gate1-Participant-Pack.md`](../SupportingDocs/Gate1-Participant-Pack.md). Pack §4 fixes the deliverable's required content list; §6.3 fixes the buildability bar; §7 *"Hand-waving verbs"*, *"Implicit state"*, and *"Integration hand-wave"* anti-patterns apply directly.
- **Upstream deliverables (strongly preferred):** the most recent runs of
  - `Week1/Gate1/Output/problem-statement-{{scenario-slug}}-{NNN}.md` (Deliverable 1 — success metrics the spec must serve, especially M1 SLA, M2 routing-quality, M5 boundary-respect),
  - `Week1/Gate1/Output/delegation-analysis-{{scenario-slug}}-{NNN}.md` (Deliverable 2 — the boundary the spec must not cross, the work inventory, and the hard-constraints table).
  If either exists, load it and treat its work inventory, hard constraints, and boundary-respect metric as authoritative. If it does not exist, flag the gap in the Assumption Log rather than silently re-deriving the boundary.
- **Standing sources** inherited per `CLAUDE.md` § *Prompt Authoring Conventions* (applied automatically, not restated):
  - `CLAUDE.md` — repository structure, Core Entities, diagram rules.
  - `SupportingDocs/Week1-Thinking-Discipline-Primer.md` — reasoning and documentation style.
  - `SupportingDocs/production-spec-checklist.md` — **the buildability bar this deliverable must clear line-by-line.**
  - `SupportingDocs/spec-ambiguity-vs-builder-mistakes.md` — diagnostic taxonomy used when the build loop surfaces a mismatch.
  - `SupportingDocs/the-fde.md` — FDE Level 1 framing; entity / state-machine / bounded-context discipline.

If the scenario file is not specified at run time, default to `Week1/Gate1/gate-scenario.md`.

## Output

Write a new file at:

```
Week1/Gate1/Output/agent-specification-{{scenario-slug}}-{random-3-digits}.md
```

where `{{scenario-slug}}` is the scenario filename without the `.md` extension (e.g. `gate-scenario`). Do not overwrite a previous run — always create a new file so iterations remain auditable.

## Required structure of the output

The output file must contain, in order:

### 1. Front-matter block

- Submission ID (filename without extension).
- Source scenario file path (relative link).
- Links to the upstream problem-statement and delegation-analysis files used, with their run suffixes. If either was not used, say so explicitly and raise an Assumption Log entry.
- Date produced (`DD.MM.YYYY`).
- Status line — *"Gate 1 timed-exercise draft, no coach-session validation possible per Pack §2."* All assumptions in §2 sit at **Medium** or **Low** by construction; **High** is not available for this deliverable.

### 2. Assumption Log (at the top, per primer)

Same shape as in the other Gate 1 prompts, scoped to assumptions that load-bear on the agent spec itself — chiefly **feasibility** (SOAP / REST API shapes, request/response envelopes, auth flavours, rate limits, p95 latency) and **viability** (audit retention, governance, cost per execution).

- **Scan table** — one row per assumption: `#`, source (HUMAN / AGENT), one-line assumption, Cagan risk attacked, confidence, which rule / integration / entity is at risk if wrong.
- **Walkthrough / client-validation priority queue** — ordered, highest-leverage first. An assumption that *blocks a capability from being buildable* (e.g. *"SOAP WSDL is unknown; cannot define coverage-validation request envelope"*) ranks above one that only shifts a threshold. None of these get resolved before submission.
- **Update protocol** — standard "update in place, do not silently delete" language from the primer. Confidence ratings cannot move to **High** within the Gate 1 window.
- **Full entries** — Assumption / Hypothesis / How I'd test it / Confidence for each numbered entry.

Rules inherited from `CLAUDE.md` § *Prompt Authoring Conventions* apply, with the same Gate 1-specific tightening as the sibling prompts:

- Every non-trivial claim is **[CITED]** (scenario text, named regulation, explicit prompt rule) or **[ASSUMED]** (numbered Assumption Log entry).
- **High** confidence is unavailable per Pack §2; entries sit at **Medium** or **Low**.
- Unknowns are marked `[UNKNOWN]` and raised in the Assumption Log — never silently filled in. The usual suspects in this scenario: SOAP WSDL for the legacy policy admin (request/response shape, latency, availability); CRM tenant URLs and OAuth scopes; DMS API and retention policy; ack-channel SDKs (email transactional API, SMS gateway, claimant portal).
- A `[UNKNOWN]` that blocks building (cannot define an integration request envelope, cannot resolve a state transition guard) is flagged **build-blocking** and raised to the top of the priority queue. Pack §4 explicitly permits a *"named scope-out with a concrete plan to resolve"* — silent omission is not the same as an honest scope-out.
- Pack §7 *"Bluffing"* applies: confident integration shapes the scenario did not state — and the participant did not mark as an assumption — will be challenged.

### 3. Capability Set Overview

A short paragraph naming the 1–3 capabilities this spec covers and why that decomposition was chosen. Each capability is a bounded context per `SupportingDocs/the-fde.md` — its own purpose, its own inputs and outputs, a named seam with the others.

Name each capability in one line. For the FNOL scenario, the natural decomposition is the four-step pipeline split along delegation seams; a typical 3-capability cut is:

1. **Capability 1 — FNOL Intake & Extraction** — ingest the FNOL across email / phone transcript / web form, extract structured entities (claimant, policy number, loss date, peril, severity cues), persist raw payload to DMS, create the canonical claim record in CRM.
2. **Capability 2 — Coverage Validation & Triage** — confirm policy in force / coverage / deductible / limit via SOAP, assign severity band, evaluate the *high-value or ambiguous* trigger, route routine claims to the appropriate adjuster queue or escalate to a specialist for human-in-loop sign-off.
3. **Capability 3 — Claimant Acknowledgement & Audit** — issue the 2-hour acknowledgement on the channel of receipt (routine path) or after specialist sign-off (escalated path); emit `HumanDecision` events for every human action; expose quiet-failure detection signals.

If the delegation analysis has more than three capability seams, pick the 1–3 that together cover the FULLY AGENTIC and AGENT-LED WITH HUMAN OVERSIGHT rows in the work inventory. Capabilities fully downstream of a HUMAN-LED decision (e.g. *"adjuster works the claim after routing"*, *"final coverage / liability decision"* — T11 in the upstream delegation analysis) stay out of scope.

### 4. Entity Model

One subsection per entity. At minimum include every entity named in the work inventory or hard constraints — typically `FNOLSubmission` (raw intake artefact), `Claim` (canonical record), `CoverageRecord` (output of validation), `RoutingAssignment`, `Acknowledgement`, `HumanDecision`. Add scenario-dependent entities only when an upstream rule references them.

For each entity, a Markdown table with columns:

| Attribute | Type | Required | Constraints | Notes |
|---|---|---|---|---|

Plus, beneath the table:

- **State machine** (if the entity is stateful) — either a fenced text block listing `from → to : trigger / guard` or a Mermaid `stateDiagram-v2` if triggers in `CLAUDE.md` § *Diagrams* fire (> 3 states or non-linear graph). Always mark `[*]` initial and `-->[*]` terminal. The natural stateful entities here are `Claim` (e.g. `RECEIVED → EXTRACTED → VALIDATED → ROUTED → ACKNOWLEDGED`, with escalation and failure branches) and `RoutingAssignment` (`PROPOSED → CONFIRMED | OVERTURNED`).
- **Immutability** — which attributes cannot change after creation (raw FNOL payload, receipt timestamp, `claim_id`).
- **Delete behaviour** — soft vs. hard; retention period (link back to any audit-trail retention cited in the delegation analysis hard-constraints table; if no retention is cited, raise `[UNKNOWN]` and flag for Deliverable 5).

Every state, enum value, and FK named in the entity model must be used in §5 business rules. If it is not used, remove it — unused structure is noise per the production-spec-checklist and falls foul of Pack §7 *"Implicit state"*.

### 5. Capability Specification — one subsection per capability

Repeat the following shape for each capability identified in §3. This is the section the AI coding agent will read most closely; precision wins over prose. Pack §4 names this deliverable as the *"largest"* — that is by design.

#### 5.n.1 Purpose
One or two sentences. What business outcome does this capability own? What does *"done"* look like from a claimant's perspective and from the insurer's?

#### 5.n.2 Scope

- **In scope:** bullet list of what this capability owns.
- **Out of scope:** bullet list of what it deliberately does not own — particularly anything HUMAN-LED or HUMAN ONLY in the delegation analysis. State the *reason* out-of-scope items are out of scope (e.g. *"Final coverage / liability decision — HUMAN ONLY per HC3."*, *"Specialist confirmation on the escalated branch — AGENT-LED WITH HUMAN OVERSIGHT, in scope but explicitly gated; see business rule §5.n.5.N."*).

#### 5.n.3 Inputs

A table:

| Input | Type | Required / Optional | Validation | Source |
|---|---|---|---|---|

Types must be specific — `policy_number: string matching ^[A-Z0-9-]{6,20}$`, `loss_date: ISO 8601 date`, `peril: enum [AUTO_COLLISION, AUTO_THEFT, PROPERTY_FIRE, PROPERTY_WATER, …]`, `severity_band: enum [S1, S2, S3, S4]`. No `string` without an enum or regex; no `number` without units and bounds. Pack §7 *"Hand-waving verbs"* applies if a type column reads *"text"* or *"object"* without a schema.

#### 5.n.4 Outputs

A table:

| Output | Type | Condition | Destination |
|---|---|---|---|

Outputs include entity writes (CRM claim record, DMS payload, `HumanDecision` event), notifications (specialist queue, on-call alert), webhooks fired, and reports emitted. If the output is a notification, the destination is a role (e.g. *"senior claims specialist for LOB X"*) — not a placeholder address.

#### 5.n.5 Business Rules

Numbered rules, each using **must / will / cannot** (checklist requirement). Every numeric threshold is explicit — no *"reasonable time"*, no *"a few minutes"*. Every conditional is IF/THEN, optionally with ELSE. Pack §6.3 *"decision logic with concrete thresholds"* is the bar.

Aim for as many rules as it takes to make every state transition, every threshold, and every escalation buildable without a clarifying question. As a practical heuristic, an orchestrating capability typically lands at 8–15 rules; a narrow capability at 5–8. Count is a heuristic, not a Pack requirement — completeness is.

Rules must cover, at minimum:

1. **Creation / instantiation** — what creates the `Claim` (an `FNOLSubmission` reaching state `EXTRACTED` with confidence ≥ threshold), uniqueness guard, duplicate-detection rule.
2. **State transitions** — who can move what to what, under which guard. Cite the entity state machine from §4.
3. **SLA computation** — `due_at = received_at + 2h` [CITED Pack §3]; whether `due_at` is immutable after set.
4. **Derived vs. stored state** — e.g. `is_breached` is derived from `due_at` vs. clock, do not store; severity-band is stored after triage.
5. **Escalation trigger logic** — IF *high-value or ambiguous* test fires, THEN `Claim.branch = ESCALATED`; cite the trigger definition (or flag as `[UNKNOWN]` per the upstream D1 / A3 assumption) and the resulting state-transition guard.
6. **Idempotency** — every external-system write (CRM claim creation, CRM routing assignment, DMS payload upload, ack send) must be idempotent against a named deterministic key (e.g. `Idempotency-Key: claim:{claim_id}:ack:{branch}:{recipient_channel}`). Pack §7 *"Integration hand-wave"* applies if any external write is silent on idempotency.
7. **Boundary guard** — an explicit rule forbidding the agent from taking any HUMAN-LED or HUMAN ONLY decision (cite the §5 hard-constraint number from the delegation analysis, typically HC1 / HC3). This is the rule that operationalises the M5 boundary-respect metric.
8. **Quiet-failure surface** — what self-monitored signals (extraction confidence, SOAP error rate, p95 ack-send latency, daily breach %) the capability emits, against which thresholds, and to which alert destination. Detail belongs to Deliverable 4; *the surfaces* belong here.

Where a rule depends on an assumption, cite the number inline (e.g. *"per A7 — SOAP coverage read-paths"*) rather than burying the dependency.

#### 5.n.6 Escalation Triggers

A table:

| Trigger code | Condition (state + time) | Who is notified | What the human must do | SLA |
|---|---|---|---|---|

Every escalation must have a named code (`ESC-AMBIG`, `ESC-HIVAL`, `ESC-COVERAGE-TIMEOUT`, `ESC-SOAP-DOWN`, `ESC-EXTRACTION-LOWCONF`, `ESC-ACK-FAIL`), a condition stated in terms of state and time (not in terms of intent), a role-level recipient, a specific required action, and a numeric SLA in business hours or minutes (the 2-hour SLA is the operational ceiling for routine; escalated SLAs are participant-judged and `[ASSUMED]`).

An escalation without a specific required human action is a notification, not an escalation — label it accordingly.

#### 5.n.7 Decision Log

A table:

| Decision point | Fields logged | Storage location | Retention |
|---|---|---|---|

Every state transition, every escalation raised, every human decision (`HumanDecision` event for T5 / T8 / T10 / T13 in the upstream work inventory), and every external-system write must have a log row. Retention aligns with the audit-trail retention cited in the delegation analysis hard-constraints table; if no retention is cited (the Gate 1 scenario does not), mark `[UNKNOWN]` and flag in the Assumption Log — do not invent a regime (Pack §7 *"Bluffing"*).

### 6. Integration Contracts

One subsection per external system named in the scenario. The Gate 1 scenario names exactly three [CITED Pack §3]: **modern CRM with APIs**, **legacy policy administration system with SOAP endpoints**, **document management system**. The acknowledgement channels (email, SMS, claimant portal) are implied by §3's intake list and the ack step; whether they are one system or three is `[UNKNOWN]` and an Assumption Log entry.

For each:

| Property | Value |
|---|---|
| Purpose | one-line description |
| Protocol | REST / SOAP / webhook / SMTP / SMS API |
| Endpoint | specific path(s); `[UNKNOWN]` if tenant-specific, with an Assumption Log entry |
| Authentication | OAuth flow / API key / mTLS / service account; secret name in the secrets manager |
| Request shape | JSON schema fragment, SOAP envelope skeleton, or named field list — Pack §6.3 names *"request"* explicitly |
| Response shape | JSON schema fragment / SOAP body skeleton / status semantics — Pack §6.3 names *"response"* explicitly |
| Timeout | seconds (typical: 5s for CRM REST per call; 15s for SOAP coverage validation; 30s for DMS upload — all `[ASSUMED]` unless cited) |
| Retry logic | 5xx / timeout retry count and backoff pattern; explicit 4xx handling (400/401/403/404/409 each named) |
| Rate limit | if known; else `[UNKNOWN]` with Assumption Log link |

Plus:

- **Fallback** — what happens when the system is unavailable beyond the retry budget. Never *"we'll retry forever"*; always a specific escalation trigger (`ESC-SOAP-DOWN`, `ESC-CRM-DOWN`, `ESC-ACK-FAIL`) and a named queue or dead-letter. Pack §7 *"Integration hand-wave"* applies otherwise.
- **Data mapping** — a table mapping internal attributes to external fields, with direction arrows (`←` read, `→` write).

A `[UNKNOWN]` here that blocks building (e.g. SOAP WSDL unknown → cannot define coverage-validation request envelope; ack-channel SDK unknown → cannot define the send call) must be flagged in the Assumption Log as **build-blocking** and raised to the top of the priority queue. Pack §4 explicitly allows a *"scope-out with a concrete plan to resolve"* — that is the senior-FDE move under gate conditions.

### 7. Diagrams (conditional)

Include Mermaid diagrams iff the triggers in `CLAUDE.md` § *Diagrams* fire. For an FNOL agent specification the usual candidates are:

- **State machine for `Claim`** — almost always exceeds 3 states once routine and escalated branches plus failure states are included. Use `stateDiagram-v2`.
- **Sequence / orchestration flow** — receipt → extraction → validation → triage → routing → acknowledgement, with the SOAP coverage-validation timeout branch and the escalation veto path. Worth including when the orchestration touches three or more external systems with distinct retry / fallback profiles.
- **Integration topology** — when the agent talks to four or more external systems with distinct auth profiles. With the scenario's three named systems plus one or more ack channels, this trigger usually fires.

Follow `CLAUDE.md` § *Diagrams* verbatim: Mermaid only, `classDef agent` / `classDef human`, dashed escalation edges with `ESC-*` labels matching the §5.n.6 codes, human-led node labels suffixed with `(human)`, external systems in named subgraphs (CRM, Policy Admin SOAP, DMS, Email/SMS/Portal), captions cross-referenced from prose.

A diagram must not introduce a state, escalation, or integration that is not already named in §4–§6. If a diagram would need to do so, update the text first.

If no trigger fires, state explicitly: *"No diagram — prose + tables carry the structure for this draft."*

### 8. Self-audit (aligned to `production-spec-checklist.md` and Pack §6.3 / §7)

A checklist the draft must pass before the file is declared complete. Check each box as `[x]` only if it is honestly true of the draft — unchecked boxes are build-blocking and must be resolved before the closed build loop.

- [ ] Every business rule uses **must / will / cannot** (Pack §7 *Hand-waving verbs* not triggered).
- [ ] Every numeric threshold is explicit (timeouts, deadlines, SLAs, counts, max sizes) — no *"a few"*, *"quick"*, *"reasonable"*.
- [ ] Every conditional has an explicit IF / THEN (and ELSE where it exists).
- [ ] Every entity has a PK, `created_at`, `updated_at`, and a state machine where stateful (Pack §7 *Implicit state* not triggered — every claim state has a creator, an invalidator, and a checker).
- [ ] Every integration has protocol, endpoint, auth, **request shape, response shape**, timeout, retry policy, rate limit, fallback, and data mapping — or an explicit `[UNKNOWN]` traced to an Assumption Log entry. (Pack §6.3 names request/response explicitly; Pack §7 *Integration hand-wave* applies if any are silent.)
- [ ] The delegation boundary from Deliverable 2 is respected in full — every HUMAN-LED or HUMAN ONLY row is out-of-scope for its capability *and* has a boundary-guard rule in §5.n.5.
- [ ] Every escalation trigger has a code, a state-and-time-based condition, a role recipient, a specific required human action, and a numeric SLA. The codes match the `ESC-*` labels used in §7 diagrams.
- [ ] Every external-system write is idempotent on a named deterministic key.
- [ ] Every `[ASSUMED]` or `[UNKNOWN]` in the body has a matching numbered entry in the Assumption Log; build-blocking unknowns are at the top of the priority queue.
- [ ] No assumption in §2 carries **High** confidence; all entries sit at **Medium** or **Low** by construction.
- [ ] No `[TODO]` markers remain open. Where time has run out on a section, it is *named as a scope-out with a concrete resolution plan* (Pack §4) rather than left silently incomplete.
- [ ] Every state transition, threshold, and escalation can be implemented from this document alone without a clarifying question. (Pack §6.3 *"Would an AI coding agent need to guess at intent?"* — answer must be *no*.)
- [ ] The spec is consistent with the latest problem-statement success metrics (especially M1 SLA, M2 routing-quality, M5 boundary-respect) and the latest delegation-analysis work inventory and hard-constraints table — any divergence is called out explicitly.

Close §8 with a one-paragraph **overall buildability read** — which capabilities are buildable now, which are pending a specific Assumption Log entry, and what the highest-leverage open question is for the Live Walkthrough.

### 9. Out of scope for this deliverable

One short paragraph naming what this file deliberately does *not* cover:

- Problem statement and success metrics (Deliverable 1).
- Delegation analysis — work inventory, hard-constraint rationale (Deliverable 2).
- Validation design — happy path, edge cases, failure modes, *quiet-failure* detection (Deliverable 4).
- The full assumptions & unknowns register (Deliverable 5).

Cross-link to the companion prompts in `Week1/Gate1/Prompts/` so a reviewer knows where the rest of the picture lives.

## Self-audit before declaring the output complete

(This is the prompt-level audit, distinct from the in-document §8 buildability audit. Both must pass.)

- [ ] The output sits under `Week1/Gate1/Output/` with the naming convention above, and does not overwrite a prior run.
- [ ] The upstream problem-statement and delegation-analysis files (if present) were loaded and are cross-linked in the front-matter; their boundary-respect metric is honoured by an explicit boundary-guard rule in every capability's §5.n.5.
- [ ] No row in the delegation analysis has been silently re-classified in this deliverable — if a reclassification is needed, it is flagged in the Assumption Log and the delegation-analysis prompt is re-run instead.
- [ ] No validation-design content (happy-path walkthroughs, failure-mode tables, edge-case catalogues, quiet-failure detection algorithms) has leaked in from Deliverable 4 — the closest this file comes to validation is specifying *what* is logged, *what* is escalated, and *what* surfaces are emitted. The *how would we prove the system correct* question is Deliverable 4's.
- [ ] `SupportingDocs/the-fde.md` was not modified.
- [ ] Every diagram (if any) follows `CLAUDE.md` § *Diagrams* and introduces no new facts.
- [ ] No invented integration shape (no fabricated SOAP WSDL, no fabricated CRM tenant URL, no fabricated retention regime). Pack §7 *"Bluffing"* held — every integration `[UNKNOWN]` is named and traced.

## Regeneration

If the scenario file or either upstream deliverable changes — especially the delegation analysis's work inventory or hard-constraints table, or the problem statement's success metrics table — regenerate this deliverable rather than hand-editing it. A divergence between the agent spec and the upstream deliverables is a defect, diagnosed the same way a divergence between spec and built software is diagnosed in the closed build loop per `SupportingDocs/spec-ambiguity-vs-builder-mistakes.md`. Confidence ratings cannot move to **High** within the Gate 1 window (no coach session per Pack §2); regeneration in this gate is therefore driven by *new or revised* assumptions and by *cited* corrections, not by validation upgrades.
