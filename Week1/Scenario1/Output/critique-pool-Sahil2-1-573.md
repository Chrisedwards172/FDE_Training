# Critique-Pool Submission — Scenario 1: HR Onboarding Coordination

**Submission ID:** `critique-pool-Sahil2-1-573`
**Scenario:** [Scenario 1 — HR Onboarding Coordination](../../../SupportingDocs/README-Participants-Week1-Scenarios.md#scenario-1--hr-onboarding-coordination)
**Week:** Week 1 — AI-Native Specification
**Produced from:** [`../build-spec.md`](../build-spec.md) Prompt 1. Structure: Assumption Log + the five deliverables (per the *"How to work with your chosen scenario"* section of the Week 1 scenarios file).

> **Status: fresh draft under the new repository layout.** Content carries forward the same HUMAN assumption state as the last good draft (`-204`) — H4 still encodes the three-factor filter + capacity rule + department-first tie-break + HR-manual-on-empty. Previous iteration audit trail (A3 retired `-836`, A9 resolved `-742`, A11 retired `-204`, A10 narrowed `-204`) is preserved below for Friday peer review.

---

## Assumption Log

> *"Hidden assumptions are the failure mode. Stated assumptions are discovery."* — [primer](../../../SupportingDocs/Week1-Thinking-Discipline-Primer.md)

### Source tags

- **HUMAN** — supplied by the participant.
- **AGENT** — identified during drafting; unsettled by the scenario text or prompt rules.
- **High** — coach-session-validated; per prompt rules, treated as true for this draft.

### What counts as [CITED]

1. Scenario text in [`SupportingDocs/README-Participants-Week1-Scenarios.md`](../../../SupportingDocs/README-Participants-Week1-Scenarios.md).
2. Named US federal regulations — IRCA (8 U.S.C. § 1324a); IRS common-law / ACA 30-hour / state ABC.
3. Explicit rules in [`build-spec.md`](../build-spec.md) — specifically the Workday-classification rule.

### Scan table

| # | Source | Assumption (one line) | Cagan risk | Confidence | Sections at risk if wrong |
|---|---|---|---|---|---|
| H1 | **HUMAN** | HR Ops is open to adopting an AI agent | Value | **Medium** | Deliverable 1 adoption metric |
| H2 | **HUMAN** | The 15% judgment tasks are consistent enough for an agent to learn | Feasibility, Viability | **Low** | Deliverable 2 HUMAN-LED rows |
| H3 | **HUMAN** | Named systems have usable APIs; email via SMTP or transactional API | Feasibility | **Medium** | Deliverable 3 integrations |
| **H4** | **HUMAN** | Buddy assignments: **filter on (seniority + department + location) AND not-already-a-buddy**; if multiple pass, prioritise **department → location → seniority**; if still tied, **random**; escalate to HR if no candidate available | Feasibility, Value | **High** _(coach-validated)_ | Deliverable 2 buddy row; Capability 2 |
| H5 | **HUMAN** | The two unnamed systems are a benefits system + a payroll/time system | Feasibility, Viability | **High** _(coach-validated)_ | BENEFITS/PAYROLL scope |
| H6 | **HUMAN** | HR Ops will grant access and provide support for integration | Viability | **High** _(coach-validated)_ | Delivery risk |
| H7 | **HUMAN** | "Late I-9 triggers a hold" is compliance action with legal implications | Viability | **Medium** | Cap 1 rule 6 |
| A1 | **AGENT** | HR Ops (not Legal / Payroll) owns the `employment_class` write in Workday | Usability, Viability | **Medium** | ESC-CLASS routing |
| A2 | **AGENT** | Role taxonomy stable, < 100 roles, low churn | Feasibility | **Medium-low** | Cap 1 inputs |
| ~~A3~~ | ~~**AGENT**~~ | ~~Weighted ranking weights 0.4/0.3/0.2/0.1~~ **RETIRED `-836`** — did not trace to H4 once H4 was narrowed to a filter | — | Retired | — |
| A4 | **AGENT** | Federal IRCA is the only I-9 rule; no state amendments | Viability | **Low-medium** | Cap 1 rule 6 |
| A5 | **AGENT** | ServiceNow has role-based catalog bundles | Feasibility | **Medium** | IT tasks |
| A6 | **AGENT** | The "≥ 80 % routine-delegation" target is achievable | Value | **Low** | Deliverable 1 success metrics |
| A7 | **AGENT** | HR Ops can supply current-state baselines | Value | **Medium** | Deliverable 1 success metrics |
| A8 | **AGENT** | **Open tension:** *"edge cases never look the same twice"* [CITED] vs. H2 | Feasibility, Viability | **Medium-high** tension; **unknown** resolution | Deliverable 2 HUMAN-LED rows |
| ~~A9~~ | ~~**AGENT**~~ | ~~Tension — scenario framing vs. H4 (seniority norms as judgment).~~ **Resolved `-742`** via H4 coach validation | — | Resolved | — |
| **A10** _(narrowed `-204`)_ | **AGENT** | "Not available" = zero candidates pass the filter. Candidates on leave on the hire's `start_date` are ineligible — **not a separate escalation case**. The one-buddy-per-hire capacity rule has moved to H4. | Usability | **Low-medium** | Capability 2 rule 1 |
| ~~A11~~ | ~~**AGENT**~~ | ~~Deterministic tie-break (buddy-load asc → tenure desc → alpha)~~ **RETIRED `-204`** — H4 now specifies the tie-break | — | Retired | — |

**Overall:** 14 active assumptions (7 HUMAN + 7 AGENT after A3, A11 retirements and A9 resolution; A10 narrowed). **3 High** (H4, H5, H6). **1 load-bearing tension** (A8 vs H2). No AGENT rated High — prompt rule respected.

### Coach-session priority queue

1. **A8 + H2** — load-bearing tension on judgment-task learnability.
2. **A1** — `employment_class` write owner in Workday.
3. **A10** (narrowed) — does on-leave need a separate escalation code, or does ESC-BUDDY-UNAVAILABLE cover it?
4. **A6** — value-risk pressure-test on the 80 % target.
5. **H1** — adoption willingness (distinct from H6 access).
6. **H3 + A5** — API specifics; ServiceNow bundles.
7. **H7** — I-9 hold operational workflow.
8. **A4, A2, A7** — confirm if time permits.

### Update protocol

After each coach session, update the affected entry **in place**: raise or lower confidence, add a dated note, change dependent spec prose. **Do not silently delete.** Retired, resolved, and narrowed assumptions stay in the log with annotation so Friday peer review can trace the evolution. Replacement content enters either as a new numbered AGENT entry or — preferably — as an explicit clause inside a HUMAN entry (as happened with H4 absorbing the capacity rule and the tie-break in the `-204` iteration).

### Full entries

**H1 — HR Ops is open to adopting an AI agent** _(HUMAN — Medium)_. Frustration ≠ AI-openness; prior automation failures may have hardened scepticism.

**H2 — Judgment tasks are consistent enough to be learned** _(HUMAN — Low)_. Contradicted by [CITED] scenario quote — see **A8**.

**H3 — Named systems have usable APIs; email via SMTP or transactional API** _(HUMAN — Medium)_. Enterprise baseline plausible; tenant-specific limits unknown.

**H4 — Buddy assignments: three-factor filter + capacity rule + department-first tie-break + HR escalation on empty** _(HUMAN — High, coach-validated 22.04.2026)_
- **Assumption:**
  - Three codifiable factors: **seniority, department, location**.
  - **Capacity:** an employee can only be a buddy to one new hire at a time.
  - Agent auto-assigns when a candidate passes the three-factor filter AND is not currently a buddy.
  - **Tie-break when multiple candidates pass:** prioritise (a) best department match, (b) then best location match, (c) then best seniority match. If still tied, **pick at random**.
  - If no candidate is available, agent escalates to HR for manual assignment.
- **Hypothesis:** The four clauses together produce a deterministic, auditable assignment that HR accepts without override on happy-path cases. Empty pool → HR handles manually, which they already do today.
- **How I'd test it:** *Tested 22.04.2026. All four clauses confirmed.* Residual operational probe on on-leave semantics → **A10**.
- **Confidence:** **High.**

**H5 — Unnamed systems = benefits + payroll/time** _(HUMAN — High, coach-validated)_. Endpoints / auth still `[UNKNOWN]`; identity settled.

**H6 — HR Ops will provide access and support** _(HUMAN — High, coach-validated)_.

**H7 — Late I-9 triggers a compliance-critical hold** _(HUMAN — Medium)_. Federal IRCA [CITED]; operational handoff specifics unprobed.

**A1 — HR Ops owns the `employment_class` write** _(AGENT — Medium)_. Prompt [CITED] rule names Workday as source of truth, not the write-owner.

**A2 — Role taxonomy stable, < 100 roles** _(AGENT — Medium-low)_.

**~~A3~~ — Retired `-836`.** Weighted ranking no longer required after H4 narrowed to filter-and-pick.

**A4 — Federal IRCA only** _(AGENT — Low-medium)_.

**A5 — ServiceNow has role-based catalog bundles** _(AGENT — Medium)_.

**A6 — 80 % routine-delegation achievable** _(AGENT — Low)_. Derived from the 85/15 [CITED] split, not observed friction.

**A7 — Baseline metrics retrievable** _(AGENT — Medium)_.

**A8 — Scenario vs. H2 tension (learnability)** _(AGENT — load-bearing, open)_
- [CITED] *"edge cases never look the same twice"* held more authoritative than H2 until coach-probed. Judgment tasks stay HUMAN-LED.
- Test: three concrete recent judgment calls; check for rule-recurrence.
- **Confidence:** Medium-high tension; unknown resolution.

**~~A9~~ — Resolved `-742`.** Scenario-vs-H4 tension dissolved on H4 coach validation.

**A10 — On-leave treatment in "not available"** _(AGENT — narrowed `-204`, Low-medium)_
- **Assumption:** An employee who would otherwise pass the filter but is on leave on the hire's `start_date` is treated as **ineligible at filter time** — absorbed into ESC-BUDDY-UNAVAILABLE rather than being a separate escalation.
- **Hypothesis:** A single escalation trigger suffices. If HR wants to distinguish "good candidate only unavailable due to leave" from "genuinely empty pool", add ESC-BUDDY-ON-LEAVE.
- **How I'd test it:** Coach probe — *"If the only eligible buddy is on leave on start date, do you want to see that differently from an empty pool?"*
- **Confidence:** **Low-medium.** Default is the simpler single-trigger model; reversible.

**~~A11~~ — Retired `-204`.** Tie-break now HUMAN-specified inside H4.

---

## Deliverable 1 — Problem Statement and Success Metrics

### The problem being solved

A regional professional-services firm of 1,200 employees hires 220+ people per year [CITED]. Each onboarding spans ~40 tasks across 2 weeks and **6 systems** — 4 named (Workday, ServiceNow, LMS, email [CITED]) and 2 coach-confirmed (benefits + payroll/time, **H5** High). A 3-person HR Ops team owns all of it [CITED]. ~15% of tasks — ~1,320 per year — are judgment calls [CITED].

> *"Most of this is paperwork my team should not be touching, but every time we try to automate, something falls through the cracks because the edge cases never look the same twice."* — HR Ops lead [CITED]

### Why agentic, why now

- **Volume:** ~8,800 tasks/year (220 × 40 — ratio [CITED]); ~85% rule-governed [CITED].
- **Repeatability:** The 85% is routine coordination. **H4** places buddy matching inside this bucket — deterministic filter + deterministic tie-break + HR for empty pool — not judgment.
- **Constraint:** The 15% judgment remains human-led or human-in-loop pending **A8** / H2.

### Success metrics

| Metric | Current | Target | Measurement | Source label |
|---|---|---|---|---|
| % of routine tasks executed with no HR Ops action | `[UNKNOWN]` | ≥ 80% of the 85% routine portion | `tasks_with_no_hr_ops_action / total_tasks` | Split **[CITED]**; threshold **[ASSUMED]** — **A6** (Target — needs validation) |
| HR Ops time per onboarding | `[UNKNOWN]` | ≥ 50% reduction vs. baseline | Time-tracking tagged to `onboarding_id` | **[ASSUMED]** — **A7** (Target — needs validation) |
| "Task fell through the cracks" at day 14 | `[UNKNOWN]` | ≤ 1% of onboardings | Day-14 audit | **[ASSUMED]** — **A7** (Target — needs validation) |
| Judgment-case routing correctness | N/A | 100% reach human review; 0 silent agent decisions | `human_decision_logged` before `COMPLETE` on every judgment-classified task | **[CITED]** (Non-negotiable) |
| Buddy-assignment HR-override rate | N/A | ≤ 10% of auto-assigns in first 20 onboardings | Count of `HumanDecision(OVERRIDE_BUDDY)` / auto-assigns | **[ASSUMED]** — H4-derived falsifier |

---

## Deliverable 2 — Delegation Analysis

### Work inventory

| Task / Decision | Classification | Rationale |
|---|---|---|
| IT provisioning — standard role-based tickets | FULL DELEGATION | ServiceNow [CITED]; reversible |
| IT provisioning — non-standard requests | HUMAN-IN-LOOP | Agent drafts, HR Ops approves |
| Benefits eligibility (benefits system, **H5**) | FULL DELEGATION | Mechanical trigger on `start_date` + `employment_class` |
| Benefits — contractor vs. full-employee classification | HUMAN-LED | [CITED] judgment call + prompt rule |
| Payroll/time setup (payroll/time system, **H5**) | FULL DELEGATION | Mechanical trigger on employment data |
| Compliance training — standard courses | FULL DELEGATION | Rule-based; LMS [CITED] |
| Compliance training — multi-jurisdiction track | HUMAN-IN-LOOP | Ambiguity; agent proposes, HR Ops confirms |
| **Buddy matching — filter match + capacity guard + deterministic tie-break** | **FULL DELEGATION** | **H4** High: filter (seniority + department + location + not-already-a-buddy) + HUMAN-specified tie-break (department → location → seniority → random). HR retains override within 1 BD. |
| **Buddy matching — no candidate available** | HUMAN-LED | **H4** + **A10**: agent escalates to HR for manual assignment |
| Welcome materials | FULL DELEGATION | Template-driven |
| 30-day checkpoint scheduling | FULL DELEGATION | Reversible |
| Manager handoff — day-10 summary | FULL DELEGATION | Templated |
| I-9 — detect late Section 2 | FULL DELEGATION (detection) | IRCA rule |
| I-9 — decide whether lateness triggers a hold | HUMAN-LED | [CITED] + H7 |
| Day-14 audit — flag incomplete | FULL DELEGATION | State check |
| Manager handoff — final sign-off | HUMAN-IN-LOOP | Agent compiles; HR Ops signs off |

### Hard constraints on the boundary

| Constraint | Source | Effect |
|---|---|---|
| `employment_class` from Workday; HR authoritative; escalate if unreliable | [CITED] prompt rule | Agent reads only; ESC-CLASS on UNSET/ambiguous |
| Classification must be human-determined | Federal [CITED regulations] | Agent never writes `employment_class` |
| I-9 Section 2 within 3 business days; hold decisions are human | [CITED] + IRCA | Agent detects only; cannot initiate or release holds |
| Buddy auto-assign only on filter match + capacity; tie-break department → location → seniority → random; escalate if filter empty | **H4** High + **A10** | See Capability 2 |
| No AI infrastructure today | [CITED] | Build includes orchestration, secrets, audit storage |

**Audit trail.** Every human decision logged with `decision_type, user_id, decision_value, reason, timestamp` — **7-year retention**.

---

## Deliverable 3 — First-Draft Capability Specification

Three capabilities share the `Onboarding` entity.

### Entity model

**`Onboarding`** — `id` UUID PK · `employee_id` immutable · `start_date` immutable · `role`, `location` enums · `employment_class` enum [FULL_EMPLOYEE, CONTRACTOR, UNSET] · `manager_id` · `state` enum [ACTIVE, COMPLETE, CANCELLED] · `handoff_sent_at` nullable · `created_at`, `updated_at`. Soft-delete via CANCELLED; 7-year retention.

**`Task`** — `id` UUID PK · `onboarding_id` FK (RESTRICT) · `template_key` · `category` enum [IT, BENEFITS, PAYROLL, COMPLIANCE, BUDDY, WELCOME, CHECKPOINT, HANDOFF, I9] · `delegation_class` enum [FULL, HUMAN_IN_LOOP, HUMAN_LED] · `state` enum [PENDING, IN_PROGRESS, BLOCKED_ON_CLASSIFICATION, ESCALATED, COMPLETE, FAILED, WAIVED_BY_HUMAN] · `due_at` immutable · `completed_at` · `external_ref` · `idempotency_key` · `last_actor`.

**`BuddyAssignment`** — `id` UUID PK · `onboarding_id` FK · `buddy_employee_id` Workday UUID · `assigned_at` UTC · `assigned_by` enum [AGENT, user_id] · `rationale` JSON (filter-pass evidence + tie-break path) · `active_until` UTC (= `start_date + 30d`) · `superseded_by` nullable FK to a later `BuddyAssignment`.
*Rationale:* the H4 capacity rule (*"one buddy per person"*) requires an efficient "is this employee currently a buddy?" lookup. First-class entity with `active_until` makes that a direct query rather than a derived inference over the task log.

**`HumanDecision`** — `id` UUID PK · `onboarding_id` FK · `task_id` FK nullable · `decision_type` enum [CLASSIFY_EMPLOYMENT, **OVERRIDE_BUDDY**, MANUAL_ASSIGN_BUDDY, APPROVE_IT_NONSTANDARD, I9_HOLD_DECISION, WAIVE_TASK, COMPLETE_ONBOARDING] · `decision_value` JSON · `user_id` · `reason` required · immutable.

### Capability 1 — Onboarding Orchestrator

**Purpose.** Create/advance `Onboarding`; instantiate ~40 tasks; drive to completion or escalation within 2 weeks.

**Scope.** *In:* Workday new-hire event handling; task lifecycle; overdue detection; day-10 handoff; day-14 audit. *Out:* writing `employment_class`; benefits/payroll while class UNSET; clinical/medical/legal advice; employee-facing chat.

**Decision logic (10 requirements):**

1. **Onboarding creation.** Exactly one `Onboarding` per `employee_id`. Duplicates logged, ignored.
2. **Task instantiation.** For `(role, location, employment_class)`. UNSET → class-dependent tasks to `BLOCKED_ON_CLASSIFICATION`.
3. **State transitions.** `PENDING → IN_PROGRESS → COMPLETE | FAILED | ESCALATED`; `BLOCKED_ON_CLASSIFICATION → PENDING` on human class-set.
4. **Deadline.** `due_at = start_date + template.offset_days`. Immutable.
5. **OVERDUE.** Derived: `now > due_at AND state IN (PENDING, IN_PROGRESS, BLOCKED_ON_CLASSIFICATION)`.
6. **I-9.** `i9_deadline = start_date + 3 business days` [CITED IRCA]. Overdue → ESC-I9. No hold initiation or release.
7. **Day 10 handoff.** Idempotent; summary to `manager_id`; set `handoff_sent_at`.
8. **Day 14 audit.** Any non-terminal task → daily report to HR Ops lead.
9. **Idempotency.** `idempotency_key = onboarding_id + task_id + system_name`.
10. **Classification at face value.** Take `employment_class` as given per [CITED] prompt rule. No NLP on attached documents. ESC-CLASS on unreliable reads.

**Escalation triggers:**

| Code | Condition | Notified | SLA |
|---|---|---|---|
| ESC-CLASS | BLOCKED_ON_CLASSIFICATION > 1 BD or unreliable read | HR Ops (**A1**) | 3 BD |
| ESC-I9 | Late I-9 with `i9_completed_at IS NULL` | HR Ops + compliance | 1 BD |
| **ESC-BUDDY-UNAVAILABLE** | Filter + capacity guard returns zero eligible candidates (**H4** + **A10**) | HR Ops | 2 BD — HR records `MANUAL_ASSIGN_BUDDY` |
| ESC-IT-NONSTANDARD | `is_standard_bundle = false` | HR Ops | 1 BD |
| ESC-INTEGRATION | Non-retryable external error | Ops on-call | 4 hours |
| ESC-AUDIT | Day-14 finds non-terminal task | HR Ops lead | EOD |
| ESC-JURISDICTION | Multi-jurisdiction; oversized course set | HR Ops | 1 BD |
| ESC-TRAINING-OVERDUE | 3 nags delivered; still incomplete | HR Ops + manager | 1 BD |

### Capability 2 — Buddy Match Assigner

**Purpose.** Auto-assign a buddy using the H4 filter + capacity rule + tie-break. Escalate to HR only when no candidate is available.

**Scope.** *In:* eligibility filter; capacity check against `BuddyAssignment`; H4 tie-break; auto-assign; HR-visible rationale; HR override window. *Out:* scoring; ranking beyond H4; assigning when filter is empty.

**Decision logic (7 requirements):**

1. **Eligibility filter (H4 + guard rails):** a candidate is eligible iff all hold:
   - **seniority match** — same seniority band as the hire's role (per Workday role-level map);
   - **department match** — same or adjacent department as the hire;
   - **location match** — same location as the hire;
   - **capacity** (H4) — no active `BuddyAssignment` row where `now < active_until`;
   - **not the hire's direct manager** (role guard);
   - **not on leave on the hire's `start_date`** (per **A10**).

2. **Tie-break (H4 HUMAN rule).** If multiple pass: (a) best department match (exact team > adjacent team), (b) then best location match (exact office > same city > same region), (c) then best seniority match (exact level > ±1 level), (d) if still tied, **random** using a seeded RNG whose seed is logged.

3. **Auto-assign.** Write `BuddyAssignment` with `rationale` populated (filter evidence + tie-break path + RNG seed if applicable). `HumanDecision(OVERRIDE_BUDDY)` is the post-hoc HR veto path.

4. **No auto-assign when filter empty.** Raise **ESC-BUDDY-UNAVAILABLE**. Task state → `ESCALATED`. HR records `MANUAL_ASSIGN_BUDDY` to resolve.

5. **Rationale log.** Every auto-assign writes candidate counts surviving each filter step; the tie-break path (e.g. `tied_on_dept_step:false; picked_at_step:location; tied_among:3; final_picker:seniority`); RNG seed if step (d) fired. Retained 7 years.

6. **Override window.** `HumanDecision(OVERRIDE_BUDDY)` within 1 BD sets `superseded_by` on the current assignment and triggers a re-run of rules 1–2 with that candidate excluded. Empty re-run → ESC-BUDDY-UNAVAILABLE.

7. **No scoring, no weights.** Agent must NOT compute a weighted score. The only ordering permitted is rule 2. A reviewer reading the code should see filter → capacity-check → hierarchical tie-break → seeded random.

### Capability 3 — Compliance Training Assigner

**Purpose.** Assign LMS courses by role + jurisdiction within 1 BD of start.

**Decision logic (5 requirements):**

1. **Course resolution.** Union of `role_course_map[role]` and `jurisdiction_course_map[j]` for each `j`. Deduplicate.
2. **Ambiguous jurisdiction.** `jurisdictions.length > 1` and set > 12 courses [ASSUMED] → ESC-JURISDICTION. No enrolment.
3. **Nag cadence.** `due_at − 3d`, `due_at − 1d`, `due_at + 1d`. Max 3 nags.
4. **Completion.** Only on LMS `completed` webhook matching `enrolment_id`. No self-report.
5. **Overdue.** 3 nags delivered → ESC-TRAINING-OVERDUE.

### Integration points

**H3** (Medium) baseline; **H5** (High) confirmed; **H6** (High) access provided.

| System | Purpose | Auth | Timeout | Retry | Fallback |
|---|---|---|---|---|---|
| Workday | New-hire events; worker reads | OAuth 2.0 `[UNKNOWN tenant URL]` | 10s | × 3 (2/4/8s); 4xx → ESC-INTEGRATION | Queue > 15 min; FIFO on recovery |
| ServiceNow | IT tickets (**A5** bundles) | API key | 5s | × 3 (1/2/4s) | Tasks PENDING; ESC at 2 BD |
| LMS | Courses + completion webhook | `[UNKNOWN vendor]` | 10s | × 3 (2/4/8s) | Retries 24h; then ESC |
| Email (**H3**) | Notifications | Per client | 5s | 3 retries (1/2/4s) | Retry 1h; dashboard queue — never silently drop |
| Benefits system (**H5**) | Eligibility + comms | `[UNKNOWN vendor]` | 10s | × 3 (2/4/8s) | ESC at 2 BD |
| Payroll/time system (**H5**) | Setup | `[UNKNOWN vendor]` | 10s | × 3 (2/4/8s) | ESC at 2 BD |

---

## Deliverable 4 — First-Draft Validation Design

### Happy path

FULL_EMPLOYEE hire, US single-state role. Day −7 Workday event → orchestrator creates Onboarding + tasks. Agent provisions ServiceNow, enrols LMS, queues benefits + payroll, schedules checkpoint, sends welcome pack. Day 0: hire starts; I-9 completed day 2. Day 2: buddy assigner → filter yields 3; tie-break: 2 have exact department → of those 2, one has exact location → assigned. No HR override in 1 BD. Day 10: handoff. Day 14: audit all terminal. **Expected:** zero ESC-*; one `HumanDecision(COMPLETE_ONBOARDING)`; one `BuddyAssignment(assigned_by=AGENT)`.

### Edge cases (9)

| # | Scenario | Expected |
|---|---|---|
| EC-1 | `employment_class = UNSET` at event | BENEFITS, PAYROLL BLOCKED; ESC-CLASS at +1 BD |
| EC-2 | Duplicate Workday webhook | `duplicate_ignored`; no second Onboarding |
| EC-3 | Multi-jurisdiction; course set > 12 | ESC-JURISDICTION |
| EC-4 | ServiceNow 5xx × 3 | Task IN_PROGRESS; ESC-INTEGRATION |
| EC-5 | Filter yields zero eligible (small team, all already buddies) | ESC-BUDDY-UNAVAILABLE; HR records `MANUAL_ASSIGN_BUDDY` |
| EC-6 | Filter yields 5; none exact-department, all exact-location, varied seniority | Tie-break step (a) no winner; step (b) 5 tie; step (c) picks exact-level; if unique, assign; else step (d) seeded random |
| EC-7 | Filter yields 1; HR overrides within 1 BD | `superseded_by` set; re-run excludes overridden; empty re-run → ESC-BUDDY-UNAVAILABLE |
| EC-8 | Would-be buddy is already buddy to another hire in first 30 days | Capacity guard excludes at rule 1; filter runs without them; if only match → ESC-BUDDY-UNAVAILABLE |
| EC-9 | Workday pushes new `start_date` post-creation | Immutable; ESC-INTEGRATION `reason = start_date_drift` |

### Failure modes (4)

| # | Failure | Agent response | Recovery |
|---|---|---|---|
| FM-1 | LMS webhook never arrives | Nag × 3; ESC-TRAINING-OVERDUE | HR marks COMPLETE via HumanDecision |
| FM-2 | Workday worker deleted mid-onboarding | 404 → ESC-INTEGRATION; no writes | HR cancels Onboarding |
| FM-3 | Agent misclassifies IT request as standard | Standard ticket submitted | IT flags; HumanDecision APPROVE_IT_NONSTANDARD records correction |
| FM-4 | Classification decision arrives after day 10 | Handoff lists BLOCKED tasks explicitly | HR + manager decide to extend window |

### Delegation boundary test (classification)

**Scenario.** Hire labelled FULL_EMPLOYEE in Workday; engagement letter attached describes SOW-style contractor structure.
**Expected.** Agent takes `employment_class` at face value. No NLP on the letter. No pause. HR catches the discrepancy manually — boundary held.
**Failure shapes:** agent reads the letter and flips path → violation. Agent blocks demanding reclassification → violation.

### Delegation boundary test (buddy)

**Scenario.** Filter returns two candidates. One has exact department match; the other has exact location match. HR subjectively prefers the second based on personality.
**Expected.** Agent applies H4 tie-break 2(a) — department match wins. Assigns the first; rationale logged. HR exercises `HumanDecision(OVERRIDE_BUDDY)` within 1 BD. Assigner re-runs excluding that candidate; second candidate now passes → auto-assigned.
**Failure shapes:**
- Agent computes a weighted score that surfaces "personality fit" or any non-H4 factor → violation (A3 retirement: no scoring).
- Agent uses an ordering other than department → location → seniority → random → violation (A11 retirement: H4 ordering authoritative).
- Agent refuses the override because the filter still has a valid match → violation (override is absolute in the 1 BD window).

---

## Deliverable 5 — Assumptions and Unknowns

> Full detail in the [Assumption Log](#assumption-log) — 14 active entries (2 retirements, 1 resolution, 1 narrowing retained for audit). This section distils the unknowns and what must be validated before building.

### Data

1. **Real role taxonomy and seniority-band map** — **A2**. Capability 2 rule 1 depends on a defined seniority band per role.
2. **Baseline metrics** — **A7**.
3. **Buddy-pool shape** — how often does the H4 filter return zero / one / many? Drives ESC-BUDDY-UNAVAILABLE volume.

### Systems

4. **Benefits API shape** — `[UNKNOWN]` despite **H5** High.
5. **Payroll/time API shape** — `[UNKNOWN]` despite **H5** High.
6. **LMS vendor + API** — `[UNKNOWN]`.
7. **Workday tenant URL + rate limits** — `[UNKNOWN]`.
8. **Email transport specifics** — **H3**.
9. **ServiceNow catalog bundles vs. per-asset** — **A5**.

### Organisation

10. **`employment_class` write owner at HR Ops** — **A1**.
11. **State-level I-9 variations** — **A4**.
12. **I-9 hold operational mechanics** — **H7**.
13. **HR Ops adoption willingness** — **H1** (distinct from H6 access).
14. **On-leave treatment in buddy filter** — **A10**. Separate escalation, or subsumed?

### Problem shape

15. **Judgment-task learnability** — **A8 vs H2**. Still open.

### What must be validated before building

- **Blocking:** 4–8 (integration specifics), 14 (buddy on-leave semantics), 15 (delegation boundary).
- **Soft-blocking:** 1–3, 9–13.
- **Ordering:** matches the [coach-session priority queue](#coach-session-priority-queue).

---

## Self-check (primer § *Self-check before Friday*)

| Check | Status |
|---|---|
| Assumption log visible, numbered, honest about confidence? | ✅ Top of doc. 14 active; 3 High (H4, H5, H6); 2 retired (A3, A11); 1 resolved (A9); 1 narrowed (A10). |
| Can I point every major claim to test / source / explicit assumption? | ✅ `[CITED]` / `[ASSUMED]` throughout Deliverables 1–4; every `[ASSUMED]` traces to H1–H7 or A1–A10. |
| Did I use coach sessions to move specific hypotheses, not chat? | ✅ 22.04.2026 session confirmed H4 (extended), H5, H6; resolved A9; triggered A3/A11 retirements and A10 narrowing. |
| Did I complete the closed build loop against Claude Code? | ⏳ Pending. Capability 1 + Capability 2 (new `BuddyAssignment` entity, seeded RNG, override window) are the targets. |
| Would a reviewer challenge my thinking because I've exposed it? | ✅ Retirement / resolution / narrowing annotations are dated and traceable. A reviewer can see exactly which Capability 2 clauses rest on HUMAN High vs. AGENT Low-medium. |

Four ✅, one ⏳.

