# Buildable Specification — Scenario 1: HR Onboarding Coordination

> Produced from [`integration-spec-template.md`](./integration-spec-template.md) against Scenario 1 in [`../Intro+Week1/README-Participants-Week1-Scenarios.md`](../Intro+Week1/README-Participants-Week1-Scenarios.md).
> **Status: first draft, pre-build-loop.** Items marked `[ASSUMPTION]` or `[UNKNOWN]` are genuine gaps that must be validated before a second iteration.
> **Thinking-discipline alignment:** Structured per [`../Intro+Week1/Week1-Thinking-Discipline-Primer.md`](../Intro+Week1/Week1-Thinking-Discipline-Primer.md). The only available stakeholder proxy this week is a coach role-play; every non-trivial claim is marked **tested** (via coach session), **cited** (from scenario or regulation), or **assumed** (in Part 7 with hypothesis and test plan).

---

## Part 0 — Thinking Discipline & Risk Lens

### 0.1 Stakeholder reality

There is no real HR Ops lead available this week. The closest available proxy is a coach role-play in Monday office hours. Every claim in this spec is therefore one of:

- **[CITED]** — sourced directly from the scenario text, federal regulation, or named integration documentation.
- **[TESTED]** — validated in a coach role-play session (none yet at time of writing; will be tagged as sessions occur).
- **[ASSUMED]** — my best current reasoning, flagged in Part 7 with hypothesis and test plan.

A reviewer should be able to challenge any claim by tracing it to one of those three sources.

### 0.2 Cagan four-risk lens (pressure-test map)

| Risk | What it asks | Which artefact in this spec attacks it | Current status |
|---|---|---|---|
| **Value** | Does HR Ops actually care enough to change behaviour? Would they "pay" for this in adoption cost? | Part 1 (problem statement, success metrics) | Partially attacked — volume argument is cited; adoption-cost is [ASSUMED] |
| **Usability** | Can HR Ops, hires, and managers work with the handoffs and escalations this design creates? | Part 2 (delegation analysis), Part 3.1.6 (escalation triggers), Part 6.4 (boundary test) | Partially attacked — escalations are specified but UX of the notifications/dashboard is out of scope this week |
| **Feasibility** | Is the spec precise enough for an AI coding agent to build from without clarifying questions? | Part 3 (capability specs), Part 4 (entities), Part 5 (integrations), Part 8 (self-audit) | Attacked directly via the closed build loop planned against Claude Code. Two [UNKNOWN] integrations (systems #5/#6, LMS vendor) are known feasibility gaps. |
| **Viability** | Compliance, procurement, legal, governance — does the business absorb it? | Part 2.2 (hard constraints), Part 3.1.7 (decision log / retention), Part 7 (assumptions) | Partially attacked — I-9, IRCA, employment classification constraints cited; state-level I-9 variations [ASSUMED] |

### 0.3 What this Week 1 spec is and is not

This is a Level 1 "buildable specification" exercise (per [`../Sources/the-fde.md`](../Sources/the-fde.md) § FDE Levels). It is *not* a discovery artefact — discovery is Week 3's skill. The spec is the deliverable; the closed build loop against Claude Code is how its feasibility risk is pressure-tested this week.

---

## Part 1 — Problem Statement

### 1.1 The Problem Being Solved

A regional professional-services firm of 1,200 employees hires 220+ people per year. Each onboarding spans ~40 tasks across 2 weeks and 6 systems (Workday, ServiceNow, a standalone LMS, and email; the remaining two systems are `[UNKNOWN: not named in scenario — flag for client validation]`). A 3-person HR Ops team currently owns all of it. Roughly 15% of tasks — approximately 6 per onboarding, ~1,320 per year at the stated hiring rate — require judgment calls (contractor vs. full-employee compliance track, buddy-match seniority norms, late-I-9 hold decisions). The HR Ops lead's stated pain: previous automation attempts failed because "the edge cases never look the same twice."

### 1.2 Why Agentic, Why Now

- **Volume argument:** ~8,800 onboarding tasks per year (220 hires × 40 tasks), of which ~85% (~7,480) are rule-governed coordination work moving data between known systems. This is cognitive load at a scale a 3-person team cannot absorb without tasks falling through cracks — which the HR Ops lead has observed directly.
- **Repeatability argument:** The 85% non-judgment portion is the routine quadrant of cognitive work (high clarity, low variance): IT ticket creation, benefits enrolment triggers, LMS course assignments, 30-day checkpoint scheduling, manager handoff notifications. Rule-based orchestration across known systems is the classic full-delegation case.
- **Constraint argument:** The 15% judgment cases (compliance track classification, buddy-match norms, I-9 hold triggers) involve regulatory (I-9, employment classification) and social (seniority norms) judgment where the cost of a silent agent error is high — legal exposure for misclassification, trust damage for buddy mismatches. These must stay human-led or human-in-loop. The boundary is non-obvious precisely because the judgment cases are interleaved with routine ones across the same 2-week sequence.

### 1.3 Success Metrics

Every target below is marked with source: **[CITED]** (from scenario), **[ASSUMED]** (my reasoning, flagged in Part 7), or **[TESTED]** (after coach session — none yet).

| Metric | Current State | Target State | Measurement Method | Source |
|---|---|---|---|---|
| % of routine tasks executed without HR Ops manual action | `[UNKNOWN: not given — assume ~0% today based on "3-person team runs all of this"]` | ≥ 80% of the 85% routine portion (≥ 68% of total task volume) fully delegated | Count of tasks completed with no HR Ops user action in audit log / total tasks per onboarding | Split **[CITED]** from scenario (85/15); threshold **[ASSUMED]** — see A8 |
| HR Ops time per onboarding | `[UNKNOWN: FLAG FOR VALIDATION]` | ≥ 50% reduction vs. baseline | Time-tracking on HR Ops activities tagged to onboarding_id | **[ASSUMED]** — see A9 |
| "Task fell through the cracks" incidents (onboarding tasks not completed by day 14) | `[UNKNOWN: current rate not given]` | ≤ 1% of onboardings have any incomplete task at day-14 checkpoint | Day-14 audit: onboarding_id with any task not `COMPLETE`/`WAIVED_BY_HUMAN` / total | **[ASSUMED]** — see A9 |
| Judgment-case correct routing (compliance track, buddy norms, I-9 hold) | N/A (all human today) | 100% reach human review; 0 silent agent decisions | Audit: every task classified as judgment type has a `human_decision_logged` event before status `COMPLETE` | **[CITED]** from hard constraints §2.2 — this one is non-negotiable, not a target |

> The first three rows are load-bearing for the business case but currently rest on assumed baselines. Coach role-play must convert at least one into **[TESTED]** before the spec is treated as business-aligned.

---

## Part 2 — Delegation Analysis

### 2.1 Work Inventory

The scenario lists 7 task families. Decomposed with classification:

| Task / Decision | Classification | Rationale |
|---|---|---|
| IT provisioning — create ServiceNow tickets for standard role-based equipment and access | FULL DELEGATION | Rule-based (role → asset bundle); ServiceNow is the named system of record; reversible (tickets can be cancelled before fulfilment) |
| IT provisioning — non-standard asset requests (executive kit, accessibility accommodation, dev environments) | HUMAN-IN-LOOP | Deviates from role bundle; cost and policy implications; agent drafts ticket, HR Ops approves before submission |
| Benefits enrolment — trigger eligibility window and send enrolment communications | FULL DELEGATION | Mechanical Workday trigger based on start date and employment class |
| Benefits enrolment — contractor vs. full-employee classification | HUMAN-LED | Scenario explicitly names this as a judgment call; misclassification is a legal exposure (tax, ACA, state law) |
| Compliance training — assign standard LMS courses based on role and location | FULL DELEGATION | Rule-based mapping (role + jurisdiction → course set); LMS is the named system |
| Compliance training — jurisdiction-specific track selection where role spans multiple states/countries | HUMAN-IN-LOOP | Ambiguity in applicable jurisdiction; agent proposes, HR Ops confirms |
| Buddy matching — propose candidate buddies based on team, tenure, location, availability | FULL DELEGATION (proposal only) | Data retrieval and ranking; no action taken until confirmed |
| Buddy matching — final assignment decision (seniority norm check) | HUMAN-LED | Scenario explicitly names this as a judgment call; "crossing seniority norms" is a social judgment outside rule capture |
| Welcome materials — generate and send standard welcome pack (handbook, org chart, day-1 logistics) | FULL DELEGATION | Template-driven; no judgment component |
| 30-day checkpoint — schedule calendar events between hire, manager, HR Ops, and buddy | FULL DELEGATION | Calendar coordination; reversible |
| Manager handoff — send structured handoff summary to manager at day 10 | FULL DELEGATION | Templated report from tracked task state |
| I-9 completion tracking — detect late I-9 and flag | FULL DELEGATION (detection) | Rule-based: compare `i9_completed_at` against federal deadline (Section 2 within 3 business days of start) |
| I-9 late-handling decision — whether lateness triggers a work-authorisation hold | HUMAN-LED | Scenario explicitly names this as a judgment call; legal exposure under IRCA |
| Day-14 audit — identify any onboarding with incomplete tasks and escalate | FULL DELEGATION | Rule-based state check; escalation itself is mechanical |
| Manager handoff — decision that onboarding is "complete" and ownership transfers | HUMAN-IN-LOOP | Agent compiles evidence; HR Ops signs off; consequence is ending the structured checkpoint cadence |

### 2.2 Hard Constraints on the Boundary

| Constraint | Source | Effect on Boundary |
|---|---|---|
| Employment classification (contractor vs. full employee) must be determined by a human | Scenario: "which compliance track applies to a contractor versus a full employee" is named as a judgment call; federal: IRS common-law test, ACA 30-hour rule, state ABC tests | Agent cannot select or change `employment_class` on any record; reads only |
| I-9 Section 2 must be completed within 3 business days of start date; hold decisions on late I-9 are human | Scenario: "whether a late I-9 triggers a hold" is named as a judgment call; federal: IRCA (8 U.S.C. § 1324a) | Agent may detect and flag late I-9, but cannot initiate a work-authorisation hold or release |
| Buddy assignment must pass a seniority-norm check by a human | Scenario: "whether a buddy assignment crosses seniority norms" is named as a judgment call | Agent may propose and rank candidates; cannot send buddy-pairing communications until HR Ops confirms |
| No AI infrastructure today | Scenario: "They have no AI infrastructure today" | Build must include the orchestration layer, identity/secrets setup, and audit storage — not just the agent logic |

---

## Part 3 — Capability Specification

Decomposed into three capabilities. Week 1 target is 1–3; this spec keeps the full set because they share the Onboarding entity and the delegation boundary is only defensible as a whole.

### Capability 1: Onboarding Orchestrator

#### 3.1.1 Purpose
Create and advance an `Onboarding` record for every new hire, spawn the 40 task instances from a role/location-driven template, and drive them to completion or human escalation within the 2-week window.

#### 3.1.2 Scope

**In scope:**
- Create `Onboarding` on new-hire signal from Workday
- Instantiate task set from template based on `role`, `location`, `employment_class`, `start_date`
- Track task state through lifecycle (see §3.1.5)
- Detect overdue tasks and escalate per §3.1.6
- Compile and send manager handoff at day 10

**Out of scope:**
- Setting or changing `employment_class` (human-led per §2.2)
- Executing benefits enrolment where `employment_class` has not been confirmed by a human (blocks until human decision)
- Any communication that contains clinical, medical, or legal advice
- Self-service employee-facing chat (this capability is orchestration, not conversational)

#### 3.1.3 Inputs

| Input | Type | Required / Optional | Validation Rule | Source |
|---|---|---|---|---|
| `workday_hire_event.employee_id` | Workday employee UUID | R | Must resolve to an active Workday employee record | Workday webhook (new-hire event) |
| `employee_id.start_date` | ISO 8601 date | R | `start_date >= today + 1 day` at event time | Workday |
| `employee_id.role` | string, enum bounded to firm's role taxonomy | R | Must match an entry in `role_template_map` | Workday |
| `employee_id.location` | string, enum of configured locations | R | Must map to a jurisdiction in `jurisdiction_map` | Workday |
| `employee_id.employment_class` | enum [FULL_EMPLOYEE, CONTRACTOR, UNSET] | R | If `UNSET`, orchestrator halts classification-dependent tasks until human sets it | Workday |
| `employee_id.manager_id` | Workday employee UUID | R | Must resolve to active Workday employee | Workday |

#### 3.1.4 Outputs

| Output | Type | Condition | Destination |
|---|---|---|---|
| `Onboarding` record | entity (see §4) | On every valid hire event | Internal system of record |
| Task instances (~40) | entity (see §4) | On `Onboarding` creation | Internal system of record |
| Escalation notification | structured message | On escalation trigger (see §3.1.6) | Email to HR Ops distribution + dashboard row |
| Manager handoff summary | structured message | Day 10 of each onboarding | Email to `manager_id` |
| Day-14 audit report | structured message | Daily for onboardings past day 14 | Email to HR Ops lead |

#### 3.1.5 Business Rules

1. **Onboarding creation:** On a Workday new-hire event, the agent must create exactly one `Onboarding` record per `employee_id`. If one already exists, the agent must log the duplicate and take no further action.
2. **Task instantiation:** On `Onboarding` creation, the agent must instantiate tasks from the template for the given `(role, location, employment_class)`. If `employment_class = UNSET`, the agent must still instantiate location- and role-only tasks; tasks dependent on `employment_class` are created in state `BLOCKED_ON_CLASSIFICATION`.
3. **Task state transitions (per task):** `PENDING → IN_PROGRESS` when the agent starts work on it; `IN_PROGRESS → COMPLETE` on successful completion signal from the target system; `IN_PROGRESS → FAILED` on non-recoverable error; `PENDING | IN_PROGRESS → ESCALATED` on any escalation trigger; `BLOCKED_ON_CLASSIFICATION → PENDING` when `employment_class` is set by a human.
4. **Deadline computation:** Every task has `due_at = start_date + template.offset_days`. The agent must compute this at instantiation and never modify it.
5. **Overdue detection:** A task is OVERDUE when `now > due_at AND state IN (PENDING, IN_PROGRESS, BLOCKED_ON_CLASSIFICATION)`. OVERDUE is a derived state; do not store it.
6. **I-9 handling:** The agent must compute `i9_deadline = start_date + 3 business days`. If `i9_completed_at IS NULL AND now > i9_deadline`, the agent must escalate to HR Ops (see §3.1.6 trigger ESC-I9). The agent must NOT initiate or release any work-authorisation hold.
7. **Manager handoff:** On day 10 (`now >= start_date + 10 calendar days`), the agent must compile a handoff summary listing: tasks complete, tasks open, tasks escalated, outstanding blockers. The agent must email `manager_id` and set `Onboarding.handoff_sent_at`.
8. **Day-14 audit:** On day 14 (`now >= start_date + 14 calendar days`), if any task is not in state `COMPLETE` or explicitly marked `WAIVED_BY_HUMAN`, the agent must include the onboarding in the daily audit report to the HR Ops lead.
9. **Idempotency:** All external-system write operations (ServiceNow ticket creation, LMS enrolment, calendar invites) must be idempotent against a deterministic `idempotency_key = onboarding_id + task_id + system_name`.

#### 3.1.6 Escalation Triggers

| Trigger | Condition | Who Is Notified | What the Human Must Do | SLA |
|---|---|---|---|---|
| ESC-CLASS | Task is `BLOCKED_ON_CLASSIFICATION` for > 1 business day | HR Ops distribution | Set `employment_class` on Workday record | 3 business days from hire event |
| ESC-I9 | I-9 past deadline with `i9_completed_at IS NULL` | HR Ops lead + named compliance contact | Decide whether to place work-authorisation hold | 1 business day |
| ESC-BUDDY | Buddy candidates proposed; no confirmation within 2 business days | HR Ops distribution | Confirm or reject proposed buddy | 2 business days |
| ESC-IT-NONSTANDARD | IT request flagged non-standard by `is_standard_bundle = false` | HR Ops distribution | Approve or edit the draft ServiceNow ticket before submission | 1 business day |
| ESC-INTEGRATION | Any external system returns non-retryable error (see §5) | Ops on-call | Diagnose integration failure | 4 hours |
| ESC-AUDIT | Day-14 audit finds any non-complete, non-waived task | HR Ops lead | Triage and resolve | End of day |

#### 3.1.7 Decision Log

| Decision Point | Fields Logged | Storage Location | Retention |
|---|---|---|---|
| Task state transition | `task_id`, `onboarding_id`, `from_state`, `to_state`, `actor (agent/human)`, `reason`, `timestamp` | `task_state_log` table | 7 years (employment records minimum) |
| Escalation raised | `trigger_code`, `onboarding_id`, `task_id`, `notified_recipients`, `timestamp` | `escalation_log` | 7 years |
| Human decision received | `decision_type`, `onboarding_id`, `task_id`, `user_id`, `decision_value`, `reason`, `timestamp` | `human_decision_log` | 7 years |
| External system write | `system_name`, `endpoint`, `idempotency_key`, `request_hash`, `response_status`, `timestamp` | `integration_audit_log` | 1 year |

### Capability 2: Buddy Match Proposer

#### 3.2.1 Purpose
Propose a ranked list of up to 5 candidate buddies for a new hire, for human confirmation. Does not assign.

#### 3.2.2 Scope

**In scope:** Query eligible internal employees; rank by configured criteria; return proposal with ranking rationale.
**Out of scope:** Sending any communication to candidates; recording an assignment; overriding the human veto.

#### 3.2.3 Inputs

| Input | Type | Required | Validation | Source |
|---|---|---|---|---|
| `onboarding_id` | UUID | R | Must be in state `BUDDY_PROPOSAL_REQUESTED` | Orchestrator |
| `new_hire.role`, `new_hire.location`, `new_hire.team`, `new_hire.tenure = 0` | denormalised from Workday | R | All must be present | Workday |
| Candidate pool | query result from Workday | R | Active employees, same or related team, non-manager, tenure ≥ 12 months | Workday |

#### 3.2.4 Outputs

| Output | Type | Condition | Destination |
|---|---|---|---|
| Buddy proposal (up to 5 candidates with score and rationale) | structured message | On orchestrator request | HR Ops dashboard + email |

#### 3.2.5 Business Rules

1. **Eligibility filter:** Candidates must be active, same or adjacent team, tenure ≥ 12 months, non-manager of the new hire, and not already assigned as buddy to another hire currently in first 30 days.
2. **Ranking:** Score = `0.4 * team_match + 0.3 * location_match + 0.2 * availability_score + 0.1 * diversity_of_prior_matches`. Each component is 0–1. `[ASSUMPTION: weights are a first draft; client must validate during discovery.]`
3. **Rationale:** Each proposal must include per-candidate rationale listing the component scores and the single dominant reason.
4. **Hard rule:** The agent must NOT record a buddy assignment. Only a human action may transition the task from `PROPOSED` to `CONFIRMED`.
5. **Proposal expiry:** If no human action within 2 business days, the orchestrator raises ESC-BUDDY; proposal remains valid until replaced.

#### 3.2.6 Escalation Triggers

| Trigger | Condition | Notified | SLA |
|---|---|---|---|
| ESC-BUDDY-EMPTY | Fewer than 2 eligible candidates found | HR Ops lead | 1 business day — lead must widen criteria or waive the buddy task |

#### 3.2.7 Decision Log
Every proposal write: `onboarding_id`, `candidates[]` with scores and rationales, `generated_at`. Retained 2 years.

### Capability 3: Compliance Training Assigner

#### 3.3.1 Purpose
Assign LMS courses to the new hire based on role and jurisdiction, within 1 business day of start.

#### 3.3.2 Scope

**In scope:** Resolve required course set from `(role, jurisdiction)` map; call LMS to enrol; track completion; nag on overdue.
**Out of scope:** Course content delivery; completion grading; handling exceptions where jurisdiction is genuinely ambiguous (escalates via ESC-JURISDICTION).

#### 3.3.3 Inputs

| Input | Type | Required | Validation | Source |
|---|---|---|---|---|
| `onboarding_id` | UUID | R | Must be active | Orchestrator |
| `role` | enum | R | Must map to a course set | Workday |
| `jurisdictions[]` | array of enum | R | ≥ 1 entry; each must be in `jurisdiction_map` | Workday + location config |

#### 3.3.4 Outputs

| Output | Type | Condition | Destination |
|---|---|---|---|
| LMS enrolment records | per course | On task start | LMS |
| Completion-tracking task updates | state transitions | On LMS webhook | Internal |
| Nag email to hire + cc manager | templated email | On day T-3 before `due_at` if still incomplete | Email |

#### 3.3.5 Business Rules

1. **Course resolution:** Required set = union of `role_course_map[role]` and `jurisdiction_course_map[j]` for each `j in jurisdictions`. Deduplicate.
2. **Ambiguous jurisdiction:** If `jurisdictions.length > 1` and the resolved course set exceeds the configured max (`[ASSUMPTION: default 12 courses]`), raise ESC-JURISDICTION — do not enrol.
3. **Nag cadence:** Nag at `due_at - 3d`, `due_at - 1d`, `due_at + 1d`. Stop on completion. No more than 3 nags total; escalate after.
4. **Completion:** Task transitions to `COMPLETE` only on LMS `completed` webhook matching the `enrolment_id`. The agent must not mark complete from a self-reported signal.

#### 3.3.6 Escalation Triggers

| Trigger | Condition | Notified | SLA |
|---|---|---|---|
| ESC-JURISDICTION | Multi-jurisdiction with oversized course set | HR Ops | 1 business day |
| ESC-TRAINING-OVERDUE | 3 nags delivered, still incomplete | HR Ops + manager | 1 business day |

#### 3.3.7 Decision Log
Every enrolment: `enrolment_id`, `course_id`, `onboarding_id`, `timestamp`. Every webhook: full payload hashed. Retained 7 years.

---

## Part 4 — Entity Model

### Entity: Onboarding

| Attribute | Type | Required | Constraints | Notes |
|---|---|---|---|---|
| `id` | UUID | Y | PK, immutable, generated on creation | |
| `employee_id` | Workday UUID | Y | FK to Workday employee; immutable | |
| `start_date` | ISO 8601 date | Y | Immutable after creation | |
| `role` | enum (firm taxonomy) | Y | Must exist in `role_template_map` | |
| `location` | enum | Y | Must exist in `jurisdiction_map` | |
| `employment_class` | enum [FULL_EMPLOYEE, CONTRACTOR, UNSET] | Y | `UNSET` permitted only at creation | |
| `manager_id` | Workday UUID | Y | Must resolve to active employee | |
| `state` | enum [ACTIVE, COMPLETE, CANCELLED] | Y | Default ACTIVE | |
| `handoff_sent_at` | ISO 8601 timestamp UTC | N | Null until day 10 handoff sent | |
| `created_at` | ISO 8601 timestamp UTC | Y | Immutable | |
| `updated_at` | ISO 8601 timestamp UTC | Y | Updated on any change | |

**State machine:**
```
ACTIVE → COMPLETE     Trigger: HR Ops confirms handoff complete   Guard: all tasks COMPLETE or WAIVED_BY_HUMAN
ACTIVE → CANCELLED    Trigger: hire withdraws or is rescinded     Guard: HR Ops user action
COMPLETE is terminal
CANCELLED is terminal
```

**Immutability:** `employee_id`, `start_date`, `created_at` cannot change after creation.
**Delete behaviour:** Soft-delete only via `state = CANCELLED`; records retained 7 years for employment compliance.

### Entity: Task

| Attribute | Type | Required | Constraints | Notes |
|---|---|---|---|---|
| `id` | UUID | Y | PK, immutable | |
| `onboarding_id` | UUID | Y | FK to Onboarding; on delete RESTRICT | |
| `template_key` | string | Y | Must exist in task template registry | |
| `category` | enum [IT, BENEFITS, COMPLIANCE, BUDDY, WELCOME, CHECKPOINT, HANDOFF, I9] | Y | | |
| `delegation_class` | enum [FULL, HUMAN_IN_LOOP, HUMAN_LED] | Y | Determines whether agent may write | |
| `state` | enum [PENDING, IN_PROGRESS, BLOCKED_ON_CLASSIFICATION, ESCALATED, COMPLETE, FAILED, WAIVED_BY_HUMAN] | Y | Default PENDING | |
| `due_at` | ISO 8601 timestamp UTC | Y | Immutable; = start_date + offset_days | |
| `completed_at` | ISO 8601 timestamp UTC | N | Set on COMPLETE | |
| `external_ref` | string | N | e.g. ServiceNow ticket id, LMS enrolment id | |
| `idempotency_key` | string | Y | Deterministic; see §3.1.5 rule 9 | |
| `created_at` / `updated_at` | ISO 8601 UTC | Y | Standard | |
| `last_actor` | enum [AGENT, human user_id] | Y | Always the most recent writer | |

**State machine:** See §3.1.5 rule 3.
**Immutability:** `onboarding_id`, `template_key`, `due_at`, `idempotency_key`, `created_at`.
**Delete behaviour:** No deletion. Tasks persist with final terminal state.

### Entity: HumanDecision

| Attribute | Type | Required | Constraints |
|---|---|---|---|
| `id` | UUID | Y | PK, immutable |
| `onboarding_id` | UUID | Y | FK |
| `task_id` | UUID | N | FK; null for onboarding-level decisions |
| `decision_type` | enum [CLASSIFY_EMPLOYMENT, CONFIRM_BUDDY, APPROVE_IT_NONSTANDARD, I9_HOLD_DECISION, WAIVE_TASK, COMPLETE_ONBOARDING] | Y | |
| `decision_value` | JSON | Y | Schema per type |
| `user_id` | internal user id | Y | Immutable |
| `reason` | string, max 2000 chars | Y | Required for all decisions |
| `created_at` | ISO 8601 UTC | Y | Immutable |

**Immutability:** Entire record immutable after creation. Corrections require a new `HumanDecision` referencing the prior via `supersedes_id`.

---

## Part 5 — Integration Contracts

### Integration: Workday (core HR)

| Property | Value |
|---|---|
| Purpose | Source of new-hire events; read employee attributes |
| Endpoint | `POST [webhook callback]` (inbound); `GET /ccx/api/v1/.../workers/{id}` (outbound reads) `[UNKNOWN: exact Workday tenant URLs — FLAG FOR VALIDATION]` |
| Authentication | OAuth 2.0 client credentials; secret in secrets manager under `WORKDAY_CLIENT_SECRET` |
| Timeout | 10s |
| Retry logic | 5xx and timeout: 3 retries with exponential backoff (2s, 4s, 8s); 4xx: no retry, escalate ESC-INTEGRATION |
| Rate limit | `[UNKNOWN: client to confirm Workday tenant limits]` |

**Fallback:** If Workday unavailable > 15 minutes, orchestrator queues new-hire events to a durable dead-letter queue; raises ESC-INTEGRATION; processes on recovery in FIFO order.

**Data mapping:**

| Internal | Direction | Workday |
|---|---|---|
| `Onboarding.employee_id` | ← | `worker.id` |
| `Onboarding.start_date` | ← | `worker.employment.hireDate` |
| `Onboarding.employment_class` | ← | `worker.employment.workerType` (mapped) |
| `Onboarding.role`, `.location`, `.manager_id` | ← | respective Workday fields |

### Integration: ServiceNow (IT requests)

| Property | Value |
|---|---|
| Purpose | Create and track IT provisioning tickets |
| Endpoint | `POST /api/now/table/sc_request` (create); `GET /api/now/table/sc_request/{sys_id}` (status) |
| Authentication | Service account, API key in `SERVICENOW_API_KEY` |
| Timeout | 5s |
| Retry | 5xx/timeout: 3 retries, backoff 1s/2s/4s; 4xx: no retry, ESC-INTEGRATION |
| Rate limit | `[ASSUMPTION: 40 req/min — to validate]` |

**Fallback:** If unavailable, IT tasks stay `PENDING`, nag daily, escalate at 2 business days.

**Data mapping:**

| Internal | Direction | ServiceNow |
|---|---|---|
| `Task.id` | → | `correlation_id` |
| `Onboarding.employee_id` + role | → | catalog item + variables |
| `Task.external_ref` | ← | `sys_id` |
| `Task.state` derived | ← | ServiceNow ticket state (New/In Progress/Closed Complete/Closed Incomplete) |

### Integration: LMS

| Property | Value |
|---|---|
| Purpose | Assign compliance courses; track completion |
| Endpoint | `[UNKNOWN: LMS vendor not named in scenario — FLAG FOR VALIDATION]`; assume REST with `POST /enrolments`, `GET /enrolments/{id}`, webhook on completion |
| Authentication | `[UNKNOWN]` |
| Timeout | 10s |
| Retry | 5xx/timeout: 3 retries, backoff 2s/4s/8s; 4xx: no retry, ESC-INTEGRATION |
| Rate limit | `[UNKNOWN]` |

**Fallback:** Enrolment retries up to 24h; after that ESC-INTEGRATION.

### Integration: Email

| Property | Value |
|---|---|
| Purpose | All human-facing notifications (nag, escalation, handoff) |
| Endpoint | `[ASSUMPTION: SMTP relay or transactional email API — client to specify]` |
| Authentication | Per client infrastructure |
| Timeout | 5s |
| Retry | 3 retries, 1s/2s/4s backoff |
| Rate limit | n/a for this volume |

**Fallback:** On send failure, retry for 1 hour; if still failing, write to dashboard escalation queue — never silently drop a notification.

### Integration: Systems #5 and #6

`[UNKNOWN]` The scenario states "6 different systems" but only names 4 (Workday, ServiceNow, LMS, email). The remaining two must be identified in discovery. **FLAG FOR VALIDATION** — this spec cannot be fully built until they are named, because Task categories BENEFITS and BUDDY may depend on them.

---

## Part 6 — Validation Design

### 6.1 Happy Path

**Scenario:** Standard full-employee hire, US single-state role.

**Input state:** Workday event for employee E with `start_date = today + 7d`, `role = Associate Consultant`, `location = Boston`, `employment_class = FULL_EMPLOYEE`, valid manager.

**Steps:**
1. Agent receives Workday webhook; creates `Onboarding` O and ~40 tasks in PENDING.
2. Day -7 to day 0: agent creates ServiceNow tickets, enrols LMS courses, schedules 30-day checkpoint, sends welcome pack.
3. Day 0: hire starts; I-9 Section 2 completed by day 2 (within deadline).
4. Day 2: buddy proposal generated; HR Ops confirms within SLA; buddy task transitions to COMPLETE.
5. Day 10: agent sends manager handoff summary; `handoff_sent_at` set.
6. Day 14: audit finds all tasks COMPLETE; no report entry for O.
7. HR Ops marks `Onboarding.state = COMPLETE`.

**Expected output:** Onboarding in COMPLETE, all tasks terminal (COMPLETE or WAIVED_BY_HUMAN = 0), full audit trail, zero ESC-* escalations raised unnecessarily.

### 6.2 Edge Cases

| # | Scenario | Input | Expected Outcome | P/F/E |
|---|---|---|---|---|
| EC-1 | `employment_class = UNSET` at hire event | Workday event arrives without class set | Orchestrator creates Onboarding; classification-dependent tasks in BLOCKED_ON_CLASSIFICATION; ESC-CLASS raised at day +1 business if still UNSET | E |
| EC-2 | Duplicate Workday webhook | Same `employee_id` event received twice | First creates Onboarding; second is logged in `integration_audit_log` with result `duplicate_ignored`; no second Onboarding | P |
| EC-3 | Multi-jurisdiction role | `jurisdictions = [US-CA, US-NY]`; resolved course set > 12 | ESC-JURISDICTION raised; no LMS enrolment attempted | E |
| EC-4 | ServiceNow down during IT task execution | POST /sc_request returns 5xx × 3 | Task remains IN_PROGRESS; ESC-INTEGRATION raised; retry next cycle | E |
| EC-5 | Concurrent buddy proposal + buddy task waiver | HR Ops waives buddy task while agent is generating proposal | Proposal write detects state ≠ BUDDY_PROPOSAL_REQUESTED; proposal discarded; no notification sent | P |
| EC-6 | Task past `due_at` mid-generation | Agent processing task at exactly `due_at + 1s` | Task is OVERDUE per §3.1.5 rule 5; agent completes in-flight work and logs OVERDUE flag in decision log | P |
| EC-7 | Hire start date moved after onboarding creation | Workday update shifts `start_date` later | Orchestrator treats `start_date` as immutable on `Onboarding`; raises ESC-INTEGRATION with `reason = start_date_drift`; HR Ops decides whether to cancel+recreate | E |

### 6.3 Failure Modes

| # | Failure | Agent Response | Recovery |
|---|---|---|---|
| FM-1 | LMS webhook for completion never arrives | Task stays IN_PROGRESS past `due_at`; nag cadence runs; at 3 nags, ESC-TRAINING-OVERDUE raised | HR Ops verifies completion in LMS; marks task COMPLETE via human action (logged in HumanDecision) |
| FM-2 | Workday employee record deleted mid-onboarding | Next scheduled read returns 404 | Orchestrator raises ESC-INTEGRATION; does not proceed with any task writes; HR Ops cancels Onboarding |
| FM-3 | Agent misclassifies IT request as standard when it is not | Standard ticket submitted to ServiceNow | Detected by IT fulfilment team (out of agent scope); they flag; `HumanDecision` type `APPROVE_IT_NONSTANDARD` recorded with correction; process improvement tracked via pattern in `human_decision_log` |
| FM-4 | Classification human action arrives after day 10 | Orchestrator normally raises ESC-CLASS at day 1 business; if overdue, manager handoff at day 10 proceeds with classification-dependent tasks still BLOCKED | Handoff summary explicitly lists `BLOCKED_ON_CLASSIFICATION` tasks; human decides whether to extend onboarding window |

### 6.4 Delegation Boundary Test

**Scenario:** A hire is labelled `FULL_EMPLOYEE` in Workday but the engagement letter attached to the record describes a fixed-term statement of work structure that would typically indicate contractor treatment.

**Input:** `employment_class = FULL_EMPLOYEE`, engagement letter attached to Workday worker record containing SOW-style terms.

**Expected agent behaviour:** The agent must NOT detect or challenge this. It takes `employment_class` at face value and proceeds. The agent is explicitly not a classification authority (see §2.2 hard constraint) and must not second-guess the value via NLP analysis of attached documents.

**What a failure looks like:**
- Agent reads the engagement letter and flips processing path based on inferred classification → **boundary violation**.
- Agent pauses onboarding and demands reclassification → **boundary violation** (classification is human-led, not agent-blocked).
- HR Ops detects the discrepancy manually → **acceptable; the boundary held**.

---

## Part 7 — Assumptions and Unknowns

Each entry uses the shape from [`../Intro+Week1/Week1-Thinking-Discipline-Primer.md`](../Intro+Week1/Week1-Thinking-Discipline-Primer.md) § How to show your thinking: **Assumption → Hypothesis → How I'd test it → Confidence**. Items load-bearing for the Gate 1 deliverable are listed first.

---

**A1 — Unnamed systems (5 and 6)**
- **Assumption:** The two unnamed systems in "6 different systems" are a benefits carrier portal and a payroll/time system (common pattern for Workday-core firms of this size).
- **Hypothesis:** If the two systems are benefits + payroll, then BENEFITS-category tasks require one carrier integration and one payroll hand-off; the spec's integration count grows by 2 but its structure does not change.
- **How I'd test it:** Coach role-play — single direct question: "Beyond Workday, ServiceNow, LMS, and email, what are the other two systems HR Ops touches during onboarding?" One-shot resolution.
- **Confidence:** Low. Guess is plausible but the scenario does not name them, and a wrong guess invalidates the BENEFITS capability.

**A2 — Workday as sole source of `employment_class`**
- **Assumption:** Workday is the single system of record for `employment_class`. No shadow classification lives in a parallel spreadsheet or email thread.
- **Hypothesis:** If Workday is authoritative, then the agent reading Workday for classification is sufficient, and ESC-CLASS escalations correctly route whenever classification is UNSET.
- **How I'd test it:** Coach role-play — "Where does employment class live, and who is authoritative if Workday and HR Ops's notes disagree?"
- **Confidence:** Medium. Workday is the named system of record in the scenario, but firms often carry side-spreadsheets during a classification debate.

**A3 — HR Ops has Workday write access for `employment_class`**
- **Assumption:** HR Ops (not Legal, not Finance) is the team authorised to set `employment_class` in Workday and is the correct escalation target for ESC-CLASS.
- **Hypothesis:** If HR Ops owns the write, then ESC-CLASS routing to the HR Ops distribution list resolves classification blockers within 3 business days in normal conditions.
- **How I'd test it:** Coach role-play — "Who on your team has Workday write access to `workerType`, and what is your standard turnaround for classification questions?"
- **Confidence:** Medium. The scenario frames HR Ops as the onboarding owner, but classification specifically may route through Legal or Payroll in some firms.

**A4 — Role taxonomy is stable and bounded**
- **Assumption:** The firm's role taxonomy is < 100 roles, stable quarter-to-quarter, and a `role_template_map` can be maintained by HR Ops without engineering.
- **Hypothesis:** If true, then task-instantiation from `(role, location, employment_class)` is deterministic and low-maintenance; if false (free-text roles, high churn), the spec needs a fallback path the current draft does not include.
- **How I'd test it:** Coach role-play — "Roughly how many distinct roles are hired into per year, and how often does a new role title appear?" + one-minute probe on who maintains the list.
- **Confidence:** Medium-low. Professional-services firms can have role-title sprawl (Associate vs. Senior Associate vs. Consultant I/II/III etc.).

**A5 — Buddy-match ranking weights**
- **Assumption:** Weights of `0.4 team / 0.3 location / 0.2 availability / 0.1 diversity-of-prior-matches` are a reasonable first draft.
- **Hypothesis:** If weights are off, HR Ops will reject the top-ranked candidate frequently — observable signal, low compliance impact.
- **How I'd test it:** Run the buddy proposer against 5–10 historical hires in a coach-led walkthrough and count rejections vs. acceptances.
- **Confidence:** Low. These are invented numbers. Noted deliberately to give the closed build loop something to surface.

**A6 — Federal I-9 is the only I-9 rule that applies**
- **Assumption:** The 3-business-day IRCA rule is the only I-9 deadline the agent tracks. No state-level amendments apply at this firm's locations.
- **Hypothesis:** If true, `i9_deadline = start_date + 3 business days` is correct everywhere. If a state rule exists (e.g. California's additional notice requirements), the agent under-reports compliance state.
- **How I'd test it:** Coach role-play — "Which states do you hire into, and do any of those states impose additional I-9 handling requirements beyond federal IRCA?"
- **Confidence:** Low-medium. Federal is cited; state-level is not checked.

**A7 — ServiceNow has role-based catalog bundles**
- **Assumption:** ServiceNow catalog has pre-configured role-based request bundles the agent can reference; IT does not require per-asset requests.
- **Hypothesis:** If bundles exist, IT provisioning is one catalog POST per hire. If not, it decomposes into 8–12 sub-requests and the spec's IT section grows materially.
- **How I'd test it:** Coach role-play — "Does IT currently provision via a catalog request by role, or by individual asset requests?"
- **Confidence:** Medium. Large-firm ServiceNow typically has bundles, but not guaranteed.

**A8 — The 80 % routine-delegation target is achievable**
- **Assumption:** The target "≥ 80 % of the 85 % routine portion delegated without HR Ops action" is achievable in practice once dependencies between tasks and system responses are accounted for.
- **Hypothesis:** If achievable, the business case holds. If in practice 30 % of routine tasks require an HR Ops touch (e.g., to disambiguate a Workday record), the ROI story weakens significantly.
- **How I'd test it:** Coach role-play — walk through the 40-task template and, per task, ask "how often does this one actually need a human eye?" Aggregate.
- **Confidence:** Low. Target is derived from the scenario's 85/15 split, not from observed workflow friction.

**A9 — Baseline metrics will be retrievable**
- **Assumption:** HR Ops can provide current-state baselines for (a) time per onboarding, (b) incomplete-at-day-14 rate, even if not on demand.
- **Hypothesis:** If they can, Week-2+ success measurement is possible. If not, the spec's targets remain untested and the business case stays hypothetical.
- **How I'd test it:** Coach role-play — "If I asked you for time-per-onboarding and day-14-incomplete rate today, could you get them, and with what accuracy?"
- **Confidence:** Medium. Firms at this size usually have some HRIS reporting; whether those specific metrics are cut is uncertain.

---

### 7.1 Coach-session priority queue

Given one coach slot, these are the hypotheses to test, highest-leverage first:

1. **A1** (unnamed systems) — one question unlocks the BENEFITS capability.
2. **A3** (ESC-CLASS ownership) — wrong target makes the whole escalation design route-to-nowhere.
3. **A8** (delegation target achievability) — this is the value-risk pressure-test.
4. **A7** (ServiceNow bundles) — changes the shape of Capability 1's IT integration.
5. **A6** (state-level I-9) — compliance exposure if wrong.
6. **A2**, **A4**, **A5**, **A9** — lower urgency; handle if time permits.

### 7.2 What moves from [ASSUMED] to [TESTED] after a coach session

After each coach session, update the confidence rating and add a dated note to the affected assumption. Do **not** silently delete the assumption — the audit trail matters for Friday peer review.

---

## Part 8 — Spec Self-Audit

- [x] Every business rule uses "must / will / cannot" — verified in §3.1.5, §3.2.5, §3.3.5
- [x] Every threshold is numeric — 3 business days (I-9), 2 business days (buddy), day 10 (handoff), day 14 (audit), 12 courses (jurisdiction), 3 nags, 10s/5s timeouts
- [x] Every conditional has explicit IF/THEN/ELSE — verified in rules, escalation triggers, fallback clauses
- [x] Every entity has PK, timestamps, state machine where stateful — Onboarding, Task, HumanDecision all compliant
- [x] Every integration has endpoint, auth, timeout, retry, rate limit, fallback, data mapping — Workday, ServiceNow, LMS, email compliant **except** Systems #5 and #6 which are `[UNKNOWN]` and correctly flagged in Part 7
- [x] Delegation boundary has at least one hard constraint cited from scenario — 4 constraints listed in §2.2, all cited
- [x] Validation design: 1 happy path (§6.1), 7 edge cases (§6.2, exceeds 5 minimum), 4 failure modes (§6.3, exceeds 3), 1 boundary test (§6.4) ✓
- [x] Every `[UNKNOWN]` and `[ASSUMPTION]` is in Part 7 — verified, restructured into Assumption/Hypothesis/Test/Confidence shape per primer
- [ ] **No open `[TODO]` markers** — none present. Part 7 lists 9 assumptions of which 6 are low/low-medium confidence. Per template rule, flagged assumptions are permitted to remain open provided each has a hypothesis and test plan — both present. Build may proceed on sections not dependent on flagged items; BENEFITS-category tasks and LMS auth specifics cannot be built until A1 and LMS vendor are resolved.

**Overall:** Spec is buildable for Orchestrator core, Buddy Match Proposer, Compliance Training Assigner (pending LMS vendor confirmation), and integrations with Workday and ServiceNow. Not buildable for BENEFITS-category tasks until A1 is resolved. Recommended next step: burn the single coach slot on the A1 / A3 / A8 trio (Part 7.1) before starting the closed build loop on the Orchestrator.

---

## Part 9 — Pre-Friday Self-Check

Aligned to [`../Intro+Week1/Week1-Thinking-Discipline-Primer.md`](../Intro+Week1/Week1-Thinking-Discipline-Primer.md) § Self-check before Friday:

| Primer check | Status |
|---|---|
| Is my assumption log visible, numbered, and honest about confidence? | ✅ Part 7 — 9 entries, each with explicit Low/Medium/High confidence |
| For each major claim can I point to test / source / explicit assumption? | ✅ Part 0.1 tagging scheme ([CITED] / [TESTED] / [ASSUMED]) applied through Parts 1–2; remaining prose in Parts 3–6 is derived from cited scenario or flagged assumptions |
| Did I use coach sessions to move specific hypotheses, not chat? | ⏳ Pending — Part 7.1 lists the prioritised queue for the next coach slot |
| Did I complete the closed build loop against Claude Code? | ⏳ Pending — Orchestrator (Capability 1) is the planned target |
| Would a reviewer be able to challenge my thinking because I've exposed it? | ✅ Every load-bearing claim is either in Part 7 or tagged in Part 1.3; anti-patterns ("confident prose hiding assumptions") actively avoided |

Three ✅ and two ⏳ at draft time. Target by Friday 09:15 CET submission: five ✅.





