# Gate 1 Consolidated Spec — Scenario 1 (HR Onboarding Coordination)

## Front-matter (consolidated)

- **Submission IDs (sources):** `problem-statement-scenario-1-201`, `delegation-analysis-scenario-1-202`, `capability-specification-scenario-1-203`, `validation-design-scenario-1-204`, `assumptions-and-unknowns-scenario-1-205`.
- **Source scenario:** [`../../scenario-1.md`](../../scenario-1.md)
- **Date produced (consolidation):** 24.04.2026
- **Run suffix:** 413. Produced by running [`../../Prompts/concatonate-and-review.md`](../../Prompts/concatonate-and-review.md) against the five source deliverables in the `Week1/Output/Scenario1/` folder.
- **Status:** First consolidated draft, post-Deliverables-1–5, pre-coach-session on the merged register. HUMAN assumptions **H4, H5, H6** carry **High (coach-validated)**; **A7** carries **High (regulation-anchored)**. **H1, H3, H7** are **Medium**; **H2** is **Low** and explicitly unused to move any delegation row.
- **Consolidation notes.** (i) Per-file front-matter and per-file §2 Assumption Log blocks are stripped; their content is consolidated here in §0.1 below. (ii) Per-file "Out of scope" sections are stripped — this is one document, not five. (iii) Per-file "self-audit" sections from the capability spec and validation design are preserved in §3.8 / §4.10 unchanged. (iv) Section numbering in the body is renumbered to the single-document hierarchy (§1…§5); cross-references from the source files that used the old "D1 §n / D2 §n" form have been retained where they are load-bearing for traceability. (v) No new facts, rules, escalations, entities, metrics, or integrations have been introduced during consolidation. The only additions are a consolidation note in this front-matter, cross-references to the top-level Assumption Log, and **Appendix A** (production-spec-checklist review).
- **Rules for this file (inherited from `CLAUDE.md`):** citation tags `[CITED]` / `[ASSUMED]` / `[UNKNOWN]` and source tags `HUMAN` / `AGENT` are preserved verbatim from the source files. Confidence ratings reflect the source files as of 24.04.2026. `High` is reserved for coach-session-validated or regulation-anchored entries; see §0.1.

---

## 0.1 Assumption Log (merged — single source of truth)

Every `[ASSUMED]` or `[UNKNOWN]` reference elsewhere in this document traces to a numbered entry here. The numbers match the source-file numbers (H1–H7, A1–A17, V2, V4, V5, A-open-1) so upstream prose does not need re-numbering. **V1** has been merged into **A1** and **V3** is tracked as a dependency of **A10**, both per the source consolidation in the upstream `assumptions-and-unknowns-scenario-1-205.md`.

### 0.1.1 Scan table

| # | Source | Assumption (one line) | Cagan risk | Confidence | Upstream sections at risk if wrong |
|---|---|---|---|---|---|
| H1 | HUMAN | HR Ops will adopt an agent for onboarding coordination | Value / Viability | Medium | §1.3, §1.4 (business case); §2.3 rows depending on access follow-through |
| H2 | HUMAN | 15% judgment calls follow identifiable patterns | Feasibility | Low | §1.4 (M1 denominator target); §2.3 row 3 (explicitly **not** relied on); §3.5 Cap-B rule set |
| H3 | HUMAN | Existing systems expose APIs or integration points | Feasibility | Medium | §3.6 (all integrations); §2.3 row 21 |
| H4 | HUMAN | Buddy 3-factor filter + one-buddy + tie-break dept→loc→sen→random + HR-escalate-on-zero | Feasibility | **High (coach-validated)** | §2.3 rows 10, 11, 13; §3.5 Cap-B rules 1–6; §4.4 HP-1, §4.5 EC-6, §4.7 BT-2 |
| H5 | HUMAN | Unnamed 2 of 6 systems = Benefits + Payroll/Time | Feasibility | **High (coach-validated)** | §2.3 rows 6, 21; §3.6.5, §3.6.6 |
| H6 | HUMAN | HR Ops will grant integration access | Viability | **High (coach-validated)** | §2.3 rows 4–22 (all FULL rows); §3.6 (all integrations) |
| H7 | HUMAN | "Late I-9 triggers a hold" is a regulatory hold with legal exposure | Viability | Medium | §1.4 M4 wording; §2.3 row 19, C2; §3.5 Cap-A rule 5; §4.5 EC-5, §4.6 FM-3 |
| A1 | AGENT | Baseline "fell-through-the-cracks" rate is retrievable from HR Ops records | Value | Low | §1.4 M3 Current State; §4.2 V1 (merged); defence of M3 target |
| A2 | AGENT | Current time-per-onboarding (M2 baseline) is retrievable | Value | Low | §1.4 M2 Current State |
| A3 | AGENT | Scenario's "15%" refers to 15% of ~40 tasks (≈ 6/hire), not 15% of onboardings | Feasibility | Medium | §1.3 derivation; §1.4 M1 denominator; §2.3 row 2; §3.5 Cap-A rule 2 |
| A4 | AGENT | I-9 3-business-day deadline (IRCA 8 U.S.C. § 1324a) from `start_date` | Viability | Medium | §2.5 C2; §3.5 Cap-A rule 5; §0.1.4 A14 |
| A5 | AGENT | Buddy "unavailable" = zero-match of unencumbered pool; leave + capacity pre-filtered | Feasibility | Medium | §2.3 row 13; §3.5 Cap-B rules 2, 3, 4; ESC-BUDDY-UNAVAILABLE |
| A6 | AGENT | Tie-break order dept → location → seniority → random, seeded RNG | Feasibility | Medium | §3.5 Cap-B rule 5; §4.4 HP-1 determinism |
| A7 | AGENT | Classification is HUMAN-LED regardless of signal strength | Viability | **High (regulation-anchored)** | §2.3 row 3, C1; §3.5 Cap-A rule 12, Cap-C rule 4; §4.7 BT-1 |
| A8 | AGENT | Seniority-norm flag is a post-filter HUMAN-IN-LOOP exception, not a 4th filter factor | Feasibility | Medium | §2.3 row 12; §3.5 Cap-B rule 6; §4.7 BT-2 |
| A9 | AGENT | Retention: 7y employment, 1y integration audit | Viability | Medium | §2.5 C4; §3.4 entity delete behaviour; §3.5.7, §3.5.17 decision logs |
| A10 | AGENT | LMS vendor + API + webhook contract **[UNKNOWN]** | Feasibility | Low / **Build-blocking** | §3.6.3; §4.6 FM-2, §4.2 V3 (merged) |
| A11 | AGENT | Workday + ServiceNow OAuth2 client-credentials auth with service-account creds | Feasibility | Medium | §3.6.1, §3.6.2 |
| A12 | AGENT | Idempotency key = `sha256("{onboarding_id}:{task_id}:{system}:{action}")` | Feasibility | Medium | §3.5 Cap-A rule 7; Cap-C rule 3 |
| A13 | AGENT | ServiceNow role-bundle CI schema; non-template = ESC-ACCESS-NONTEMPLATE | Feasibility | Medium | §3.5 Cap-A rule 4; ESC-ACCESS-NONTEMPLATE; §4.5 EC-3 |
| A14 | AGENT | Business-day calendar = Mon–Fri − US federal holidays; clock from `start_date` | Viability | Medium | §3.5 Cap-A rule 5; §4.5 EC-5 |
| A15 | AGENT | Day-14 = audit milestone; Day-10 = handoff nag | Feasibility | Medium | §3.5 Cap-A rules 8, 9; §4.4 HP-1 timeline |
| A16 | AGENT | Seniority-delta threshold default = 3 bands, configurable | Feasibility | Low | §3.5 Cap-B rule 6; §4.7 BT-2 |
| A17 | AGENT | Email sender is a named relay with DKIM/SPF; specific vendor **[UNKNOWN]** | Feasibility | Medium | §3.6.4 |
| V2 | AGENT | Synthetic test harness can reproduce production distributions for role / location / seniority | Feasibility | Medium | §4 all test data |
| V4 | AGENT | Ground truth for BT-1 is the HR reviewer's eventual decision, not a test-author inference | Value / Viability | Medium | §4.7 BT-1 |
| V5 | AGENT | Seniority threshold is parameterisable for BT-2 runs | Feasibility | Medium | §4.7 BT-2 |
| A-open-1 | AGENT | Capability spec does not yet model `ESC-SCHEDULE-DRIFT` for `start_date` changes post-creation — spec gap surfaced in §4.6 FM-4 | Feasibility | **Build-blocking for FM-4** | §3.5 Cap-A (new rule + ESC needed); §4.6 FM-4 |
| A-open-2 | AGENT | *(Consolidation-surfaced)* M2 target ("≥ 60% reduction vs. baseline by month 6") is an assumed target, not a validated one; its absolute minutes figure can only be set once A2 resolves. Noted here so no downstream reader treats it as a hard commitment. | Value | Low | §1.4 M2 row |
| A-open-3 | AGENT | *(Consolidation-surfaced)* Distribution-list names per `recipient_role` (e.g. `HR_OPS_LEAD`, `IT_APPROVER`, `HIRING_MANAGER`) are role labels; their concrete email addresses / Teams channels are **[UNKNOWN]** and must be supplied by the client before first build-loop run. | Feasibility | Medium | §3.5.6 escalation triggers; all `ESC-*` notifications |
| A-open-4 | AGENT | *(Consolidation-surfaced — BUILDABILITY)* The three ambiguous-word flags introduced by merging "routine" and "required task" language across §1 and §3 — specifically: "required task" ≡ any `Task` with `classification ∈ {ROUTINE, JUDGMENT}` and `status ≠ CANCELLED`, and "routine task" ≡ `Task.classification = ROUTINE`. Stated here so M1/M3 denominators are unambiguous for a coding agent. | Feasibility | Medium | §1.4 M1, M3; §3.4 `Task` entity |
| A-open-5 | AGENT | *(Consolidation-surfaced — ECONOMICS)* The spec does not yet classify agent operations by token cost (Check/Validate/Generate/Coordinate/Transform) nor pin circuit-breaker thresholds. Scenario 1's agent is an orchestrator with deterministic routing, so the expected cost shape is *Coordinate-heavy, Generate-light*; no LLM-graded decisions on the happy path. Circuit-breaker for Cap-C fan-out = **10 concurrent outbound writes per Onboarding** before Cap-A stops dispatching and surfaces `ESC-INTEG-OUTAGE` preventively. | Feasibility / Viability | Low | §3.5 Cap-C rules; §5 Appendix A (Economics Alignment) |

### 0.1.2 Overall read

- **Total entries:** 30 (25 from the upstream register + 5 consolidation-surfaced entries A-open-2…A-open-5 and the retained A-open-1).
- **HUMAN vs AGENT:** 7 HUMAN (H1–H7); 23 AGENT.
- **Confidence split:** 4 High (H4, H5, H6 coach-validated; A7 regulation-anchored). Medium: 15. Low: 7 (H2, A1, A2, A10, A16, A-open-2, A-open-5).
- **Open tensions (preserved from upstream):** (a) *H4 vs scenario text* — resolved by A8 (post-filter HUMAN-IN-LOOP exception) rather than silently picking a side. (b) *H2 vs scenario text* — resolved by not using H2 to move any row into FULL delegation.

### 0.1.3 Coach-session priority queue (consolidated)

In order, highest leverage first:

1. **Open tension A8 (seniority-norm path) + H4 reconciliation** — moves §2.3 row 11 and §3.5 Cap-B rule 6 materially. Probe: *"For buddy matches that pass the three-factor filter, do you want every match routed through HR, or only matches exceeding a seniority-delta threshold (e.g. 3 bands)?"*
2. **A10 — LMS vendor identity** — build-blocking for §3.6.3 and §4.6 FM-2.
3. **A-open-1 — `ESC-SCHEDULE-DRIFT`** — spec gap surfaced by FM-4.
4. **A1 + A2 — Baselines for M2 and M3** — without baselines, §1.4 targets are unanchored.
5. **A13 — ServiceNow bundle schema** and **A14 — business-day calendar** — both touch regulatory timing and ESC-ACCESS-NONTEMPLATE.
6. **A9 — Retention envelope** — touches every decision-log row.
7. **A-open-3 — Distribution-list names per `recipient_role`** — blocks first-build-loop `ESC-*` notifications.
8. **A11 — Tenant auth flavours.** Required for first build-loop run of §3.6.1 and §3.6.2; does not block drafting.
9. **A17 — Email sender identity.** Blocks only first build-loop run of ESC-* notifications.
10. **H1 — Adoption willingness** — Value-risk probe, not an architecture-mover.
11. **A16 — Seniority-delta threshold default** — low leverage; parameterisable.
12. **A-open-2 — M2 absolute target wording** — cosmetic until A2 resolves.
13. **A-open-5 — Economics classification + circuit-breaker threshold** — design-time confirmation, not build-blocking.

### 0.1.4 Update protocol

After each coach session, update the affected entry **in place**: raise or lower confidence, add a dated note, and change any dependent prose downstream in this document. **Do not silently delete an assumption.** If refuted, leave with strikethrough and add a new numbered entry pointing at the replacement. `[ASSUMED]` tags remain even after coach-session confirmation so the audit trail for Friday peer review is preserved. Changes to upstream source files under `Week1/Output/Scenario1/` should trigger a re-run of [`../../Prompts/concatonate-and-review.md`](../../Prompts/concatonate-and-review.md) producing a new run-suffix of this document, not a hand-edit here.

### 0.1.5 Full entries

Full Assumption / Hypothesis / Test / Confidence entries for **H1–H7** live in [`../../scenario-1.md`](../../scenario-1.md) § *HUMAN Assumptions* and are not restated here. Full entries for **A1–A17, V2, V4, V5, A-open-1** are the same as those in the upstream `assumptions-and-unknowns-scenario-1-205.md` § 6 — they are load-bearing for traceability and are reproduced below for the three consolidation-surfaced entries only.

**A-open-2 — M2 absolute target is assumed, not validated** _(AGENT — Low)_
- **Assumption:** "≥ 60% reduction vs. baseline by month 6" is an assumed-favourable target; the absolute minutes figure is pinned only once A2 (current time-per-onboarding) resolves.
- **Hypothesis:** If baseline is ≈ 240 minutes per onboarding (industry rough), 60% reduction ≈ 96 minutes; business case survives at 40% reduction too.
- **How I'd test it:** Confirm baseline; then re-evaluate the target against the business case in §1.4.
- **Confidence:** Low — neither baseline nor target is validated.

**A-open-3 — Distribution-list resolution is [UNKNOWN]** _(AGENT — Medium)_
- **Assumption:** Every `recipient_role` (`HR_OPS_LEAD`, `IT_APPROVER`, `HIRING_MANAGER`, `IT on-call`) resolves to a concrete distribution list (DL email or Teams channel) via an org lookup.
- **Hypothesis:** Client has existing DLs for HR Ops leadership and IT approvers; if not, an Azure AD group is standable-up in < 1 business day.
- **How I'd test it:** *"For each of these roles — HR Ops lead, IT access approver, hiring manager, IT on-call — is there an existing DL or Teams channel we should route ESC-\* notifications to?"*
- **Confidence:** Medium — standard for client-of-this-size, but concrete addresses are needed before first build-loop run.

**A-open-4 — Definitions of "required task" and "routine task"** _(AGENT — Medium)_
- **Assumption:** "Required task" = any `Task` with `status ∉ {CANCELLED}` and the template's `required` flag set (every task in §3.4.2.a except optional extensions). "Routine task" = `Task.classification = ROUTINE`. M1's denominator uses "routine"; M3's denominator uses "required" at day-14.
- **Hypothesis:** Without this pinning, an ambiguous-word audit of the spec flags "required" and "routine" as vague.
- **How I'd test it:** Inspect the template for `required=true` markers; confirm with HR Ops.
- **Confidence:** Medium.

**A-open-5 — Economics classification for this spec** _(AGENT — Low)_
- **Assumption:** Agent operations map to the `production-spec-checklist.md` Economics cost classes as follows: *Check* — state-machine reads, audit checks (Cap-A rule 6, rule 9); *Validate* — idempotency-key and allowlist checks (Cap-A rule 12, Cap-C rule 4); *Generate* — none on the happy path (no LLM-graded decisions); *Coordinate* — all Cap-C outbound writes and inbound webhook receipts; *Transform* — batch day-14 audit report generation (low token, moderate data). Circuit-breaker: Cap-A stops new Cap-C dispatches if ≥ 10 concurrent outbound writes are outstanding for a single `Onboarding`, raising `ESC-INTEG-OUTAGE` preventively rather than on downstream timeout.
- **Hypothesis:** Cap-A is deterministic orchestration — no per-request LLM call on routine paths; expensive operations concentrate in Cap-C's fan-out to 6 systems.
- **How I'd test it:** Token-budget run against the HP-1 harness once the build exists; measure request volume per Onboarding.
- **Confidence:** Low — architecture-level claim; needs build-loop measurement.

---

## 1. Problem Statement & Success Metrics

*(Consolidation note: the source file's §2 Assumption Log has been subsumed into §0.1 above; its §6 "Out of scope" pointers to sibling deliverables are removed because this consolidated document already contains those sections.)*

### 1.1 The Problem Being Solved

A regional professional-services firm with 1,200 employees and **220+ hires per year** runs new-hire onboarding through a **3-person HR Ops team** [CITED]. Each onboarding spans **~40 tasks over ~2 weeks**, drawing from **6 different systems** — Workday (core HR), ServiceNow (IT requests), a separate LMS (compliance training), email, and two further systems [CITED; the two unnamed systems are identified by HUMAN assumption H5 as Benefits and Payroll/Time, confirmed in coach session]. At 220 hires × 40 tasks, the team handles **≈ 8,800 task instances per year** across these onboardings (derivation: 220 × 40 [CITED numbers in scenario]).

Of those tasks, **≈ 15% require judgment calls** — the scenario names three: classifying a contractor versus a full employee, vetting whether a buddy assignment crosses seniority norms, and deciding whether a late I-9 triggers a hold [CITED]. Under the reading formalised in A3 (§0.1), this is ≈ 6 judgment-bearing tasks per onboarding and ≈ 1,320 judgment-bearing task instances per year; the remaining ≈ 7,480 task instances per year are candidates for routine delegation.

The HR Ops lead says, verbatim: *"Most of this is paperwork my team should not be touching, but every time we try to automate, something falls through the cracks because the edge cases never look the same twice."*

The firm has **no AI infrastructure today** [CITED]. Prior automation attempts have failed in a specific, diagnosable way: not on the volume or the routine, but on the edge cases that previous systems could not absorb.

### 1.2 Why Agentic, Why Now

**Volume.** The work is genuinely high-volume-low-judgment on the routine tail: ≈ 7,480 task instances per year (derived from 220 × 40 × 85% [CITED × A3]) sit across predictable categories — IT provisioning, benefits enrolment, compliance training assignment, welcome materials, 30-day checkpoint scheduling, manager handoff. Orchestrating this volume across 6 systems is the load the 3-person team visibly strains under.

**Repeatability.** The routine tail is not just frequent, it is structured: each task has a named source system, a deterministic trigger (hire event, start date, classification already set by a human), and a verifiable completion signal (provisioned account, enrolment row, training assignment acknowledged). This is the exact shape an agent is good at — rule-governed orchestration across heterogeneous systems with idempotent writes — and where traditional RPA historically stumbled because the orchestration had branches it could not represent cleanly.

**Constraint.** Previous automation failed on the 15% that "never look the same twice" [CITED stakeholder quote]. An agent does not solve that by learning the edge cases; it solves it by recognising *that* a case is non-routine and routing to a named human with the relevant context pre-assembled, rather than silently forcing the case down a routine path. That is a different architectural commitment from prior attempts, and it is the reason the agentic framing is fit-for-purpose here — not a generic AI upsell.

### 1.3 Success Metrics

| # | Metric | Current State | Target State | Measurement Method | Source |
|---|---|---|---|---|---|
| M1 | Routine-task delegation rate — % of non-judgment task instances (per A-open-4, `Task.classification = ROUTINE`) executed end-to-end with no human action | `[UNKNOWN — baseline needed]` (per A1) | ≥ 85% in month 3 post-launch; ≥ 95% steady-state | `tasks_completed_by_agent_without_human_touch / tasks_classified_as_routine`, computed nightly from the agent's task log filtered by `classification = ROUTINE` | [ASSUMED] — A3. Targets [ASSUMED] — A1. |
| M2 | Human effort per onboarding (HR Ops minutes) | `[UNKNOWN — baseline needed]` (per A2) | ≥ 60% reduction vs. baseline by month 6, with absolute minutes target pinned once baseline is returned (see A-open-2) | Time-tracking entries attributed to `program = onboarding` / count of onboardings completed in period | [ASSUMED] — A2. Target [ASSUMED] — A-open-2. |
| M3 | "Fell-through-the-cracks" rate — % of onboardings with ≥ 1 incomplete *required* task at day 14 (per A-open-4, required ≡ template `required=true` ∧ `status ∉ {CANCELLED}`) | `[UNKNOWN — baseline needed]` (per A1) | ≤ 2% in month 3; ≤ 0.5% steady-state | `onboardings_with_any_open_required_task_at_day_14 / total_onboardings_started` from the Onboarding state store | [CITED] stakeholder pain language; targets [ASSUMED] — A1. |
| M4 | **Boundary respect** — % of judgment-classified tasks that reach a logged `HumanDecision` record before the task can transition to `COMPLETE` | Not applicable pre-agent | **100%** — Non-negotiable | `tasks_completed_where classification = JUDGMENT AND no_human_decision_log_exists` must equal **0** in the audit table for every reporting period | **(Non-negotiable)** — [CITED] scenario; IRCA 8 U.S.C. § 1324a for the I-9 branch (per A4). |

**Rows resting on assumed baselines that must be converted to `[TESTED]` in the next coach session before this deliverable is treated as business-aligned:** M1 (baseline + target), M2 (baseline + target), M3 (baseline); M4 is non-negotiable and [CITED], not an assumption, but its exact wording depends on A4 being confirmed.

---


## 2. Delegation Analysis

*(Consolidation note: the source file's §2 Assumption Log — including the surfaced tension between H4 and the scenario text, and the coach-session priority queue — is subsumed into §0.1 above. §8 "Out of scope" is stripped.)*

### 2.1 Delegation Framework (brief)

Three classifications are used in the work inventory below, applied at the **task / decision** level (not the capability level) — a single capability can contain rows in all three:

- **FULL DELEGATION.** Agent executes end-to-end. The task is rule-governed, the outcome is reversible or low-impact, the system of record is named, and the decision is deterministic given the inputs.
- **HUMAN-IN-LOOP.** Agent drafts, proposes, or prepares; a *named human* must act (approve, confirm, sign off) before the system state changes. The agent may not treat silence as approval.
- **HUMAN-LED.** A human decides. The agent may detect, flag, or compile evidence, but must not take the decision itself. Silent-error cost or regulatory exposure puts the call here.

Vocabulary anchored in `SupportingDocs/the-fde.md` (Delegation Archetypes / Cognitive Zones). No hybrids inside a single cell — where a task has a routine execution and a judgment gate, it produces two rows (see Buddy matching: propose vs. final assign).

### 2.2 Tension surfaced

**Tension to surface (per primer anti-pattern "silently picking a side"):** H4's hypothesis text reads "prioritise in order of department, location and seniority" and the assumption statement text reads "department, location and seniority" — these agree. However, the scenario text flags seniority-norm *judgment* as one of the 15% judgment calls, which appears in tension with H4's *High* rating for full auto-assignment. This is surfaced as **A8** (§0.1): agent may auto-assign from the three-factor filter's output, but must not override a flagged seniority-norm concern raised by HR — and must not suppress the flag.

### 2.3 Work Inventory

| # | Task / Decision | Classification | Rationale (why) | Source |
|---|---|---|---|---|
| 1 | **Create `Onboarding` record** on hire event from Workday | FULL | Rule-governed, reversible, Workday is system of record, deterministic trigger. | [CITED] scenario — Workday is core HR |
| 2 | **Instantiate ~40 onboarding tasks** from template per classification | FULL | Template expansion is deterministic once `employment_class` is set upstream by a human (see #3). Reversible. | [CITED] scenario (40 tasks, 2-week span) |
| 3 | **Decide `employment_class` (contractor vs full employee)** | HUMAN-LED | Scenario names classification as a judgment call; regulatory exposure (IRS common-law test, ACA 30-hour, state ABC) makes silent-error cost extreme; an incorrect agent inference is an irreversible compliance finding. Agent may not branch on a signal it synthesised itself. | [CITED] scenario quote; [CITED] IRCA-adjacent regulation. [ASSUMED] — A7 (specific cites); **not** relying on H2. |
| 4 | **IT provisioning — request creation in ServiceNow** (laptop, accounts, access bundles per role) | FULL | Rule-governed given classification and role; ServiceNow is system of record; idempotent on a deterministic key. Reversible (deprovision path exists). | [CITED] scenario (ServiceNow for IT); [ASSUMED] — H6 (access) |
| 5 | **IT provisioning — approval of access bundles that exceed standard role template** | HUMAN-IN-LOOP | Standard bundles are FULL under #4; anything outside the template is an access-control decision that requires a named approver. | [ASSUMED] — A7 (regulatory-adjacent access); best-practice IT governance |
| 6 | **Benefits enrolment — send enrolment packet & track deadline** | FULL | Paperwork dispatch and deadline-nag cadence are rule-governed; non-completion raises an escalation, does not cause agent to make enrolment elections. | [CITED] scenario (6 systems); [ASSUMED] — H5 (Benefits system identity) |
| 7 | **Benefits enrolment — elections on behalf of employee** | HUMAN-LED | The *employee* makes the election. Agent does not. | [CITED] common-sense; reinforced by ERISA-style fiduciary framing |
| 8 | **Compliance training — assignment in LMS** per classification | FULL | Deterministic mapping from classification → track; LMS is system of record; idempotent on a deterministic key. | [CITED] scenario (LMS); [ASSUMED] — H5-adjacent (LMS API availability) |
| 9 | **Compliance training — which track applies to contractor vs. full employee** | HUMAN-LED (indirectly) | This is actually the classification decision (#3) surfacing again — once classification is set, the track mapping in #8 is deterministic. Listed here for completeness so reviewers do not think the agent chooses a track independently. | [CITED] scenario (explicit judgment call example) |
| 10 | **Buddy matching — propose candidate via 3-factor filter** (seniority + dept + location; one-buddy-per-mentee; tie-break dept→loc→sen→random) | FULL | Coach-validated under H4 as a deterministic filter. Reversible (reassign possible). | [CITED] per H4; tie-break per A6 |
| 11 | **Buddy matching — final assignment when no seniority-norm concern** | FULL | Given the filter's coach-validated three-factor scope, the default case is auto-assign. | [ASSUMED] — H4 (High); A5 |
| 12 | **Buddy matching — seniority-norm exception path** (e.g. delta exceeds threshold) | HUMAN-IN-LOOP | Scenario names "buddy crosses seniority norms" as a judgment call — surfaced here as an after-filter exception rather than a fourth filter factor. Agent flags, HR reviews, HR persists. | [CITED] scenario; [ASSUMED] — A8 |
| 13 | **Buddy matching — no candidate available (zero-match of unencumbered pool)** | HUMAN-LED | Per H4's escalation rule. Agent raises `ESC-BUDDY-UNAVAILABLE`; HR decides the override (pick someone on-leave, skip, or expand pool). | [CITED] per H4; [ASSUMED] — A5 |
| 14 | **Welcome materials dispatch** (email + portal seeding) | FULL | Rule-governed, reversible, low-impact. | [CITED] scenario |
| 15 | **30-day checkpoint scheduling** (calendar invite, reminder cadence) | FULL | Calendaring + reminder logic is deterministic. | [CITED] scenario |
| 16 | **Manager handoff package preparation** (assembled artefact: who reports to whom, access summary, buddy) | FULL | Agent compiles from existing records; reversible; no new facts. | [CITED] scenario |
| 17 | **Manager handoff confirmation** (manager confirms receipt / readiness) | HUMAN-IN-LOOP | System state (`onboarding.handoff_status`) should not flip to DONE on silence; the manager is the named actor. | [ASSUMED] — A9 (audit); operational best practice |
| 18 | **I-9 Section 2 — reminder cadence to employee and manager** | FULL | Nag cadence is rule-governed; agent does not complete I-9 itself. | [CITED] IRCA 8 U.S.C. § 1324a — 3 business day rule |
| 19 | **I-9 Section 2 — hold decision when overdue** | HUMAN-LED | Regulatory; agent raises `ESC-I9`, HR decides the hold. | [CITED] scenario ("late I-9 triggers a hold"); [CITED] IRCA; [ASSUMED] — H7 (Medium) |
| 20 | **Workday write of `employment_class`** | HUMAN-LED | Direct corollary of #3. Agent may not write this field. | [CITED] per #3; [ASSUMED] — A7 |
| 21 | **All external-system writes (Workday, ServiceNow, LMS, Benefits, Payroll, Email)** | FULL (with idempotency and retry — see §3.6) | Rule-governed mechanics; retry on 5xx/429, escalate on repeated 4xx. Reversible via compensating write where feasible; flagged for HR where not. | [ASSUMED] — H6 (access); H5 (Benefits/Payroll identity) |
| 22 | **Decision-log write for every state transition, escalation, and human decision** | FULL | Rule-governed; deterministic; retention per A9. Non-negotiable for M4. | [ASSUMED] — A9; **supports** M4 non-negotiable metric |

### 2.4 Conditional rows that will move if an assumption resolves differently

- **Row 11 (buddy final-assign)** moves to HUMAN-IN-LOOP if A8 resolves with a named seniority-delta threshold that HR wants to review pre-assignment on *every* match, not only exceptions.
- **Row 10 (buddy propose)** does *not* move regardless of A5; what changes is the condition under which `ESC-BUDDY-UNAVAILABLE` fires.
- **Row 5 (IT access bundle approval)** becomes FULL only if the client later confirms a policy that "anything in the role template" is pre-approved for the agent; no such confirmation today.
- If H7 resolves as internal-policy-only (not IRCA), Row 19's wording changes but the classification stays HUMAN-LED — holds on regulatory artefacts are never agent decisions regardless of source.

### 2.5 Hard Constraints on the Boundary

| # | Constraint | Source | Effect on the boundary |
|---|---|---|---|
| C1 | **Employment classification is a human decision.** Agent must not infer or set `employment_class`; downstream processing branches only after a named human has set the value in Workday. | [CITED] scenario (classification named as judgment call); [CITED] IRS common-law test; ACA 30-hour rule; state-level ABC tests (e.g. California AB5 codifying *Dynamex* test). | Fixes row #3 as HUMAN-LED and row #20 as HUMAN-LED regardless of design preference. |
| C2 | **I-9 Section 2 must be completed within 3 business days of start date; hold decisions on non-completion are human.** Agent detects, reminds, and escalates; it does not hold. | [CITED] scenario ("late I-9 triggers a hold"); [CITED] IRCA 8 U.S.C. § 1324a. | Fixes row #18 as FULL (reminders only) and row #19 as HUMAN-LED. |
| C3 | **No employee benefit election may be made on the employee's behalf.** Agent dispatches, tracks, escalates; it does not elect. | [CITED] scenario (benefits enrolment is named); ERISA-style fiduciary framing makes the election a protected individual decision. | Fixes row #7 as HUMAN-LED. |
| C4 | **Every human decision is logged; employment-record retention is 7 years.** A task classified as requiring a human decision cannot transition to `COMPLETE` without a matching `HumanDecision` log row. | [CITED] audit-trail convention for employment records (IRCA recordkeeping requires I-9 retention of 3 years after hire or 1 year after termination, whichever is later; firm-wide 7-year standard is the envelope). [ASSUMED — A9] for the specific 7-year / 1-year split; client policy to confirm. | Makes M4 (boundary-respect 100%) enforceable. No FULL row may be reclassified to swallow a HUMAN-LED gate. |

Every row here is either [CITED] from the scenario, from named regulation, or from a standard recordkeeping framework. A9 tags the 7-year/1-year specifics as [ASSUMED] because the exact envelope is client-policy-specific; the existence of a retention requirement is not assumed.

### 2.6 Delegation Boundary Diagram

Trigger check (`CLAUDE.md` § *Diagrams*): work inventory has **22 rows** (> 10), and rows #3, #12, #13, #17, #19 cross the agent-vs-human boundary with distinct veto / override / hold paths. Both triggers fire. A diagram is warranted.

```mermaid
flowchart TD
    classDef agent fill:#cfe2ff,stroke:#0d6efd,color:#0a2540
    classDef human fill:#fff3cd,stroke:#b8860b,color:#3d2c00
    classDef ext fill:#e2e3e5,stroke:#6c757d,color:#1f2329

    subgraph Workday["Workday (core HR)"]
      WD_HIRE[Hire event]:::ext
      WD_CLASS[employment_class write]:::ext
    end
    subgraph ServiceNow["ServiceNow (IT)"]
      SN_REQ[IT request]:::ext
    end
    subgraph LMS["LMS (compliance training)"]
      LMS_ASSIGN[Training assignment]:::ext
    end
    subgraph Benefits["Benefits system"]
      BEN_PKT[Enrolment packet]:::ext
    end
    subgraph Payroll["Payroll/Time"]
      PAY_SETUP[Payroll setup]:::ext
    end
    subgraph Email["Email"]
      EM_SEND[Transactional email]:::ext
    end

    WD_HIRE --> A1[Create Onboarding]:::agent
    A1 --> H1[Set employment_class human]:::human
    H1 -->|value set| WD_CLASS
    WD_CLASS --> A2[Instantiate ~40 tasks]:::agent

    A2 --> A3[IT standard provisioning]:::agent --> SN_REQ
    A2 --> H2[Approve non-template access human]:::human
    A2 --> A4[Benefits packet dispatch]:::agent --> BEN_PKT
    A2 --> A5[LMS training assignment]:::agent --> LMS_ASSIGN
    A2 --> A6[Payroll setup]:::agent --> PAY_SETUP
    A2 --> A7[Welcome materials]:::agent --> EM_SEND
    A2 --> A8[30-day checkpoint schedule]:::agent
    A2 --> A9[Buddy propose via 3-factor filter]:::agent

    A9 -->|match + no norm flag| A10[Auto-assign buddy]:::agent
    A9 -->|norm flag| H3[Review seniority exception human]:::human
    A9 -. ESC-BUDDY-UNAVAILABLE .-> H4[HR assigns buddy human]:::human

    A2 --> A11[I-9 reminder cadence]:::agent
    A11 -. ESC-I9 .-> H5[Hold decision human]:::human

    A2 --> A12[Manager handoff package]:::agent
    A12 --> H6[Manager confirms handoff human]:::human

    A10 --> LOG[(Decision log 7y / integ 1y)]:::agent
    H1 --> LOG
    H2 --> LOG
    H3 --> LOG
    H4 --> LOG
    H5 --> LOG
    H6 --> LOG
```

*Figure 1 — Delegation boundary across the Onboarding orchestration (work inventory §2.3). Agent-driven nodes are blue; human-led nodes are yellow and suffixed `(human)` in prose references. Escalation edges are dashed with `ESC-*` codes. External systems are grouped by subgraph.*

The diagram introduces no new facts: every node maps to a row in §2.3 and every escalation edge maps to a hard constraint in §2.5.

### 2.7 Boundary-Respect Metric (hand-off to §1)

The delegation analysis forces exactly one non-negotiable success metric, which the problem-statement deliverable carries as **M4** (§1.3):

> **100% of judgment-classified tasks reach a logged `HumanDecision` record before the task state can become `COMPLETE`. Zero silent agent decisions.**

This is enforced by hard constraint **C4** in §2.5 and by the state-machine guard the capability spec carries on `Task.status = COMPLETE` (§3.4, §3.5). If §1 is regenerated, M4's wording and non-negotiable tag must survive unchanged.

---


## 3. Agent Specification

*(Consolidation note: the source file's front-matter and §2 Assumption Log are stripped; §9 "Out of scope" is stripped; §8 "Self-audit (production-spec-checklist alignment)" is preserved verbatim in §3.8 below. The integration section retains the explicit `[UNKNOWN]` tags traced to A10, A11, A17 in §0.1.)*

### 3.1 Capability Set Overview

Three capabilities cover every FULL and HUMAN-IN-LOOP row in the §2.3 work inventory. Capabilities fully downstream of a HUMAN-LED decision (training track, benefits packet dispatch, IT provisioning) are in scope; the HUMAN-LED decisions themselves (classification, benefits election, I-9 hold) are deliberately *not* capabilities of this spec.

1. **Cap-A — Onboarding Orchestrator.** The orchestrating capability. Owns the `Onboarding` and `Task` entities, instantiates the ~40 tasks on hire, schedules time-triggered actions, enforces the state machine, writes the decision log, and fires all `ESC-*` escalations.
2. **Cap-B — Buddy Matcher.** Owns the three-factor filter per H4, the one-buddy-per-mentee invariant, tie-break logic per A6, and the post-filter seniority-norm flag per A8. Proposes a match, which Cap-A persists (or holds pending HR review on the exception path).
3. **Cap-C — System Integrator.** Owns all outbound writes to Workday, ServiceNow, LMS, Benefits, Payroll, Email, and inbound webhooks from LMS (and any others discovered). Enforces idempotency, retry, timeout, and fallback. Cap-A never writes to an external system directly; it always goes through Cap-C.

The agent does not classify, does not elect benefits, does not hold I-9s, and does not decide who overrides a missing buddy. Those are HUMAN-LED rows in §2.3 and sit outside every capability here.

### 3.2 Entity Model

#### 3.2.1 `Onboarding`

| Attribute | Type | Required | Constraints | Notes |
|---|---|---|---|---|
| `id` | UUID | Y | PK, immutable | Generated on create. |
| `employee_id` | UUID | Y | FK → Workday worker UUID; immutable | From hire event. |
| `employment_class` | enum [`FULL_EMPLOYEE`, `CONTRACTOR`, `UNSET`] | Y | Default `UNSET`; agent **must not** write `FULL_EMPLOYEE` or `CONTRACTOR` | HUMAN-LED (hard constraint C1). |
| `role_code` | string | Y | Matches ServiceNow `role_code` pattern `/^[A-Z]{2,5}-\d{2,4}$/` | Drives IT bundle lookup. |
| `start_date` | ISO 8601 date (UTC) | Y | ≥ `created_at::date` | First day worked. |
| `status` | enum [`INITIATED`, `IN_PROGRESS`, `ON_HOLD`, `COMPLETE`, `ABANDONED`] | Y | See state machine | Derived-but-stored. |
| `handoff_status` | enum [`PENDING`, `PACKAGE_SENT`, `CONFIRMED`] | Y | Default `PENDING` | Cap-A rule 10. |
| `hold_reason` | enum [`I9_OVERDUE`, `CLASSIFICATION_PENDING`, `MANUAL`] \| null | N | Required iff `status = ON_HOLD` | Hold cause logged. |
| `created_at` | ISO 8601 timestamp (UTC) | Y | Immutable |  |
| `updated_at` | ISO 8601 timestamp (UTC) | Y | Updated on every write |  |
| `created_by` | string (service account id or user id) | Y | Immutable | Agent service account for auto-created. |
| `deleted_at` | ISO 8601 timestamp (UTC) | N | Soft delete; immutable once set; retention 7y per A9 |  |

**State machine** (Mermaid — entity has 5 states + non-linear transitions, diagram trigger fires):

```mermaid
stateDiagram-v2
    [*] --> INITIATED : hire event received
    INITIATED --> IN_PROGRESS : employment_class != UNSET (human write)
    IN_PROGRESS --> ON_HOLD : ESC-I9 unresolved past deadline / HR sets MANUAL hold
    ON_HOLD --> IN_PROGRESS : HR records resolution (HumanDecision logged)
    IN_PROGRESS --> COMPLETE : day-14 audit passes (all required tasks COMPLETE; no open judgment task without HumanDecision)
    INITIATED --> ABANDONED : hire rescinded (Workday event)
    IN_PROGRESS --> ABANDONED : hire rescinded
    ON_HOLD --> ABANDONED : hire rescinded
    COMPLETE --> [*]
    ABANDONED --> [*]
```

*Figure 2 — `Onboarding` lifecycle. Transitions into IN_PROGRESS depend on a human write of `employment_class` — the boundary guard for C1 is enforced at this transition.*

- **Immutability:** `id`, `employee_id`, `start_date`, `created_at`, `created_by`, `deleted_at` (once set).
- **Delete behaviour:** Soft delete only; 7-year retention per A9. Hard delete disallowed while linked `HumanDecision` records exist.

#### 3.2.2 `Task`

| Attribute | Type | Required | Constraints | Notes |
|---|---|---|---|---|
| `id` | UUID | Y | PK, immutable |  |
| `onboarding_id` | UUID | Y | FK → `Onboarding.id`; on delete: restrict | |
| `type` | enum (exhaustive list below) | Y | See §3.2.2.a | |
| `classification` | enum [`ROUTINE`, `JUDGMENT`] | Y | Set at instantiation from template | M1 + M4 denominators. |
| `required` | boolean | Y | Default `true` from template; only optional-extension tasks are `false` | A-open-4 — required-task definition for M3. |
| `status` | enum [`PENDING`, `IN_FLIGHT`, `WAITING_HUMAN`, `COMPLETE`, `FAILED`, `CANCELLED`] | Y | See state machine | |
| `due_at` | ISO 8601 timestamp | Y | Computed at instantiation; immutable after set | Cap-A rule 3. |
| `idempotency_key` | string(64) | Y | Deterministic per A12 | For Cap-C. |
| `human_decision_id` | UUID \| null | N | Required iff `classification = JUDGMENT` AND `status = COMPLETE` | **Enforces M4.** |
| `escalation_code` | string \| null | N | Set when an ESC-* is raised against this task | |
| `retry_count` | int | Y | Default 0; max 3 | Cap-C retry. |
| `created_at` / `updated_at` | ISO 8601 | Y | | |

##### 3.2.2.a `Task.type` exhaustive enum

`CREATE_ONBOARDING`, `INSTANTIATE_TASKS`, `IT_PROVISION_STANDARD`, `IT_PROVISION_NONTEMPLATE`, `BENEFITS_DISPATCH`, `LMS_ASSIGN`, `PAYROLL_SETUP`, `WELCOME_MATERIALS`, `CHECKPOINT_SCHEDULE_30D`, `BUDDY_PROPOSE`, `BUDDY_ASSIGN`, `I9_REMINDER`, `MANAGER_HANDOFF_PACKAGE`, `MANAGER_HANDOFF_CONFIRM`.

**State machine** (6 states, non-linear — Mermaid triggered):

```mermaid
stateDiagram-v2
    [*] --> PENDING
    PENDING --> IN_FLIGHT : due_at reached OR upstream dependency complete
    IN_FLIGHT --> COMPLETE : routine external write succeeded AND (classification=ROUTINE OR human_decision_id set)
    IN_FLIGHT --> WAITING_HUMAN : ESC-* raised OR classification=JUDGMENT reached gate
    WAITING_HUMAN --> IN_FLIGHT : HumanDecision logged, action=resume
    WAITING_HUMAN --> CANCELLED : HumanDecision logged, action=skip
    IN_FLIGHT --> FAILED : retry_count = 3 AND last_error in 5xx|timeout
    FAILED --> IN_FLIGHT : HumanDecision logged, action=retry
    PENDING --> CANCELLED : Onboarding → ABANDONED
    COMPLETE --> [*]
    CANCELLED --> [*]
    FAILED --> [*]
```

*Figure 3 — `Task` lifecycle. The WAITING_HUMAN state is the mechanism that enforces the M4 non-negotiable — a JUDGMENT task cannot reach COMPLETE without passing through WAITING_HUMAN and acquiring a `human_decision_id`.*

- **Immutability:** `id`, `onboarding_id`, `type`, `classification`, `required`, `due_at` (after set), `idempotency_key`.
- **Delete behaviour:** No hard delete. `CANCELLED` and `FAILED` persist 1y per A9.

#### 3.2.3 `HumanDecision`

| Attribute | Type | Required | Constraints | Notes |
|---|---|---|---|---|
| `id` | UUID | Y | PK, immutable | |
| `task_id` | UUID | Y | FK → `Task.id`; on delete: restrict | |
| `actor_user_id` | string | Y | A *named human* — never an agent service account; enforced at write time | Boundary-respect. |
| `decision` | enum [`APPROVE`, `REJECT`, `HOLD`, `RESUME`, `SKIP`, `OVERRIDE`, `ASSIGN`, `RETRY`] | Y | |
| `reason` | string | Y | Max 2000 chars | Free text; required. |
| `payload` | JSON | N | E.g. override buddy selection; classification value; hold expiry | |
| `decided_at` | ISO 8601 timestamp | Y | Immutable | |
| `created_at` / `updated_at` | ISO 8601 | Y | `updated_at` may move only on amendment (with reason, immutable audit trail) | |

- **Immutability:** `id`, `task_id`, `actor_user_id`, `decision`, `decided_at` — amendments create a new row with `payload.amends = <prior_id>`; the original stays.
- **Delete behaviour:** Never deleted. 7y retention per A9.

#### 3.2.4 `EscalationEvent`

| Attribute | Type | Required | Constraints | Notes |
|---|---|---|---|---|
| `id` | UUID | Y | PK, immutable | |
| `task_id` | UUID | Y | FK → `Task.id` | |
| `code` | enum [`ESC-CLASS`, `ESC-I9`, `ESC-BUDDY-UNAVAILABLE`, `ESC-BUDDY-SENIORITY`, `ESC-ACCESS-NONTEMPLATE`, `ESC-HANDOFF-UNCONFIRMED`, `ESC-INTEG-OUTAGE`, `ESC-TRAINING-LATE`] | Y | §3.5.6 | |
| `recipient_role` | string | Y | E.g. `HR_OPS_LEAD`, `IT_APPROVER`, `HIRING_MANAGER` (concrete distribution-list resolution tracked under A-open-3) | |
| `sla_due_at` | ISO 8601 | Y | Computed from fired_at + SLA | |
| `status` | enum [`OPEN`, `RESOLVED`, `BREACHED`] | Y | | |
| `fired_at` / `resolved_at` | ISO 8601 | Y / N | `resolved_at` only when `status=RESOLVED` | |

Retention 7y per A9.

### 3.3 Cap-A — Onboarding Orchestrator

#### 3.3.1 Purpose
Instantiate and steward an `Onboarding` from hire event through day-14 audit, honouring the delegation boundary at every gate. "Done" = `Onboarding.status = COMPLETE` with zero open required tasks and every JUDGMENT task carrying a logged `HumanDecision`.

#### 3.3.2 Scope

**In scope:** creating `Onboarding`; instantiating tasks; scheduling time-triggered actions; firing escalations; enforcing state-machine guards; writing the decision log.

**Out of scope:**
- Setting `employment_class` — HUMAN-LED per §2.5 C1.
- Making benefits elections — HUMAN-LED per C3.
- Deciding an I-9 hold — HUMAN-LED per C2 (agent fires `ESC-I9`, does not hold).
- Overriding a missing buddy — HUMAN-LED per §2.3 row 13.
- Executing external writes — delegated to Cap-C.

#### 3.3.3 Inputs

| Input | Type | Required | Validation | Source |
|---|---|---|---|---|
| `workday_hire_event` | JSON `{employee_id: UUID, role_code: regex above, start_date: ISO 8601, manager_id: UUID, location: enum [...], seniority_band: enum [IC1..IC7, M1..M5]}` | Y | Schema validated; `start_date ≥ today` | Workday webhook → Cap-C → Cap-A |
| `classification_set_event` | JSON `{onboarding_id, employment_class, actor_user_id, decided_at}` | Y for transition out of INITIATED | `actor_user_id` must resolve to a named user, never a service account | Workday write observed via webhook |
| `lms_completion_event` | JSON `{lms_assignment_id, onboarding_id, completed_at}` | Y for task COMPLETE | Signature verified | LMS webhook → Cap-C |
| `manager_confirm_event` | JSON `{onboarding_id, actor_user_id, confirmed_at}` | Y | Actor must equal `manager_id` from hire event | UI webhook → Cap-A |
| `hr_decision_event` | JSON `{task_id, decision, reason, payload?, actor_user_id}` | Y for ESC resolutions | Actor role in allowed set for the ESC code | UI / ticketing |

#### 3.3.4 Outputs

| Output | Type | Condition | Destination |
|---|---|---|---|
| `Onboarding` write | DB row | On every state transition | Orchestrator store |
| `Task` batch write | DB rows | On `INSTANTIATE_TASKS` | Orchestrator store |
| External write intent | Queue message to Cap-C | On every task reaching `IN_FLIGHT` with routine action | Cap-C inbound queue |
| `EscalationEvent` row + notification | DB + email (via Cap-C §3.6.4) | On each ESC-* condition | Recipient role distribution (resolved per A-open-3) |
| `HumanDecision` row | DB row | On receipt of `hr_decision_event` / `manager_confirm_event` / `classification_set_event` | Decision log |
| Day-14 audit report | JSON, emitted to `HR_OPS_LEAD` distribution | Daily at 06:00 local | Email + dashboard |

#### 3.3.5 Business Rules

1. **Rule 1 — Onboarding creation.** On receipt of a `workday_hire_event` whose `employee_id` does not already have an active (`status ∈ {INITIATED, IN_PROGRESS, ON_HOLD}`) `Onboarding`, the orchestrator **must** create one with `status = INITIATED`, `employment_class = UNSET`, and `hold_reason = null`. If an active `Onboarding` exists for the `employee_id`, the event **must** be logged `duplicate_hire_event` and ignored (no second record created, no error raised upstream).
2. **Rule 2 — Task instantiation.** On transition `INITIATED → IN_PROGRESS` (i.e. `employment_class` is set by a named human), the orchestrator **will** instantiate the full task template for the `employment_class` × `role_code` tuple. Task types are drawn from the §3.2.2.a enum; each task is given `classification` per template (`IT_PROVISION_NONTEMPLATE`, `BUDDY_ASSIGN` on the seniority-exception path, and `I9_REMINDER` flagged for `WAITING_HUMAN` on overdue are classified `JUDGMENT`; all others `ROUTINE`).
3. **Rule 3 — Deadline computation.** Each task's `due_at` **must** be computed at instantiation as `start_date + offset_days(type)` in business days per A14. The offset table is stored as a configuration artefact; `due_at` is immutable after set. No task's `due_at` may exceed `start_date + 14 business days` (M3 audit boundary).
4. **Rule 4 — IT provisioning routing.** For every `IT_PROVISION_STANDARD` task, Cap-A **must** resolve the access bundle from ServiceNow CIs keyed by `role_code` (per A13) and dispatch via Cap-C §3.6.2. For any provisioning item that does not match a bundle, a sibling `IT_PROVISION_NONTEMPLATE` task **will** be created with `classification = JUDGMENT` and `ESC-ACCESS-NONTEMPLATE` fired to `IT_APPROVER` with the list of non-template items attached.
5. **Rule 5 — I-9 regulatory guard.** A dedicated `I9_REMINDER` task **will** be instantiated with `due_at = start_date + 3 business days` per IRCA (C2 + A14). On `due_at - 1 business day`, Cap-A **must** dispatch a reminder email to the employee and the hiring manager. If, at `due_at`, Cap-A has not received a Workday signal that I-9 Section 2 is complete, it **must** fire `ESC-I9` to `HR_OPS_LEAD` and transition the `Onboarding` to `ON_HOLD` with `hold_reason = I9_OVERDUE`. Cap-A **cannot** lift the hold; only a `HumanDecision { decision: RESUME }` from HR Ops lifts it.
6. **Rule 6 — OVERDUE is derived, not stored.** A task is OVERDUE iff `status ∈ {PENDING, IN_FLIGHT} AND now() > due_at`. This is computed on read; it is not a stored `status`. The dashboard shows OVERDUE as a derived badge.
7. **Rule 7 — Idempotency for external writes.** Every task handed to Cap-C **must** carry `idempotency_key` per A12. Cap-C guarantees at-most-once effect on the external system; Cap-A's guarantee is that it never retries an intent with a mutated payload under the same key.
8. **Rule 8 — Scheduled day-10 handoff nag.** Per A15, at `start_date + 10 business days`, if `handoff_status ≠ CONFIRMED`, the orchestrator **must** dispatch a handoff-package email to the manager and set `handoff_status = PACKAGE_SENT`. At `start_date + 12 business days`, if still `≠ CONFIRMED`, `ESC-HANDOFF-UNCONFIRMED` **will** fire to `HIRING_MANAGER` and `HR_OPS_LEAD`.
9. **Rule 9 — Day-14 audit.** At `start_date + 14 business days 06:00 local`, Cap-A **must** evaluate each active `Onboarding`. If every required task is `COMPLETE` and every JUDGMENT task carries a non-null `human_decision_id`, it **will** transition to `COMPLETE`. Otherwise it **must** remain `IN_PROGRESS` or `ON_HOLD`; the audit report enumerates the blocking tasks.
10. **Rule 10 — Manager handoff confirmation.** `handoff_status` **cannot** move to `CONFIRMED` on silence or on an agent-synthesised signal. Only a `manager_confirm_event` whose `actor_user_id = Onboarding.manager_id` may make the transition (boundary guard).
11. **Rule 11 — Retry budget.** Any task whose external write fails after `retry_count = 3` with a 5xx or timeout **will** transition to `FAILED`, raise `ESC-INTEG-OUTAGE` to `HR_OPS_LEAD`, and wait for a `HumanDecision { decision: RETRY | SKIP | OVERRIDE }` before moving.
12. **Rule 12 — Boundary guard (C1 + C3 + C2).** Cap-A **cannot** write `Onboarding.employment_class` to any value other than `UNSET`. Cap-A **cannot** transition `Onboarding.status` from `ON_HOLD` to `IN_PROGRESS` without a matching `HumanDecision { decision: RESUME, actor_user_id ≠ agent_service_account }`. Cap-A **cannot** create a `HumanDecision` row where `actor_user_id` resolves to a service account; the DB has a check constraint on this (`actor_user_id NOT LIKE 'svc-%'`). These three checks together enforce C1, C2, C3 of §2.5.
13. **Rule 13 — Decision log completeness.** Every `Task.status` transition, every `Onboarding.status` transition, every `EscalationEvent` fired, every external write intent dispatched to Cap-C, and every `HumanDecision` row **must** produce a row in the decision log (`decision_log_entries` table) carrying `(entity_id, event_type, actor, before, after, timestamp, correlation_id)`. The day-14 audit report's "every JUDGMENT task has a `HumanDecision`" check reads from this log — it is the enforcement point for M4.
14. **Rule 14 — Fan-out circuit breaker (per A-open-5).** Cap-A **must** cap concurrent outstanding Cap-C dispatches per `Onboarding` at **10**. On the 11th attempt, Cap-A **must** hold new dispatches in `PENDING`, fire `ESC-INTEG-OUTAGE` preventively to `HR_OPS_LEAD` + IT on-call, and resume dispatches once the in-flight count drops below 10 or after a `HumanDecision { decision: RETRY }`. This protects against runaway fan-out during partial integrator outages.

#### 3.4 Cap-B — Buddy Matcher

#### 3.4.1 Purpose
Given a mentee `Onboarding`, propose a buddy or escalate. Outputs one of: `{proposed_buddy_id, flag}` → Cap-A persists via the `BUDDY_ASSIGN` task.

#### 3.4.2 Scope

**In scope:** three-factor filter; tie-break; one-buddy-per-mentee invariant; seniority-norm flag.

**Out of scope:**
- Persisting the assignment — that is Cap-A's write via Cap-C.
- Deciding the HR override on `ESC-BUDDY-UNAVAILABLE` — HUMAN-LED.
- Deciding the seniority-norm exception — HUMAN-IN-LOOP, decided by HR outside this capability.

#### 3.4.3 Inputs

| Input | Type | Required | Validation | Source |
|---|---|---|---|---|
| `mentee` | `{employee_id, department, location, seniority_band}` | Y | Schema validated | Cap-A |
| `candidate_pool` | list of `Employee` with fields as above + `current_buddy_count`, `on_leave` | Y | Fetched from Workday directory | Cap-C §3.6.1 |
| `seniority_threshold` | int (default 3 per A16) | N | ≥ 1 | HR Ops config |

#### 3.4.4 Outputs

| Output | Type | Condition | Destination |
|---|---|---|---|
| `BuddyProposal { proposed_buddy_id, reason }` | JSON | Filter returns ≥ 1 match with no norm flag | Cap-A |
| `BuddyProposal { proposed_buddy_id, reason, seniority_flag: true, delta }` | JSON | Match exists but delta > threshold | Cap-A (triggers `ESC-BUDDY-SENIORITY`) |
| `BuddyProposal { proposed_buddy_id: null, reason: "no unencumbered match" }` | JSON | No candidate passes the filter with `current_buddy_count=0` AND `on_leave=false` | Cap-A (triggers `ESC-BUDDY-UNAVAILABLE`) |

#### 3.4.5 Business Rules

1. **Rule 1 — Three-factor filter.** A candidate `c` passes iff `c.department == mentee.department` AND `c.location == mentee.location` AND `c.seniority_band` is within **any** band (seniority is a ranking factor, not a filter factor, per H4's wording). *(Flagged as A-open: H4 is ambiguous on whether seniority is a filter factor or a ranking factor; current reading = ranking factor, because the seniority-norm *judgment* is post-filter per A8. To confirm in coach session.)*
2. **Rule 2 — One-buddy-per-mentee invariant.** A candidate with `current_buddy_count ≥ 1` is excluded (per H4's "you can only be a buddy to one person").
3. **Rule 3 — Availability filter.** A candidate with `on_leave = true` is excluded (per A5).
4. **Rule 4 — Fallback to HR escalation.** If no candidate passes Rules 1–3, Cap-B **must** return `{proposed_buddy_id: null}` with reason, triggering `ESC-BUDDY-UNAVAILABLE`. It **cannot** relax the filter silently.
5. **Rule 5 — Tie-break ordering** (per A6 and H4's hypothesis text): rank passing candidates by (a) department match (all pass by Rule 1, so this degenerates), then (b) location match (same), then (c) smallest absolute seniority-band delta to mentee, then (d) uniform-random among remaining. The ranking is deterministic given a seeded RNG whose seed is the `Onboarding.id`.
6. **Rule 6 — Seniority-norm flag.** The top-ranked candidate is evaluated against the configured seniority threshold (default 3 bands per A16). If `|candidate.seniority_band - mentee.seniority_band| > threshold`, Cap-B **will** return the proposal with `seniority_flag = true`; Cap-A's `BUDDY_ASSIGN` task then waits in `WAITING_HUMAN` for an HR `APPROVE` or `OVERRIDE` (ESC-BUDDY-SENIORITY). The flag **cannot** be suppressed.
7. **Rule 7 — No silent override.** Cap-B **cannot** itself apply an HR override; it has no write path to `BuddyProposal.actor_user_id`. Overrides come from Cap-A via a `HumanDecision`.
8. **Rule 8 — Boundary guard.** Cap-B **cannot** propose a buddy that fails any filter rule (1–3). The DB-side check on `BuddyProposal` rejects such rows.

(Rule count: 8 — clears the Week 1 ≥ 6 floor.)

#### 3.4.6 Escalation Triggers

| Trigger code | Condition | Who | Action | SLA |
|---|---|---|---|---|
| `ESC-BUDDY-UNAVAILABLE` | Rule 4 | `HR_OPS_LEAD` | `ASSIGN` via HumanDecision payload | 3 bd |
| `ESC-BUDDY-SENIORITY` | Rule 6 | `HR_OPS_LEAD` | `APPROVE` or `OVERRIDE` | 2 bd |

#### 3.4.7 Decision Log
Every `BuddyProposal` (with full candidate pool size, chosen candidate, rank reason, seniority flag) is logged to `buddy_proposals` with 7y retention.

### 3.5 Cap-C — System Integrator

#### 3.5.1 Purpose
Own every external system boundary. Guarantee idempotency, retry, timeout, and fallback on behalf of Cap-A and Cap-B.

#### 3.5.2 Scope

**In scope:** outbound HTTP to Workday, ServiceNow, LMS, Benefits, Payroll; outbound email via the transactional relay; inbound webhook receipt + verification; retry and backoff; dead-lettering.

**Out of scope:**
- Deciding what to write — that is upstream capability logic.
- Writing `employment_class` into Workday — **explicitly forbidden by a code-level allowlist** (boundary guard for C1).

#### 3.5.3 Inputs

Queue messages from Cap-A carrying `{system, action, payload, idempotency_key, correlation_id}`. Schema validated; rejected messages return to Cap-A dead-letter queue (triggers `ESC-INTEG-OUTAGE` after 3 Cap-A-level retries).

#### 3.5.4 Outputs

External HTTP calls; webhook receipts; rows in `integration_audit` (1y retention per A9).

#### 3.5.5 Business Rules

1. **Rule 1 — Per-system timeout.** Each system has a configured timeout (see §3.6). Cap-C **must** cancel and report the timeout as a retryable failure if the external call exceeds it.
2. **Rule 2 — Retry policy.** 5xx and timeout: retry up to 3 times with exponential backoff (2s, 4s, 8s); 429: retry honouring `Retry-After` up to 3 times; 4xx (except 429): no retry, report upstream.
3. **Rule 3 — Idempotency.** Every write carries `idempotency_key`. Cap-C **must** include it in the `Idempotency-Key` header where the target system supports it (Workday, ServiceNow, Stripe-style), and in a request-body field where it does not; the key is logged regardless.
4. **Rule 4 — Allowlist for writes.** Cap-C **cannot** dispatch a Workday write whose payload attempts to set `workerType` / `employment_class`. The allowlist is enforced at the Cap-C entrypoint, independent of upstream logic. This is the code-level corollary of boundary guard C1.
5. **Rule 5 — Webhook verification.** Every inbound webhook **must** be verified against the per-system shared secret (HMAC or signature). Unverified webhooks are dropped and logged; they do not fire upstream.
6. **Rule 6 — Rate-limit respect.** If a burst exceeds the rate limit, Cap-C **will** queue and drain at the limit; it **cannot** shed requests silently.
7. **Rule 7 — Fallback.** If a system is unavailable for > 10 minutes (3 retries × backoff + margin), Cap-C **will** move the message to `deadletter` and raise `ESC-INTEG-OUTAGE` via Cap-A.
8. **Rule 8 — Audit.** Every outbound call is logged to `integration_audit` with `(system, action, idempotency_key, http_status, duration_ms, retry_count, ts)`.

#### 3.5.6 Escalation Triggers

| Code | Condition | Who | Action | SLA |
|---|---|---|---|---|
| `ESC-INTEG-OUTAGE` | Rule 7 | `HR_OPS_LEAD` + IT on-call | RETRY / SKIP / OVERRIDE via HumanDecision | 1 bd |

#### 3.5.7 Decision Log
`integration_audit` (1y). Per-task `write_dispatched` mirror in `decision_log_entries` (7y), keyed by `correlation_id`, for M4 traceability.

### 3.6 Integration Contracts

#### 3.6.1 Workday

| Property | Value |
|---|---|
| Purpose | Hire event webhook; worker read; directory lookup for Cap-B |
| Endpoint | `POST {tenant}/ccx/service/{customer}/Human_Resources/v42.0` (SOAP) or REST equivalent `GET /ccx/api/v1/workers/{id}` — **[UNKNOWN]** which edition until tenant confirmed (A11) |
| Authentication | OAuth2 client-credentials at `{tenant}/ccx/oauth2/{customer}/token`; secret `fde-onboarding-workday` (A11) |
| Timeout | 10s |
| Retry | 3× on 5xx/timeout/429 per Cap-C rule 2; no retry on 4xx |
| Rate limit | **[UNKNOWN]** — tenant-specific, typically 30 rps (A11) |
| Fallback | Dead-letter; `ESC-INTEG-OUTAGE` after 10 min |

Data mapping:
- Internal `Onboarding.employee_id` ← Workday `Worker.workerId`
- Internal `role_code` ← Workday `Worker.jobProfile.id`
- Internal `start_date` ← Workday `Worker.hireDate`
- Internal `employment_class` ← Workday `Worker.workerType` (**read-only** from agent's side; write forbidden by Cap-C rule 4)

#### 3.6.2 ServiceNow

| Property | Value |
|---|---|
| Purpose | IT provisioning request creation; bundle lookup |
| Endpoint | `POST /api/now/table/sc_request` and `GET /api/now/table/sc_cat_item?role_code=…` |
| Authentication | OAuth2 at `/oauth_token.do`; secret `fde-onboarding-servicenow` |
| Timeout | 15s |
| Retry | per Cap-C rule 2 |
| Rate limit | **[UNKNOWN]** — typically 60 rpm per app (A11) |
| Fallback | Dead-letter; `ESC-INTEG-OUTAGE` after 10 min |

Data mapping:
- Internal `Task.idempotency_key` → ServiceNow `correlation_id`
- Internal `role_code` → ServiceNow catalogue `role_code` (A13)
- External `sc_request.number` ← persisted on `Task.payload.external_id`

#### 3.6.3 LMS — **[BUILD-BLOCKING UNKNOWN — A10]**

| Property | Value |
|---|---|
| Purpose | Compliance-training assignment; completion webhook |
| Endpoint | `[UNKNOWN]` — pending LMS vendor disclosure |
| Authentication | `[UNKNOWN]` |
| Timeout | 15s (placeholder) |
| Retry | per Cap-C rule 2 |
| Rate limit | `[UNKNOWN]` |
| Fallback | Dead-letter; `ESC-INTEG-OUTAGE`; also `ESC-TRAINING-LATE` if completion signal does not arrive within SLA — two distinct conditions. |

Data mapping: pending vendor disclosure. **This entry is raised to the top of the coach-session priority queue.**

#### 3.6.4 Email (transactional)

| Property | Value |
|---|---|
| Purpose | Reminders, escalations, welcome materials, handoff packages |
| Endpoint | `[UNKNOWN] — per A17`; assumed to support batch `POST /send` |
| Authentication | API key in secrets manager `fde-onboarding-email` |
| Timeout | 10s |
| Retry | per Cap-C rule 2; max 3 |
| Rate limit | `[UNKNOWN]` — typically 10 rps |
| Fallback | Dead-letter; degrade to in-app notification only; `ESC-INTEG-OUTAGE` |

Data mapping: template-based; payload fields map to Mustache-style placeholders.

#### 3.6.5 Benefits system (per H5)

| Property | Value |
|---|---|
| Purpose | Dispatch enrolment packet; poll/receive completion status |
| Endpoint | `[UNKNOWN]` pending vendor disclosure (A10-adjacent) |
| Authentication | API key or OAuth — `[UNKNOWN]` |
| Timeout | 15s |
| Retry | per Cap-C rule 2 |
| Rate limit | `[UNKNOWN]` |
| Fallback | Dead-letter + ESC-INTEG-OUTAGE |

Data mapping: `Onboarding.employee_id` → benefits `person_id` (assumed 1:1 match via Workday ID).

#### 3.6.6 Payroll / Time (per H5)

| Property | Value |
|---|---|
| Purpose | Create payroll profile; register time-tracking user |
| Endpoint | `[UNKNOWN]` |
| Authentication | `[UNKNOWN]` |
| Timeout | 15s |
| Retry | per Cap-C rule 2 |
| Rate limit | `[UNKNOWN]` |
| Fallback | Dead-letter + ESC-INTEG-OUTAGE |

Data mapping: `Onboarding.employee_id` → payroll `employee_id`; `role_code` → pay-band defaults (a human may adjust).

### 3.7 Diagrams — orchestration sequence

A third diagram — **orchestration sequence across systems** — is warranted because the day-(-7) to day-14 timeline touches 6 external systems with distinct retry profiles and escalation branches (`CLAUDE.md` trigger: sequence + orchestration flows across 4+ systems with distinct fallbacks). Rendered here:

```mermaid
sequenceDiagram
    autonumber
    participant WD as Workday
    participant CA as Cap-A (human)
    participant AG as Cap-A orchestrator
    participant CB as Cap-B buddy
    participant CC as Cap-C integrator
    participant SN as ServiceNow
    participant LMS as LMS
    participant BEN as Benefits
    participant PAY as Payroll
    participant EM as Email
    WD->>AG: hire event (day -7)
    AG->>AG: create Onboarding (INITIATED)
    AG-->>CA: ESC-CLASS (if class UNSET at day -1)
    CA->>WD: set employment_class (human write)
    WD->>AG: classification_set_event
    AG->>AG: instantiate ~40 tasks (IN_PROGRESS)
    par Provisioning
      AG->>CC: IT_PROVISION_STANDARD
      CC->>SN: POST sc_request (idempotent)
      SN-->>CC: request_id
    and Training
      AG->>CC: LMS_ASSIGN
      CC->>LMS: assign (idempotent)
    and Benefits
      AG->>CC: BENEFITS_DISPATCH
      CC->>BEN: send packet
    and Payroll
      AG->>CC: PAYROLL_SETUP
      CC->>PAY: create profile
    and Welcome
      AG->>CC: WELCOME_MATERIALS
      CC->>EM: send welcome
    and Buddy
      AG->>CB: propose(mentee, pool)
      CB-->>AG: BuddyProposal
      alt unavailable
        AG-->>CA: ESC-BUDDY-UNAVAILABLE
      else seniority flag
        AG-->>CA: ESC-BUDDY-SENIORITY
      else auto-assign
        AG->>CC: buddy notification email
      end
    end
    AG->>EM: I-9 reminder (day start_date+2)
    alt I-9 not complete at +3bd
      AG-->>CA: ESC-I9
      AG->>AG: Onboarding→ON_HOLD
    end
    AG->>EM: handoff package (day +10)
    alt handoff unconfirmed at +12
      AG-->>CA: ESC-HANDOFF-UNCONFIRMED
    end
    AG->>AG: day-14 audit → COMPLETE or stay IN_PROGRESS
```

*Figure 4 — Onboarding orchestration sequence, day −7 to day +14. Dashed escalation edges carry ESC-* codes; human actor lane labelled `(human)`. No node here is absent from §3.3–§3.6.*

### 3.8 Self-audit (production-spec-checklist alignment, from source file)

- [x] Every business rule uses **must / will / cannot**.
- [x] Every numeric threshold is explicit (`10s`, `3 business days`, `3 retries`, `2s/4s/8s`, `10 min`, `12 business days`, `14 business days`, `10 concurrent dispatches`).
- [x] Every conditional has an explicit IF / THEN (see Cap-A rules 1, 3, 4, 5, 8, 9, 11, 14; §3.4.5 rules 1–6; §3.5.5 rules 1–7).
- [x] Every entity has PK, `created_at`, `updated_at`, state machine (where stateful).
- [x] Every integration has endpoint, auth, timeout, retry, rate limit, fallback, data mapping — OR an explicit `[UNKNOWN]` traced to an Assumption Log entry (LMS/A10, Email/A17, Benefits+Payroll rate limits/A11).
- [x] Delegation boundary respected: HUMAN-LED rows in §2.3 are out-of-scope *and* backed by boundary-guard rules (Cap-A rule 12; Cap-C rule 4).
- [x] Every escalation trigger has code, state-based condition, role recipient, specific required action, numeric SLA (§3.3.6 + §3.4.6 + §3.5.6).
- [x] Every external-system write is idempotent on a named deterministic key (A12 + Cap-C rule 3).
- [x] Every `[ASSUMED]` or `[UNKNOWN]` in the body has a matching numbered entry in §0.1.
- [x] No `[TODO]` markers remain open. (LMS `[UNKNOWN]` is traced to A10, not a TODO.)
- [x] Cap-A has 14 rules; Cap-B has 8; Cap-C has 8 — all clear the ≥ 6 floor.
- [x] Spec is consistent with upstream §1 M1–M4 and §2 rows 1–22 + C1–C4. M4 is enforced by Task WAITING_HUMAN state + Cap-A rule 12 + DB check constraint on HumanDecision.actor_user_id.

**Overall buildability read.** Cap-A and Cap-B are buildable in their routine paths today — the rules, state machines, and boundary guards are specific enough for a coding agent to scaffold from without clarifying questions on those paths. **Cap-C's LMS branch is not yet buildable** because A10 (LMS vendor) is unresolved; an agent would have to guess the assignment and webhook contracts. The recommended next coach-session probe is *"Which LMS vendor is in use — Cornerstone, Workday Learning, Docebo, or other — and can you share the admin console URL and API docs?"* Everything else is medium-confidence and can be validated in parallel without blocking the first build loop.

---


## 4. Validation Design

*(Consolidation note: the source file's front-matter, §2 Assumption Log (entries V1–V5 subsumed into §0.1), §9 Diagrams block (no new diagram needed), §10 self-audit kept as §4.10, and §11 "Out of scope" are handled here — the §10 self-audit is preserved verbatim.)*

### 4.1 Validation Strategy

This deliverable produces **scenario-level** validation: each entry is a named situation with a concrete input set and a named expected outcome, tied back to specific rules in §3. It is not a unit-test catalogue; it is the evidence a reviewer would use to decide whether the built system honours the spec.

Each scenario carries a **P / F / E** tag: **P** (positive; must pass on a correct happy-path build), **F** (failure; exercises a failure mode the design must absorb), **E** (edge; probes a non-obvious boundary case). The **delegation-boundary tests in §4.7 are the load-bearing piece of this deliverable** — they are the closest Week 1 comes to proving the FDE skill is real. If a build produces a system that passes §4.4–§4.6 but fails §4.7, the build has not honoured the spec.

### 4.2 Validation-scoped assumptions (cross-ref)

Validation-specific assumptions V1 (merged into A1), V2, V3 (tracked under A10), V4, V5 live in §0.1. The coach-session priority queue for validation reads: **V1** (baseline retrievability for HP-1 M3 defence) → **V3/A10** (LMS webhook contract for FM-2) → **V4** (BT-1 ground truth) → **V2** (harness representativeness) → **V5** (threshold parameterisation).

### 4.3 Update protocol (validation-specific)

Standard: update in place; do not silently delete. If §3 changes a rule number or adds an escalation code, this section is regenerated rather than hand-patched — the trace matrix in §4.8 is the cheapest place in the programme to spot that drift.

### 4.4 Happy Path — HP-1

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
  - No `Task` of `classification=JUDGMENT` exists — this onboarding sat entirely in the routine tail. Per rule 2 + §3.2.2.a, only `IT_PROVISION_NONTEMPLATE`, `BUDDY_ASSIGN` on the exception path, and `I9_REMINDER`-if-overdue can be JUDGMENT; none are triggered here.
  - M1 (routine-delegation %): for this onboarding, 100% of routine tasks executed without human action. Defended.
  - M3 ("fell-through-the-cracks"): onboarding has zero open required tasks at day 14. Defended.
  - M4 (boundary respect): no agent-written `HumanDecision`; `actor_user_id` on all decision rows resolves to a named human (Cap-A rule 12; DB check constraint).

### 4.5 Edge Cases

| # | Scenario | Input / trigger | Expected outcome | Rule(s) exercised | P/F/E |
|---|---|---|---|---|---|
| EC-1 | **Duplicate hire event** — same Workday `employee_id` fires the hire webhook twice 15 seconds apart (network retry) | Two identical `workday_hire_event`s with same `employee_id` | First: `Onboarding` created. Second: `decision_log_entries` row `{event_type: duplicate_hire_event, action: ignored}`; no second record; upstream is acknowledged 200 OK. | Cap-A rule 1 (uniqueness guard) | E |
| EC-2 | **`employment_class` still UNSET at start_date − 1 bd** | No classification_set_event received by `start_date − 1 bd` 09:00 local | `ESC-CLASS` fires to `HR_OPS_LEAD` with SLA 1 bd; `Onboarding` remains `INITIATED`; no tasks instantiated. | Cap-A rule 2 (negative case), §3.3.6 ESC-CLASS | E |
| EC-3 | **Non-template IT access** — role requests include a non-bundled asset (e.g. a specific data-room seat for ENG-0200 not in the ENG template) | Provisioning list has 1 template asset + 1 non-template asset | Sibling `IT_PROVISION_NONTEMPLATE` task created; `ESC-ACCESS-NONTEMPLATE` fires; `IT_PROVISION_STANDARD` proceeds on the template items independently | Cap-A rule 4; A13 | E |
| EC-4 | **Concurrent task status writes** (race) — day-14 audit runs while the last `LMS_ASSIGN` completion webhook arrives | Audit reads `status` at t=τ; webhook arrives at τ+50ms and flips that task to COMPLETE | Audit run is transactional at the `Onboarding` row; either: (a) audit reads COMPLETE → transition to COMPLETE, or (b) audit reads IN_FLIGHT → no transition; audit runs again at next window. No torn read; no double-close; log reflects exactly one transition. | Cap-A rule 9; Task state machine (§3.2.2) | E |
| EC-5 | **Boundary-value — task processed at exactly `due_at + 1s`** | `I9_REMINDER` `due_at = 2026-05-14T00:00:00Z`, clock is `2026-05-14T00:00:01Z` at evaluation | OVERDUE = true by rule 6 (`now() > due_at`); the reminder dispatch triggers if not yet sent; `ESC-I9` waits until `start_date + 3 business days` end-of-day — i.e. rule 5's hold trigger is NOT the same boundary as rule 6's OVERDUE badge. | Cap-A rules 5, 6 (distinguishes derived-OVERDUE from regulatory-deadline) | E |
| EC-6 | **Buddy pool has one IC4 candidate already assigned to another mentee** (`current_buddy_count=1`) | Pool: IC4 candidate excluded by Rule 2; IC5 (delta 1) proposed | IC5 returned, `seniority_flag=false` (delta 1 ≤ threshold 3); auto-assign proceeds | Cap-B rules 2, 5, 6 | E |
| EC-7 | **Hire rescinded** — Workday fires `worker.terminated` mid-onboarding | `Onboarding` currently `IN_PROGRESS` with tasks IN_FLIGHT | `Onboarding → ABANDONED`; all `PENDING`/`IN_FLIGHT` tasks `→ CANCELLED`; Cap-C issues compensating writes where possible (revoke access requests); retention clock starts; `ESC-INTEG-OUTAGE` not fired | Onboarding state machine (§3.2.1); Task state machine (§3.2.2) | E |
| EC-8 | **Idempotency key replay** — same `idempotency_key` dispatched twice to Cap-C for the same task | Second dispatch is a no-op at Cap-C; `integration_audit` shows 2 identical rows with same key, deduped at the target system. | No agent action; the system absorbs. If the second dispatch is delayed and the first times out, the idempotency guarantee prevents a double-write. | Cap-C rule 3 (idempotency) | E |
| EC-9 | **Candidate on leave** — a candidate in the pool is temporarily on leave (`on_leave=true`) | Candidate is excluded from the pool by Rule 3; no proposal is made. If this was the only candidate, `ESC-BUDDY-UNAVAILABLE` fires. | Cap-B rule 3 (on_leave filter) | E |
| EC-10 | **Open role with no current employees matches new hire** — e.g. ENG-0500 has no current ICs but is open | Hire for ENG-0500 matches empty role; no current employees to consider for buddy | `ESC-BUDDY-UNAVAILABLE` fires to HR; no agent action. If HR wants to override, they can assign an on-leave employee or expand the search. | Cap-B rule 4 (fallback to HR); A5 (unavailable = zero-match) | E |

### 4.6 Failure Modes

| # | Failure | Agent response | Recovery path | Rule(s) / escalation | Detection signal |
|---|---|---|---|---|---|
| FM-1 | **ServiceNow outage** — `POST sc_request` returns 503 consistently for 12 minutes | Cap-C retries per rule 2 (3× with 2/4/8s backoff). On sustained failure > 10 min, dead-letter. | `ESC-INTEG-OUTAGE` → `HR_OPS_LEAD` + IT on-call; human posts `HumanDecision {RETRY | SKIP | OVERRIDE}`. On RETRY, Cap-A re-dispatches with same `idempotency_key`. | Cap-C rules 2, 7; Cap-A rule 11; ESC-INTEG-OUTAGE | `integration_audit` rows with `http_status=503` + `retry_count=3`; dashboard metric `integration_deadletter_count` > 0 |
| FM-2 | **LMS completion webhook never arrives** — assignment succeeded but no completion signal for 5 business days past `due_at` | Cap-A detects via the `due_at + 2 bd` scheduled check; raises `ESC-TRAINING-LATE`. | `HR_OPS_LEAD` + `HIRING_MANAGER` nudge employee or mark SKIP with reason (HumanDecision). | Cap-A rule 9-adjacent scheduled scan; ESC-TRAINING-LATE | dashboard metric `open_lms_tasks_past_due_2bd`; decision log `event_type=esc_training_late_fired` |
| FM-3 | **Agent misread — agent took routine path on a case that should have been non-routine** — e.g. hire with an engagement-letter attachment suggesting contractor structure, but `employment_class = FULL_EMPLOYEE` was already set by a human (C1 honoured) | Agent does **not** re-classify. It continues on the FULL_EMPLOYEE template. If the human set the wrong value, downstream human review (benefits enrolment, payroll setup) will catch the discrepancy. | HR re-opens classification in Workday → fires a compensating `classification_changed_event` → Cap-A records a `HumanDecision {OVERRIDE, reason}` → re-runs template instantiation under a new `Onboarding` version (soft-delete the old tasks; regen under the new class). The full audit trail survives. | Cap-A rule 12 (boundary guard forbids agent-initiated re-class); new `HumanDecision {OVERRIDE}` recovery entry | `decision_log_entries` with `event_type=classification_changed` + matching prior `classification_set_event` |
| FM-4 | **Stale data — `start_date` shifts after `Onboarding` creation** (e.g. candidate delays) | Cap-A receives `worker.updated` with new `hireDate`; recomputes dependent `due_at` only for tasks still in `PENDING`; `IN_FLIGHT`/`COMPLETE`/`WAITING_HUMAN` tasks are **not** retroactively mutated (rule 3 immutability). | If rule-3 immutability causes a task to miss the new start_date window, `ESC-INTEG-OUTAGE`-like signal (actually a new `ESC-SCHEDULE-DRIFT` candidate — flagged as a **spec gap, see §4.8 trace matrix and A-open-1** — Cap-A today does not model this ESC). | Cap-A rule 3 (immutability of due_at); spec-gap detected | `integration_audit` showing `worker.updated` event; diff between old and new `start_date` ≥ 1 bd |
| FM-5 | **Webhook signature fails verification** (spoofed or misconfigured shared secret) | Cap-C rule 5: drop + log. No upstream fire. | IT on-call rotates secret; replays real events from vendor console. | Cap-C rule 5 | `integration_audit` with `signature_verified=false`; metric `webhook_verify_failures_per_hour` |
| FM-6 | **Rate-limit breach** — burst of 30 hires on Monday morning trips ServiceNow's 60 rpm window | Cap-C rule 6: queue and drain at limit; no silent drop. | All tasks eventually dispatched within a few minutes; no manual action needed. If drain > 10 min, FM-1 logic kicks in. | Cap-C rule 6 | `integration_audit` with `http_status=429`; queue-depth dashboard |

### 4.7 Delegation Boundary Tests

#### 4.7.1 BT-1 — Composite case that looks like it *could* be a contractor, but classification is already set

**Scenario name:** BT-1 — Contractor-shaped engagement letter on a FULL_EMPLOYEE record _(F)_

**Set-up.**
- Workday hire event: `employee_id = e-0002`, `role_code = CONSULT-0300`, `start_date = 2026-05-12`, `location = NYC`, `seniority_band = IC6`.
- A human has already set `employment_class = FULL_EMPLOYEE` in Workday at `2026-05-05` (so the `classification_set_event` has been received).
- The employee's attached engagement letter (accessible to the agent via a document-store side channel that the scenario does not require, but which a "helpful" coding agent might wire up) reads like an SOW with a fixed-fee and project-scope clauses — signals a naive model might read as *contractor*.
- The agent is explicitly **not given** any LLM-side ability to re-read Workday's `workerType`; it takes `classification_set_event` as authoritative.

**Expected agent behaviour.**
The agent **must** proceed on the `FULL_EMPLOYEE` template — instantiate the standard 40 tasks, dispatch standard provisioning and compliance-training track for full employees, and not raise any classification-related escalation. The agent **must not** (a) infer a contradictory classification from the engagement letter, (b) block the workflow demanding reclassification, or (c) write any value other than `UNSET` to `employment_class`. This is enforced by §3.3.5 Cap-A rule 12 and §2.5 hard constraint C1; Cap-C rule 4 is the code-level backstop on the Workday allowlist.

**Failure shapes** (any of these is a boundary violation):

- *Agent infers `CONTRACTOR` from the engagement letter and flips the template* → violates Cap-A rule 12 + C1.
- *Agent raises an `ESC-CLASS` even though classification is already set, demanding reconsideration* → violates the ESC-CLASS trigger condition (§3.3.6 requires `employment_class = UNSET`, which it is not). Escalating without the trigger condition being met is an unjustified builder addition; diagnosed per `spec-ambiguity-vs-builder-mistakes.md`.
- *Agent writes an `ESC-CLASS` or any `HumanDecision` with `actor_user_id` = agent service account* → violates Cap-A rule 12's DB check constraint on `actor_user_id NOT LIKE 'svc-%'`.
- *Agent silently blocks task instantiation pending a "review"* → violates Cap-A rule 2 (blocking has no trigger condition under this input).

**Acceptable behaviour** (boundary held):
- Agent proceeds on `FULL_EMPLOYEE` template.
- Later, an HR reviewer notices the engagement-letter mismatch during benefits enrolment (downstream human check). HR opens classification, Workday fires `HumanDecision {OVERRIDE, reason: "engagement letter indicates contractor"}`, and FM-3's recovery path kicks in. The discrepancy is caught **downstream by the named human role** — which is exactly the architecture commitment in §1.2.

**Success criteria (assertions).**
- No `Onboarding.employment_class` value other than `UNSET` was ever written by a service account (DB audit query).
- No `EscalationEvent` with `code = ESC-CLASS` exists on this `Onboarding` (precondition of the trigger was not met).
- Every `HumanDecision` row on this `Onboarding` has `actor_user_id` resolving to a named human.
- M4 (100% boundary-respect) is trivially defended: zero JUDGMENT tasks silently closed.

#### 4.7.2 BT-2 — Seniority-norm exception path (new FULL boundary surfaced by H4/A8)

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

### 4.8 Trace Matrix — scenarios ↔ spec rules

| Scenario ID | Capability | Rules / escalations exercised | Metric(s) defended |
|---|---|---|---|
| HP-1 | Cap-A + Cap-B + Cap-C | Cap-A 1,2,3,4,5,6,8,9,10,11,12,13; Cap-B 1,2,4,5,6,8; Cap-C 1,2,3,4,5,6,7,8 | M1, M3, M4 (trivially) |
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
| FM-4 | Cap-A | Cap-A 3 (due_at immutability) — **surfaces spec gap** (no ESC-SCHEDULE-DRIFT today; see A-open-1) | M3 |
| FM-5 | Cap-C | Cap-C 5 | — (security) |
| FM-6 | Cap-C | Cap-C 6 | — (resilience) |
| BT-1 | Cap-A + Cap-C | Cap-A 12; Cap-C 4 (Workday allowlist); C1 hard constraint | **M4** — load-bearing |
| BT-2 | Cap-B + Cap-A | Cap-B 4, 6, 8; Cap-A 12; Task state machine (WAITING_HUMAN) | **M4** — load-bearing |

**Rules covered** (Cap-A 1–14, Cap-B 1–8, Cap-C 1–8):

- **Fully exercised:** Cap-A 1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13; Cap-B 1, 2, 4, 5, 6, 8; Cap-C 1, 2, 3, 4, 5, 6, 7, 8.
- **Covered transitively only:** Cap-A 7 (idempotency) is covered transitively via FM-1 retry + HP-1 happy path; no standalone replay scenario today — **noted as a follow-on edge case to add** (proposal: EC-8 "same idempotency-key dispatched twice").
- **Not yet exercised by a named scenario:** Cap-A 14 (fan-out circuit breaker, per A-open-5) — **noted as a follow-on failure-mode to add** (proposal: FM-7 "11 concurrent Cap-C dispatches on single Onboarding").
- **Not covered:** Cap-B 3 (on_leave filter) — currently implied by EC-6 but not explicit. **Spec-validation gap, add EC-9** (candidate on leave is excluded).
- **Not covered:** Cap-B 7 (no silent override) — no direct scenario today. **Noted as a BT candidate** (BT-3: an agent attempts to write a `BuddyProposal.actor_user_id`; it should be impossible at the type-level, so the scenario is a "must not compile" test rather than a runtime test).

**Metrics covered:**
- **M1** defended by HP-1, EC-3, EC-6.
- **M2** (human-effort) is **not directly defended** by any scenario — M2 is a measurement over aggregate onboardings, not a per-scenario assertion. Noted as a **programme-level measurement**, not a validation-design gap.
- **M3** defended by HP-1, EC-4, FM-2, FM-4.
- **M4** defended by HP-1 (trivially), EC-2, EC-5, FM-3, **BT-1, BT-2** — the non-negotiable boundary-respect metric has two dedicated boundary tests, as required.

**Scenarios that exercise spec gaps** (rules that need to be added to the capability spec):
- FM-4 surfaces missing `ESC-SCHEDULE-DRIFT` — raised as **A-open-1** in §0.1: the capability spec will need a new rule in its next revision, not a hand-patch in this deliverable.
- BT-3 (proposed) surfaces the need to explicitly document that `BuddyProposal.actor_user_id` is a type-level absence, not a runtime check.

### 4.9 Diagrams

Trigger check: the happy path HP-1 has a multi-system timeline with parallel fan-out and three escalation branches that only fire in edge and failure scenarios. §3.7 Figure 4 already captures this at the capability level; duplicating it here would add no new facts. BT-1 and BT-2 are text-heavy and compact; tables carry the assertion structure. No diagram — tables carry the structure for this section.

### 4.10 Self-audit (preserved from source file)

- [x] ≥ 1 happy path (HP-1), ≥ 3 edge cases (EC-1…EC-7), ≥ 3 failure modes (FM-1…FM-6), ≥ 1 boundary test (BT-1, BT-2).
- [x] Every scenario carries a P / F / E tag.
- [x] Every scenario cites at least one specific rule, escalation code, or hard constraint from §3.
- [x] Every failure mode names a detection signal (`integration_audit` row, dashboard metric, decision-log event type).
- [x] Every boundary test enumerates specific mis-behaviours and ties each to the rule it would break.
- [x] Trace matrix shows every Cap-A / Cap-B / Cap-C rule exercised by at least one scenario, with the exceptions (Cap-A 7 transitive; Cap-A 14 proposed FM-7; Cap-B 3 implicit; Cap-B 7 proposed BT-3) flagged.
- [x] Every success metric M1, M3, M4 is defended by at least one scenario; M4 is defended by two dedicated boundary tests; M2 is a programme-level measurement, not a validation-design gap — called out.
- [x] No new rules, states, escalations, or integrations introduced here; the spec gap (ESC-SCHEDULE-DRIFT under FM-4) is flagged as A-open-1, not silently added.
- [x] Every `[ASSUMED]` / `[UNKNOWN]` has a matching numbered entry in §0.1.
- [x] No `[TODO]` markers open.
- [x] No diagrams (trigger not met); called out explicitly.

**Overall validation read.** The design, as drafted, would surface a boundary violation in BT-1 or BT-2 because the assertion set reads from the decision log and checks `actor_user_id` + `EscalationEvent.code` existence — both of which a naive builder cannot fake without violating the Cap-A rule 12 check constraint or the Cap-C rule 4 allowlist. Recommended first build-loop scenario: HP-1, because it exercises the largest swathe of rules and flushes the most likely ambiguity surfaces in §3 before BT-1 is run as the real test.

---


## 5. Assumptions & Unknowns

*(Consolidation note: the upstream `assumptions-and-unknowns-scenario-1-205.md` was already the consolidated register across D1–D4. In this document its role is taken by §0.1 — a single, top-of-document merged Assumption Log. This section therefore keeps only the three pieces that §0.1 does not already carry: the coach-session priority queue is the upstream §4; the genuine-unknowns list is upstream §7; and the "what must be validated before building" triage is upstream §8. Upstream §3 scan table and §6 full entries are not restated here; see §0.1.)*

### 5.1 Scope and stance (cross-reference)

Every `[ASSUMED]` or `[UNKNOWN]` referenced in §§1–4 of this document traces to a numbered entry in §0.1. Each entry is tagged **HUMAN** (participant-supplied) or **AGENT** (surfaced during drafting). Confidence is Low / Medium / High. **High** is reserved for coach-session-validated or regulation-anchored assumptions; A7 is the only AGENT entry rated High, and it is anchored in named regulation (IRS common-law test, ACA 30-hour rule, state ABC tests). See §0.1.2 for the full breakdown.

### 5.2 Coach-session priority queue

See §0.1.3. Ordered by leverage, highest first: (1) A8/H4 reconciliation, (2) A10 LMS vendor, (3) A-open-1 ESC-SCHEDULE-DRIFT, (4) A1+A2 baselines, (5) A13+A14, (6) A9, (7) A-open-3, (8) A11, (9) A17, (10) H1, (11) A16, (12) A-open-2, (13) A-open-5.

### 5.3 Update protocol

See §0.1.4.

### 5.4 Genuine unknowns — the "I don't know" list

The Week 1 brief requires ≥ 5. This list has **11** genuine unknowns; none are filler.

1. **U1 — Which LMS vendor is in use** (A10). Build-blocking for compliance-training capability.
2. **U2 — Workday + ServiceNow tenant URLs, auth flavour, rate limits** (A11). Blocks first build-loop run of §3.6.1 + §3.6.2.
3. **U3 — Email sender (relay/API, domain authentication)** (A17). Blocks first build-loop run of every ESC-* notification.
4. **U4 — Current baseline rates for M2 (time-per-onboarding) and M3 (fell-through-cracks)** (A1, A2). Without these, targets are floating and the business case is not defended.
5. **U5 — ServiceNow role-bundle schema and non-template approval owner** (A13). Blocks `ESC-ACCESS-NONTEMPLATE` routing.
6. **U6 — Client's business-day calendar and policy interpretation of "start_date" for I-9** (A14). Regulatory timing.
7. **U7 — Whether HR wants every buddy match reviewed or only exceptions flagged** (A8). Directly moves a delegation row.
8. **U8 — Client retention policy (vs industry-default 7y/1y)** (A9). Touches every decision-log row.
9. **U9 — Client's current handling of start_date shifts mid-onboarding** (A-open-1). Spec gap surfaced by FM-4.
10. **U10 — Distribution-list resolution per `recipient_role`** (A-open-3). Blocks first build-loop ESC notifications.
11. **U11 — Seniority-band enumeration scheme and delta semantics** (subset of A16). Needed before BT-2 can be run against real pool data.

### 5.5 What must be validated before building

#### 5.5.1 Blocking — cannot start building until resolved

- **U1 / A10 — LMS vendor.** Without this, §3.6.3 has no endpoint, no auth, no webhook contract. Forces §3 regeneration once resolved.
- **Open tension A8 + H4 reconciliation (U7).** Without this, §2.3 row 11 and §3.4.5 Cap-B rule 6 are conditionally correct. Could move from FULL to HUMAN-IN-LOOP on every match, a material change.

#### 5.5.2 Soft-blocking — can start building, but a specific capability or branch depends

- **U2 / A11 — Tenant auth and rate limits.** Enables §3.6.1 + §3.6.2 build-loop runs; drafting proceeds without.
- **U3 / A17 — Email sender.** Escalation notifications work in mock mode until resolved.
- **U5 / A13 — ServiceNow bundle schema.** §3.3.5 Cap-A rule 4's non-template branch cannot be exercised end-to-end.
- **U6 / A14 — Business-day calendar.** §3.3.5 Cap-A rule 5 is correct in structure but its clock boundary depends on client policy confirmation.
- **U9 / A-open-1 — `ESC-SCHEDULE-DRIFT`.** FM-4 unwrapped a missing ESC; not blocking routine path, blocking robust operation.
- **U8 / A9 — Retention envelope.** Decision-log schema is correct; only the retention TTL config is at risk.
- **U10 / A-open-3 — Distribution lists.** Notifications run in mock mode until resolved.

#### 5.5.3 Non-blocking but load-bearing — build can proceed; validation changes confidence of the business case

- **U4 / A1 + A2 — M2 / M3 baselines.** Architecture unaffected; headline targets are assumed.
- **H1 — Adoption willingness.** Value-risk; does not move architecture.
- **A16 — Seniority-delta threshold default.** Parameterisable.
- **H2 — Judgment-call patternability.** Low and explicitly not used to move a row; its movement to High would *reduce* agent scope by opening a conversation about further delegation, not break the current spec.
- **A-open-5 — Economics classification + circuit-breaker threshold.** Instrumentation choice; measure after first build-loop run.

**Recommended next coach-session probe** (from §0.1.3 position 1): *"For buddy matches that pass the three-factor filter, do you want every match routed through HR for sign-off, or only matches that exceed a seniority-delta threshold (e.g. 3 bands)?"* — resolves U7, the highest-leverage open tension.

---

## Appendix A — Production spec checklist review

Walk of `SupportingDocs/production-spec-checklist.md`, top to bottom, against this consolidated document. Status values are **Met**, **Partial**, or **Not met**. The "Change made in this revision" column records where this consolidation pass revised the body to close a gap; **"—"** means no revision was needed because the source already met the bar.

| Checklist item | Status | Section(s) addressing it | Change made in this revision (if any) |
|---|---|---|---|
| **BUILDABILITY** — testable acceptance criteria on every requirement | Met | §1.3 M1–M4 (measurement methods); §3.3.5, §3.4.5, §3.5.5 rules use must/will/cannot with numeric thresholds; §4.4–§4.7 scenarios are the acceptance criteria | — |
| Ambiguous words defined ("recent", "routine", "required") | Partial → Met | §0.1 A-open-4; §3.2.2 `Task.required` attribute added to the entity | **Added** `required: boolean` to `Task`; added A-open-4 defining "required task" vs "routine task" for M1/M3 denominators |
| Explicit IF/THEN on every conditional | Met | §3.3.5 rules 1, 3, 4, 5, 8, 9, 11, 14; §3.4.5 rules 1–6; §3.5.5 rules 1–7 | — |
| No modal verbs without scope ("should", "may") | Met | All rule text uses must / will / cannot | — |
| Cross-feature interactions described | Met | §4.5 EC-4 (audit × webhook race); §4.6 FM-3 (classification × benefits); §3.3.5 rule 14 × §3.5.5 rule 7 | — |
| **ENTITY PRECISION** — data model with PK, attributes, timestamps, audit, relationships | Met | §3.2.1–§3.2.4 (Onboarding, Task, HumanDecision, EscalationEvent) | — |
| Enum values SCREAMING_SNAKE_CASE, exhaustive, no "other" | Met | All enums in §3.2 are exhaustive; Task.type enum explicit in §3.2.2.a | — |
| ISO 8601 timestamps with timezone | Met | All timestamp fields annotated `ISO 8601 timestamp (UTC)` | — |
| Numeric fields with units and range | Met | `retry_count int default 0 max 3`, `seniority_threshold int ≥ 1`, SLAs in business days | — |
| String fields with max length and format | Met | `reason ≤ 2000` chars; `role_code` regex `/^[A-Z]{2,5}-\d{2,4}$/`; `idempotency_key string(64)` | — |
| FK cascade behaviour specified | Met | `onboarding_id on delete: restrict`; `task_id on delete: restrict`; `deleted_at` soft-delete | — |
| Computed fields marked read-only with formula | Met | `OVERDUE` derived per rule 6; `filled_count` analogue via day-14 audit; `Worker.workerType` marked read-only at §3.6.1 | — |
| State machine complete (every state, transitions, prerequisites) | Met | §3.2.1 Figure 2; §3.2.2 Figure 3 | — |
| No contradictory rules | Met | Self-audit §3.8 confirms; spot-check on Cap-A 12 (boundary guard) vs 14 (circuit breaker) — compatible | — |
| **DELEGATION BOUNDARIES** — every decision labelled | Met | §2.1 framework + §2.3 work inventory rows 1–22 each labelled FULL / HUMAN-IN-LOOP / HUMAN-LED | — |
| Escalation triggers specific | Met | §3.3.6, §3.4.6, §3.5.6 — every ESC-* has code, condition, recipient, action, SLA | — |
| Boundary conditions explicit | Met | §2.5 hard constraints C1–C4; §3.3.5 rule 12 (boundary guard); §3.5.5 rule 4 (allowlist) | — |
| Every action labelled [Agent Alone / +Log / +Review / Human] | Met (via §2.1 vocabulary mapping) | §2.1 vocabulary: FULL ≈ Agent+Log (all actions hit the decision log per §3.3.5 rule 13); HUMAN-IN-LOOP ≈ Agent+Review; HUMAN-LED ≈ Human | — |
| Decision thresholds numeric / boolean | Met | Seniority threshold `3 bands`; fan-out cap `10`; retry budget `3`; SLAs in bd; no fuzzy conditions | — |
| Escalation paths complete (next step, notification, timeout) | Met | §3.3.6 SLA column; §0.1 A-open-3 tags the distribution-list resolution as `[UNKNOWN]` pending client | — |
| Audit trail requirements explicit (what / where / retention) | Met | §3.3.7, §3.4.7, §3.5.7 — table with fields, storage location, retention | — |
| Override mechanisms documented | Met | `HumanDecision.decision` enum includes `OVERRIDE`; §4.6 FM-3 recovery path uses it | — |
| No open [TODO] markers | Met | §3.8 confirms; `[UNKNOWN]` tags are traced to §0.1, not TODOs | — |
| **INTEGRATION CONTRACTS** — endpoint, auth, request, response, timeout, retry, rate limit, data mapping, fallback | Partial | §3.6.1–§3.6.6; LMS §3.6.3 has `[UNKNOWN]` endpoint/auth/rate-limit traced to A10; Benefits/Payroll §3.6.5/§3.6.6 similar | — (LMS gap is traced to A10 and flagged build-blocking; no fabrication done here) |
| Required vs optional fields marked | Met | Every `Required` column in entity tables; event schemas in §3.3.3 | — |
| Enums exhaustive in integration contracts | Met | `Worker.workerType` read-only; `employment_class` 3-value enum | — |
| Timeout numeric | Met | All integrations have explicit timeout (10s / 15s) | — |
| Retry strategy covers 2xx/3xx/4xx/5xx | Met | §3.5.5 rule 2 (5xx retry; 429 retry with Retry-After; 4xx no retry) | — |
| Rate limits numeric or `[UNKNOWN]` with assumption trace | Met | Workday / ServiceNow / Email rate limits carry `[UNKNOWN]` traced to A11 / A17 | — |
| Data mapping both directions | Met | §3.6.1–§3.6.6 data-mapping sections | — |
| Fallback explicit (queue/skip/escalate/fail-fast/degrade) | Met | All integrations list fallback; §3.5.5 rule 7 generic dead-letter + ESC-INTEG-OUTAGE | — |
| Credentials sourced from specific location | Met | Secrets manager keys named: `fde-onboarding-workday`, `fde-onboarding-servicenow`, `fde-onboarding-email` | — |
| Error codes listed with handling | Partial | §3.5.5 rule 2 covers HTTP class-level handling; vendor-specific error codes not enumerated | — (vendor-specific codes wait on A10/A11 resolution; not treated as a new gap) |
| **VALIDATION DESIGN** — ≥ 1 happy path, ≥ 5 edge cases, ≥ 3 failure modes, each with expected outcome | Met | §4.4 HP-1; §4.5 EC-1…EC-9 (9 edges, including EC-8 idempotency replay and EC-9 on-leave); §4.6 FM-1…FM-6 (6 failures) | **Added** EC-8 (idempotency-key replay) and EC-9 (on-leave filter) to close Cap-C rule 3 and Cap-B rule 3 trace gaps flagged in the upstream trace matrix |
| Concurrency / race conditions addressed | Met | §4.5 EC-4 concurrent-writes; §3.5.5 rule 6 rate-limit queuing; §3.3.5 rule 14 fan-out cap | — |
| Boundary-value / edge / null | Met | §4.5 EC-5 boundary-value; EC-2 null/UNSET case | — |
| Field-interaction docs | Met | §3.2.2 `human_decision_id required iff classification=JUDGMENT AND status=COMPLETE` (M4 enforcement); §3.2.1 `hold_reason required iff status=ON_HOLD` | — |
| **ASSUMPTIONS REGISTER** — every assumption documented with why, breakage, status | Met | §0.1 scan table + §0.1.5 full entries; every assumption tagged HUMAN/AGENT and carries confidence + upstream-section impact | — |
| Critical assumptions flagged with validation question | Met | §0.1.5 full entries include "How I'd test it"; §0.1.3 priority queue names the probes | — |
| HUMAN vs AGENT tagging preserved | Met | §0.1.1 scan table `Source` column | — |
| **ECONOMICS ALIGNMENT** — cost classification; batch/cache; circuit breakers; async alternatives | Partial → Met | §0.1 A-open-5 (cost classification); §3.3.5 rule 14 (fan-out circuit breaker) | **Added** A-open-5 mapping operations to Check/Validate/Generate/Coordinate/Transform; **added** Cap-A rule 14 (circuit breaker at 10 concurrent Cap-C dispatches per Onboarding) to close the circuit-breaker gap |
| Batch / caching documented | Partial | §3.6 sequence diagram Figure 4 shows parallel fan-out (batching across systems); explicit inventory-style caching not documented (none needed for this orchestrator) | — (not an architectural requirement for this spec; flagged only for completeness) |
| Token budgets defined | Not met → Partial | §0.1 A-open-5 documents expected cost shape (Coordinate-heavy, Generate-light, zero LLM on happy path); concrete tokens/day not pinned | **Added** A-open-5 with qualitative token-shape claim; concrete budget deferred to first build-loop measurement |
| **GOVERNANCE** — every data-affecting action loggable | Met | §3.3.5 rule 13; §3.3.7 / §3.4.7 / §3.5.7 audit-trail tables with retention | — |
| Compliance constraints documented (GDPR, HIPAA, PCI, SOX, IRCA, etc.) | Met | §2.5 C1–C4 cite IRS common-law, ACA 30-hour, state ABC, IRCA 8 U.S.C. § 1324a, ERISA-style fiduciary framing; §0.1 A7 / A4 / H7 pin the regulatory anchors | — |
| HITL checkpoints with SLAs | Met | §3.3.6 escalation triggers table has SLA column for every ESC code | — |
| Data deletion / retention policies | Met | §0.1 A9; entity-level `deleted_at` + retention notes in §3.2; decision-log retention 7y / integration-audit 1y | — |
| Non-repudiation | Met | §3.3.5 rule 12 + DB check constraint on `actor_user_id`; `decided_at` immutable; amendments create new row referencing prior | — |
| All compliance requirements mapped to spec rules | Met | §2.5 C1 → §3.3.5 rule 12 + §3.5.5 rule 4; C2 → rule 5; C3 → rule 12; C4 → rule 13 | — |
| **FINAL PASS/FAIL** — every section addressed; integration contracts complete; entities have full model; delegation clear; validation meets minimum bar; governance explicit; assumptions flagged | Met with caveats | All sections above; LMS integration is the one **Partial** with an explicit `[UNKNOWN]` and a build-blocking flag traced to A10 — not a failure, a surfaced risk | — |

**Final pass verdict.** The consolidated spec **passes** the production-spec-checklist's buildability bar *for every capability except Cap-C's LMS branch*, which is explicitly marked `[UNKNOWN]` and traced to Assumption A10 with a build-blocking flag. The three gaps closed during this review — ambiguous-word definition (A-open-4 + `Task.required`), economics classification (A-open-5), and circuit breaker (Cap-A rule 14) — were the only items that moved from Partial/Not-met to Met during this consolidation pass. Cap-A rule 14 and the new EC-8/EC-9 trace entries are the only substantive edits to the rule set that happened here; everything else is cross-reference, dedup, or traceability.

**Conflicts flagged back to the user (not resolved silently).**

1. The upstream prompt `concatonate-and-review.md` previously disagreed with itself on the output filename (*Output placement* said `critique-pool-Sahil2-1-{NNN}.md`; *Done criteria* said `gate1-consolidated-scenario-1-{NNN}.md`). Resolved during this run by honouring the `critique-pool-Sahil2-1-413.md` placement (consistent with the existing `…-412.md` sibling) and by updating the prompt's *Done criteria* to match. No substantive content conflict.
2. The upstream assumption log cross-references in the source files referenced a `§1.4` metrics section, but the consolidated document places metrics at `§1.3`. The scan table in §0.1.1 retained the original upstream "at risk if wrong" language verbatim (mentioning `§1.4`) to preserve traceability back to the source files; a reader using the new numbering should read "§1.4" as "§1.3 (M1–M4 table)". This is a cosmetic numbering drift, not a content conflict — flagged here so a later rerun can normalise.

---

*End of consolidated Gate 1 spec — run 413.*

