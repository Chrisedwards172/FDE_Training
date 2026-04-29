# Problem Statement & Success Metrics — Gate 1 (FNOL)

## Front-matter

- **Submission ID:** `problem-statement-gate-scenario-317`
- **Source scenario:** [`../gate-scenario.md`](../gate-scenario.md) (verbatim from [`../SupportingDocs/Gate1-Participant-Pack.md`](../SupportingDocs/Gate1-Participant-Pack.md) §3)
- **Date produced:** 27.04.2026
- **Status:** First draft, pre-coach-session. Per Pack §2, this is produced inside the 2.5-hour timed gate window — no coach-session validation has occurred. All HUMAN assumptions in the scenario file are empty (timed exercise has not populated them); every assumption surfaced below is **AGENT** and sits at **Medium** or **Low** confidence. The Live Walkthrough (Pack §5) is the first opportunity to convert any of these to **High**.

---

## 2. Assumption Log

> Per `SupportingDocs/Week1-Thinking-Discipline-Primer.md`, the log sits at the top of the document and is scoped to assumptions that load-bear on the problem statement and success metrics only. Delegation, capability spec, and validation-design assumptions are owned by the companion prompts.

### 2.1 Scan table

| # | Source | Assumption (one line) | Cagan risk | Confidence | What's at risk if wrong |
|---|---|---|---|---|---|
| A1 | AGENT | "Routing error rate: 18%" measures *adjuster-overturned* routings (not operational re-queues by ops staff). | Feasibility | Medium | M2 (routing-quality) baseline definition; target threshold meaningful only if denominator matches. |
| A2 | AGENT | The 2-hour SLA clock starts at *system-of-record receipt timestamp* and is uniform across email / phone-transcript / web-form intake. | Feasibility | Medium | M1 (SLA / latency) baseline of `69% within 2h`; phone-transcript may have a transcription lag the scenario does not name. |
| A3 | AGENT | "High-value or ambiguous claims" is a definable threshold (e.g. reserve estimate ≥ $X, or coverage-validation confidence < Y%) the client can articulate, even if the exact numbers are not in scope today. | Value | Low | M5 (boundary-respect) is non-negotiable in *direction* but cannot be measured without a definable trigger; without it, "every ambiguous claim reaches a logged human decision" is unfalsifiable. |
| A4 | AGENT | Specialist fully-loaded cost is in the £40–80k/year band typical for mid-size insurance claims roles. Used only to size the ROI envelope; no client-confirmed figure exists. | Viability | Low | The ROI / payback narrative behind any non-cited target. Cost-per-claim is **not** included as a metric in this deliverable because the baseline is `[UNKNOWN]`. |
| A5 | AGENT | Claimant acknowledgement is delivered through the same channel the FNOL was received on (email-in → email-ack, web-form → portal/email-ack, phone → SMS/email-ack). | Usability | Medium | M4 (claimant-experience) measurement method assumes a single ack-event per claim; if multi-channel ack is required, the metric needs decomposition. |
| A6 | AGENT | The target thresholds in the Success Metrics table (SLA breach ≤ 5%, routing error ≤ 3%, ≥ 70% no-touch on routine claims) are FDE-judged values, not client-validated. They are defensible directions, not commitments. | Value | Low | All four operational targets in §4. |
| A7 | AGENT | The legacy policy admin SOAP endpoints expose the *coverage-validation* read paths needed to confirm policy-in-force, deductible, and coverage limits. Write paths (e.g. claim-creation in policy admin) are out of scope for the agent — claim records live in CRM. | Feasibility | Medium | M2 (routing-quality) and M5 (boundary-respect) — if SOAP cannot return coverage in time, the 2-hour SLA target is unreachable for any claim that needs validation. |

### 2.2 Coach-session priority queue (highest leverage first)

1. **A3** — definition of *high-value or ambiguous*. Without this, the Pack §6.2 challenge *"Is the codifiability of each agentic step addressed?"* cannot be answered for the boundary that the scenario itself flags as non-negotiable.
2. **A1** — routing-error denominator. Drives whether M2's target is operational truth or marketing.
3. **A7** — SOAP coverage read-paths. Build-blocking for the policy-validation step; without confirmation the 2h SLA is unreachable.
4. **A6** — target thresholds. Lower-stakes than A3/A1/A7 because direction (down-and-to-the-right) holds even if the magnitude shifts.
5. **A2** — SLA clock-start convention. Baseline-defining; cheap to confirm.
6. **A5** — ack channel symmetry. Affects measurement, not feasibility.
7. **A4** — fully-loaded cost band. Only matters when the ROI narrative is built; not part of this deliverable.

### 2.3 Update protocol

Update assumptions in place — never silently delete. When evidence shifts confidence, edit the entry, append a dated `→ [TESTED]` or `→ [REVISED]` annotation, and adjust any metric target the assumption load-bears on. A divergence between this log and the metrics table is a defect, diagnosed the same way as a spec-vs-code divergence per `SupportingDocs/spec-ambiguity-vs-builder-mistakes.md`.

### 2.4 Full entries

**A1 — Routing-error denominator.**
- *Assumption:* The 18% routing-error figure measures claims where the adjuster the agent (or human specialist) routed to was the wrong one and the claim was reassigned by an adjuster (not by ops triage, not by the claimant calling back).
- *Hypothesis:* If the figure is adjuster-overturned routings, then the agent's routing-quality target is directly comparable; if it is operational re-queues, the agent will appear to "improve" the metric simply by virtue of reaching adjusters at all.
- *How I'd test it:* Ask the client for the SQL or report definition behind the 18%. One question, one artefact.
- *Confidence:* Medium — the scenario uses the unqualified phrase "Error rate on routing: 18%" which most often means downstream-overturned, but is not airtight.

**A2 — SLA clock-start.**
- *Assumption:* The 2-hour SLA starts at receipt-timestamp in the source system (email-in time, web-form submit time, phone-call end time) and is uniform across channels.
- *Hypothesis:* If clock-start is uniform, the 31% breach baseline is comparable to a future automated baseline; if phone transcripts arrive on a delay, the agent inherits a hidden latency budget.
- *How I'd test it:* Ask for the breach calculation source — what timestamp pair produces the 31%?
- *Confidence:* Medium.

**A3 — *High-value or ambiguous* is definable.**
- *Assumption:* The client can articulate (even if not formally documented) the criteria that flip a claim into "human oversight required" — e.g. estimated reserve over a threshold, prior-claims pattern, ambiguous coverage, missing key fields.
- *Hypothesis:* If the criteria are codifiable, M5 (boundary-respect) is measurable; if they are tacit, then the agent's escalation logic is unbuildable to spec and the boundary becomes prose, not contract. Pack §6.3 *"decision logic with concrete thresholds"* applies.
- *How I'd test it:* Walk five recent claims with the claims supervisor — three routine, two escalated — and ask "what flagged this one?" Look for a rule, not a vibe.
- *Confidence:* Low. This is the highest-leverage unknown for Deliverable 3.

**A4 — Specialist loaded cost.**
- *Assumption:* Fully-loaded specialist cost sits in £40–80k/year. Used only to bound ROI conversation, not to set targets in this deliverable.
- *Hypothesis:* Within that band, even modest no-touch automation pays back the build cost within ~12 months at 300 FNOL/day volume. Outside that band the ROI story changes shape.
- *How I'd test it:* Ask HR / finance for fully-loaded cost; mark `[TESTED]` and recalculate.
- *Confidence:* Low.

**A5 — Acknowledgement channel symmetry.**
- *Assumption:* Acknowledgement returns on the same channel the FNOL arrived on, with phone-originated claims acknowledged via the claimant's contact preference on file.
- *Hypothesis:* If symmetric, M4 (claimant-experience) is a single-event metric per claim. If multi-channel, M4 must split.
- *How I'd test it:* Confirm with comms / customer-experience owner; check current ack templates.
- *Confidence:* Medium.

**A6 — Target thresholds are FDE-judged, not client-set.**
- *Assumption:* Targets such as `SLA breach ≤ 5%`, `routing error ≤ 3%`, `≥ 70% no-touch on routine claims` are reasonable directions for a first conversation, not commitments. The Pack §7 *"polished spec dodging the riskiest unknown"* anti-pattern applies if these are presented as settled.
- *Hypothesis:* The client will accept *direction* (down for breach/error, up for no-touch) and negotiate *magnitude* in a follow-up.
- *How I'd test it:* Present the table in the Live Walkthrough; treat magnitude challenges as expected and update in place.
- *Confidence:* Low (on magnitude); Medium (on direction).

**A7 — SOAP coverage read-paths.**
- *Assumption:* The legacy policy admin's SOAP endpoints can answer, for a given policy number + loss date: policy-in-force? coverage type? deductible? coverage limit? — within a budget that fits inside the 2-hour SLA.
- *Hypothesis:* If yes, coverage-validation is automatable for the bulk of FNOLs and the 2h SLA target is reachable; if no (or if SOAP latency / availability is poor), policy validation becomes the bottleneck and the agent's value collapses to triage + ack only.
- *How I'd test it:* Ask for SOAP WSDL + recent uptime / latency stats. Pack §7 *"Integration hand-wave"* applies — naming this gap explicitly is the senior-FDE move; silently designing around it is the failure mode.
- *Confidence:* Medium.

---

## 3. The Problem Being Solved

A mid-size insurer's claims team takes **300 FNOL reports per day** [CITED] across **email, phone transcript, and web form** [CITED]. Each FNOL must be **triaged by severity, validated against policy coverage, routed to the appropriate adjuster, and acknowledged to the claimant — within 2 hours of receipt** [CITED]. The work is done today by **12 specialists** [CITED] at **22 minutes average handling time per claim** [CITED]. That is `300 × 22 min = 6,600 min/day ≈ 110 specialist-hours/day` of cognitive load, against ~96 hours of nominal team capacity at an 8-hour day [CITED inputs, derived total]. The team operates with **no AI infrastructure today** [CITED].

**Claimant perspective.** A claimant submitting an FNOL today has two structural problems they feel directly. First, **31% of claims breach the 2-hour acknowledgement SLA** [CITED] — almost a third of claimants are left in silence past the window the insurer set itself. Second, **18% of claims are routed wrong** [CITED] — when the routing fails, the claimant's first substantive contact is with an adjuster who is not the right adjuster, producing handoff delay, repeated information-gathering, and a worse first impression at the moment a claimant most needs predictability. The Pack §3 scenario distinguishes claimant from customer for a reason: a claim is the moment the policy stops being abstract. Late acknowledgement and wrong routing are both **claimant-visible** failures, not just operational ones.

**Business perspective.** The insurer is running a high-volume, latency-bound, repeatable pipeline almost entirely on cognitive labour. The four steps — triage, coverage validation, routing, acknowledgement — apply uniformly to every FNOL [CITED from §3]. The integration estate that any solution must work through is fixed and unambiguous: **a modern CRM with APIs, a legacy policy administration system with SOAP endpoints, and a document management system** [CITED]. The client is **open to full automation where appropriate but insists on human oversight for high-value or ambiguous claims** [CITED] — that boundary is the non-negotiable, and it pre-defines where the agent's authority must stop. No baseline cost-per-claim, error-cost, or churn figure is given in the scenario; pain is quantified in latency (31% breach), accuracy (18% misroute), and effort (22-minute AHT × 300/day), and any further pain claim is `[ASSUMED]`.

The scenario contains **no stakeholder quote**; none is invented here.

---

## 4. Why Agentic, Why Now

**Volume.** `300 FNOL/day × 22 min ≈ 110 specialist-hours/day` of work [CITED inputs, derived total], on a fixed pipeline applied to every claim. At ~96 hours of nominal team capacity (12 specialists × 8h), the team is structurally close to or over capacity before considering breaks, holiday, or sickness — which is consistent with a 31% SLA breach [CITED]. Volume alone is not justification, but volume × repeatability × latency-pressure is.

**Repeatability.** The four-step pipeline (triage → coverage validation → routing → acknowledgement) [CITED §3 task list] is the same shape on every claim. Two of those four steps — coverage validation against policy data, and routing-on-rule — are codifiable lookup-and-decision tasks against named systems (SOAP policy admin, CRM). The third — triage by severity — is codifiable for the bulk and judgment-call for the tail. The fourth — acknowledgement — is templated comms. The judgment-call fraction the scenario flags ("high-value or ambiguous claims" [CITED]) is the explicit human-oversight boundary; everything outside it is candidate for full or supervised delegation.

**Constraint.** The 2-hour SLA with 31% breach today [CITED] makes this a **latency-bound** problem, not just a cost-bound one. A solution that is cheaper but no faster does not move the breach metric; a solution that is faster but no cheaper does. Agents are well-suited to the *latency* lever (parallelism across 300 claims/day, sub-second classification and lookup, machine-speed acknowledgement) without disturbing the human-oversight boundary on the judgment tail. That is the *why now*.

---

## 5. Success Metrics

| # | Metric | Current State | Target State | Measurement Method | Source |
|---|---|---|---|---|---|
| M1 | **SLA / latency.** % of FNOLs with claimant acknowledgement issued within 2 hours of receipt timestamp. | 69% (= 100 − 31% breach) | ≥ 95% | `count(claims_acknowledged_within_2h) / count(claims_received)`, measured daily on the receipt-timestamp → ack-event interval. | Current: [CITED]. Target: [ASSUMED] — A6. |
| M2 | **Routing quality.** % of claims whose initial adjuster assignment is *not* overturned by the receiving adjuster within 24 hours of pickup. | 82% (= 100 − 18% routing error) | ≥ 97% | `1 − (count(routings_overturned_within_24h) / count(routings_made))`, measured weekly; overturn = adjuster-initiated reassignment, not ops re-queue. | Current: [CITED]. Target: [ASSUMED] — A6. Definition: [ASSUMED] — A1. |
| M3 | **Human effort / throughput.** % of FNOLs fully handled (triage → validation → routing → ack) with no specialist touch. | 0% (no AI today, [CITED]) | ≥ 70% on routine (non-escalated) claims; 0% target on escalated claims by design (M5). | `count(claims_with_no_human_action_pre_routing) / count(claims_received)`, segmented by escalated vs routine. | Current: [CITED]. Target: [ASSUMED] — A6. |
| M4 | **Claimant experience.** % of acknowledgements that (a) reach the claimant within SLA *and* (b) name the assigned adjuster correctly on first send (no follow-up correction needed). | [UNKNOWN — baseline needed; combined SLA + first-time-right not separately reported in the scenario] | ≥ 95% | `count(acks_in_sla AND no_correction_within_24h) / count(acks_sent)`. | Current: [UNKNOWN] — flag for Deliverable 5. Target: [ASSUMED] — A6. Channel-symmetry: [ASSUMED] — A5. |
| M5 | **Boundary respect (non-negotiable).** Every claim classified as *high-value or ambiguous* reaches a logged human decision before any irreversible action (no silent agent decisions on the human-oversight side of the boundary). | Not currently measured (no agent today) | **100%** — zero silent agent decisions on escalated claims | `count(escalated_claims_with_logged_human_decision_before_irreversible_action) / count(escalated_claims) == 1.000`; alert on any deviation. | Direction: **(Non-negotiable)** [CITED] from Pack §3 *"insist on human oversight for high-value or ambiguous claims"*. Threshold definition: [ASSUMED] — A3. |

> Rows resting on assumed targets or assumed baselines: **M1, M2, M3, M4** (targets — A6); **M2** (definition — A1); **M4** (baseline `[UNKNOWN]`, channel — A5); **M5** (trigger definition — A3). M5's *direction* is non-negotiable and cited; its *measurability* depends on A3 being closed. None of M1–M4 is `[TESTED]` until a coach-session or client conversation confirms the magnitude.

Cost-per-claim and ROI metrics are deliberately **not** included in this deliverable: the scenario gives no fully-loaded specialist cost, no error cost, and no churn figure to anchor them, and inventing a baseline would trigger the Pack §7 *"Filler assumptions"* anti-pattern. A4 holds the placeholder for when ROI work begins.

---

## 6. Out of scope for this deliverable

This file covers Pack §4 Deliverable 1 only: problem framing and success metrics. It does not cover:

- **Delegation analysis** (Deliverable 2) — agentic / agent-led / human-led / human-only assignment for each pipeline step, with rationale. See `Week1/Gate1/Prompts/delegation-analysis.md` (when authored).
- **Agent specification** (Deliverable 3) — purpose, scope, I/O, decision logic with thresholds, escalation triggers, integration contracts (CRM REST, policy admin SOAP, DMS), state model, error handling. See `Week1/Gate1/Prompts/capability-specification.md`.
- **Validation design** (Deliverable 4) — happy path, edge cases, failure modes, *quiet-failure* detection. See `Week1/Gate1/Prompts/validation-design.md`.
- **Assumptions & unknowns register** (Deliverable 5) — full client-validation backlog, ≥ 5 genuine unknowns. The seven entries in §2 above are scoped to this deliverable; Deliverable 5 owns the consolidated, deduplicated register across all five deliverables. See `Week1/Gate1/Prompts/assumptions-and-unknowns.md`.

