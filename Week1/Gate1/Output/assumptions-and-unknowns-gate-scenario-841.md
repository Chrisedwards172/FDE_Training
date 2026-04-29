# Assumptions & Unknowns — Gate 1 (FNOL)

## Front-matter

- **Submission ID:** `assumptions-and-unknowns-gate-scenario-841`
- **Source scenario:** [`../gate-scenario.md`](../gate-scenario.md) (verbatim from [`../SupportingDocs/Gate1-Participant-Pack.md`](../SupportingDocs/Gate1-Participant-Pack.md) §3)
- **Upstream deliverables consolidated:**
    - Deliverable 1 — [`./problem-statement-gate-scenario-317.md`](./problem-statement-gate-scenario-317.md) (A1–A7).
    - Deliverable 2 — [`./delegation-analysis-gate-scenario-503.md`](./delegation-analysis-gate-scenario-503.md) (D1–D7; HC1–HC4).
    - Deliverable 3 — [`./agent-specification-gate-scenario-612.md`](./agent-specification-gate-scenario-612.md) (S1–S10; entities, R-A-1..10, R-B-1..14, R-C-1..11; ESC codes; integration contracts).
    - Deliverable 4 — [`./validation-design-gate-scenario-729.md`](./validation-design-gate-scenario-729.md) (V1–V7; HP-1, EC-1..7, FM-L-1..5, FQ-1..6, BV-1, BV-2).
      All four loaded. No gaps.
- **Date produced:** 27.04.2026
- **Status:** Gate 1 timed-exercise draft, no coach-session validation possible per Pack §2. All assumptions sit at **Medium** or **Low** by construction; **High** is not available for this deliverable. The Live Walkthrough (Pack §5) is a post-submission challenge, not a validation channel that can elevate confidence ratings before submission.

---

## 2. Scope and Stance

This deliverable is the **single consolidated assumption register** for the Gate 1 FNOL scenario. Every `[ASSUMED]` or `[UNKNOWN]` referenced anywhere in Deliverables 1–4 traces to a numbered entry here (prefixed `U` for *unified*). The register does not re-derive upstream analysis — it consolidates, deduplicates, and orders.

Each entry is tagged **HUMAN** (participant-supplied, from `gate-scenario.md`) or **AGENT** (identified during drafting). The scenario file's HUMAN assumptions section was empty at time of generation — all entries below are therefore **AGENT**.

Confidence is **Low** or **Medium**. **High** is unavailable per Pack §2 — no coach session exists inside the Gate 1 window. An entry rated High here would be a defect. Pack §7 *"Bluffing"* and *"Filler unknowns"* anti-patterns apply directly: every entry names the decision, threshold, integration shape, or rule that breaks if the assumption is wrong.

---

## 3. Scan Table

| # | Source | Assumption (one line) | Cagan risk | Confidence | Upstream sections at risk if wrong |
|---|---|---|---|---|---|
| U1 | AGENT | *High-value or ambiguous* is codifiable as a threshold-based trigger the client can articulate. | Value | Low | D1 §2 A3; D2 §4 T7,T8,T10,T13; D3 §5.B.5 R-B-6; D4 §8 BV-1,BV-2; M5 definition. |
| U2 | AGENT | Legacy Policy Admin SOAP exposes `GetCoverage(policyId, lossDate)` → `{inForce, coverageType, deductible, limit}` with p95 ≤ 15s and ≥ 99% availability. | Feasibility | Low | D1 §2 A7; D2 §2 D2; D3 §2 S1, §6.2; D4 FM-L-1, FQ-1. **Build-blocking.** |
| U3 | AGENT | CRM exposes REST endpoints for claim creation, update, and routing under OAuth 2.0 client-credentials with named scopes. | Feasibility | Low | D3 §2 S2, §6.1; D4 FM-L-2. **Build-blocking.** |
| U4 | AGENT | DMS exposes `PUT /artefacts/{key}` REST endpoint accepting up to 25 MB with API-key auth. | Feasibility | Low | D3 §2 S3, §6.3; D4 FM-L-5. **Build-blocking.** |
| U5 | AGENT | Ack channels are three transactional systems (email API, SMS gateway, claimant-portal write) with consistent send semantics. | Feasibility | Low | D1 §2 A5; D2 §2 D7; D3 §2 S4, §6.4; D4 FM-L-3, FQ-4. **Build-blocking.** |
| U6 | AGENT | Routing-error 18% measures adjuster-overturned routings, not operational re-queues. | Feasibility | Medium | D1 §2 A1; M2 baseline definition. |
| U7 | AGENT | 2-hour SLA clock starts at system-of-record receipt timestamp, uniform across all channels. | Feasibility | Medium | D1 §2 A2; M1 baseline; D3 §5.A.5 R-A-7. |
| U8 | AGENT | Specialist fully-loaded cost is in the £40–80k/year band. | Viability | Low | D1 §2 A4; ROI envelope (not in current deliverables). |
| U9 | AGENT | Ack is delivered on the same channel the FNOL arrived on; phone-originated uses contact preference on file. | Usability | Medium | D1 §2 A5; D2 §2 D7; D3 §5.C.5 R-C-2; D4 EC-4. |
| U10 | AGENT | Target thresholds (SLA ≤ 5% breach, routing error ≤ 3%, ≥ 70% no-touch) are FDE-judged, not client-set. | Value | Low | D1 §2 A6; M1–M4 target columns. |
| U11 | AGENT | Phone-transcript intake is delivered as text by an upstream telephony stack, not transcribed by the agent. | Feasibility | Medium | D2 §2 D4; D3 §5.A Capability A scope. |
| U12 | AGENT | CRM is the system-of-record for the claim record; Policy Admin is queried for coverage only, not written to. | Feasibility | Medium | D2 §2 D5; D3 §5.A.5 R-A-6, §5.B.5 R-B-3. |
| U13 | AGENT | Routing rules (LOB, peril, geography, severity → adjuster queue) exist today, even if in spreadsheets or heads. | Feasibility | Medium | D2 §2 D3; D3 §2 S8; D4 FQ-2. |
| U14 | AGENT | No category of FNOL is reserved by external regulation to a human-only path beyond the scenario's *high-value or ambiguous* clause. | Viability | Low | D2 §2 D6; could add net-new HUMAN ONLY rows to D2 §4. |
| U15 | AGENT | Extraction confidence threshold 0.85 is a defensible starting point; tunable from production telemetry. | Feasibility | Medium | D3 §2 S5; D3 §5.A.5 R-A-4; D4 EC-6, FQ-5, FQ-6. |
| U16 | AGENT | SLA budget allocation: routine path p95 ≤ ~2 min, leaving ~118 min reserve. | Feasibility | Medium | D3 §2 S6; D3 §5.A.5 R-A-9, §5.B.5 R-B-13, §5.C.5 R-C-10. |
| U17 | AGENT | Severity bands S1–S4 are codifiable from a published rubric (peril, loss magnitude, injury indicator). | Feasibility | Medium | D3 §2 S7; D3 §5.B.5 R-B-5; D4 FQ-3. |
| U18 | AGENT | All external-system writes use idempotency-key format `claim:{claim_id}:{action}:{discriminator}` with 24h dedup. | Feasibility | Medium | D3 §2 S9; all R-x-6 rules; D4 EC-1. |
| U19 | AGENT | Audit-trail retention defaults to 7 years for `HumanDecision` and `Claim` records. No regulatory citation. | Viability | Low | D3 §2 S10; D3 §5.A.7 / §5.B.7 / §5.C.7. |
| U20 | AGENT | Synthetic test data (HP-1 inputs, peril mix) is representative of the 300-FNOL/day production distribution. | Feasibility | Medium | D4 §2 V1; HP-1 timing assertions; EC-3/EC-6 precision. |
| U21 | AGENT | 5% sample rate on (deductible, limit) cross-check is sufficient for FQ-1 detection within 5 days. | Feasibility | Medium | D4 §2 V2; FQ-1 detection rule. Internal tension with U23. |
| U22 | AGENT | Historical baseline for `severity_band × peril` distribution exists (insurer BI, past 12 months). | Feasibility | Low | D4 §2 V3; FQ-3 KL-divergence detector. **Build-blocking for FQ-3.** |
| U23 | AGENT | Claims operations lead has ~30 min/day audit capacity for FQ-* sample-verification. | Viability | Medium | D4 §2 V5; all FQ verification steps. Internal tension with U21. |
| U24 | AGENT | Insurer captures a claimant-feedback signal (NPS, complaint webhook) at sufficient rate for FQ-4 post-send detection within 1 week. | Feasibility | Low | D4 §2 V4; FQ-4 verification step. |
| U25 | AGENT | Pre-send template-lint is buildable as a synchronous gate inside R-C-3 / R-C-5 within the 30s p95 budget. | Feasibility | Medium | D4 §2 V6; FQ-4 prevention rule. Could require a new R-C-* spec rule. |
| U26 | AGENT | A 5-day rolling window is acceptable lag for M2 routing-quality drift detection. | Value | Medium | D4 §2 V7; FQ-2 detection rule. |
| U27 | AGENT | Spec-vs-test tension: R-B-6 *low-confidence-intake* threshold `< 0.95` means any happy-path requires `extraction_confidence ≥ 0.95`, colliding with R-A-4's `≥ 0.85` gate. | Feasibility | Medium | D4 §9 spec gap 1; HP-1 validity; R-B-6 and R-A-4 band definition. *Surfaced during consolidation.* |
| U28 | AGENT | No spec rule exists for the 30-min ack-delivery sweep job (FM-L-4) or for the pre-send template-integrity gate (FQ-4). | Feasibility | Medium | D4 §9 spec gaps 2 & 3; D3 would need R-C-12 and R-C-13. *Surfaced during consolidation.* |

**Overall read.** 28 entries total: 0 HUMAN, 28 AGENT. 11 Low, 17 Medium, 0 High. 0 open HUMAN-vs-scenario tensions (no HUMAN assumptions were populated in the scenario file). 2 entries (U27, U28) were surfaced during consolidation from D4 §9 spec gaps. 1 internal tension exists between U21 and U23 (sample-rate vs. audit-capacity).

---

## 4. Walkthrough / Client-Validation Priority Queue

Under gate conditions none of these get resolved before submission. This queue is what the participant defends in the Live Walkthrough (Pack §5) and would take into a real client conversation.

1. **U1** — *high-value or ambiguous* trigger codifiability. Moves the most rows in the delegation analysis; without it M5 is unfalsifiable and the entire escalated branch in Capability B is unbuildable. *"Can you walk me through five recent claims your specialists flagged as 'ambiguous', and tell me what tipped each one?"*
2. **U2** — SOAP WSDL for `GetCoverage`. Build-blocking. Cannot define the coverage-validation request envelope without it.
3. **U3** — CRM REST API catalogue + OAuth scopes. Build-blocking. Capability A claim creation and Capability B routing writes both depend.
4. **U4** — DMS write API. Build-blocking. Capability A's first action.
5. **U5** — Ack-channel SDKs and vendor identity. Build-blocking. Capability C's only outbound integration.
6. **U14** — Regulatory carve-outs. Could add net-new HUMAN ONLY rows; refusing to invent citations is the honest move (Pack §7 *"Bluffing"*).
7. **U19** — Audit-trail retention regime. Drives HumanDecision table sizing, log retention, FQ-* sample-audit cadence.
8. **U22** — Historical severity baseline. Build-blocking for FQ-3 KL-divergence detector.
9. **U6** — Routing-error denominator. Defines whether M2 baseline is operational truth.
10. **U13** — Codifiable routing rules. Determines whether *Route — routine* is FULLY AGENTIC or HUMAN-LED.
11. **U27** — R-B-6 / R-A-4 confidence-threshold collision. Spec re-tune needed before build.
12. **U10** — Target thresholds. Direction holds; magnitude is negotiable.
13. **U24** — Claimant-feedback signal. Build-blocking for FQ-4 post-send detection.
14. **U7** — SLA clock-start. Baseline-defining; cheap to confirm.
15. **U9** — Ack channel symmetry. Affects measurement, not architecture.
16. **U8** — Specialist loaded cost. Only matters for ROI; not part of current deliverables.

---

## 5. Update Protocol

> Update assumptions in place — never silently delete. If a Live Walkthrough challenge surfaces new evidence, leave the entry with strikethrough and append a dated `→ [REVISED]` annotation, plus a new numbered entry pointing at the replacement. **Confidence ratings cannot move to High within the Gate 1 window.** If a post-gate coach session subsequently validates an entry, raise the confidence in place and add a dated coach-session note; the `[ASSUMED]` tag remains on the original entry so the audit trail is preserved.
>
> If an assumption no longer traces to a HUMAN anchor (e.g. because a HUMAN assumption was refined and its operational details were lifted to new AGENT entries), retire with strikethrough and a footnote — do not delete.
>
> Any entry tagged *"surfaced during consolidation"* must name the upstream section that triggered the surfacing. Pack §7 *"Bluffing"* applies — an entry that asserts a regulator-mandated requirement without a citable section number is downgraded to `[UNKNOWN]` rather than carried as a hard constraint.

---

## 6. Full Entries

**U1 — *High-value or ambiguous* is codifiable.** _(AGENT — Low)_

- **Upstream traceability:** A3 (D1 §2.1); D1 (D2 §2.1).
- **Assumption:** The client can articulate the criteria (reserve estimate ≥ $X, coverage-validation confidence < Y%, prior-loss pattern, ambiguous coverage language, missing key fields) that flip a claim onto the human-oversight branch.
- **Hypothesis:** If the criteria are codifiable, escalation classification (T7 in D2) is FULLY AGENTIC and M5 is measurable via a deterministic trigger. If they are tacit, T7 drops to HUMAN-LED WITH AGENT SUPPORT and M5 becomes unfalsifiable.
- **How I'd test it:** *"Can you walk me through five recent claims your specialists flagged as 'ambiguous', and tell me what tipped each one? I'm looking for a rule, not a vibe."*
- **Confidence:** Low — highest-leverage open question. The scenario uses a qualitative phrase; no quantitative definition is given.

**U2 — SOAP `GetCoverage` shape and reliability.** _(AGENT — Low)_

- **Upstream traceability:** A7 (D1 §2.1); D2 (D2 §2.1); S1 (D3 §2.1).
- **Assumption:** The legacy policy admin's SOAP endpoints answer the four coverage questions (in-force, type, deductible, limit) keyed on `(policyId, lossDate)` with p95 ≤ 15s and ≥ 99% availability.
- **Hypothesis:** If yes, Cap B §5.B.5 R-B-3 is buildable from the WSDL alone. If no (latency poor or multiple operations required), the FULLY AGENTIC routine validation path drops to AGENT-LED WITH HUMAN OVERSIGHT and the SLA target collapses.
- **How I'd test it:** *"Can you share the WSDL for the policy admin's coverage-lookup operation, and do you have 30-day p95 latency and availability stats?"*
- **Confidence:** Low. **Build-blocking** — cannot define the SOAP request/response envelope without the WSDL.

**U3 — CRM REST API catalogue.** _(AGENT — Low)_

- **Upstream traceability:** S2 (D3 §2.1).
- **Assumption:** Claim creation, claim update, and routing assignment are three REST writes under OAuth2 client-credentials with documented scopes.
- **Hypothesis:** If true, Cap A and Cap B integrate against documented endpoints; if the CRM lacks idempotency primitives, the agent owns deduplication via a write-log keyed on U18.
- **How I'd test it:** *"Can you share the CRM OpenAPI / Swagger spec and the auth handbook?"*
- **Confidence:** Low. **Build-blocking.**

**U4 — DMS write API.** _(AGENT — Low)_

- **Upstream traceability:** S3 (D3 §2.1).
- **Assumption:** A single REST `PUT /artefacts/{key}` accepts raw FNOL payloads up to 25 MB with API-key auth and returns a stable artefact URI.
- **Hypothesis:** If true, Cap A R-A-1 is one call. If DMS has a different shape, the intake step needs redesigning.
- **How I'd test it:** *"Can you share the DMS integration guide?"*
- **Confidence:** Low. **Build-blocking.**

**U5 — Ack-channel inventory and vendor identity.** _(AGENT — Low)_

- **Upstream traceability:** A5 (D1 §2.1); D7 (D2 §2.1); S4 (D3 §2.1).
- **Assumption:** Three channels — transactional-email API (SendGrid-class), SMS gateway (Twilio-class), claimant-portal write API — with consistent send semantics (accept → deliver-webhook).
- **Hypothesis:** If true, Cap C is one switch on source-channel. If channels are fewer or have different semantics, R-C-2 / R-C-3 / R-C-5 need redesigning.
- **How I'd test it:** *"Which email / SMS / portal vendors do you use today for claimant comms, and do they expose a transactional-send API with delivery webhooks?"*
- **Confidence:** Low. **Build-blocking.**

**U6 — Routing-error denominator.** _(AGENT — Medium)_

- **Upstream traceability:** A1 (D1 §2.1).
- **Assumption:** The 18% routing-error figure measures adjuster-overturned routings, not operational re-queues.
- **Hypothesis:** If adjuster-overturned, M2 baseline is directly comparable. If operational re-queues, the agent "improves" the metric by reaching adjusters at all — the comparison is hollow.
- **How I'd test it:** *"Can you share the SQL or report definition behind the 18% routing-error stat?"*
- **Confidence:** Medium — the unqualified phrase "Error rate on routing: 18%" most often means downstream-overturned.

**U7 — SLA clock-start convention.** _(AGENT — Medium)_

- **Upstream traceability:** A2 (D1 §2.1).
- **Assumption:** The 2-hour SLA starts at receipt-timestamp in the source system and is uniform across email / phone / web.
- **Hypothesis:** If uniform, the 31% breach baseline is directly comparable. If phone transcripts arrive on a delay, the agent inherits a hidden latency budget.
- **How I'd test it:** *"What timestamp pair produces the 31% breach stat?"*
- **Confidence:** Medium.

**U8 — Specialist fully-loaded cost.** _(AGENT — Low)_

- **Upstream traceability:** A4 (D1 §2.1).
- **Assumption:** Fully-loaded cost sits in the £40–80k/year band.
- **Hypothesis:** Within that band, modest no-touch automation pays back within ~12 months at 300 FNOL/day volume. Outside it, the ROI story shifts.
- **How I'd test it:** *"What is the fully-loaded annual cost for a claims specialist?"*
- **Confidence:** Low. Only matters for ROI; not part of current deliverables.

**U9 — Acknowledgement channel symmetry.** _(AGENT — Medium)_

- **Upstream traceability:** A5 (D1 §2.1); D7 (D2 §2.1).
- **Assumption:** Ack returns on the same channel the FNOL arrived on; phone-originated claims use contact preference on file.
- **Hypothesis:** If symmetric, M4 is a single-event metric per claim. If multi-channel, M4 splits.
- **How I'd test it:** Confirm with comms / CX owner; check current ack templates.
- **Confidence:** Medium.

**U10 — Target thresholds are FDE-judged.** _(AGENT — Low)_

- **Upstream traceability:** A6 (D1 §2.1).
- **Assumption:** Targets (SLA breach ≤ 5%, routing error ≤ 3%, ≥ 70% no-touch) are reasonable directions, not commitments.
- **Hypothesis:** The client accepts direction (down for breach/error, up for no-touch) and negotiates magnitude in a follow-up.
- **How I'd test it:** Present the table in the Live Walkthrough; treat magnitude challenges as expected.
- **Confidence:** Low (on magnitude); Medium (on direction).

**U11 — Phone transcription is upstream.** _(AGENT — Medium)_

- **Upstream traceability:** D4 (D2 §2.1).
- **Assumption:** Phone calls are transcribed by the contact-centre / telephony stack and arrive at the agent as text with a timestamp reflecting call-end time.
- **Hypothesis:** If yes, intake is uniform text-handling. If transcription is in-scope, agent owns transcription quality and a new failure mode lands in D4.
- **How I'd test it:** *"Does your contact-centre produce call transcripts automatically, and when does the transcript become available?"*
- **Confidence:** Medium.

**U12 — CRM is system-of-record for the claim.** _(AGENT — Medium)_

- **Upstream traceability:** D5 (D2 §2.1).
- **Assumption:** New claim records are created and updated in the CRM; the SOAP policy admin is queried for coverage data only, not written to.
- **Hypothesis:** If yes, write paths are CRM REST. If claim records live in policy admin, write-over-SOAP becomes in-scope and several rows shift toward AGENT-LED WITH HUMAN OVERSIGHT.
- **How I'd test it:** *"Where does a new claim record get created today — CRM or policy admin?"*
- **Confidence:** Medium.

**U13 — Codifiable routing rules.** _(AGENT — Medium)_

- **Upstream traceability:** D3 (D2 §2.1); S8 (D3 §2.1).
- **Assumption:** The mapping from (LOB, peril, geography, severity) → adjuster queue exists today, even if held in spreadsheets or specialists' heads.
- **Hypothesis:** If yes, *Route — routine* is FULLY AGENTIC against a deterministic rule table. If no, that row drops to HUMAN-LED WITH AGENT SUPPORT and M2's 3% target is unreachable.
- **How I'd test it:** *"Can you walk me through 10 recent claim-to-adjuster assignments? I'm looking for the 'why' behind each one."*
- **Confidence:** Medium.

**U14 — No regulatory human-only carve-out beyond the scenario's own clause.** _(AGENT — Low)_

- **Upstream traceability:** D6 (D2 §2.1).
- **Assumption:** No external regulation forces any FNOL category into HUMAN ONLY. Candidates the client may yet name: state insurance code prompt-ack language, SIU/fraud workflow, HIPAA for medical-claim PHI, jurisdictional workers'-comp rules.
- **Hypothesis:** If a carve-out is named, new HUMAN ONLY row(s) are added to D2 §4.
- **How I'd test it:** *"Are there any claim categories where regulation or internal policy requires a human to handle the FNOL — beyond the high-value/ambiguous threshold?"*
- **Confidence:** Low. Pack §7 *"Bluffing"* held — refused to invent regulatory citations.

**U15 — Extraction confidence threshold = 0.85.** _(AGENT — Medium)_

- **Upstream traceability:** S5 (D3 §2.1).
- **Assumption:** 0.85 is a defensible starting point for FULLY AGENTIC progression; tunable from production telemetry.
- **Hypothesis:** Too low → agent over-reaches on garbled intake (silent error). Too high → escalation rate rises and M3 throughput softens.
- **How I'd test it:** Shadow-run on 200 historical FNOLs; tune to maximise M3 subject to M2 ≥ 97% and M5 = 100%.
- **Confidence:** Medium — internal tuneable, not client-dependent.

**U16 — SLA budget allocation.** _(AGENT — Medium)_

- **Upstream traceability:** S6 (D3 §2.1).
- **Assumption:** Routine path p95 ≤ ~2 minutes; ~118 minutes reserve for retries and escalated-path human action.
- **Hypothesis:** If production latencies differ significantly (e.g. SOAP p95 is 45s not 15s), the reserve shrinks but routine path still fits in 2h. If extraction alone takes 5+ minutes, the budget is blown.
- **How I'd test it:** Benchmark in build; tune from production p95s.
- **Confidence:** Medium.

**U17 — Severity-band rubric is codifiable.** _(AGENT — Medium)_

- **Upstream traceability:** S7 (D3 §2.1).
- **Assumption:** S1–S4 bands keyed on (peril, loss magnitude, injury indicator) are codifiable from a published or publishable rubric.
- **Hypothesis:** If codifiable, R-B-5 is FULLY AGENTIC. If tacit, triage drops to HUMAN-LED WITH AGENT SUPPORT, mirroring D1 fallback.
- **How I'd test it:** *"Walk me through 20 recent claims — how did your team decide severity on each?"*
- **Confidence:** Medium.

**U18 — Idempotency-key convention.** _(AGENT — Medium)_

- **Upstream traceability:** S9 (D3 §2.1).
- **Assumption:** `claim:{claim_id}:{action}:{discriminator}` is unique per logical write; 24-hour dedup window.
- **Hypothesis:** If external systems support this, all R-x-6 idempotency rules hold. If not, the agent must own dedup via a write-log.
- **How I'd test it:** Confirm idempotency support per-system during integration onboarding.
- **Confidence:** Medium.

**U19 — Audit-trail retention = 7 years.** _(AGENT — Low)_

- **Upstream traceability:** S10 (D3 §2.1).
- **Assumption:** Claims-records retention sits in the 7-year band typical for financial records; insurer's actual policy may differ.
- **Hypothesis:** If shorter, spec over-allocates storage. If longer, decision-log retention rows in D3 §5.x.7 must extend.
- **How I'd test it:** *"What is your records-retention policy for claims data and associated audit logs?"*
- **Confidence:** Low. Pack §7 *"Bluffing"* held — flagged as assumption, not asserted as regulation.

**U20 — Synthetic test data is representative.** _(AGENT — Medium)_

- **Upstream traceability:** V1 (D4 §2.1).
- **Assumption:** The peril mix, policy shapes, and claimant attributes in HP-1 / EC / FM test rows approximate the 300-FNOL/day production distribution.
- **Hypothesis:** If representative, HP-1 latency assertions hold. If not, the S6 budget may be over- or under-fit.
- **How I'd test it:** Request 30-day production peril distribution and compare to test data.
- **Confidence:** Medium.

**U21 — 5% sample rate sufficient for FQ-1.** _(AGENT — Medium)_

- **Upstream traceability:** V2 (D4 §2.1).
- **Assumption:** 5% random sample of `CoverageRecord` rows (raised from initial 1% per V2 internal analysis) is sufficient to detect a mis-mapping defect within 5 days at 300 FNOLs/day.
- **Hypothesis:** 15 audits/day for 5 days = 75 samples; binomial CI for 1% defect rate at 95% confidence wants ≥ 300 — at 5% that's 75 samples in 5 days, still below 300. Detection-time-to-95% is ~20 days at 5%. **Internal tension with U23** (audit capacity).
- **How I'd test it:** Run the sample-size calculation against production volume once live.
- **Confidence:** Medium — known weakness flagged in D4 §11 read.

**U22 — Historical severity baseline exists.** _(AGENT — Low)_

- **Upstream traceability:** V3 (D4 §2.1).
- **Assumption:** The insurer's BI / data-warehouse has a `severity_band × peril` distribution for the past 12 months.
- **Hypothesis:** If it exists, FQ-3's KL-divergence detector has a comparator. If not, FQ-3 collapses to manual rubric review on a quarterly cadence.
- **How I'd test it:** *"Does your BI team track severity distribution by peril type? Can you share the last 12 months?"*
- **Confidence:** Low. **Build-blocking for FQ-3.**

**U23 — Audit capacity (~30 min/day).** _(AGENT — Medium)_

- **Upstream traceability:** V5 (D4 §2.1).
- **Assumption:** The claims operations lead has ~30 minutes/day available for FQ-* sample-verification (~3 audits/day).
- **Hypothesis:** If less, FQ-1 / FQ-2 / FQ-5 sampling rates must drop, detection lag rises.
- **How I'd test it:** *"How much time can your claims operations lead realistically spend on daily quality audits once the agent is live?"*
- **Confidence:** Medium.

**U24 — Claimant-feedback signal exists.** _(AGENT — Low)_

- **Upstream traceability:** V4 (D4 §2.1).
- **Assumption:** The insurer captures a per-claim claimant-feedback signal (post-claim NPS, complaint webhook, call-back tag) at a rate observable within a week.
- **Hypothesis:** If per-claim signal exists, FQ-4 post-send detection is fast. If only annual surveys, detection is months-late; the pre-send gate (U25) is the load-bearing detector.
- **How I'd test it:** *"Do you capture any per-claim claimant feedback (NPS, complaint, call-back) — and how quickly after the FNOL?"*
- **Confidence:** Low.

**U25 — Pre-send template-lint is buildable within budget.** _(AGENT — Medium)_

- **Upstream traceability:** V6 (D4 §2.1).
- **Assumption:** A substring-check for `"{{"` in the rendered ack body adds < 5ms to the 30s R-C-10 budget.
- **Hypothesis:** If buildable, FQ-4 has a pre-send prevention gate. If not, the only defence is the post-send claimant-feedback signal (U24).
- **How I'd test it:** Benchmark in build.
- **Confidence:** Medium. Note: the upstream agent-spec does not yet contain a spec rule for this — D4 §9 gap 3 recommends adding R-C-13.

**U26 — 5-day window for M2 drift detection.** _(AGENT — Medium)_

- **Upstream traceability:** V7 (D4 §2.1).
- **Assumption:** A 5-day rolling window is acceptable lag for M2 routing-quality drift detection.
- **Hypothesis:** Shorter (1–2 days) catches volatility, not drift. Longer (10+ days) lags real change.
- **How I'd test it:** Propose at Live Walkthrough; tune with claim-turnaround data once available.
- **Confidence:** Medium.

**U27 — R-B-6 / R-A-4 confidence-threshold collision.** _(AGENT — Medium)_

- **Upstream traceability:** *Surfaced during consolidation*, triggered by D4 §9 spec gap 1.
- **Assumption:** The upstream R-B-6 *low-confidence-intake* threshold of `< 0.95` means any happy-path claim requires `extraction_confidence ≥ 0.95` to stay on the routine branch, while R-A-4 gates at `≥ 0.85`. The band `[0.85, 0.95)` is silently routine for R-A-4 but triggers escalation under R-B-6. The spec needs a re-tune: either R-B-6's low-confidence driver should be renamed / tightened, or the threshold pair should be explicitly documented as intentional.
- **Hypothesis:** If intentional (the 0.85–0.95 band is a *"safe to proceed but escalation-eligible"* zone), document it explicitly as a design decision. If unintentional, re-tune R-B-6 in a fresh agent-spec run.
- **How I'd test it:** Re-read the upstream R-B-6 rule and decide — this is a spec-consistency question, not a client question.
- **Confidence:** Medium — a spec re-tune resolves it without client input.

**U28 — Missing spec rules for sweep job and template lint.** _(AGENT — Medium)_

- **Upstream traceability:** *Surfaced during consolidation*, triggered by D4 §9 spec gaps 2 & 3.
- **Assumption:** D4 validation scenarios FM-L-4 (missing delivery webhook, 30-min sweep) and FQ-4 (pre-send template-lint gate) reference behaviours that have no matching R-C-* rule in the upstream agent specification. D4 §9 recommends adding R-C-12 (sweep-and-flag) and R-C-13 (pre-send template-integrity gate) in a fresh agent-spec run.
- **Hypothesis:** If the rules are added, FM-L-4 and FQ-4 have full spec traceability. If not, those validation scenarios assert against undefined behaviour.
- **How I'd test it:** Re-run the agent-specification prompt to add R-C-12 and R-C-13.
- **Confidence:** Medium — a spec regeneration resolves it.

---

## 7. Genuine Unknowns — The "I Don't Know" List

These are questions to which the honest answer today is *"I don't know"*, even after consolidating the four upstream assumption logs. Each references a §6 entry.

1. **What are the codifiable criteria for *high-value or ambiguous*?** — U1. The scenario uses a qualitative phrase. Without a definition, escalation logic is unbuildable and M5 is unfalsifiable.
2. **What is the SOAP WSDL for the legacy policy admin's coverage-lookup operation?** — U2. Cannot define the request/response envelope; build-blocking for Capability B.
3. **What is the CRM's REST API surface — endpoint paths, OAuth scopes, rate limits, webhook availability?** — U3. Build-blocking for Capabilities A and B.
4. **What ack-channel vendors does the insurer use, and do they expose transactional-send APIs with delivery webhooks?** — U5. Build-blocking for Capability C; unknown whether this is one system or three.
5. **What is the insurer's audit-trail retention regime for claims data?** — U19. No scenario citation; no inferred regulatory cover (Pack §7 *"Bluffing"*). Drives `HumanDecision` table sizing, log retention, and FQ-* sample-audit cadence.
6. **Does the insurer's BI / data-warehouse hold a historical `severity_band × peril` distribution?** — U22. Build-blocking comparator for FQ-3's KL-divergence detector.
7. **Does the insurer capture a per-claim claimant-feedback signal, and how quickly after the FNOL?** — U24. Build-blocking for FQ-4 post-send detection.
8. **Are there any regulatory or internal-policy carve-outs that require specific FNOL categories to be human-only beyond the scenario's own clause?** — U14. Could add rows to the delegation analysis.

---

## 8. What Must Be Validated Before Building

### Blocking — cannot start building until resolved

- **U2** — SOAP WSDL + latency / availability. Capability B's coverage-validation step is a scope-out without it (D3 §5.B, §6.2).
- **U3** — CRM REST API catalogue + OAuth. Capability A claim creation and Capability B routing (D3 §5.A, §5.B, §6.1).
- **U4** — DMS write API. Capability A's intake persist (D3 §5.A, §6.3).
- **U5** — Ack-channel vendor identity + SDK. Capability C's send paths (D3 §5.C, §6.4).

### Soft-blocking — can start building around, but a specific capability or branch depends on resolution

- **U1** — *High-value or ambiguous* trigger. Capabilities A and C build cleanly; the escalated branch in Capability B and BV-1 / BV-2 in Deliverable 4 depend on it (D2 §4 T7–T10,T13; D3 §5.B.5 R-B-6; D4 §8).
- **U27** — R-B-6 / R-A-4 confidence-threshold collision. A spec re-tune — no client input needed, but the agent-spec prompt must be re-run before the build loop starts (D3 §5.B.5 R-B-6; D4 HP-1).
- **U28** — Missing R-C-12 / R-C-13. Agent-spec re-run adds the two rules; Deliverable 4 FM-L-4 and FQ-4 depend (D3 §5.C; D4 §6 FM-L-4, §7 FQ-4).
- **U13** — Codifiable routing rules. If tacit, *Route — routine* drops classification (D2 §4 T9; D3 §5.B.5 R-B-7).
- **U22** — Historical severity baseline. Build-blocking for FQ-3 only; other capabilities proceed (D4 §7 FQ-3).

### Non-blocking but load-bearing — build can proceed; validation changes the confidence of the business case, not the architecture

- **U6** — Routing-error denominator. Shifts M2 baseline meaning (D1 §5 M2).
- **U7** — SLA clock-start. Shifts M1 baseline meaning (D1 §5 M1).
- **U10** — Target thresholds. Magnitude negotiable; direction holds (D1 §5 M1–M4).
- **U14** — Regulatory carve-outs. Could add rows post-build (D2 §4).
- **U19** — Retention regime. Storage policy, not architecture (D3 §5.x.7).
- **U15, U17** — Extraction and severity thresholds. Internal tunables (D3 §5.A.5 R-A-4, §5.B.5 R-B-5).
- **U21, U23** — Sample-rate vs. audit-capacity tension. Detection-lag tuning (D4 §7 FQ-1).
- **U24** — Claimant-feedback signal. FQ-4 post-send detection (D4 §7 FQ-4); pre-send gate (U25) is the load-bearing detector.
- **U26** — M2 drift-detection window. Tunable (D4 §7 FQ-2).

**Recommended next client-conversation probe:** *"Can you walk me through five recent claims your specialists flagged as 'ambiguous', and tell me what tipped each one?"* (U1) — the single highest-leverage question.

---

## 9. Diagrams

No diagram — the log is the artefact. No trigger in `CLAUDE.md` § *Diagrams* fires for this deliverable.

---

## 10. Self-audit (against Pack §6.5 / §7)

- [x] Every `[ASSUMED]` or `[UNKNOWN]` reference in upstream Deliverable 1–4 files has a matching numbered entry in §6 (A1–A7 → U1,U2,U3,U5,U6,U7,U8,U9,U10; D1–D7 → U1,U2,U11,U12,U13,U14,U9; S1–S10 → U2,U3,U4,U5,U15,U16,U17,U18,U19; V1–V7 → U20,U21,U22,U23,U24,U25,U26). Plus U27 and U28 surfaced during consolidation.
- [x] Every entry is tagged **AGENT** (no HUMAN assumptions were populated in the scenario file).
- [x] Every entry has Upstream traceability, Assumption, Hypothesis, How I'd test it, and Confidence.
- [x] **No entry is rated High** (Pack §2 ceiling).
- [x] No open HUMAN-vs-scenario tensions exist (HUMAN assumptions section was empty). Two cross-deliverable spec gaps (U27, U28) captured as distinct AGENT entries during consolidation.
- [x] Scan table (§3) and full entries (§6) are consistent in numbering, tags, and confidence.
- [x] The Pack §4 floor of **≥ 5 genuine unknowns** is cleared by §7 (8 items). Each is real, not Pack §7 filler — each names the decision, rule, or integration shape that breaks if the assumption is wrong.
- [x] Walkthrough priority queue (§4) is ordered by leverage, not by entry number.
- [x] §8 is split into Blocking / Soft-blocking / Non-blocking with explicit citations to §6 entries.
- [x] No `[TODO]` markers remain.
- [x] No upstream deliverable was silently re-derived — U27 and U28 flag spec gaps for an upstream re-run.
- [x] No regulatory citation is asserted as a hard constraint without a section-number reference (Pack §7 *"Bluffing"* — U14 and U19 explicitly refuse to invent citations).

**Overall assumption-register read.** A reviewer scanning this log sees where the spec is load-bearing: four build-blocking integration unknowns (U2–U5), one build-blocking boundary definition (U1), one build-blocking detection comparator (U22), two spec-consistency gaps surfaced during consolidation (U27, U28), and one internal tension between sample-rate and audit-capacity (U21/U23). The Pack §6.5 question — *"are at least five genuine unknowns surfaced, real, not filler?"* — is answered yes by §7's eight entries, each naming the specific rule or integration that breaks. The single highest-leverage open question for the Live Walkthrough is **U1** — the codifiable definition of *high-value or ambiguous*, without which M5 is prose, not contract.

---

## 11. Out of Scope for This Deliverable

This file covers Pack §4 Deliverable 5 only: the consolidated assumption register. It does not cover:

- **Problem statement & success metrics** (Deliverable 1) — see [`./problem-statement-gate-scenario-317.md`](./problem-statement-gate-scenario-317.md) and [`../Prompts/problem-statement.md`](../Prompts/problem-statement.md).
- **Delegation analysis** (Deliverable 2) — see [`./delegation-analysis-gate-scenario-503.md`](./delegation-analysis-gate-scenario-503.md) and [`../Prompts/delegation-analysis.md`](../Prompts/delegation-analysis.md).
- **Agent specification** (Deliverable 3) — see [`./agent-specification-gate-scenario-612.md`](./agent-specification-gate-scenario-612.md) and [`../Prompts/agent-specification.md`](../Prompts/agent-specification.md).
- **Validation design** (Deliverable 4) — see [`./validation-design-gate-scenario-729.md`](./validation-design-gate-scenario-729.md) and [`../Prompts/validation-design.md`](../Prompts/validation-design.md).

