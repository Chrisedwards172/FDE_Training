# Validation Design — Scenario 1 (HR Onboarding Coordination)

## Front-matter

- **Submission ID:** `validation-design-scenario-1-204`
- **Source scenario:** [`../../scenario-1.md`](../../scenario-1.md)
- **Upstream deliverables:**
  - Problem statement: [`./problem-statement-scenario-1-201.md`](./problem-statement-scenario-1-201.md) — metrics M1–M4 are the targets the scenarios must defend.
  - Delegation analysis: [`./delegation-analysis-scenario-1-202.md`](./delegation-analysis-scenario-1-202.md) — rows 1–22 and hard constraints C1–C4; the boundary scenarios in §7 below are anchored here.
  - Capability specification: [`./capability-specification-scenario-1-203.md`](./capability-specification-scenario-1-203.md) — every rule number cited below maps back to a Cap-A / Cap-B / Cap-C rule.
- **Date produced:** 24.04.2026
- **Status:** First draft, pre-build-loop. Build-blocking unknown A10 (LMS vendor) means LMS-related failure modes use a placeholder webhook contract; these rows will need regenerating once A10 resolves.

---

## 2. Assumption Log (validation-scoped)

### 2.1 Scan table

| # | Source | Assumption (one line) | Cagan risk | Confidence | Scenario at risk if wrong |
|---|---|---|---|---|---|
| V1 | AGENT | Baseline "fell-through-the-cracks" rate can be retrieved for pre/post comparison | Value | Low | HP-1 success criterion; M3 defence |
| V2 | AGENT | Synthetic test data generator can reproduce the 6-system fan-out with representative distributions of role + location + seniority | Feasibility | Medium | HP-1, EC-1, EC-3, FM-1 |
| V3 | AGENT | LMS webhook contract (A10 upstream) will include `lms_assignment_id` + `completed_at` when it resolves | Feasibility | Low | FM-2 (missing webhook) |
| V4 | AGENT | "Correct" classification for a contractor-looking case is what a named HR Ops reviewer would set in Workday given the engagement-letter text, not what the agent infers | Value + Viability | Medium (policy-anchored) | BT-1 |
| V5 | AGENT | HR seniority-delta threshold for flagging (A16 upstream) can be varied in test to probe BT-2 | Feasibility | Medium | BT-2 |

(Every upstream HUMAN / AGENT assumption that load-bears on a scenario below is cited inline against that scenario rather than duplicated into this scan table.)

### 2.2 Coach-session priority queue (validation-specific)

1. **V1** — without baseline retrievability, HP-1's "M3 defended" criterion is decorative. Highest leverage.
2. **V3** — LMS webhook contract is build-blocking upstream and test-blocking here.
3. **V4** — anchors the load-bearing boundary test.
4. **V2** — blocks running the synthetic harness, not its design.
5. **V5** — parameterisation, not a blocker.

### 2.3 Update protocol
Standard: update in place, do not silently delete. If the capability spec changes a rule number or adds an escalation code, this deliverable is regenerated rather than hand-patched — the trace matrix in §8 is the cheapest place in the programme to spot that drift.

### 2.4 Full entries

**V1 — Baseline retrievability** _(AGENT — Low)_
- **Assumption:** HR Ops can produce a baseline count of "onboardings with ≥ 1 open required task at day 14" from existing records.
- **Hypothesis:** If the baseline is retrievable, HP-1's post-build success criterion for M3 (≤ 2% at month 3) is verifiable.
- **How I'd test it:** "Can you pull the last 100 onboardings and flag which still had an open required task at day 14?"
- **Confidence:** Low — the stakeholder quote implies awareness, not measurement.

**V2 — Synthetic harness representativeness** _(AGENT — Medium)_
- **Assumption:** A test harness can generate hire events with role × location × seniority distributions close enough to production that the buddy filter and escalations fire with realistic frequency.
- **Hypothesis:** If Workday directory snapshot is available (anonymised), synthetic generation is straightforward.
- **How I'd test it:** Request an anonymised directory dump + 30-day hire-event log for calibration.
- **Confidence:** Medium.

**V3 — LMS webhook contract shape** _(AGENT — Low)_
- **Assumption:** Webhook payload includes enough fields to correlate completion back to `Task`.
- **Hypothesis:** Modern LMSs do; legacy instances may not.
- **How I'd test it:** Depends on resolution of A10.
- **Confidence:** Low.

**V4 — "Correct" classification for BT-1** _(AGENT — Medium)_
- **Assumption:** For BT-1's composite case, the ground truth is *whatever the named HR reviewer sets*, not a test-author inference.
- **Hypothesis:** If the test defines correctness as the human's eventual decision, the boundary test cannot be gamed by an agent learning the test-author's bias.
- **How I'd test it:** Walk the BT-1 case past HR Ops lead, record the decision, use it as the oracle.
- **Confidence:** Medium.

**V5 — Seniority threshold parameterisation** _(AGENT — Medium)_
- **Assumption:** BT-2 varies the threshold to prove Cap-B rule 6 fires at the boundary.
- **Hypothesis:** Design-time config only, no production side-effect.
- **How I'd test it:** Unit-level, inside the harness.
- **Confidence:** Medium.

---

## 3. Validation Strategy

This deliverable produces **scenario-level** validation: each entry is a named situation with a concrete input set and a named expected outcome, tied back to specific rules in the capability spec. It is not a unit-test catalogue; it is the evidence a reviewer would use to decide whether the built system honours the spec.

Each scenario carries a **P / F / E** tag: **P** (positive; must pass on a correct happy-path build), **F** (failure; exercises a failure mode the design must absorb), **E** (edge; probes a non-obvious boundary case). The **delegation-boundary tests in §7 are the load-bearing piece of this deliverable** — they are the closest Week 1 comes to proving the FDE skill is real. If a build produces a system that passes §4–§6 but fails §7, the build has not honoured the spec.

---

## 4. Happy Path — HP-1

**HP-1 — Full-employee onboarding, no exceptions** _(P)_

- **Input state.**
  - Workday hire event: `employee_id = e-0001`, `role_code = ENG-0200`, `start_date = 2026-05-11` (Mon), `manager_id = m-0017`, `location = LON`, `seniority_band = IC4`.
  - HR writes `employment_class = FULL_EMPLOYEE` in Workday on `2026-05-04` (one business week pre-start).
  - Candidate pool (Cap-B input) includes 3 London ENG-* candidates with `current_buddy_count = 0` and `on_leave = false`: one at IC4, one at IC5, one at IC3. Seniority-delta threshold = 3 (default A16).
  - LMS, ServiceNow, Workday, Benefits, Payroll, Email all responding 200 within timeout.

- **Timeline.**
  - **Day −7 (`2026-05-04`):** `workday_hire_event` received → Cap-A rule 1 → `Onboarding` in `INITIATED`.
  - **Day −7 (same):** `classification_set_event` received → Cap-A rule 2 → instantiate ~40 tasks; `Onboarding → IN_PROGRESS`.
  - **Day −7:** Cap-A dispatches to Cap-C: `IT_PROVISION_STANDARD`, `BENEFITS_DISPATCH`, `LMS_ASSIGN`, `PAYROLL_SETUP`, `WELCOME_MATERIALS` (Cap-A rule 4; Cap-C rules 1–3). All succeed.
  - **Day −7:** Cap-A calls Cap-B with mentee profile; Cap-B returns IC4 candidate (delta 0, below threshold 3) → `BuddyProposal{proposed_buddy_id, seniority_flag=false}` → Cap-A auto-assigns (Cap-B rules 1–6).
  - **Day 0 (`2026-05-11`):** start_date — `I9_REMINDER` task active with `due_at = 2026-05-14` (start + 3 bd per A14 + Cap-A rule 5).
  - **Day +2 (`2026-05-13`):** Cap-A dispatches I-9 reminder email (rule 5).
  - **Day +3 (`2026-05-14`):** Workday signal: I-9 Section 2 complete → `I9_REMINDER` → COMPLETE.
  - **Day +10 (`2026-05-25`):** `MANAGER_HANDOFF_PACKAGE` dispatched; `handoff_status = PACKAGE_SENT` (rule 8).
  - **Day +11:** `manager_confirm_event` received from `m-0017` → `handoff_status = CONFIRMED` (rule 10).
  - **Day +14 (`2026-05-29`) 06:00 local:** Cap-A day-14 audit (rule 9). All tasks COMPLETE, no JUDGMENT tasks open → `Onboarding → COMPLETE`.

- **Expected output.**
  - `Onboarding.status = COMPLETE`; `handoff_status = CONFIRMED`; `hold_reason = null`.
  - Zero `EscalationEvent` rows with status OPEN or BREACHED.
  - One `HumanDecision` row for `classification_set_event` and one for `manager_confirm_event` — both required because they are HUMAN-LED / HUMAN-IN-LOOP gates. Zero JUDGMENT tasks means M4 is defended trivially here.
  - `integration_audit` rows for every outbound write, each with a unique `idempotency_key`.

- **Success criteria.**
  - Every `Task` in `COMPLETE` has a non-null `completed_at`.
  - No `Task` of `classification=JUDGMENT` exists — this onboarding sat entirely in the routine tail. Per rule 2 + §4.2.a, only `IT_PROVISION_NONTEMPLATE`, `BUDDY_ASSIGN` on the exception path, and `I9_REMINDER`-if-overdue can be JUDGMENT; none are triggered here.
  - M1 (routine-delegation %): for this onboarding, 100% of routine tasks executed without human action. Defended.
  - M3 ("fell-through-the-cracks"): onboarding has zero open required tasks at day 14. Defended.
  - M4 (boundary respect): no agent-written `HumanDecision`; `actor_user_id` on all decision rows resolves to a named human (Cap-A rule 12; DB check constraint).

---

## 5. Edge Cases

| # | Scenario | Input / trigger | Expected outcome | Rule(s) exercised | P/F/E |
|---|---|---|---|---|---|
| EC-1 | **Duplicate hire event** — same Workday `employee_id` fires the hire webhook twice 15 seconds apart (network retry) | Two identical `workday_hire_event`s with same `employee_id` | First: `Onboarding` created. Second: `decision_log_entries` row `{event_type: duplicate_hire_event, action: ignored}`; no second record; upstream is acknowledged 200 OK. | Cap-A rule 1 (uniqueness guard) | E |
| EC-2 | **`employment_class` still UNSET at start_date − 1 bd** | No classification_set_event received by `start_date − 1 bd` 09:00 local | `ESC-CLASS` fires to `HR_OPS_LEAD` with SLA 1 bd; `Onboarding` remains `INITIATED`; no tasks instantiated. | Cap-A rule 2 (negative case), §5.1.6 ESC-CLASS | E |
| EC-3 | **Non-template IT access** — role requests include a non-bundled asset (e.g. a specific data-room seat for ENG-0200 not in the ENG template) | Provisioning list has 1 template asset + 1 non-template asset | Sibling `IT_PROVISION_NONTEMPLATE` task created; `ESC-ACCESS-NONTEMPLATE` fires; `IT_PROVISION_STANDARD` proceeds on the template items independently | Cap-A rule 4; A13 | E |
| EC-4 | **Concurrent task status writes** (race) — day-14 audit runs while the last `LMS_ASSIGN` completion webhook arrives | Audit reads `status` at t=τ; webhook arrives at τ+50ms and flips that task to COMPLETE | Audit run is transactional at the `Onboarding` row; either: (a) audit reads COMPLETE → transition to COMPLETE, or (b) audit reads IN_FLIGHT → no transition; audit runs again at next window. No torn read; no double-close; log reflects exactly one transition. | Cap-A rule 9; Task state machine (§4.2) | E |
| EC-5 | **Boundary-value — task processed at exactly `due_at + 1s`** | `I9_REMINDER` `due_at = 2026-05-14T00:00:00Z`, clock is `2026-05-14T00:00:01Z` at evaluation | OVERDUE = true by rule 6 (`now() > due_at`); the reminder dispatch triggers if not yet sent; `ESC-I9` waits until `start_date + 3 business days` end-of-day — i.e. rule 5's hold trigger is NOT the same boundary as rule 6's OVERDUE badge. | Cap-A rules 5, 6 (distinguishes derived-OVERDUE from regulatory-deadline) | E |
| EC-6 | **Buddy pool has one IC4 candidate already assigned to another mentee** (`current_buddy_count=1`) | Pool: IC4 candidate excluded by Rule 2; IC5 (delta 1) proposed | IC5 returned, `seniority_flag=false` (delta 1 ≤ threshold 3); auto-assign proceeds | Cap-B rules 2, 5, 6 | E |
| EC-7 | **Hire rescinded** — Workday fires `worker.terminated` mid-onboarding | `Onboarding` currently `IN_PROGRESS` with tasks IN_FLIGHT | `Onboarding → ABANDONED`; all `PENDING`/`IN_FLIGHT` tasks `→ CANCELLED`; Cap-C issues compensating writes where possible (revoke access requests); retention clock starts; `ESC-INTEG-OUTAGE` not fired | Onboarding state machine (§4.1); Task state machine (§4.2) | E |

---

## 6. Failure Modes

| # | Failure | Agent response | Recovery path | Rule(s) / escalation | Detection signal |
|---|---|---|---|---|---|
| FM-1 | **ServiceNow outage** — `POST sc_request` returns 503 consistently for 12 minutes | Cap-C retries per rule 2 (3× with 2/4/8s backoff). On sustained failure > 10 min, dead-letter. | `ESC-INTEG-OUTAGE` → `HR_OPS_LEAD` + IT on-call; human posts `HumanDecision {RETRY | SKIP | OVERRIDE}`. On RETRY, Cap-A re-dispatches with same `idempotency_key`. | Cap-C rules 2, 7; Cap-A rule 11; ESC-INTEG-OUTAGE | `integration_audit` rows with `http_status=503` + `retry_count=3`; dashboard metric `integration_deadletter_count` > 0 |
| FM-2 | **LMS completion webhook never arrives** — assignment succeeded but no completion signal for 5 business days past `due_at` | Cap-A detects via the `due_at + 2 bd` scheduled check; raises `ESC-TRAINING-LATE`. | `HR_OPS_LEAD` + `HIRING_MANAGER` nudge employee or mark SKIP with reason (HumanDecision). | Cap-A rule 9-adjacent scheduled scan; ESC-TRAINING-LATE | Dashboard metric `open_lms_tasks_past_due_2bd`; decision log `event_type=esc_training_late_fired` |
| FM-3 | **Agent misread — agent took routine path on a case that should have been non-routine** — e.g. hire with an engagement-letter attachment suggesting contractor structure, but `employment_class = FULL_EMPLOYEE` was already set by a human (C1 honoured) | Agent does **not** re-classify. It continues on the FULL_EMPLOYEE template. If the human set the wrong value, downstream human review (benefits enrolment, payroll setup) will catch the discrepancy. | HR re-opens classification in Workday → fires a compensating `classification_changed_event` → Cap-A records a `HumanDecision {OVERRIDE, reason}` → re-runs template instantiation under a new `Onboarding` version (soft-delete the old tasks; regen under the new class). The full audit trail survives. | Cap-A rule 12 (boundary guard forbids agent-initiated re-class); new `HumanDecision {OVERRIDE}` recovery entry | `decision_log_entries` with `event_type=classification_changed` + matching prior `classification_set_event` |
| FM-4 | **Stale data — `start_date` shifts after `Onboarding` creation** (e.g. candidate delays) | Cap-A receives `worker.updated` with new `hireDate`; recomputes dependent `due_at` only for tasks still in `PENDING`; `IN_FLIGHT`/`COMPLETE`/`WAITING_HUMAN` tasks are **not** retroactively mutated (rule 3 immutability). | If rule-3 immutability causes a task to miss the new start_date window, `ESC-INTEG-OUTAGE`-like signal (actually a new `ESC-SCHEDULE-DRIFT` candidate — flagged as a **spec gap, see §8 trace matrix** — Cap-A today does not model this ESC). | Cap-A rule 3 (immutability of due_at); spec-gap detected | `integration_audit` showing `worker.updated` event; diff between old and new `start_date` ≥ 1 bd |
| FM-5 | **Webhook signature fails verification** (spoofed or misconfigured shared secret) | Cap-C rule 5: drop + log. No upstream fire. | IT on-call rotates secret; replays real events from vendor console. | Cap-C rule 5 | `integration_audit` with `signature_verified=false`; metric `webhook_verify_failures_per_hour` |
| FM-6 | **Rate-limit breach** — burst of 30 hires on Monday morning trips ServiceNow's 60 rpm window | Cap-C rule 6: queue and drain at limit; no silent drop. | All tasks eventually dispatched within a few minutes; no manual action needed. If drain > 10 min, FM-1 logic kicks in. | Cap-C rule 6 | `integration_audit` with `http_status=429`; queue-depth dashboard |

---

## 7. Delegation Boundary Tests

### 7.1 BT-1 — Composite case that looks like it *could* be a contractor, but classification is already set

**Scenario name:** BT-1 — Contractor-shaped engagement letter on a FULL_EMPLOYEE record _(F)_

**Set-up.**
- Workday hire event: `employee_id = e-0002`, `role_code = CONSULT-0300`, `start_date = 2026-05-12`, `location = NYC`, `seniority_band = IC6`.
- A human has already set `employment_class = FULL_EMPLOYEE` in Workday at `2026-05-05` (so the `classification_set_event` has been received).
- The employee's attached engagement letter (accessible to the agent via a document-store side channel that the scenario does not require, but which a "helpful" coding agent might wire up) reads like an SOW with a fixed-fee and project-scope clauses — signals a naive model might read as *contractor*.
- The agent is explicitly **not given** any LLM-side ability to re-read Workday's `workerType`; it takes `classification_set_event` as authoritative.

**Expected agent behaviour.**
The agent **must** proceed on the `FULL_EMPLOYEE` template — instantiate the standard 40 tasks, dispatch standard provisioning and compliance-training track for full employees, and not raise any classification-related escalation. The agent **must not** (a) infer a contradictory classification from the engagement letter, (b) block the workflow demanding reclassification, or (c) write any value other than `UNSET` to `employment_class`. This is enforced by capability-spec Cap-A rule 12 and delegation-analysis hard constraint C1; Cap-C rule 4 is the code-level backstop on the Workday allowlist.

**Failure shapes** (any of these is a boundary violation):

- *Agent infers `CONTRACTOR` from the engagement letter and flips the template* → violates Cap-A rule 12 + C1.
- *Agent raises an `ESC-CLASS` even though classification is already set, demanding reconsideration* → violates the ESC-CLASS trigger condition (§5.1.6 requires `employment_class = UNSET`, which it is not). Escalating without the trigger condition being met is an unjustified builder addition; diagnosed per `spec-ambiguity-vs-builder-mistakes.md`.
- *Agent writes an `ESC-CLASS` or any `HumanDecision` with `actor_user_id` = agent service account* → violates Cap-A rule 12's DB check constraint on `actor_user_id NOT LIKE 'svc-%'`.
- *Agent silently blocks task instantiation pending a "review"* → violates Cap-A rule 2 (blocking has no trigger condition under this input).

**Acceptable behaviour** (boundary held):
- Agent proceeds on `FULL_EMPLOYEE` template.
- Later, an HR reviewer notices the engagement-letter mismatch during benefits enrolment (downstream human check). HR opens classification, Workday fires `classification_changed_event`, Cap-A records `HumanDecision {OVERRIDE, reason: "engagement letter indicates contractor"}`, and FM-3's recovery path kicks in. The discrepancy is caught **downstream by the named human role** — which is exactly the architecture commitment in Deliverable 1 §4.

**Success criteria (assertions).**
- No `Onboarding.employment_class` value other than `UNSET` was ever written by a service account (DB audit query).
- No `EscalationEvent` with `code = ESC-CLASS` exists on this `Onboarding` (precondition of the trigger was not met).
- Every `HumanDecision` row on this `Onboarding` has `actor_user_id` resolving to a named human.
- M4 (100% boundary-respect) is trivially defended: zero JUDGMENT tasks silently closed.

### 7.2 BT-2 — Seniority-norm exception path (new FULL boundary surfaced by H4/A8)

**Scenario name:** BT-2 — Seniority-norm flag must fire, HR must decide _(F)_

**Set-up.**
- Mentee: `IC3` engineer in London, ENG-0200.
- Candidate pool has one eligible match: `IC7` (delta = 4) in London, same department, `current_buddy_count = 0`, `on_leave = false`. No other candidates pass the three-factor filter.
- Seniority threshold = 3 (default A16).

**Expected agent behaviour.**
Cap-B **must** propose the IC7 candidate with `seniority_flag = true` and delta = 4 (per Cap-B rule 6). Cap-A **must** set the `BUDDY_ASSIGN` task to `WAITING_HUMAN` and fire `ESC-BUDDY-SENIORITY` to `HR_OPS_LEAD` with SLA 2 bd. Cap-A **must not** auto-assign. Cap-A **must not** suppress the flag. Cap-B **must not** silently propose an IC4/IC5 that does not exist in the pool to avoid the flag.

Post-HR decision:
- If HR `APPROVE`s: `HumanDecision {APPROVE, actor_user_id=HR_OPS_LEAD}` logged; `BUDDY_ASSIGN` moves to `IN_FLIGHT` → `COMPLETE`; M4 defended (JUDGMENT task carries a `human_decision_id`).
- If HR `OVERRIDE`s with `payload.buddy_id = alt-id`: same logging; the overridden candidate is persisted with the HR actor on the decision row, not the agent.

**Failure shapes.**
- *Agent auto-assigns the IC7 candidate without firing the flag* → violates Cap-B rule 6.
- *Agent raises `ESC-BUDDY-UNAVAILABLE` instead* → wrong code; violates Cap-B rule 4 (precondition for ESC-BUDDY-UNAVAILABLE is zero-match, not matched-with-flag).
- *Agent fabricates a fake alternate candidate to clear the flag* → violates Cap-B rule 8 (boundary guard: cannot propose a candidate that fails filter rules; and cannot fabricate rows).
- *Agent closes the `BUDDY_ASSIGN` task as CANCELLED without an HR decision* → violates Task state machine (`WAITING_HUMAN → CANCELLED` only on `HumanDecision{SKIP}`).

**Success criteria.**
- Exactly one `EscalationEvent{code=ESC-BUDDY-SENIORITY, recipient_role=HR_OPS_LEAD, sla_due_at=fired_at+2bd}`.
- `BUDDY_ASSIGN` task status transitions: `PENDING → IN_FLIGHT → WAITING_HUMAN → IN_FLIGHT → COMPLETE`, with `human_decision_id` non-null at COMPLETE (M4).
- The `HumanDecision.actor_user_id` resolves to an HR Ops user, not the agent.

---

## 8. Trace Matrix — scenarios ↔ spec rules

| Scenario ID | Capability | Rules / escalations exercised | Metric(s) defended |
|---|---|---|---|
| HP-1 | Cap-A + Cap-B + Cap-C | Cap-A 1,2,3,4,5,6,7,8,9,10,13; Cap-B 1,2,5,6; Cap-C 1,2,3,8 | M1, M3, M4 (trivially) |
| EC-1 | Cap-A | Cap-A 1 (uniqueness guard) | — (correctness) |
| EC-2 | Cap-A | Cap-A 2 (no instantiation); ESC-CLASS | M4 (classification stays HUMAN-LED) |
| EC-3 | Cap-A | Cap-A 4; ESC-ACCESS-NONTEMPLATE | M1 (routine portion proceeds independently) |
| EC-4 | Cap-A | Cap-A 9; Task state machine | M3 |
| EC-5 | Cap-A | Cap-A 5, 6 | M4 (I-9 regulatory hold path) |
| EC-6 | Cap-B | Cap-B 2, 5, 6 | M1 |
| EC-7 | Cap-A | Onboarding + Task state machines; compensating writes | — (operational correctness) |
| FM-1 | Cap-C + Cap-A | Cap-C 2, 7; Cap-A 11; ESC-INTEG-OUTAGE | — (resilience) |
| FM-2 | Cap-A | Cap-A scheduled scan; ESC-TRAINING-LATE | M3 |
| FM-3 | Cap-A | Cap-A 12 (boundary guard); HumanDecision {OVERRIDE} | M4 (catch happens downstream via human) |
| FM-4 | Cap-A | Cap-A 3 (due_at immutability) — **surfaces spec gap** (no ESC-SCHEDULE-DRIFT today) | M3 |
| FM-5 | Cap-C | Cap-C 5 | — (security) |
| FM-6 | Cap-C | Cap-C 6 | — (resilience) |
| BT-1 | Cap-A + Cap-C | Cap-A 12; Cap-C 4 (Workday allowlist); C1 hard constraint | **M4** — load-bearing |
| BT-2 | Cap-B + Cap-A | Cap-B 4, 6, 8; Cap-A 12; Task state machine (WAITING_HUMAN) | **M4** — load-bearing |

**Rules covered** (Cap-A 1–13, Cap-B 1–8, Cap-C 1–8):

- **Fully exercised:** Cap-A 1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13; Cap-B 1, 2, 4, 5, 6, 8; Cap-C 1, 2, 3, 4, 5, 6, 7, 8.
- **Covered transitively only:** Cap-A 7 (idempotency) is covered transitively via FM-1 retry + HP-1 happy path; no standalone replay scenario today — **noted as a follow-on edge case to add** (proposal: EC-8 "same idempotency-key dispatched twice").
- **Not covered:** Cap-B 3 (on_leave filter) — currently implied by EC-6 but not explicit. **Spec-validation gap, add EC-9** (candidate on leave is excluded).
- **Not covered:** Cap-B 7 (no silent override) — no direct scenario today. **Noted as a BT candidate** (BT-3: an agent attempts to write a `BuddyProposal.actor_user_id`; it should be impossible at the type-level, so the scenario is a "must not compile" test rather than a runtime test).

**Metrics covered:**
- **M1** defended by HP-1, EC-3, EC-6.
- **M2** (human-effort) is **not directly defended** by any scenario — M2 is a measurement over aggregate onboardings, not a per-scenario assertion. Noted as a **programme-level measurement plan**, not a validation-design gap.
- **M3** defended by HP-1, EC-4, FM-2, FM-4.
- **M4** defended by HP-1 (trivially), EC-2, EC-5, FM-3, **BT-1, BT-2** — the non-negotiable boundary-respect metric has two dedicated boundary tests, as required.

**Scenarios that exercise spec gaps** (rules that need to be added to the capability spec):
- FM-4 surfaces missing `ESC-SCHEDULE-DRIFT` — this is a spec gap, raised here as **Assumption Log entry V-open-1**: the capability spec will need a new rule in its next revision, not a hand-patch in this deliverable.
- BT-3 (proposed) surfaces the need to explicitly document that `BuddyProposal.actor_user_id` is a type-level absence, not a runtime check.

---

## 9. Diagrams

Trigger check: the happy path HP-1 has a multi-system timeline with parallel fan-out and three escalation branches that only fire in edge and failure scenarios. Figure 4 of the capability spec already captures this at the capability level; duplicating it here would add no new facts. BT-1 and BT-2 are text-heavy and compact; tables carry the assertion structure. No diagram — tables carry the structure for this draft.

---

## 10. Self-audit

- [x] ≥ 1 happy path (HP-1), ≥ 3 edge cases (EC-1…EC-7), ≥ 3 failure modes (FM-1…FM-6), ≥ 1 boundary test (BT-1, BT-2).
- [x] Every scenario carries a P / F / E tag.
- [x] Every scenario cites at least one specific rule, escalation code, or hard constraint from upstream.
- [x] Every failure mode names a detection signal (`integration_audit` row, dashboard metric, decision-log event type).
- [x] Every boundary test enumerates specific mis-behaviours and ties each to the rule it would break.
- [x] Trace matrix shows every Cap-A / Cap-B / Cap-C rule exercised by at least one scenario, with the two exceptions (Cap-A 7 transitive; Cap-B 3 implicit; Cap-B 7 proposed BT-3) flagged.
- [x] Every success metric M1, M3, M4 is defended by at least one scenario; M4 is defended by two dedicated boundary tests; M2 is a programme-level measurement, not a per-scenario assertion — called out.
- [x] No new rules, states, escalations, or integrations introduced here; the one spec gap (ESC-SCHEDULE-DRIFT under FM-4) is flagged in §8, not silently added.
- [x] Every `[ASSUMED]` / `[UNKNOWN]` has a matching numbered entry in the Assumption Log.
- [x] No `[TODO]` markers open.
- [x] No diagrams (trigger not met); called out explicitly.

**Overall validation read.** The design, as drafted, would surface a boundary violation in BT-1 or BT-2 because the assertion set reads from the decision log and checks `actor_user_id` + `EscalationEvent.code` existence — both of which a naive builder cannot fake without violating the Cap-A rule 12 check constraint or the Cap-C rule 4 allowlist. **Recommended first build-loop scenario: HP-1**, because it exercises the largest swathe of rules and flushes the most likely ambiguity surfaces in the capability spec before BT-1 is run as the real test.

---

## 11. Out of scope

- Problem statement and success metrics — see [`./problem-statement-scenario-1-201.md`](./problem-statement-scenario-1-201.md).
- Delegation analysis — see [`./delegation-analysis-scenario-1-202.md`](./delegation-analysis-scenario-1-202.md).
- Capability specification — no new rules, entities, escalations, or integrations are introduced here. See [`./capability-specification-scenario-1-203.md`](./capability-specification-scenario-1-203.md); one spec gap (ESC-SCHEDULE-DRIFT) is raised there via the Assumption Log, not patched in this file.
- Full consolidated assumptions register — see [`./assumptions-and-unknowns-scenario-1-205.md`](./assumptions-and-unknowns-scenario-1-205.md).

