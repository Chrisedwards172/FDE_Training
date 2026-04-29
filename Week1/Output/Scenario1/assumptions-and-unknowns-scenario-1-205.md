# Assumptions & Unknowns — Scenario 1 (HR Onboarding Coordination)

## Front-matter

- **Submission ID:** `assumptions-and-unknowns-scenario-1-205`
- **Source scenario:** [`../../scenario-1.md`](../../scenario-1.md)
- **Upstream deliverables consolidated:**
  - [`./problem-statement-scenario-1-201.md`](./problem-statement-scenario-1-201.md) (entries H1, H2, H7, A1, A2, A3, A4)
  - [`./delegation-analysis-scenario-1-202.md`](./delegation-analysis-scenario-1-202.md) (entries H4, H5, H6, A5, A6, A7, A8, A9)
  - [`./capability-specification-scenario-1-203.md`](./capability-specification-scenario-1-203.md) (entries A10, A11, A12, A13, A14, A15, A16, A17)
  - [`./validation-design-scenario-1-204.md`](./validation-design-scenario-1-204.md) (entries V1, V2, V3, V4, V5)
- **Date produced:** 24.04.2026
- **Status:** First draft, pre-coach-session for this consolidated register. H4, H5, H6 carry **High** (coach-validated per scenario file); every AGENT entry is **Medium** or **Low** until a dated coach-session note raises it — per `CLAUDE.md`, no AGENT entry is rated High without validation.

---

## 2. Scope and stance

This deliverable is the **single consolidated assumption register** for Scenario 1. Every `[ASSUMED]` or `[UNKNOWN]` referenced anywhere in Deliverables 1–4 traces to a numbered entry below. Each entry is tagged **HUMAN** (participant-supplied, lifted from the scenario file) or **AGENT** (surfaced during drafting of Deliverables 1–4).

Confidence is **Low / Medium / High**. Per `CLAUDE.md` § *Prompt Authoring Conventions*, **High** is reserved for coach-session-validated assumptions. An AGENT entry rated High without a dated coach-session note would be a red flag per the primer's anti-pattern *"confusing 'I decided' with 'I validated'."* The only exception permitted here is **A7**, which is rated High because it is anchored in *named regulation* (IRS common-law test, ACA 30-hour rule, state ABC tests) rather than in coach consensus — regulation is as-settled-as-coach-validation for boundary purposes.

---

## 3. Scan table

| # | Source | Assumption (one line) | Cagan risk | Confidence | Upstream sections at risk if wrong |
|---|---|---|---|---|---|
| H1 | HUMAN | HR Ops will adopt an agent for onboarding coordination | Value / Viability | Medium | D1 §4, §5 (business case); D2 §4 rows depending on access follow-through |
| H2 | HUMAN | 15% judgment calls follow identifiable patterns | Feasibility | Low | D1 M1 target; D2 row 3 (explicitly **not** relied on); D3 Cap-B rule set |
| H3 | HUMAN | Existing systems expose APIs or integration points | Feasibility | Medium | D3 §6 (all integrations); D2 row 21 |
| H4 | HUMAN | Buddy three-factor filter + one-buddy + tie-break dept→loc→sen→random + HR escalation on unavailable | Feasibility | **High (coach-validated)** | D2 rows 10, 11, 13; D3 Cap-B rules 1–6; D4 HP-1, EC-6, BT-2 |
| H5 | HUMAN | Unnamed 2 of 6 systems = Benefits + Payroll/Time | Feasibility | **High (coach-validated)** | D2 rows 6, 21; D3 §6.5, §6.6 |
| H6 | HUMAN | HR Ops will grant integration access | Viability | **High (coach-validated)** | D2 rows 4–22 (all FULL rows); D3 §6 (all integrations) |
| H7 | HUMAN | "Late I-9 triggers a hold" is a regulatory hold with legal exposure | Viability | Medium | D1 M4 wording; D2 row 19, C2; D3 Cap-A rule 5; D4 EC-5, FM-3 |
| A1 | AGENT | Baseline "fell-through-the-cracks" rate is retrievable from HR Ops records | Value | Low | D1 M3 Current State; D4 V1; defence of M3 target |
| A2 | AGENT | Current time-per-onboarding (M2 baseline) is retrievable | Value | Low | D1 M2 Current State |
| A3 | AGENT | Scenario's "15%" refers to 15% of ~40 tasks (≈ 6/hire), not 15% of onboardings | Feasibility | Medium | D1 §3 derivation; D1 M1 denominator; D2 row 2; D3 Cap-A rule 2 |
| A4 | AGENT | I-9 3-business-day deadline (IRCA 8 U.S.C. § 1324a) from `start_date` | Viability | Medium (regulation settled; client-specific "business day" definition the variable part) | D2 C2; D3 Cap-A rule 5, A14 |
| A5 | AGENT | Buddy "unavailable" = zero-match of unencumbered pool; leave + capacity pre-filtered | Feasibility | Medium | D2 row 13; D3 Cap-B rules 2, 3, 4; D4 ESC-BUDDY-UNAVAILABLE semantics |
| A6 | AGENT | Tie-break order dept → location → seniority → random, seeded RNG | Feasibility | Medium | D3 Cap-B rule 5; D4 HP-1 determinism |
| A7 | AGENT | Classification is HUMAN-LED regardless of signal strength | Viability | **High (regulation-anchored — see note above)** | D2 row 3, C1; D3 Cap-A rule 12, Cap-C rule 4; D4 BT-1 |
| A8 | AGENT | Seniority-norm flag is a post-filter HUMAN-IN-LOOP exception, not a 4th filter factor | Feasibility | Medium | D2 row 12; D3 Cap-B rule 6; D4 BT-2 |
| A9 | AGENT | Retention: 7y employment, 1y integration audit | Viability | Medium | D2 C4; D3 §4 entity delete behaviour; D3 §5.1.7, §5.3.7 |
| A10 | AGENT | LMS vendor + API + webhook contract **[UNKNOWN]** | Feasibility | Low / **Build-blocking** | D3 §6.3; D4 FM-2, V3 |
| A11 | AGENT | Workday + ServiceNow OAuth2 client-credentials auth with service-account creds | Feasibility | Medium | D3 §6.1, §6.2 |
| A12 | AGENT | Idempotency key = `sha256("{onboarding_id}:{task_id}:{system}:{action}")` | Feasibility | Medium | D3 Cap-A rule 7; Cap-C rule 3 |
| A13 | AGENT | ServiceNow role-bundle CI schema; non-template = ESC-ACCESS-NONTEMPLATE | Feasibility | Medium | D3 Cap-A rule 4; ESC-ACCESS-NONTEMPLATE; D4 EC-3 |
| A14 | AGENT | Business-day calendar = Mon–Fri − US federal holidays; clock from `start_date` | Viability | Medium | D3 Cap-A rule 5; D4 EC-5 |
| A15 | AGENT | Day-14 = audit milestone; Day-10 = handoff nag | Feasibility | Medium | D3 Cap-A rules 8, 9; D4 HP-1 timeline |
| A16 | AGENT | Seniority-delta threshold default = 3 bands, configurable | Feasibility | Low | D3 Cap-B rule 6; D4 BT-2 |
| A17 | AGENT | Email sender is a named relay with DKIM/SPF; specific vendor **[UNKNOWN]** | Feasibility | Medium | D3 §6.4 |
| V1 | AGENT | Baseline "fell-through-the-cracks" rate is retrievable for pre/post comparison (operational duplicate of A1 from the validation angle — consolidated under A1) | Value | Low | merged with A1 |
| V2 | AGENT | Synthetic test harness can reproduce production distributions for role / location / seniority | Feasibility | Medium | D4 all test data |
| V3 | AGENT | LMS webhook includes `lms_assignment_id` + `completed_at` (dependent on A10) | Feasibility | Low | D4 FM-2 (merged downstream of A10) |
| V4 | AGENT | Ground truth for BT-1 is the HR reviewer's eventual decision, not a test-author inference | Value / Viability | Medium | D4 BT-1 |
| V5 | AGENT | Seniority threshold is parameterisable for BT-2 runs | Feasibility | Medium | D4 BT-2 |
| A-open-1 | AGENT | Capability spec does not yet model `ESC-SCHEDULE-DRIFT` for `start_date` changes post-creation — surfaces as a **spec gap** in D4 FM-4 | Feasibility | **Build-blocking for FM-4** | D3 Cap-A (new rule + ESC needed); D4 FM-4 |

### Overall read
- **Total entries:** 25 unique (V1 consolidated into A1; V3 tracked as dependency of A10).
- **HUMAN vs AGENT:** 7 HUMAN (H1–H7); 18 AGENT (A1–A17 + V2, V4, V5 + A-open-1; A-open-1 is a spec-gap-surfacing AGENT entry).
- **Confidence split:** 3 High (H4, H5, H6 coach-validated) + 1 High-by-regulation (A7) = 4 High. Medium: 14. Low: 7 (H2, A1, A2, A10, A16, V1→A1, V3).
- **Open tensions:** 2 — (a) **H4 vs scenario text**: scenario names buddy seniority-norm as a judgment call; H4 coach-validated as fully auto-assign. Resolved in this spec by surfacing **A8** (post-filter exception → HUMAN-IN-LOOP), rather than silently picking a side. (b) **H2 vs scenario text**: scenario quote "edge cases never look the same twice" contradicts H2's patternability claim. Resolved by **not using H2** to move any row into FULL delegation; the classification, seniority-norm, and I-9 rows stay HUMAN-LED on scenario text + regulation, not on H2.
- No AGENT entry is rated High without a dated coach-session note except **A7**, which is regulation-anchored. Flag preserved for transparency.

---

## 4. Coach-session priority queue

In order, highest leverage first:

1. **Open tension A8 (seniority-norm path) + H4 reconciliation.** Resolution moves D2 row 11 (buddy final-assign) and Cap-B rule 6 materially. If HR confirms every match should be HR-reviewed, the row becomes HUMAN-IN-LOOP by default; if HR confirms only exceptions, the current spec stands.
2. **A10 — LMS vendor identity.** Build-blocking for D3 §6.3 and D4 FM-2; webhook contract cannot be specified without it. The top probe: *"Which LMS vendor and edition is in use? Share admin console URL and API docs."*
3. **A-open-1 — `ESC-SCHEDULE-DRIFT`.** Spec-gap surfaced by FM-4; requires a new rule in Cap-A on the next regeneration of the capability spec. Ask HR Ops how they currently handle a `start_date` shift mid-onboarding so the ESC wording matches the existing workflow.
4. **A1 + A2 — Baselines for M2 and M3.** Without baselines, the business case in D1 is not defended; targets are assumed, not grounded.
5. **A13 — ServiceNow bundle structure** and **A14 — business-day calendar.** Both touch regulatory timing (I-9) and the most common ESC (ACCESS-NONTEMPLATE).
6. **A9 — Retention envelope.** 7y / 1y is industry default, but client policy may tighten it. Affects every decision-log row.
7. **A11 — Tenant auth flavours.** Required for build-loop run 1 of D3 §6.1 and §6.2; does not block drafting.
8. **A17 — Email sender identity.** Same: blocks only first build-loop run.
9. **H1 — Adoption willingness.** Already Medium; Value-risk probe, not an architecture-mover.
10. **A16 — Seniority-delta threshold default.** Low leverage; parameterisable.

This is the scarce-interview-slot plan for the next coach session per the primer: show up with a prioritised list, not open-ended chat.

---

## 5. Update protocol

> After each coach session, update the affected entry **in place**: raise or lower confidence, add a dated note, and change any dependent spec prose in the upstream deliverables.
>
> **Do not silently delete an assumption.** If an assumption is refuted, leave it with strikethrough and add a new numbered entry pointing at the replacement. If an assumption no longer traces to a HUMAN anchor (e.g. because a HUMAN assumption was refined and its operational details were lifted to new AGENT entries), retire with strikethrough and a footnote — do not delete.
>
> `[ASSUMED]` items do not migrate to a new source tag after a coach session. The original entry carries a dated confirmation note; the `[ASSUMED]` tag remains so the audit trail is preserved for Friday peer review.

---

## 6. Full entries

Full Assumption/Hypothesis/Test/Confidence entries for **H1–H7** are in [`../../scenario-1.md`](../../scenario-1.md) § *HUMAN Assumptions* and are not restated here; confidence ratings below reflect the scenario file as of 24.04.2026. AGENT entries A1–A17 are restated from the upstream deliverables with no new invention. **V1 is merged into A1**; **V3 is tracked under A10 as a dependency**.

### H1 — HR Ops adoption willingness (HUMAN — Medium)
*See `scenario-1.md` §HUMAN Assumptions #1.* Confidence carried: Medium. Next probe in queue position 9.

### H2 — Judgment-call patternability (HUMAN — Low)
*See `scenario-1.md` #2.* **Explicitly not used** to move any row from HUMAN-LED to FULL in D2. Retained in this register so that if a future coach session raises it, the dependent rules can be re-evaluated deliberately rather than by drift.

### H3 — Systems expose APIs (HUMAN — Medium)
*See `scenario-1.md` #3.* Specifics per-system tracked under A10, A11, A17.

### H4 — Buddy three-factor filter (HUMAN — High, coach-validated)
*See `scenario-1.md` #4.* High on the three-factor model + HR-on-empty escalation rule. Operational details carried under A5, A6, A8 per the scenario-file's own note that those probes are build-blocking but not confidence-blocking.

### H5 — Unnamed systems = Benefits + Payroll/Time (HUMAN — High)
*See `scenario-1.md` #5.*

### H6 — HR Ops willingness to grant access (HUMAN — High)
*See `scenario-1.md` #6.* Named-owner-per-system still needs surfacing; tracked under A11 + A10 + A17.

### H7 — Late I-9 is regulatory (HUMAN — Medium)
*See `scenario-1.md` #7.* Regulatory anchor per A4 is settled; the Medium reflects client-specific "hold" procedure semantics, not the existence of the regulation.

### A1 — Baseline "fell-through-the-cracks" rate retrievability (AGENT — Low)
- **Assumption:** HR Ops can retrieve the count of onboardings with ≥ 1 incomplete required task at day 14 from existing records.
- **Hypothesis:** If they can, M3's Current State column can be filled and the target is defendable. If not, the target is floating.
- **How I'd test it:** *"Can you run a report showing, for the last 100 onboardings, how many had any open required task at day 14?"*
- **Confidence:** Low — the stakeholder quote "something falls through the cracks" is qualitative, not measured.

### A2 — Current time-per-onboarding retrievability (AGENT — Low)
- **Assumption:** HR Ops can produce or estimate minutes-per-onboarding end-to-end for the 3-person team.
- **Hypothesis:** An estimate with ± 20% band is sufficient for the M2 baseline.
- **How I'd test it:** *"What's the current average time your team spends per onboarding, and how was that number produced?"*
- **Confidence:** Low.

### A3 — 15% refers to tasks, not onboardings (AGENT — Medium)
- **Assumption:** Scenario's "roughly 15% require judgment calls" applies to tasks (~6 per hire), not to onboardings (would be ~33 fully-judgment onboardings/year).
- **Hypothesis:** The three scenario-named examples (classification, buddy norm, late I-9) are task-level, which supports the reading.
- **How I'd test it:** Confirm denominator with HR Ops lead.
- **Confidence:** Medium.

### A4 — I-9 deadline semantics (AGENT — Medium)
- **Assumption:** "Late I-9" means Section 2 not completed within 3 business days of start_date per IRCA 8 U.S.C. § 1324a.
- **Hypothesis:** If so, agent's role is reminder + escalate, never hold decision.
- **How I'd test it:** Client's written I-9 procedure + IRCA text cross-check.
- **Confidence:** Medium.

### A5 — Buddy "unavailable" sub-cases (AGENT — Medium)
- **Assumption:** ESC-BUDDY-UNAVAILABLE fires only on zero-match of pool filtered for capacity (`current_buddy_count=0`) and leave (`on_leave=false`).
- **Hypothesis:** Filter subsumes these as exclusions rather than separate escalations.
- **How I'd test it:** *"When HR takes over buddy assignment today, do they work from a pool with leave + capacity pre-filtered?"*
- **Confidence:** Medium.

### A6 — Tie-break order (AGENT — Medium)
- **Assumption:** dept → location → seniority → random; deterministic via seeded RNG on `Onboarding.id`.
- **Hypothesis:** Deterministic ordering is necessary for audit and replay.
- **How I'd test it:** Confirm priority order + acceptance of deterministic random.
- **Confidence:** Medium.

### A7 — Classification is HUMAN-LED (AGENT — High, regulation-anchored)
- **Assumption:** `employment_class` is never agent-inferred; agent does not branch on signals.
- **Hypothesis:** IRS common-law test, ACA 30-hour rule, state ABC tests all put classification squarely in human judgment; an agent-synthesised classification is an irreversible compliance exposure.
- **How I'd test it:** Not testable; regulation is the source. Named-human owner in the client's org is a *separate* confirmation (still needed) — tracked here as part of A7's outstanding sub-probe.
- **Confidence:** High on the boundary itself; named-human ownership sub-probe still Medium.

### A8 — Seniority-norm is post-filter exception (AGENT — Medium)
- **Assumption:** Scenario's "whether buddy assignment crosses seniority norms" is evaluated on the filter's output, not a fourth filter factor. Agent flags via `ESC-BUDDY-SENIORITY`; HR decides.
- **Hypothesis:** The three-factor filter's coach validation plus the scenario's separate call-out of seniority norms is most consistent with an after-filter check.
- **How I'd test it:** *"Is there a seniority-delta threshold you'd like surfaced for review before auto-assign, or would you prefer every match reviewed?"*
- **Confidence:** Medium.

### A9 — Retention envelope (AGENT — Medium)
- **Assumption:** 7y employment records, 1y integration audit.
- **Hypothesis:** Industry standard; IRCA minimum for I-9 is the lower bound (3y post-hire or 1y post-termination, whichever later) but 7y firm-wide is typical.
- **How I'd test it:** Client's records-retention policy owner.
- **Confidence:** Medium.

### A10 — LMS vendor + contract [UNKNOWN] (AGENT — Low, build-blocking)
- **Assumption:** The LMS has an assignment API and completion webhook; specific vendor unidentified.
- **Hypothesis:** Cornerstone / Workday Learning / Docebo / LinkedIn Learning / TalentLMS all expose both.
- **How I'd test it:** *"Which LMS vendor and edition is in use? Share admin console URL and API/webhook docs."*
- **Confidence:** Low — top priority to resolve. Dependency: V3 (webhook contract shape) collapses into this entry.

### A11 — Tenant auth (AGENT — Medium)
- **Assumption:** OAuth2 client-credentials on both Workday + ServiceNow.
- **Hypothesis:** Modern default; legacy basic-auth still appears in older tenants.
- **How I'd test it:** IT contact for tenant URLs + service-account provisioning turnaround.
- **Confidence:** Medium.

### A12 — Idempotency key formula (AGENT — Medium)
- **Assumption:** `sha256("{onboarding_id}:{task_id}:{system}:{action}")`.
- **Hypothesis:** Deterministic per task-system-action; collisions desirable on retry, never on distinct actions.
- **How I'd test it:** Replay test against sandbox.
- **Confidence:** Medium.

### A13 — ServiceNow bundle schema (AGENT — Medium)
- **Assumption:** Role-keyed CIs; non-template items → `ESC-ACCESS-NONTEMPLATE` to a named approver.
- **Hypothesis:** Standard IT-services pattern.
- **How I'd test it:** Catalogue console view.
- **Confidence:** Medium.

### A14 — Business-day calendar (AGENT — Medium)
- **Assumption:** Mon–Fri − client-observed US federal holidays; I-9 clock from `start_date`.
- **Hypothesis:** Industry-standard reading of IRCA; client's policy may define further.
- **How I'd test it:** Client's written I-9 policy.
- **Confidence:** Medium.

### A15 — Day-14 + Day-10 milestones (AGENT — Medium)
- **Assumption:** Day-14 = onboarding-complete audit; Day-10 = handoff nag.
- **Hypothesis:** Scenario's "~2 weeks" and named 30-day checkpoint suggest handoff sits earlier than 30.
- **How I'd test it:** Confirm with HR Ops lead.
- **Confidence:** Medium.

### A16 — Seniority-delta default = 3 (AGENT — Low)
- **Assumption:** Default threshold 3 bands; HR-configurable.
- **Hypothesis:** Typical career-framework delta.
- **How I'd test it:** HR Ops.
- **Confidence:** Low.

### A17 — Email sender identity [UNKNOWN] (AGENT — Medium)
- **Assumption:** Named transactional relay with DKIM/SPF on HR domain.
- **Hypothesis:** Any of SES / SendGrid / Mailgun / client-SMTP works.
- **How I'd test it:** IT for outbound relay.
- **Confidence:** Medium.

### V2 — Synthetic harness representativeness (AGENT — Medium)
- **Assumption:** Production-like distributions can be generated from an anonymised Workday directory dump.
- **Hypothesis:** Access to snapshot unlocks calibration.
- **How I'd test it:** Request dump.
- **Confidence:** Medium.

### V4 — Ground truth for BT-1 (AGENT — Medium)
- **Assumption:** HR reviewer's decision defines correctness for the classification boundary test.
- **Hypothesis:** Anchors the oracle to the human, not the test author.
- **How I'd test it:** Walk BT-1 past HR Ops lead.
- **Confidence:** Medium.

### V5 — BT-2 threshold parameterisation (AGENT — Medium)
- **Assumption:** Threshold varies at harness level only; no production side-effect.
- **Hypothesis:** Straightforward config.
- **How I'd test it:** Harness-internal.
- **Confidence:** Medium.

### A-open-1 — `ESC-SCHEDULE-DRIFT` is a spec gap (AGENT — Build-blocking for FM-4)
- **Assumption:** The capability spec needs a new escalation + rule to handle `start_date` changes after Onboarding creation; D4 FM-4 surfaced this.
- **Hypothesis:** A scheduled-drift ESC + a rule scoping which task `due_at`s get recomputed (only PENDING; not IN_FLIGHT / COMPLETE) would close the gap.
- **How I'd test it:** Coach session — confirm HR's handling of start-date shifts today, then regenerate D3 with the new rule.
- **Confidence:** Not applicable until resolved; treated as spec gap.

---

## 7. Genuine unknowns — the "I don't know" list

The Week 1 brief requires ≥ 5. This list has 9 genuine unknowns; none are filler.

1. **U1 — Which LMS vendor is in use.** (A10.) Build-blocking for compliance-training capability.
2. **U2 — Workday + ServiceNow tenant URLs, auth flavour, rate limits.** (A11.) Blocks first build-loop run of §6.1 + §6.2.
3. **U3 — Email sender (relay/API, domain authentication).** (A17.) Blocks first build-loop run of every ESC-* notification.
4. **U4 — Current baseline rates for M2 (time-per-onboarding) and M3 (fell-through-cracks).** (A1, A2.) Without these, targets are floating and the business case is not defended.
5. **U5 — ServiceNow role-bundle schema and non-template approval owner.** (A13.) Blocks `ESC-ACCESS-NONTEMPLATE` routing.
6. **U6 — Client's business-day calendar and policy interpretation of "start_date" for I-9.** (A14.) Regulatory timing.
7. **U7 — Whether HR wants every buddy match reviewed or only exceptions flagged.** (A8.) Directly moves a delegation row.
8. **U8 — Client retention policy (vs industry-default 7y/1y).** (A9.) Touches every decision-log row.
9. **U9 — Client's current handling of start_date shifts mid-onboarding.** (A-open-1.) Spec gap surfaced by FM-4.

A reviewer scanning §7 alone should see where the spec is load-bearing on unvalidated ground: LMS, baselines, buddy-review policy, schedule-drift.

---

## 8. What must be validated before building

### 8.1 Blocking — cannot start building until resolved

- **U1 / A10 — LMS vendor.** Without this, Cap-C §6.3 has no endpoint, no auth, no webhook contract. Forces D3 regeneration once resolved.
- **Open tension A8 + H4 reconciliation (U7).** Without this, D2 row 11 and D3 Cap-B rule 6 are conditionally correct. Could move from FULL to HUMAN-IN-LOOP on every match, a material change.

### 8.2 Soft-blocking — can start building, but a specific capability or branch depends

- **U2 / A11 — Tenant auth and rate limits.** Enables §6.1 + §6.2 build-loop runs; drafting proceeds without.
- **U3 / A17 — Email sender.** Escalation notifications work in mock mode until resolved.
- **U5 / A13 — ServiceNow bundle schema.** Cap-A rule 4's non-template branch cannot be exercised end-to-end.
- **U6 / A14 — Business-day calendar.** Cap-A rule 5 is correct in structure but its clock boundary depends on client policy confirmation.
- **U9 / A-open-1 — `ESC-SCHEDULE-DRIFT`.** FM-4 unwrapped a missing ESC; not blocking routine path, blocking robust operation.
- **U8 / A9 — Retention envelope.** Decision-log schema is correct; only the retention TTL config is at risk.

### 8.3 Non-blocking but load-bearing — build can proceed; validation changes confidence of the business case

- **U4 / A1 + A2 — M2 / M3 baselines.** Architecture unaffected; headline targets are assumed.
- **H1 — Adoption willingness.** Value-risk; does not move architecture.
- **A16 — Seniority-delta threshold default.** Parameterisable.
- **H2 — Judgment-call patternability.** Low and explicitly not used to move a row; its movement to High would *reduce* agent scope by opening a conversation about further delegation, not break the current spec.

**Recommended next coach-session probe** (from §4 position 1): *"For buddy matches that pass the three-factor filter, do you want every match routed through HR for sign-off, or only matches that exceed a seniority-delta threshold (e.g. 3 bands)?"* — resolves U7, which is the highest-leverage open tension and conditions Cap-B's delegation shape.

---

## 9. Diagrams

No diagram — the log is the artefact.

---

## 10. Self-audit

- [x] Every `[ASSUMED]` or `[UNKNOWN]` reference in D1–D4 has a matching numbered entry here.
- [x] Every entry is tagged HUMAN or AGENT.
- [x] Every entry has Assumption, Hypothesis, Test, Confidence (via reference to scenario file for H1–H7; full entries here for AGENT).
- [x] No AGENT entry is rated High without justification; A7's High is regulation-anchored and the justification is called out explicitly.
- [x] Open tensions (H4 vs scenario text → A8; H2 vs scenario text → not-used) are surfaced as distinct AGENT entries rather than silently resolved.
- [x] Scan table §3 and full entries §6 are consistent (same numbers, same tags, same confidence, same one-line summary).
- [x] Week 1 floor of ≥ 5 genuine unknowns is cleared — §7 has 9.
- [x] Coach-session priority queue §4 is ordered by leverage, not by entry number (open tension first, build-blocker next, etc.).
- [x] §8 split into Blocking / Soft-blocking / Non-blocking with explicit Assumption Log citations.
- [x] No `[TODO]` markers.
- [x] No upstream deliverable was silently re-derived. Where D4 surfaced a spec gap (ESC-SCHEDULE-DRIFT), it is raised here as A-open-1 for the next D3 regeneration — not patched.

**Overall assumption-register read.** A reviewer can scan this log and know exactly where the spec is load-bearing: LMS contract, buddy-review policy, M2/M3 baselines, and the spec gap around start_date drift. The Week 1 self-check question — *"would a reviewer be able to challenge my thinking because I've exposed it, rather than in spite of hiding it?"* — can be answered honestly **yes**: the two tensions (H2 vs scenario text, H4 vs scenario text) are explicitly surfaced rather than elided, and the two regulation-anchored Highs (A4 on IRCA, A7 on classification) are distinguished from coach-session-validated Highs by an explicit note.

---

## 11. Out of scope

- Problem statement + success metrics — see [`./problem-statement-scenario-1-201.md`](./problem-statement-scenario-1-201.md).
- Delegation analysis — see [`./delegation-analysis-scenario-1-202.md`](./delegation-analysis-scenario-1-202.md).
- Capability specification — see [`./capability-specification-scenario-1-203.md`](./capability-specification-scenario-1-203.md).
- Validation design — see [`./validation-design-scenario-1-204.md`](./validation-design-scenario-1-204.md).

