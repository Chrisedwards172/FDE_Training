# Problem Statement & Success Metrics — Scenario 1 (HR Onboarding Coordination)

## Front-matter

- **Submission ID:** `problem-statement-scenario-1-201`
- **Source scenario:** [`../../scenario-1.md`](../../scenario-1.md)
- **Date produced:** 24.04.2026
- **Status:** First draft, pre-coach-session for this deliverable. HUMAN assumptions **H4**, **H5**, **H6** already carry **High** (coach-validated) ratings per the scenario file; **H1**, **H3**, **H7** are **Medium**; **H2** is **Low**.

---

## 2. Assumption Log (scoped to this deliverable)

### 2.1 Scan table

| # | Source | Assumption (one line) | Cagan risk | Confidence | Metric/statement at risk if wrong |
|---|---|---|---|---|---|
| H1 | HUMAN | HR Ops will adopt an agent for onboarding coordination | Value | Medium | The whole business case; without adoption, no baseline improvement |
| H2 | HUMAN | The 15% judgment-call tasks follow identifiable patterns | Feasibility | Low | Routine-delegation % target (over-claims if patterns do not hold) |
| H7 | HUMAN | "Late I-9 triggers a hold" implies a regulatory hold with legal exposure | Viability | Medium | Boundary-respect non-negotiable; wrong → compliance breach framing wrong |
| A1 | AGENT | Baseline "fell-through-the-cracks" rate exists in HR Ops records (e.g. open-task-at-day-14 count) but is not stated in scenario | Value | Low | Quality metric "Current State" column — cannot set target without baseline |
| A2 | AGENT | Current time-per-onboarding for the 3-person HR Ops team is ≈ 220 hires × 40 tasks ÷ 3 FTE workload-share, but actual minutes-per-hire unknown | Value | Low | Human-effort metric baseline |
| A3 | AGENT | The scenario's "roughly 15%" is 15% of the ~40 tasks (≈ 6 tasks per onboarding) rather than 15% of onboardings overall | Feasibility | Medium | Routine-delegation denominator and target |
| A4 | AGENT | I-9 Section 2 deadline is 3 business days from start date (IRCA 8 U.S.C. § 1324a) — used to frame the "late I-9" hold | Viability | Medium | Boundary-respect wording; target of 100% becomes ambiguous if deadline semantics wrong |

### 2.2 Coach-session priority queue (for this deliverable)

1. **A1** — Baseline "fell-through-the-cracks" rate. Without a baseline, the quality metric is unanchored and the business case cannot be defended. **Highest leverage.**
2. **A2** — Current minutes-per-onboarding for HR Ops. Same reason; drives the human-effort target.
3. **A3** — Denominator for the 15% judgment-call framing. Moves the routine-delegation target materially.
4. **H2** — Patterning of judgment calls. Risk of over-claiming what is routine.
5. **H7 / A4** — I-9 "hold" semantics. Must be confirmed against IRCA before the boundary-respect metric is treated as business-aligned.
6. **H1** — Adoption signal. Load-bearing on Viability but does not move any target number, only the probability the business case is realised.

### 2.3 Update protocol

After each coach session, update the affected entry **in place**: raise or lower confidence, add a dated note, and change dependent prose in this deliverable. Do not silently delete an assumption — if refuted, leave with strikethrough and add a new numbered entry pointing at the replacement. `[ASSUMED]` tags remain even after coach-session confirmation so the audit trail for Friday peer review is preserved.

### 2.4 Full entries

**H1 — HR Ops adoption willingness** _(HUMAN — Medium)_
- **Assumption:** The HR Ops team are open to adopting an AI agent for onboarding coordination.
- **Hypothesis:** If they are open, they will collaborate on defining the agent's capabilities and giving feedback during development, because they have expressed frustration with current automation efforts.
- **How I'd test it:** Coach-session role-play with the HR Ops lead; separately, ask to see previous automation attempts and the reasons they stalled.
- **Confidence:** Medium — frustration with current automation is a receptivity signal but not proof of willingness to delegate judgment-adjacent work to an agent.

**H2 — Judgment-call patternability** _(HUMAN — Low)_
- **Assumption:** The 15% of onboarding tasks requiring judgment are consistent enough for an agent to learn to handle effectively.
- **Hypothesis:** If the judgment calls follow identifiable patterns, then the agent could apply codified rules, because HR processes generally have written guidelines.
- **How I'd test it:** Ask HR Ops for a sample of 20 recent judgment calls with the outcome; categorise them and check whether >80% fall into a small rule set.
- **Confidence:** Low — the scenario quote "the edge cases never look the same twice" is explicit counter-evidence. This deliverable does **not** claim judgment calls as delegable.

**H7 — Late I-9 = regulatory hold** _(HUMAN — Medium)_
- **Assumption:** "Late I-9 triggers a hold" means a compliance-driven stop on onboarding progression with legal implications.
- **Hypothesis:** If the phrase refers to IRCA Section 2 non-compliance, then the agent must escalate rather than decide the hold itself.
- **How I'd test it:** Ask HR Ops for the written policy text; cross-check against IRCA 8 U.S.C. § 1324a.
- **Confidence:** Medium — reasonable inference, but "hold" could be an internal process term with different semantics.

**A1 — Baseline "fell-through-the-cracks" rate** _(AGENT — Low)_
- **Assumption:** HR Ops can retrieve the count of onboardings with ≥ 1 incomplete task at day 14.
- **Hypothesis:** If HR Ops tracks open tasks per onboarding, the baseline is retrievable from Workday or a shared tracker.
- **How I'd test it:** "Can you run a report showing, for the last 100 onboardings, how many had any open required task at day 14?"
- **Confidence:** Low — the HR Ops lead's quote "something falls through the cracks" suggests awareness but not necessarily measurement.

**A2 — Current time-per-onboarding** _(AGENT — Low)_
- **Assumption:** HR Ops can produce minutes-per-onboarding from time-tracking or retrospective estimate.
- **Hypothesis:** If the team knows their workload at the onboarding level, a per-hire figure can be produced.
- **How I'd test it:** "What's the current time your team spends per onboarding, end-to-end?"
- **Confidence:** Low — may be estimated, not measured.

**A3 — 15% refers to tasks, not onboardings** _(AGENT — Medium)_
- **Assumption:** The scenario's "roughly 15% require judgment calls" applies to the ~40 tasks per onboarding — i.e. ≈ 6 tasks per hire — not to 15% of onboardings being entirely judgment-driven.
- **Hypothesis:** If 15% of ~40 tasks are judgment calls, then the remaining ~34 tasks are candidates for routine delegation.
- **How I'd test it:** Ask the HR Ops lead to confirm the denominator.
- **Confidence:** Medium — the scenario wording "15% require judgment calls" most naturally reads as 15% of tasks, consistent with the examples given (classification, buddy norms, late I-9).

**A4 — I-9 deadline semantics** _(AGENT — Medium)_
- **Assumption:** "Late I-9" means Section 2 not completed within 3 business days of the employee's first day (IRCA 8 U.S.C. § 1324a).
- **Hypothesis:** If this is the semantics, then the hold decision is HUMAN-LED and the agent's role is detect-and-escalate.
- **How I'd test it:** Confirm against client's own written compliance policy.
- **Confidence:** Medium — the regulation is settled, but the client's specific "hold" procedure may layer on internal rules.

---

## 3. The Problem Being Solved

A regional professional-services firm with 1,200 employees and **220+ hires per year** runs new-hire onboarding through a **3-person HR Ops team** [CITED]. Each onboarding spans **~40 tasks over ~2 weeks**, drawing from **6 different systems** — Workday (core HR), ServiceNow (IT requests), a separate LMS (compliance training), email, and two further systems [CITED; the two unnamed systems are identified by HUMAN assumption H5 as benefits and payroll/time, confirmed in coach session]. At 220 hires × 40 tasks, the team handles **≈ 8,800 task instances per year** across these onboardings (derivation: 220 × 40 [CITED numbers in scenario]).

Of those tasks, **≈ 15% require judgment calls** — the scenario names three: classifying a contractor versus a full employee, vetting whether a buddy assignment crosses seniority norms, and deciding whether a late I-9 triggers a hold [CITED]. Under the reading formalised in A3, this is ≈ 6 judgment-bearing tasks per onboarding and ≈ 1,320 judgment-bearing task instances per year; the remaining ≈ 7,480 task instances per year are candidates for routine delegation.

The HR Ops lead says, verbatim: *"Most of this is paperwork my team should not be touching, but every time we try to automate, something falls through the cracks because the edge cases never look the same twice."*

The firm has **no AI infrastructure today** [CITED]. Prior automation attempts have failed in a specific, diagnosable way: not on the volume or the routine, but on the edge cases that previous systems could not absorb.

---

## 4. Why Agentic, Why Now

**Volume.** The work is genuinely high-volume-low-judgment on the routine tail: ≈ 7,480 task instances per year (derived from 220 × 40 × 85% [CITED × A3]) sit across predictable categories — IT provisioning, benefits enrolment, compliance training assignment, welcome materials, 30-day checkpoint scheduling, manager handoff. Orchestrating this volume across 6 systems is the load the 3-person team visibly strains under.

**Repeatability.** The routine tail is not just frequent, it is structured: each task has a named source system, a deterministic trigger (hire event, start date, classification already set by a human), and a verifiable completion signal (provisioned account, enrolment row, training assignment acknowledged). This is the exact shape an agent is good at — rule-governed orchestration across heterogeneous systems with idempotent writes — and where traditional RPA historically stumbled because the orchestration had branches it could not represent cleanly.

**Constraint.** Previous automation failed on the 15% that "never look the same twice" [CITED stakeholder quote]. An agent does not solve that by learning the edge cases; it solves it by recognising *that* a case is non-routine and routing to a named human with the relevant context pre-assembled, rather than silently forcing the case down a routine path. That is a different architectural commitment from prior attempts, and it is the reason the agentic framing is fit-for-purpose here — not a generic AI upsell.

---

## 5. Success Metrics

| # | Metric | Current State | Target State | Measurement Method | Source |
|---|---|---|---|---|---|
| M1 | Routine-task delegation rate — % of non-judgment task instances executed end-to-end with no human action | `[UNKNOWN — baseline needed]` (per A1, the team knows "things fall through" but the delegation rate is not measured today) | ≥ 85% in month 3 post-launch; ≥ 95% steady-state | `tasks_completed_by_agent_without_human_touch / tasks_classified_as_routine`, computed nightly from the agent's task log filtered by `classification = ROUTINE` | [ASSUMED] — A3 (the 15%-of-tasks reading). Targets [ASSUMED] — A1. |
| M2 | Human effort per onboarding (HR Ops minutes) | `[UNKNOWN — baseline needed]` (per A2) | ≥ 60% reduction vs. baseline by month 6, with absolute target pinned once baseline is returned | Time-tracking entries attributed to `program = onboarding` / count of onboardings completed in period | [ASSUMED] — A2. Target [ASSUMED] — A1. |
| M3 | "Fell-through-the-cracks" rate — % of onboardings with ≥ 1 incomplete required task at day 14 | `[UNKNOWN — baseline needed]` (per A1; the stakeholder quote is qualitative evidence but not a number) | ≤ 2% in month 3; ≤ 0.5% steady-state | `onboardings_with_any_open_required_task_at_day_14 / total_onboardings_started` from the Onboarding state store | [CITED] stakeholder pain language; targets [ASSUMED] — A1. |
| M4 | Boundary respect — % of judgment-classified tasks that reach a logged `HumanDecision` record before the task can transition to `COMPLETE` | Not applicable pre-agent (no agent exists today) | **100%** — Non-negotiable | `tasks_completed_where classification = JUDGMENT AND no_human_decision_log_exists` must equal **0** in the audit table for every reporting period | **(Non-negotiable)** — [CITED] scenario (judgment calls explicitly require human involvement; "late I-9 triggers a hold" per H7 / A4) + IRCA 8 U.S.C. § 1324a for the I-9 branch. |

**Rows resting on assumed baselines that must be converted to `[TESTED]` in the next coach session before this deliverable is treated as business-aligned:** M1 (baseline + target), M2 (baseline + target), M3 (baseline); M4 is non-negotiable and [CITED], not an assumption, but its exact wording depends on A4 being confirmed.

---

## 6. Out of scope for this deliverable

This file produces Deliverable 1 only — problem framing and success metrics. It deliberately does not cover:

- **Delegation analysis** — which tasks become fully agentic vs. agent-led vs. human-led, with rationale. See [`../../Prompts/delegation-analysis.md`](../../Prompts/delegation-analysis.md) and the produced file in this folder.
- **Capability specification** — inputs, outputs, business rules, state machines, escalation codes, integration contracts. See [`../../Prompts/capability-specification.md`](../../Prompts/capability-specification.md).
- **Validation design** — happy path, edge cases, failure modes, boundary tests. See [`../../Prompts/validation-design.md`](../../Prompts/validation-design.md).
- **The full assumptions / unknowns register.** Consolidated in [`../../Prompts/assumptions-and-unknowns.md`](../../Prompts/assumptions-and-unknowns.md) — the entries above feed that register, they do not replace it.

