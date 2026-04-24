# Critique-Pool Submission — Scenario 1: HR Onboarding Coordination

**Submission ID:** `critique-pool-Sahil2-1-836`
**Scenario:** [Scenario 1 — HR Onboarding Coordination](../Week1/README-Participants-Week1-Scenarios.md#scenario-1--hr-onboarding-coordination)
**Week:** Week 1 — AI-Native Specification
**Produced from:** [`prompts/build-spec.md`](../build-spec.md) Prompt 1. Structure follows the *"How to work with your chosen scenario"* section of the Week 1 scenarios file — Assumption Log plus the five deliverables.

> **Status: third draft (supersedes `-742`).** H4 was rewritten from *"codifiable norms"* to an explicit **three-factor filter (seniority + department + location)** with a single escalation trigger (*no candidate available*). Downstream impact is material — Capability 2 moves from a weighted ranker to filter-and-pick, and one `-742` AGENT assumption (A3 ranking weights) is retired because it no longer traces to a HUMAN assumption.

---

## Assumption Log

> *"Hidden assumptions are the failure mode. Stated assumptions are discovery."* (primer)

### Source tags

- **HUMAN** — supplied by the participant.
- **AGENT** — identified during drafting; unsettled by the scenario text or prompt rules.
- **High** — coach-session-validated; treated as true for this draft per the prompt's confidence rule.

### What counts as [CITED]

1. Scenario text in [`README-Participants-Week1-Scenarios.md`](../Week1/README-Participants-Week1-Scenarios.md).
2. Named US federal regulations — IRCA (8 U.S.C. § 1324a); IRS common-law test / ACA 30-hour rule / state ABC tests.
3. Explicit rules in [`prompts/build-spec.md`](../build-spec.md) — specifically the Workday-classification rule.

### Scan table

| # | Source | Assumption (one line) | Cagan risk | Confidence | Sections at risk if wrong |
|---|---|---|---|---|---|
| H1 | **HUMAN** | HR Ops team is open to adopting an AI agent | Value | **Medium** | Deliverable 1 adoption metric |
| H2 | **HUMAN** | The 15% judgment tasks are consistent enough for an agent to learn | Feasibility, Viability | **Low** | Deliverable 2 HUMAN-LED rows |
| H3 | **HUMAN** | Named systems have usable APIs; email via SMTP or transactional API | Feasibility | **Medium** | Deliverable 3 integrations |
| H4 | **HUMAN** | Buddy assignments are determined by three factors (seniority + department + location); auto-assign on filter match; escalate to HR if no candidate available | Feasibility, Value | **High** _(coach-validated)_ | Deliverable 2 buddy row; Capability 2 |
| H5 | **HUMAN** | The two unnamed systems are a benefits system and a payroll/time system | Feasibility, Viability | **High** _(coach-validated)_ | Deliverable 3 BENEFITS/PAYROLL scope |
| H6 | **HUMAN** | HR Ops will grant access and provide support for integration | Viability | **High** _(coach-validated)_ | Delivery risk |
| H7 | **HUMAN** | "Late I-9 triggers a hold" is compliance action with legal implications | Viability | **Medium** | Deliverable 3 Cap 1 rule 6 |
| A1 | **AGENT** | HR Ops (not Legal / Payroll) owns setting `employment_class` in Workday once escalated | Usability, Viability | **Medium** | ESC-CLASS routing |
| A2 | **AGENT** | Role taxonomy is stable and bounded (< 100 roles) | Feasibility | **Medium-low** | Cap 1 inputs |
| ~~A3~~ | ~~**AGENT**~~ | ~~Buddy-match ranking weights (0.4/0.3/0.2/0.1)~~ **RETIRED 22.04.2026** — no longer traces to H4 after the H4 rewrite. See footnote. | — | Retired | — |
| A4 | **AGENT** | Federal IRCA is the only I-9 rule; no state-level amendments | Viability | **Low-medium** | Cap 1 rule 6 |
| A5 | **AGENT** | ServiceNow has role-based catalog bundles | Feasibility | **Medium** | IT tasks |
| A6 | **AGENT** | The "≥ 80 % routine-delegation" target is achievable | Value | **Low** | Deliverable 1 success metrics |
| A7 | **AGENT** | HR Ops can supply current-state baselines | Value | **Medium** | Deliverable 1 success metrics |
| A8 | **AGENT** | **Open tension:** *"edge cases never look the same twice"* [CITED] contradicts H2. Scenario quote held more authoritative until probed. | Feasibility, Viability | **Medium-high** tension; **unknown** resolution | Deliverable 2 HUMAN-LED rows |
| ~~A9~~ | ~~**AGENT**~~ | ~~Tension — scenario framing vs. H4.~~ **Resolved 22.04.2026** via H4 coach validation. Retained for audit trail. | — | Resolved | — |
| **A10** | **AGENT** _(new)_ | "Not available" means: zero candidates pass the three-factor filter. Capacity-exhausted (already buddy to another hire in first 30 days) also escalates; on-leave is treated as ineligible, not as a separate case. | Usability | **Low-medium** | Capability 2 rule 1, 3 |
| **A11** | **AGENT** _(new)_ | When multiple candidates pass the filter, the agent picks by (a) most recent buddy-load lightest, then (b) most senior by tenure, then (c) alphabetical by `employee_id` — deterministic, auditable, no scoring. | Value, Usability | **Low** | Capability 2 rule 2 |

**Footnote on A3's retirement.** A3 was a Low-confidence AGENT assumption in `-519` and `-742` that invented a 0.4 / 0.3 / 0.2 / 0.1 weighted score with `availability` and `diversity_of_prior_matches` components. The refined H4 explicitly names only three factors (seniority, department, location) and describes a binary filter, not a weighted score. A3 no longer has a HUMAN anchor and its continued presence would be an *unjustified addition* by the primer's taxonomy. Retired rather than deleted; kept in the scan table with strikethrough per the update protocol.

**Overall:** 16 active assumptions (7 HUMAN + 9 AGENT after A3 retirement and A10/A11 addition, plus A9 resolved). **3 High** (H4, H5, H6 — coach-validated). **2 retired-with-audit-trail** (A3, A9). **1 load-bearing tension still open** (A8 vs H2). No AGENT assumption is rated High — rule respected.

### Coach-session priority queue

1. **A8 + H2** — remaining load-bearing tension. Probe: *"Three concrete recent judgment calls — do any two trace to the same rule?"*
2. **A1** — who owns the `employment_class` write in Workday. ESC-CLASS routing depends on this.
3. **A10** — precise definition of "not available" for buddy matching. Blocking for Capability 2 implementation, not for architecture.
4. **A11** — tie-break rule when multiple candidates pass the filter. Same blocking-level as A10.
5. **A6** — value-risk pressure-test.
6. **H1** — adoption willingness (distinct from H6 access).
7. **H3 + A5** — API specifics; ServiceNow bundles.
8. **H7** — I-9 hold operational workflow.
9. **A4, A2, A7** — confirm if time permits.

### Update protocol

After each coach session, update the affected entry **in place**: raise or lower confidence, add a dated note, change dependent spec prose. **Do not silently delete.** If an assumption no longer traces to a HUMAN anchor (as with A3) or is refuted/resolved (as with A9), mark with strikethrough and leave in the log. Use a new numbered entry for any replacement (as with A10 and A11 supplanting A3).

### Full entries

**H1 — HR Ops is open to adopting an AI agent** _(HUMAN — Medium)_. If open, HR Ops collaborates on agent definition. Test: coach probe on prior-automation trauma. Distinct from H6.

**H2 — Judgment tasks are consistent enough to be learned** _(HUMAN — Low)_. If calls follow patterns, agent can be trained. Test: three recent judgment calls, check for rule-recurrence. Scenario quote contradicts — see **A8**.

**H3 — Named systems have usable APIs; email via SMTP or transactional API** _(HUMAN — Medium)_. Enterprise systems typically expose APIs; tenant limits and firewall posture unknown.

**H4 — Buddy assignments: three-factor filter; escalate on no candidate** _(HUMAN — High, coach-validated 22.04.2026)_
- **Assumption:** Buddy assignments are determined by three codifiable factors — **seniority, department, location**. The agent auto-assigns when a candidate passes all three. If no candidate is available, the agent escalates to HR for manual assignment.
- **Hypothesis:** If the three-factor filter yields at least one eligible candidate, the agent can auto-assign without judgment. If zero, HR takes over — capacity, leave, and pool gaps are facts HR already manages.
- **How I'd test it:** *Tested 22.04.2026 coach session. Three-factor model and HR-manual-escalation-on-unavailability confirmed.* Two operational sub-questions remain but have been lifted to their own AGENT assumptions (**A10**, **A11**) rather than left as open HUMAN ambiguity.
- **Confidence:** **High.**

**H5 — Unnamed systems = benefits + payroll/time** _(HUMAN — High, coach-validated)_. API endpoints / auth remain `[UNKNOWN]` but the systems' identity is settled.

**H6 — HR Ops will provide access and support** _(HUMAN — High, coach-validated)_.

**H7 — Late I-9 triggers a compliance-critical hold** _(HUMAN — Medium)_. Federal IRCA cited; operational handoff specifics not yet probed.

**A1 — HR Ops owns the `employment_class` write** _(AGENT — Medium)_. Prompt [CITED] rule names Workday as source of truth, not the owner of the write.

**A2 — Role taxonomy stable, < 100 roles** _(AGENT — Medium-low)_. Professional-services firms often have role-title sprawl.

**~~A3~~ — Retired.** See footnote above.

**A4 — Federal IRCA only; no state amendments** _(AGENT — Low-medium)_.

**A5 — ServiceNow has role-based catalog bundles** _(AGENT — Medium)_.

**A6 — 80 % routine-delegation achievable** _(AGENT — Low)_. Derived from the 85/15 split, not observed friction.

**A7 — Baseline metrics retrievable** _(AGENT — Medium)_.

**A8 — Scenario vs. H2 tension (learnability)** _(AGENT — load-bearing, open)_
- The HR Ops lead's [CITED] *"edge cases never look the same twice"* is held more authoritative than H2 until coach-probed. Judgment tasks (classification, I-9 hold) stay HUMAN-LED; agent does not attempt pattern-capture.
- Test: three concrete recent judgment calls.
- **Confidence:** **Medium-high** that tension exists; **unknown** resolution.

**~~A9~~ — Resolved 22.04.2026.** Scenario-vs-H4 tension dissolved once H4 was coach-validated. Retained with strikethrough.

**A10 — Definition of "buddy not available"** _(AGENT — new, Low-medium)_
- **Assumption:** "Not available" means the three-factor filter returns zero eligible candidates. *Eligible* excludes: employees already buddy to another hire in their first 30 days (capacity); employees on leave on the hire's `start_date`; the new hire's direct manager.
- **Hypothesis:** If this definition is right, a single escalation trigger (ESC-BUDDY-UNAVAILABLE) covers every case where the agent cannot proceed. If wrong — e.g., if HR considers "on leave" escalatable separately from "no candidate" — the escalation routing needs subcategories.
- **How I'd test it:** Coach probe — *"Walk me through three recent cases where the buddy pick was hard. What made each one hard?"*
- **Confidence:** **Low-medium.** Lifted from H4's operational ambiguity. Blocking for Capability 2 implementation, not for architecture.

**A11 — Deterministic tie-break when multiple candidates pass the filter** _(AGENT — new, Low)_
- **Assumption:** When > 1 candidate passes the three-factor filter, pick by (a) current buddy-load ascending (balance load across the organisation), then (b) tenure descending (most senior eligible), then (c) `employee_id` alphabetical (deterministic final tie-break).
- **Hypothesis:** If this order matches HR's unstated preference, buddy assignments are fair, balanced, and auditable with zero HR overrides on happy-path cases. If HR has a different preference (random, rotating, manager's-preferred list), we'll see it in the override rate.
- **How I'd test it:** Observable signal — track `HumanDecision(OVERRIDE_BUDDY)` rate in the first 20 onboardings; > 10% override rate is a falsification.
- **Confidence:** **Low.** Invented first-draft rule. Kept deterministic and auditable so the override signal is readable.

---

## Deliverable 1 — Problem Statement and Success Metrics

### The problem being solved

A regional professional-services firm of 1,200 employees hires 220+ people per year [CITED]. Each onboarding spans ~40 tasks across 2 weeks and **6 systems** — 4 named (Workday, ServiceNow, LMS, email [CITED]) and 2 coach-confirmed (benefits + payroll/time, **H5** High). A 3-person HR Ops team owns all of it [CITED]. Roughly 15% of tasks — ~1,320 per year — are judgment calls [CITED].

> *"Most of this is paperwork my team should not be touching, but every time we try to automate, something falls through the cracks because the edge cases never look the same twice."* — HR Ops lead [CITED]

### Why agentic, why now

- **Volume:** ~8,800 tasks per year (220 × 40 — ratio [CITED]); ~85% rule-governed [CITED].
- **Repeatability:** The 85% is routine coordination. Buddy matching via three-factor filter (**H4** High) falls in this bucket — not a judgment task.
- **Constraint:** The 15% judgment portion carries regulatory and operational risk. Remains human-led or human-in-loop pending **A8**/H2.

### Success metrics

| Metric | Current | Target | Measurement | Source label |
|---|---|---|---|---|
| % of routine tasks executed with no HR Ops action | `[UNKNOWN — assume ~0%]` | ≥ 80% of the 85% routine portion | `tasks_with_no_hr_ops_action / total_tasks` per onboarding | Split **[CITED]**; threshold **[ASSUMED]** — see **A6** (Target — needs validation) |
| HR Ops time per onboarding | `[UNKNOWN]` | ≥ 50% reduction vs. baseline | Time-tracking tagged to `onboarding_id` | **[ASSUMED]** — **A7** (Target — needs validation) |
| "Task fell through the cracks" at day 14 | `[UNKNOWN]` | ≤ 1% of onboardings | Day-14 audit | **[ASSUMED]** — **A7** (Target — needs validation) |
| Judgment-case routing correctness | N/A | 100% reach human review; 0 silent agent decisions | Audit: judgment-classified task has `human_decision_logged` before `COMPLETE` | **[CITED]** (Non-negotiable) |
| Buddy-assignment HR-override rate | N/A | ≤ 10% of auto-assigns in first 20 onboardings | Count of `HumanDecision(OVERRIDE_BUDDY)` / auto-assigns | **[ASSUMED]** — **A11** falsifier |

---

## Deliverable 2 — Delegation Analysis

### Work inventory

| Task / Decision | Classification | Rationale |
|---|---|---|
| IT provisioning — standard role-based tickets | FULL DELEGATION | Rule-based; ServiceNow is named [CITED]; reversible |
| IT provisioning — non-standard requests | HUMAN-IN-LOOP | Deviates from bundle; agent drafts, HR Ops approves |
| Benefits eligibility (benefits system, **H5**) | FULL DELEGATION | Mechanical trigger on `start_date` + `employment_class` |
| Benefits — contractor vs. full-employee classification | HUMAN-LED | [CITED] judgment call; [CITED] prompt rule routes to HR |
| Payroll/time setup (payroll/time system, **H5**) | FULL DELEGATION | Mechanical trigger on employment data |
| Compliance training — standard courses by role & location | FULL DELEGATION | Rule-based mapping; LMS [CITED] |
| Compliance training — multi-jurisdiction track | HUMAN-IN-LOOP | Ambiguity; agent proposes, HR Ops confirms |
| **Buddy matching — three-factor filter match** | **FULL DELEGATION** | **H4** High: seniority + department + location is a deterministic filter. Agent auto-assigns when filter yields an eligible candidate and tie-break (**A11**) picks one. HR Ops can override within 1 business day (auditable veto, not an ex-ante approval). |
| **Buddy matching — no candidate available** | HUMAN-LED | **H4** High + **A10**: agent escalates to HR for manual assignment |
| Welcome materials | FULL DELEGATION | Template-driven |
| 30-day checkpoint scheduling | FULL DELEGATION | Reversible coordination |
| Manager handoff — day-10 summary | FULL DELEGATION | Templated from state |
| I-9 — detect late Section 2 and flag | FULL DELEGATION (detection only) | IRCA 3-business-day rule |
| I-9 — decide whether lateness triggers a hold | HUMAN-LED | [CITED] + H7; IRCA legal exposure |
| Day-14 audit — flag incomplete onboardings | FULL DELEGATION | Rule-based state check |
| Manager handoff — final sign-off | HUMAN-IN-LOOP | Agent compiles; HR Ops signs off |

> **The buddy rows moved again.** In `-742` the auto-assign row was HUMAN-IN-LOOP with ex-ante HR visibility. Under the refined H4 it becomes **FULL DELEGATION** with a post-hoc HR override — the filter is deterministic, not judgemental. Escalation remains HUMAN-LED but triggers only on unavailability (the A10 definition), not on ambiguity or conflict.

### Hard constraints on the boundary

| Constraint | Source | Effect |
|---|---|---|
| `employment_class` determined by Workday; HR Ops authoritative; escalation if agent cannot determine | [CITED] prompt rule | Agent reads only; ESC-CLASS if UNSET or ambiguous |
| Classification must be human-determined | IRS / ACA / state ABC [CITED regulations] | Agent cannot select or change `employment_class` |
| I-9 Section 2 within 3 business days; hold decisions are human | [CITED] + IRCA | Agent detects and flags; cannot initiate or release holds |
| Buddy auto-assign only on three-factor filter match + deterministic tie-break | **H4** High + **A10** + **A11** | Agent auto-assigns; escalates only when filter yields zero candidates. HR retains override right within 1 business day |
| No AI infrastructure today | [CITED] | Build includes orchestration, secrets, audit storage |

**Audit trail.** Every human decision logged with `decision_type, user_id, decision_value, reason, timestamp` — **7-year retention**.

---

## Deliverable 3 — First-Draft Capability Specification

Three capabilities share the `Onboarding` entity.

### Entity model

**`Onboarding`** — `id` UUID PK · `employee_id` Workday UUID immutable · `start_date` ISO date immutable · `role`, `location` enums · `employment_class` enum [FULL_EMPLOYEE, CONTRACTOR, UNSET] · `manager_id` · `state` enum [ACTIVE, COMPLETE, CANCELLED] · `handoff_sent_at` nullable UTC · `created_at`, `updated_at`. Soft-delete via CANCELLED; 7-year retention.

**`Task`** — `id` UUID PK · `onboarding_id` FK (RESTRICT) · `template_key` · `category` enum [IT, BENEFITS, PAYROLL, COMPLIANCE, BUDDY, WELCOME, CHECKPOINT, HANDOFF, I9] · `delegation_class` enum [FULL, HUMAN_IN_LOOP, HUMAN_LED] · `state` enum [PENDING, IN_PROGRESS, BLOCKED_ON_CLASSIFICATION, ESCALATED, COMPLETE, FAILED, WAIVED_BY_HUMAN] · `due_at` UTC immutable · `completed_at` nullable · `external_ref` · `idempotency_key` · `last_actor`.

**`HumanDecision`** — `id` UUID PK · `onboarding_id` FK · `task_id` FK nullable · `decision_type` enum [CLASSIFY_EMPLOYMENT, **OVERRIDE_BUDDY**, MANUAL_ASSIGN_BUDDY, APPROVE_IT_NONSTANDARD, I9_HOLD_DECISION, WAIVE_TASK, COMPLETE_ONBOARDING] · `decision_value` JSON · `user_id` · `reason` required (≤ 2000 chars) · immutable. (Note: `RESOLVE_BUDDY_CONFLICT` from `-742` is removed; `OVERRIDE_BUDDY` and `MANUAL_ASSIGN_BUDDY` are the only two buddy decision types under the refined H4.)

### Capability 1 — Onboarding Orchestrator

**Purpose.** Create and advance `Onboarding`; instantiate ~40 tasks; drive to completion or escalation within 2 weeks.

**Scope.** *In:* Workday new-hire event handling; task lifecycle; overdue detection; day-10 handoff; day-14 audit. *Out:* writing `employment_class`; benefits enrolment while class is UNSET; clinical/medical/legal advice; employee-facing chat.

**Inputs (Workday):** `employee_id` (R, active worker), `start_date` (R, ≥ today + 1d), `role` (R, in `role_template_map`), `location` (R, in `jurisdiction_map`), `employment_class` (R, UNSET only at creation), `manager_id` (R, active).

**Decision logic (10 requirements):**

1. **Onboarding creation.** Exactly one `Onboarding` per `employee_id` per Workday event. Duplicates logged, ignored.
2. **Task instantiation.** For `(role, location, employment_class)`. If UNSET, role/location tasks instantiate; class-dependent (BENEFITS, PAYROLL) go to `BLOCKED_ON_CLASSIFICATION`.
3. **State transitions.** `PENDING → IN_PROGRESS → COMPLETE | FAILED | ESCALATED`; `BLOCKED_ON_CLASSIFICATION → PENDING` on human class-set.
4. **Deadline.** `due_at = start_date + template.offset_days`. Immutable.
5. **OVERDUE.** Derived: `now > due_at AND state IN (PENDING, IN_PROGRESS, BLOCKED_ON_CLASSIFICATION)`. Not stored.
6. **I-9.** `i9_deadline = start_date + 3 business days` [CITED IRCA]. Overdue → ESC-I9. Agent must NOT initiate or release holds.
7. **Day 10 handoff.** Idempotent; summary to `manager_id`; set `handoff_sent_at`.
8. **Day 14 audit.** Any task not `COMPLETE`/`WAIVED_BY_HUMAN` → daily report to HR Ops lead.
9. **Idempotency.** `idempotency_key = onboarding_id + task_id + system_name`.
10. **Classification at face value.** Take `employment_class` at face value per [CITED] prompt rule. No NLP on attached documents. ESC-CLASS if unreliable.

**Escalation triggers:**

| Code | Condition | Notified | SLA |
|---|---|---|---|
| ESC-CLASS | BLOCKED_ON_CLASSIFICATION > 1 business day OR Workday class unreliable | HR Ops (see **A1**) | 3 business days |
| ESC-I9 | Late I-9 with `i9_completed_at IS NULL` | HR Ops lead + compliance | 1 business day |
| **ESC-BUDDY-UNAVAILABLE** | Three-factor filter returns zero eligible candidates (**A10**) | HR Ops | 2 business days — HR records a `MANUAL_ASSIGN_BUDDY` decision |
| ESC-IT-NONSTANDARD | `is_standard_bundle = false` | HR Ops | 1 business day |
| ESC-INTEGRATION | Non-retryable external error | Ops on-call | 4 hours |
| ESC-AUDIT | Day-14 finds non-terminal task | HR Ops lead | End of day |
| ESC-JURISDICTION | Multi-jurisdiction; oversized course set | HR Ops | 1 business day |
| ESC-TRAINING-OVERDUE | 3 nags delivered; still incomplete | HR Ops + manager | 1 business day |

> ESC-BUDDY-CONFLICT from `-742` is **removed** — no score threshold, no gap-to-second, no seniority-level-difference check. The only buddy escalation is unavailability.

### Capability 2 — Buddy Match Assigner

**Purpose.** Auto-assign a buddy when the three-factor filter (seniority + department + location) yields at least one eligible candidate. Escalate to HR for manual assignment when the filter is empty (**H4** High, **A10**).

**Scope.** *In:* eligibility filter; tie-break pick; auto-assign; HR-visible notification with rationale; HR override within 1 business day. *Out:* scoring / ranking / weighting; second-guessing a passing candidate; assigning when filter is empty.

**Decision logic (7 requirements):**

1. **Eligibility filter (three factors + guard rails).** A candidate is eligible iff:
   - **seniority**: tenure ≥ 12 months [CITED spec hygiene; carried from `-742`] AND within the same seniority band as the hire's role (per Workday role-level map);
   - **department**: same or adjacent department as the hire;
   - **location**: same location as the hire;
   - **not the hire's direct manager** (per scenario framing of buddy role);
   - **not on leave on the hire's `start_date`** (per **A10**);
   - **not already buddy to another hire currently in first 30 days** (capacity guard per **A10**).
2. **Tie-break.** Among candidates passing filter: (a) current buddy-load ascending, (b) tenure descending, (c) `employee_id` alphabetical (per **A11**, deterministic).
3. **Auto-assign.** Top candidate per tie-break is assigned. `HumanDecision(OVERRIDE_BUDDY)` is the HR veto path (not ex-ante approval).
4. **No auto-assign when filter empty.** Raise **ESC-BUDDY-UNAVAILABLE**. Task state → `ESCALATED`. HR records `MANUAL_ASSIGN_BUDDY` to resolve.
5. **Rationale log.** Per auto-assign: the three factors matched, the tie-break path taken, candidate counts at each filter step. Written to `human_decision_log` (7-year retention) so HR can audit without replaying the filter.
6. **Override window.** `HumanDecision(OVERRIDE_BUDDY)` within 1 business day reverts the assignment and re-runs the filter with that candidate excluded. If the re-run is empty → ESC-BUDDY-UNAVAILABLE.
7. **No scoring.** The agent must NOT compute a weighted score and must NOT rank candidates beyond the tie-break order in rule 2. A reviewer reading the code should see a filter + tie-break, not a score. (This is the point at which **A3** was retired — see footnote.)

### Capability 3 — Compliance Training Assigner

**Purpose.** Assign LMS courses by role + jurisdiction within 1 business day of start.

**Scope.** *In:* course-set resolution; LMS enrolment; completion-by-webhook; nag cadence. *Out:* course content; grading; genuinely ambiguous jurisdictions (ESC-JURISDICTION).

**Decision logic (5 requirements):**

1. **Course resolution.** Union of `role_course_map[role]` and `jurisdiction_course_map[j]` for each `j`. Deduplicate.
2. **Ambiguous jurisdiction.** `jurisdictions.length > 1` and set > 12 courses [ASSUMED threshold] → ESC-JURISDICTION. No enrolment.
3. **Nag cadence.** `due_at − 3d`, `due_at − 1d`, `due_at + 1d`. Successful-send counter; max 3 nags.
4. **Completion.** `COMPLETE` only on LMS `completed` webhook matching `enrolment_id`. No self-report.
5. **Overdue.** 3 nags delivered, still incomplete → ESC-TRAINING-OVERDUE.

### Integration points

**H3** (Medium) — API baseline assumed. **H5** (High) — benefits + payroll/time confirmed. **H6** (High) — access provided.

| System | Purpose | Auth | Timeout | Retry | Fallback |
|---|---|---|---|---|---|
| Workday | New-hire events; worker reads | OAuth 2.0 `[UNKNOWN tenant URL]` | 10s | 5xx/timeout × 3 (2/4/8s); 4xx → ESC-INTEGRATION | Queue > 15 min outage; FIFO on recovery |
| ServiceNow | IT tickets (per **A5** bundles) | API key | 5s | 5xx/timeout × 3 (1/2/4s) | Tasks PENDING; daily nag; ESC-INTEGRATION at 2 business days |
| LMS | Courses + completion webhook | `[UNKNOWN vendor]` | 10s | 5xx/timeout × 3 (2/4/8s) | Retries 24h; then ESC-INTEGRATION |
| Email (**H3**) | Notifications | Per client infra | 5s | 3 retries (1/2/4s) | Retry 1h; dashboard queue — never silently drop |
| Benefits system (**H5**) | Eligibility + comms | `[UNKNOWN vendor]` | 10s | × 3 (2/4/8s) | ESC-INTEGRATION at 2 business days |
| Payroll/time system (**H5**) | Setup | `[UNKNOWN vendor]` | 10s | × 3 (2/4/8s) | ESC-INTEGRATION at 2 business days |

---

## Deliverable 4 — First-Draft Validation Design

### Happy path

FULL_EMPLOYEE hire, US single-state role. Workday event day −7. Agent creates ServiceNow tickets, enrols LMS, schedules checkpoint, sends welcome pack, queues benefits + payroll setup. Day 0: hire starts; I-9 completed day 2. Day 2: buddy auto-assigned via filter + tie-break; HR Ops sees rationale; no override in the 1-business-day window. Day 10: handoff summary. Day 14: all terminal; no audit entry. HR Ops marks COMPLETE. **Expected:** zero ESC-* raised; one `HumanDecision` (COMPLETE_ONBOARDING).

### Edge cases (7)

| # | Scenario | Expected outcome |
|---|---|---|
| EC-1 | `employment_class = UNSET` at event | BENEFITS, PAYROLL tasks BLOCKED; ESC-CLASS at +1 business day |
| EC-2 | Duplicate Workday webhook | First creates; second `duplicate_ignored`; no second Onboarding |
| EC-3 | Multi-jurisdiction, course set > 12 | ESC-JURISDICTION; no LMS enrolment |
| EC-4 | ServiceNow 5xx × 3 | Task IN_PROGRESS; ESC-INTEGRATION |
| **EC-5** | Three-factor buddy filter returns zero candidates | **ESC-BUDDY-UNAVAILABLE**; no auto-assign; HR records `MANUAL_ASSIGN_BUDDY` |
| **EC-6** | Filter returns 3 candidates; tie-break picks one; HR overrides within 1 business day | Assignment reverted; filter re-runs excluding overridden candidate; new auto-assign |
| EC-7 | Workday pushes new `start_date` post-creation | `start_date` immutable; ESC-INTEGRATION `reason = start_date_drift`; HR decides cancel + recreate |

### Failure modes (4)

| # | Failure | Agent response | Recovery |
|---|---|---|---|
| FM-1 | LMS webhook never arrives | Nag cadence; ESC-TRAINING-OVERDUE after 3 nags | HR marks COMPLETE via HumanDecision |
| FM-2 | Workday worker deleted mid-onboarding | 404 → ESC-INTEGRATION; no writes | HR cancels Onboarding |
| FM-3 | Agent misclassifies IT request as standard | Standard ticket submitted | IT fulfilment flags; HumanDecision APPROVE_IT_NONSTANDARD records correction |
| FM-4 | Classification decision arrives after day 10 | Handoff lists BLOCKED tasks explicitly | HR + manager decide to extend window |

### Delegation boundary test

**Scenario.** Hire labelled FULL_EMPLOYEE in Workday; engagement letter attached describes an SOW-style contractor structure.

**Expected.** Agent takes `employment_class` at face value. Does NOT parse the letter. Does NOT pause. HR Ops catches the discrepancy manually — boundary held.

**Failure shapes:**
- Agent reads the letter and flips path → **boundary violation**.
- Agent blocks demanding reclassification → **boundary violation**.

### Buddy-boundary test (new, under refined H4)

**Scenario.** Three-factor filter returns exactly one eligible candidate, but HR subjectively believes a different employee would be a better buddy based on personality.

**Expected.** Agent auto-assigns the one filter match. HR exercises `HumanDecision(OVERRIDE_BUDDY)` within the 1-business-day window. Filter re-runs excluding that candidate — now returns zero → ESC-BUDDY-UNAVAILABLE. HR records `MANUAL_ASSIGN_BUDDY` for their preferred pick.

**Failure shapes:**
- Agent tries to "rank" candidates beyond tie-break (score, personality inference, team chemistry) → **boundary violation** (A3 retirement means no scoring).
- Agent refuses the override because the filter still technically has a valid match → **boundary violation** (HR veto is absolute in the override window).

---

## Deliverable 5 — Assumptions and Unknowns

> Full detail in the [Assumption Log](#assumption-log) — 16 active entries (plus A3 retired, A9 resolved) in Assumption/Hypothesis/Test/Confidence shape, with scan table, priority queue, and update protocol. This section distils the genuine unknowns and what must be validated before building.

### Data

1. **Real role taxonomy** — **A2**.
2. **Baseline metrics** (time-per-onboarding; day-14 incomplete rate) — **A7**.
3. **Buddy-pool shape** — how often does the three-factor filter return zero? one? many? Affects A11 tie-break stress; affects ESC-BUDDY-UNAVAILABLE volume.

### Systems

4. **Benefits API shape** — `[UNKNOWN]` despite **H5** High.
5. **Payroll/time API shape** — `[UNKNOWN]` despite **H5** High.
6. **LMS vendor + API** — `[UNKNOWN]`.
7. **Workday tenant URL + rate limits** — `[UNKNOWN]`.
8. **Email transport** — SMTP or transactional? Which one? — **H3**.
9. **ServiceNow catalog bundles vs. per-asset** — **A5**.

### Organisation

10. **`employment_class` write owner at HR Ops** — **A1**.
11. **State-level I-9 variations** — **A4**.
12. **I-9 hold operational mechanics** — **H7**.
13. **HR Ops adoption willingness** — **H1** (distinct from H6 access).
14. **"Not available" precise definition** — **A10**.
15. **Tie-break rule preference** — **A11**.

### Problem shape

16. **Judgment-task learnability** — **A8 vs H2**. Still open. Redraws Deliverable 2 when resolved.

### What must be validated before building

- **Blocking:** 4–8 (integration specifics), 14–15 (Capability 2 operational details), 16 (delegation boundary).
- **Soft-blocking:** 1–3, 9–13.
- **Ordering:** matches the [coach-session priority queue](#coach-session-priority-queue).

---

## Self-check (primer § *Self-check before Friday*)

| Check | Status |
|---|---|
| Assumption log visible, numbered, honest about confidence? | ✅ Top of doc. 16 active; 3 High (H4, H5, H6) coach-validated; 1 retired with audit (A3); 1 resolved with audit (A9); 2 new (A10, A11) lifted from H4 operational ambiguity. |
| Can I point every major claim to test / source / explicit assumption? | ✅ `[CITED]` / `[ASSUMED]` throughout Deliverables 1–4; every `[ASSUMED]` traces to H1–H7 or A1–A11. |
| Did I use coach sessions to move specific hypotheses, not chat? | ✅ 22.04.2026 session confirmed H4, H5, H6 and resolved A9. H4 rewrite triggered A3 retirement and A10/A11 creation. |
| Did I complete the closed build loop against Claude Code? | ⏳ Pending. Capability 1 + refined Capability 2 are targets. |
| Would a reviewer challenge my thinking because I've exposed it? | ✅ A3 retirement, A10/A11 creation, and the buddy row shifting from HUMAN-IN-LOOP to FULL DELEGATION are all dated, traceable, and annotated — Friday peer review can see exactly how the refined H4 changed the spec. |

Four ✅, one ⏳.

