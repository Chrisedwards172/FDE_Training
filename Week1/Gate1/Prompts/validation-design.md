# Prompt — Validation Design (Gate 1 Deliverable 4)

This prompt produces **Deliverable 4** of the Gate 1 timed exercise, as defined in [`Week1/Gate1/SupportingDocs/Gate1-Participant-Pack.md`](../SupportingDocs/Gate1-Participant-Pack.md) §4:

> **Validation design** — *How do you know the agent is working? What do you test? What does failure look like — not just obvious failure, but **quiet** failure (the agent is wrong and no one notices)?*

It is intentionally scoped to that one deliverable. It does **not** produce the problem statement, delegation analysis, agent specification, or the full assumptions & unknowns register — those are separate prompts under `Week1/Gate1/Prompts/`.

The bar this deliverable must clear is **detection of wrongness**, against Pack §6.4 verbatim:

> *Does validation cover happy path, edge cases, and failure modes? Does it include how you would **detect** the agent is wrong — not just confirm it is right?*

That distinction — *detect wrong* vs *confirm right* — is the load-bearing skill being tested. Pack §7 anti-patterns relevant here: *Hand-waving verbs* (a test that says *"system handles X gracefully"* with no observable assertion is filler), *Implicit state* (a scenario whose *expected outcome* is named only as intent, not as state, is filler). The primer's own anti-pattern *"'we'll write tests' without specifying what behaviour they'd defend"* applies in full.

---

## Inputs

- **Scenario file (required):** [`Week1/Gate1/gate-scenario.md`](../gate-scenario.md). Contains the §3 scenario text verbatim plus any HUMAN assumptions captured during the timed exercise. **There is no coach session inside the Gate 1 window** (Pack §2 — 2.5 hours, scenario unseen, submission closes before the Live Walkthrough). Treat everything that is not directly cited from the scenario or the Pack as an **assumption**. No assumption in this deliverable can carry **High** confidence.
- **Gate 1 Participant Pack (authoritative):** [`Week1/Gate1/SupportingDocs/Gate1-Participant-Pack.md`](../SupportingDocs/Gate1-Participant-Pack.md). Pack §4 fixes the deliverable's required content list (with explicit emphasis on quiet failure); §6.4 fixes the bar; §7 anti-patterns apply.
- **Upstream deliverables (strongly preferred — validation that does not trace to specific spec rules is decoration, not validation):** the most recent runs of
  - `Week1/Gate1/Output/problem-statement-{{scenario-slug}}-{NNN}.md` (Deliverable 1 — metrics M1–M5 the validation must exercise),
  - `Week1/Gate1/Output/delegation-analysis-{{scenario-slug}}-{NNN}.md` (Deliverable 2 — boundary HC1–HC4 the failure scenarios must probe; T1–T15 work inventory),
  - `Week1/Gate1/Output/agent-specification-{{scenario-slug}}-{NNN}.md` (Deliverable 3 — business rules R-A-*, R-B-*, R-C-*, state machines, escalation codes ESC-*, integration contracts, and quiet-failure surfaces R-A-10 / R-B-14 / R-C-11 the scenarios assert against).
  If any are missing, flag the gap in the Assumption Log rather than silently re-deriving the spec.
- **Standing sources** inherited per `CLAUDE.md` § *Prompt Authoring Conventions* (applied automatically, not restated):
  - `CLAUDE.md` — repository structure, Core Entities, diagram rules.
  - `SupportingDocs/Week1-Thinking-Discipline-Primer.md` — *"failure modes tied to specific decisions in the spec"* standard.
  - `SupportingDocs/production-spec-checklist.md` — quality bar; a scenario that does not reference a specific rule or state transition is a sign the underlying spec is under-specified, not that validation needs softening.
  - `SupportingDocs/spec-ambiguity-vs-builder-mistakes.md` — the diagnostic taxonomy this deliverable is built to feed during the closed build loop.
  - `SupportingDocs/the-fde.md` — FDE Level 1 framing.

If the scenario file is not specified at run time, default to `Week1/Gate1/gate-scenario.md`.

## Output

Write a new file at:

```
Week1/Gate1/Output/validation-design-{{scenario-slug}}-{random-3-digits}.md
```

where `{{scenario-slug}}` is the scenario filename without the `.md` extension (e.g. `gate-scenario`). Do not overwrite a previous run — always create a new file so iterations remain auditable.

## Required structure of the output

The output file must contain, in order:

### 1. Front-matter block

- Submission ID (filename without extension).
- Source scenario file path (relative link).
- Links to the upstream problem-statement, delegation-analysis, and agent-specification files used, with their run suffixes. If any were not used, say so explicitly and raise the gap in the Assumption Log.
- Date produced (`DD.MM.YYYY`).
- Status line — *"Gate 1 timed-exercise draft, no coach-session validation possible per Pack §2."* All assumptions in §2 sit at **Medium** or **Low** by construction; **High** is not available for this deliverable.

### 2. Assumption Log (at the top, per primer)

Same shape as in the other Gate 1 prompts, scoped to assumptions that load-bear on validation itself — chiefly:

- assumptions about what the scenario's baseline behaviour actually is today (the cited 31% breach / 18% routing-error / 22 min AHT — what calculation produced them?),
- what *"correct"* looks like for judgement cases (the *high-value or ambiguous* trigger as drafted in upstream R-B-6),
- whether the synthetic data driving the scenarios is representative of the 300 FNOLs/day distribution.

Sections required:

- **Scan table** — `#`, source (HUMAN / AGENT), one-line assumption, Cagan risk, confidence, which test scenario / detection rule is at risk if wrong.
- **Walkthrough / client-validation priority queue** — highest-leverage first. An assumption that would change a scenario's expected outcome ranks above one that only changes the test data shape.
- **Update protocol** — standard "update in place, do not silently delete" language. Confidence ratings cannot move to **High** within the Gate 1 window.
- **Full entries** — Assumption / Hypothesis / How I'd test it / Confidence.

Rules inherited from `CLAUDE.md` § *Prompt Authoring Conventions* apply, with the same Gate 1-specific tightening as the sibling prompts. Pack §7 *"Bluffing"* applies: confident assertions about regulator-mandated test cases (e.g. *"NAIC requires an ack-template-substitution test"*) the participant cannot pin to a citation will be challenged.

### 3. Validation Strategy (brief)

Three to five sentences naming the shape of the validation:

- The deliverable produces **scenario-level** validation, not unit-test cases. Each scenario is a named situation with a named expected outcome, traceable to one or more rules in the upstream agent specification.
- Each scenario carries a **P / E / F-loud / F-quiet** marker:
  - **P** (positive) — must pass on a happy-path implementation;
  - **E** (edge) — non-obvious boundary case the spec must absorb;
  - **F-loud** — failure mode where the failure is observable from outside the agent (5xx, timeout, missing webhook, 4xx client error);
  - **F-quiet** — the **Pack §4 quiet-failure case** — *the agent is wrong and no one notices* (a clean response with mis-mapped fields; routing to a plausible-but-wrong adjuster; severity assigned one band off; ack template substitutes a stale field).
- The **delegation-boundary test(s) in §8 plus the quiet-failure detection design in §7 are the load-bearing pieces of this deliverable** — they are the closest Gate 1 comes to proving the FDE skill is real.

### 4. Happy Path (≥ 1)

A single, concrete happy-path scenario walking a typical FNOL end-to-end through Capabilities A → B → C. Use the scenario's own numbers (300 FNOLs/day cadence, 2-hour SLA, named integrations) as the backdrop; specify one concrete input set. The FNOL is routine: e.g. an `EMAIL`-sourced auto-collision claim under a current personal-auto policy with reported damage of $4,800.

Structure per happy-path scenario:

- **Scenario name + P tag.**
- **Input state** — every input field from the upstream §5.A.3 / §5.B.3 / §5.C.3 set to a specific value. No placeholders — name a real (synthetic) policy number, claimant, peril, loss_date, source_channel.
- **Timeline** — numbered steps by time-from-receipt (T+0s, T+5s, T+45s, T+1m, T+2m), each step naming the rule it exercises (*"T+0–5s: Cap A R-A-1 PUTs raw payload to DMS; R-A-2 derives `claim_id`."*). This is the point where validation stops being prose and becomes a walk-through of the upstream spec.
- **Expected output** — final state of every entity touched (`Claim.state = ACKNOWLEDGED`; `RoutingAssignment.state = PROPOSED`; `CoverageRecord.validator = AGENT, validation_confidence = 1.0`; `Acknowledgement.send_status = ACCEPTED`); count of escalations raised (zero in the happy path); count of `HumanDecision` rows (zero — the routine path is fully agentic by design).
- **Success criteria** — explicit list of what must be true for the scenario to pass. Each criterion references a specific R-x-y rule, log entry, or state transition. *"Acknowledgement sent within 2 hours of `received_at` per HC2 / R-A-7"* is acceptable; *"system works"* is not.

### 5. Edge Cases (≥ 3)

A table covering non-obvious boundary cases. Each row must trace to a business rule, a state transition, or a hard constraint in the upstream agent specification or delegation analysis.

| # | Scenario | Input / trigger | Expected outcome | Rule(s) exercised | P/E/F-loud/F-quiet |
|---|---|---|---|---|---|

Rules for the table:

- Include at minimum:
  1. **Idempotent duplicate** — same FNOL webhook delivered twice (same `external_msg_id`). Exercises R-A-2 deterministic `claim_id`, R-A-6 idempotency on CRM `POST /claims`, S9 key convention. Expected: one `Claim` row, one `Acknowledgement`, two webhook receipts logged with `duplicate_ignored`.
  2. **Lapsed-then-reinstated policy** — `loss_date` falls in a coverage-lapse gap. Exercises R-B-2, R-B-11. Expected: `state = COVERAGE_AMBIGUOUS`, `ESC-AMBIG`, no agent-side coverage decision; specialist resolves via `HumanDecision{COVERAGE_AMBIGUOUS_RESOLVED}`.
  3. **SLA boundary** — claim received at exactly `T = received_at + 2h - 1s` (just inside SLA). Expected: ack accepted, `is_breached = false` (R-A-7, derived). Symmetric case at `T + 1s` after `due_at` exercises the breach derivation.
  4. **Multi-channel ack fallback** — phone-originated claim with no mobile on file. Exercises R-C-2 fallback-to-email path. Expected: `Acknowledgement.channel = EMAIL`, not failed.
  5. **Routing-rule miss** — perfectly valid extraction whose `(LOB, peril, geography_state, severity_band)` tuple has no rule. Exercises R-B-7 + S8 + ESC-ROUTING-NOMATCH. Expected: `state = ROUTING_FAILED`, specialist queue.
  6. **Borderline extraction confidence** — `extraction_confidence = 0.849` (just below the S5 threshold of 0.85). Exercises R-A-4, ESC-EXTRACTION-LOWCONF. Expected: claim escalated, no silent-progression.
- Expected outcome names the end **state**, not the intent. *"`Claim.state = COVERAGE_AMBIGUOUS`, `ESC-AMBIG` raised, specialist queue receives event"* is acceptable; *"system handles ambiguity"* is filler.
- Every row cites the specific R-x-y rule, ESC code, or HC reference. A row without a citation is a sign the upstream spec is silent — raise it as an Assumption Log entry.

### 6. Failure Modes — Loud (≥ 3)

A table of **observable** failure modes (5xx, timeout, missing webhook, 4xx client error) the system must absorb. Each row names a specific failure and the spec-defined response.

| # | Failure | Agent response | Recovery path | Rule(s) / ESC | Detection signal |
|---|---|---|---|---|---|

Rules for the table:

- Include at minimum:
  1. **SOAP coverage outage** — Policy Admin returns 5xx beyond the 30s retry budget on R-B-3 / R-B-4. Response: `state = COVERAGE_TIMEOUT`, `ESC-SOAP-DOWN` paged to on-call SRE within 15 min. Detection: `soap_5xx_rate` aggregate (R-B-14) crosses page threshold.
  2. **CRM 5xx during claim creation** — `POST /claims` fails after retry budget on R-A-6. Response: `Claim` parked in `EXTRACTION_FAILED`, `ESC-CRM-DOWN`. Detection: `crm_5xx_rate` (R-A-10).
  3. **Ack send failure** — transactional channel returns 5xx after R-C-6 retries. Response: `state = ACK_FAILED`, `ESC-ACK-FAIL`, manual claimant outreach by specialist. Detection: `ack_5xx_rate` (R-C-11).
  4. **Missing delivery webhook** — channel accepts (202) but no delivery callback within 30 minutes. Response: `Acknowledgement.send_status` stays at `ACCEPTED` (not `DELIVERED`); a sweep flags claims with `ACCEPTED` ages > 30 min; investigation is human-driven.
- **Agent response** names a specific mechanism (queue, retry budget, ESC-* code, idempotency guard) — never *"we'll handle it"*.
- **Recovery path** names who acts, what they do, and which decision-log entry it produces.
- **Detection signal** names the observable — a quiet-failure surface row, an `ESC-*` page, a dashboard state — that tells operators the failure happened. Per Pack §6.4 / the primer: a failure mode with no detection signal is not absorbed, it is hidden.

### 7. Failure Modes — Quiet (≥ 3 — required by Pack §4)

This is the section Pack §4 explicitly demands and Pack §6.4 explicitly tests. *Quiet failure* is the case where the agent **completes** a step with a clean response, no exception, no escalation — and the answer is wrong. The detection design is the deliverable.

For each quiet-failure mode, name:

| # | Quiet failure | Why it stays quiet | Surface signal (from upstream R-A-10 / R-B-14 / R-C-11) | Detection rule (threshold + window) | Verification step (human action to confirm wrongness) | Recovery |
|---|---|---|---|---|---|---|

Include at minimum:

1. **Mis-mapped SOAP fields** — the agent maps `Deductible` ↔ `Limit` correctly per the WSDL but the WSDL itself is mis-documented and the production envelope swaps them. Coverage record looks plausible; downstream payment is wrong. Surface: comparison between agent-recorded `(deductible, limit)` and a sampled spot-check from the policy admin's UI for 1% of claims. Detection: drift > 1% triggers investigation.
2. **Wrong-but-plausible routing** — `(LOB, peril, geography, severity)` matches a rule that points at the *wrong* adjuster queue (e.g. retired skill code never updated). Adjuster picks up, works the claim, never overturns within 24h because they happen to be skilled enough. Surface: `RoutingAssignment.state = OVERTURNED` rate (drives M2). Detection: M2 < 97% target sustained over 5-day window triggers spec-rule audit.
3. **Severity-band drift** — Cap B R-B-5 rubric (per S7) consistently assigns one band low for new perils added to the enum after rubric authorship. Routine path holds; SLA is met; reserves are systematically under-set. Surface: weekly distribution of `severity_band` by `peril` compared against historical baseline. Detection: KL divergence > threshold per peril triggers rubric review.
4. **Ack template variable substitution failure** — `{{adjuster_name}}` not bound; ack sent with literal `{{adjuster_name}}` to the claimant. Send accepted, send_status = ACCEPTED; claimant confused. Surface: pre-send template-lint asserting no `{{` survives substitution; per-template send-rate vs claimant-feedback rate. Detection: any non-zero literal-mustache in production triggers immediate halt of that template.
5. **Extraction-distribution drift** — model degrades silently (e.g. new email-template formatting from a major broker confuses NER). Confidence stays just above 0.85 threshold; claims still progress; field accuracy quietly drops. Surface: `extraction_below_threshold_rate` and per-field mean-confidence aggregates (R-A-10). Detection: 7-day rolling mean confidence drops > 0.05 vs baseline triggers review.
6. **Boundary-violation by extraction confidence margin** — claim with `extraction_confidence = 0.86` (just over threshold) progresses on the routine path; should arguably have escalated under R-B-6's *low-confidence intake* clause but the threshold there is `< 0.95`. Adjuster catches a missed flag; M5 boundary metric is technically satisfied because no `HumanDecision` was bypassed (no human action was required by the spec). The quiet failure is *the spec*, not the build. Surface: rate of overturn / specialist-redirect on claims with `extraction_confidence` in the 0.85–0.95 band. Detection: that rate persistently > population baseline triggers a spec re-tune of the R-B-6 confidence band.

Rules for the table:

- *Why it stays quiet* must be a sentence that would survive a coach challenge — *"the agent does not detect it because the response shape is valid"* is the kind of admission Pack §4 is asking for.
- Detection rules must be **observable in production**, not in test. *"We will run a regression suite weekly"* is fine but is **not** detection — it is confirmation. Pack §6.4 is asking how the agent's wrongness is detected when it is live.
- The verification step must name a specific human role and a specific action — sample audit by claims operations lead; spot-check by senior adjuster; finance reconciliation against payment ledger.
- A quiet failure with no detection rule is **carried as a known accepted risk** in §10's overall validation read, not silently omitted. Pack §4 *"silent omissions"* anti-pattern applies.

### 8. Delegation Boundary Test(s) (≥ 1 — required)

This is the load-bearing scenario for HC1 / HC4 / M5. Produce at least one; produce a second when the upstream delegation analysis surfaces an open tension on the boundary (in the Gate 1 FNOL scenario, that is upstream **D1** — *high-value or ambiguous* trigger codifiability — which always counts as such a tension).

Structure per boundary test:

- **Scenario name + F-quiet tag** (boundary violations are typically silent — that is what makes them dangerous).
- **Set-up** — a concrete input that *looks* to a naive agent like it should cross the boundary. For FNOL, two strong candidates:
  - A claim with `severity_band = S2` (just under the catastrophic S1 line) and `reported_loss_amount = $49,500` (just under the $50,000 R-B-6 threshold per upstream S5/D1) — the claim is one nudge away from `branch = ESCALATED`; everything else is routine.
  - A claim where SOAP returns a clean coverage record but the policy carries an `endorsement_revision_pending` flag (assumed-tacit ambiguity per upstream D1) that R-B-6 does not test for.
- **Expected agent behaviour** — a short paragraph stating what the agent **must** do *and **must not** do*. Cite the specific HC# from the delegation analysis hard-constraints table and the specific R-x-y boundary-guard rule from the agent specification (R-A-8 / R-B-11 / R-B-12 / R-C-8).
- **Failure shapes** — a bullet list of the specific mis-behaviours that would count as boundary violations, each tied to the rule they would break:
  - *Agent infers ambiguity from a tacit signal and silently escalates without a `HumanDecision`* → boundary violation in the **agent → human** direction (the agent took a HUMAN-LED decision unilaterally — R-B-12, R-C-4 broken).
  - *Agent silently downgrades severity to keep the claim on the routine path* → boundary violation in the **human → agent** direction (the agent took a HUMAN-LED decision — R-B-12 broken).
  - *Agent passes through routinely; the receiving adjuster catches the issue and overturns; `RoutingAssignment.state = OVERTURNED` is recorded; M2 logs the overturn* → **acceptable**; the boundary held — what the spec says was followed; the quiet-failure surfaces in §7 are doing their job.
  - *Agent calls SOAP a second time with different parameters to "smooth" the response* → integration-hand-wave / hidden-state defect; the spec does not permit this (R-B-3 has one retry budget; second-call workaround is implicit state).
- **Success criteria** — the assertion set that would prove the boundary held: no state transition was taken that depends on a human-led input; `boundary_violation_count = 0` (R-C-11 invariant); `ESC-BOUNDARY-VIOLATION` is *not* fired (because no violation occurred — but the test must include a paired adversarial case where a violation **is** synthesised and `ESC-BOUNDARY-VIOLATION` **does** fire as a P0 page within 5 minutes per upstream §5.C.6).

The **paired adversarial case is required**: it proves the boundary-respect detector itself works. A boundary test that only proves the happy boundary-held path proves nothing about the production detection mechanism.

### 9. Trace Matrix — scenarios ↔ spec rules ↔ metrics

A compact matrix mapping each scenario from §4–§8 to the upstream agent-specification rules it exercises and the upstream problem-statement metric(s) it defends.

| Scenario ID | Capability | Rules / ESC exercised | HC referenced | Metric(s) defended |
|---|---|---|---|---|

- Every business rule in upstream §5.A.5 / §5.B.5 / §5.C.5 (R-A-1 … R-C-11) must appear in the *Rules exercised* column of at least one scenario. A rule with zero scenarios is either dead spec or a validation gap — call it out explicitly under the matrix.
- Every ESC code defined in upstream §5.A.6 / §5.B.6 / §5.C.6 must be exercised by at least one scenario.
- Every metric M1–M5 must appear in the *Metric defended* column of at least one scenario. **M5 (boundary-respect, non-negotiable) must be defended by at least one §8 test that includes the paired adversarial `ESC-BOUNDARY-VIOLATION` synthesis.**

Below the matrix, a short paragraph naming:

- Rules / ESC codes not yet covered — and why (e.g. *"ESC-DMS-DOWN covered transitively by FM-loud-2; no standalone scenario"*).
- Scenarios that exercise a rule the upstream spec does not yet contain — these are spec gaps, raised as Assumption Log entries; do not silently add the rule here.

### 10. Diagrams (conditional)

Include Mermaid only when `CLAUDE.md` § *Diagrams* triggers fire. For an FNOL validation design the realistic candidates are:

- A **sequence diagram** for the boundary test in §8, where timing + SOAP call + escalation branch + `HumanDecision` write + `ESC-BOUNDARY-VIOLATION` page interact in ways prose cannot carry in a glance.
- A **state diagram** of `Claim` annotated with which scenario drives each transition — only if the upstream §4.2 state diagram is being re-purposed here without modification.

Follow `CLAUDE.md` § *Diagrams* verbatim: Mermaid only; `classDef agent` / `classDef human`; dashed escalation edges with `ESC-*` labels; human-led nodes suffixed with `(human)`; subgraphs for CRM / Policy Admin SOAP / DMS / Email-SMS-Portal where integration calls cross the boundary; captions `*Figure N — …*` cross-referenced from prose.

A diagram in this deliverable must not introduce a state, ESC code, or rule that is not already named in the upstream agent specification. If it would, fix the agent specification first and regenerate that deliverable.

If no trigger fires, state explicitly: *"No diagram — tables carry the structure for this draft."*

### 11. Self-audit (aligned to Pack §6.4 / §7)

A checklist the draft must pass before the file is declared complete. Tick `[x]` only if honestly true.

- [ ] At least **one happy path**, **three edge cases**, **three loud failure modes**, **three quiet failure modes**, and **one delegation-boundary test (with paired adversarial case)** are present. Pack §4's quiet-failure emphasis is honoured by §7 carrying real detection rules, not handwaving.
- [ ] Every scenario carries a P / E / F-loud / F-quiet marker.
- [ ] Every scenario cites at least one specific rule (R-x-y), ESC code, or HC reference from the upstream deliverables. Pack §7 *Hand-waving verbs* not triggered.
- [ ] Every loud failure has a named **detection signal** (quiet-failure surface row, ESC code, dashboard state).
- [ ] Every quiet failure has a named **detection rule** (threshold + window) observable in production, plus a verification step naming the role and the action. Pack §6.4 *"detect the agent is wrong — not just confirm it is right"* answered.
- [ ] The boundary test in §8 includes a **paired adversarial case** that synthesises a violation and asserts `ESC-BOUNDARY-VIOLATION` fires as a P0 page per upstream §5.C.6 within 5 minutes. M5 defended.
- [ ] The trace matrix shows every R-x-y rule exercised by at least one scenario, every ESC code exercised, and every M1–M5 metric defended; rules / ESC / metrics with zero coverage are flagged as gaps.
- [ ] No new business rules, states, ESC codes, or integrations have been introduced in this deliverable — if one was needed, it was raised as a spec gap in the Assumption Log and the agent-specification prompt is re-run instead.
- [ ] No assumption in §2 carries **High** confidence; all entries sit at **Medium** or **Low** by construction.
- [ ] Every `[ASSUMED]` or `[UNKNOWN]` in the body has a matching numbered entry in the Assumption Log.
- [ ] No `[TODO]` markers remain open. Where time has run out on a quiet-failure detection rule, it is *named as an accepted-risk scope-out* (Pack §4) rather than left silently incomplete.
- [ ] Diagrams (if any) follow `CLAUDE.md` § *Diagrams* and introduce no new facts.

Close §11 with a one-paragraph **overall validation read** — whether the design as drafted would surface a boundary violation if the builder produced one (the answer is *yes* iff §8's paired adversarial case asserts `ESC-BOUNDARY-VIOLATION` correctly), which scenario is recommended as the first to run in the closed build loop, and which quiet-failure detection rules are the most likely to be wrong in production.

### 12. Out of scope for this deliverable

One short paragraph naming what this file deliberately does *not* cover:

- Problem statement and success metrics (Deliverable 1).
- Delegation analysis (Deliverable 2).
- Agent specification — new rules, entities, escalations, integrations (Deliverable 3).
- The full assumptions & unknowns register (Deliverable 5).

Cross-link to the companion prompts under `Week1/Gate1/Prompts/` so a reviewer knows where the rest of the picture lives.

## Self-audit before declaring the output complete

(Prompt-level audit, distinct from the in-document §11 audit. Both must pass.)

- [ ] The output sits under `Week1/Gate1/Output/` with the naming convention above, and does not overwrite a prior run.
- [ ] The upstream problem-statement, delegation-analysis, and agent-specification files (where present) were loaded and are cross-linked in the front-matter; M5 is defended; HC1 and HC4 are referenced in the boundary test.
- [ ] No row in the delegation analysis or agent specification has been silently re-classified or re-scoped — if a change is needed, it is flagged in the Assumption Log and the upstream prompt is re-run instead.
- [ ] The deliverable's scenario count clears Pack §4's coverage requirement (happy + edge + loud failure + **quiet failure** + boundary). The quiet-failure section is not a token gesture.
- [ ] `SupportingDocs/the-fde.md` was not modified.
- [ ] No invented regulator-mandated test (Pack §7 *Bluffing* held).

## Regeneration

If the scenario file or any upstream deliverable changes — especially when the agent specification adds or removes a rule, ESC code, state transition, or quiet-failure surface — regenerate this deliverable rather than hand-editing it. The trace matrix is the cheapest place in the gate to notice drift between spec and validation, and the closed build loop depends on it staying honest. Confidence ratings cannot move to **High** within the Gate 1 window (no coach session per Pack §2); regeneration in this gate is therefore driven by *new or revised* assumptions and *new or revised upstream rules / ESC codes*, not by validation upgrades.
