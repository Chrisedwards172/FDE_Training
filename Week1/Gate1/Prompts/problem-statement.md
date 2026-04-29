# Prompt — Problem Statement and Success Metrics (Gate 1 Deliverable 1)

This prompt produces **Deliverable 1** of the Gate 1 timed exercise, as defined in [`Week1/Gate1/SupportingDocs/Gate1-Participant-Pack.md`](../SupportingDocs/Gate1-Participant-Pack.md) §4:

> **Problem statement & success metrics** — *Frame the problem from both the claimant's perspective and the business's perspective. Define measurable outcomes that would justify the investment. Reference the scenario's specific numbers.*

It is intentionally scoped to that one deliverable. It does **not** produce the delegation analysis, agent specification, validation design, or the full assumptions & unknowns register — those are separate prompts under `Week1/Gate1/Prompts/`.

---

## Inputs

- **Scenario file (required):** [`Week1/Gate1/gate-scenario.md`](../gate-scenario.md). It contains the scenario text from §3 of the Participant Pack verbatim, plus any HUMAN assumptions captured during the timed exercise (Assumption / Hypothesis / Test / Confidence).
- **Gate 1 Participant Pack (authoritative):** [`Week1/Gate1/SupportingDocs/Gate1-Participant-Pack.md`](../SupportingDocs/Gate1-Participant-Pack.md). The deliverable definitions in §4, the evaluation criteria in §6, and the anti-patterns in §7 are the bar this output is judged against.
- **Standing sources** inherited per `CLAUDE.md` § *Prompt Authoring Conventions* (do not restate them — they are applied automatically):
  - `CLAUDE.md` — repository structure, Core Entities, diagram rules.
  - `SupportingDocs/Week1-Thinking-Discipline-Primer.md` — reasoning and documentation style.
  - `SupportingDocs/production-spec-checklist.md` — quality bar.
  - `SupportingDocs/spec-ambiguity-vs-builder-mistakes.md` — diagnostic taxonomy.
  - `SupportingDocs/the-fde.md` — FDE role and Level 1 framing.

If the scenario file is not specified at run time, default to `Week1/Gate1/gate-scenario.md`.

## Output

Write a new file at:

```
Week1/Gate1/Output/problem-statement-{{scenario-slug}}-{random-3-digits}.md
```

where `{{scenario-slug}}` is the scenario filename without the `.md` extension (e.g. `gate-scenario`). Do not overwrite a previous run — always create a new file so iterations remain auditable.

## Required structure of the output

The output file must contain, in order:

### 1. Front-matter block

- Submission ID (filename without extension).
- Source scenario file path (relative link).
- Date produced (`DD.MM.YYYY`).
- Status line — e.g. *"first draft, pre-coach-session"* or note which HUMAN assumptions from the scenario file are already coach-validated (**High**). Note the gate-day reality: under the 2.5-hour timed exercise (Pack §2) coach-session validation is unlikely, so most assumptions will sit at **Medium** / **Low**.

### 2. Assumption Log (at the top, per primer)

Same shape as in the other Week 1 prompts, scoped to assumptions that load-bear on the problem statement and success metrics only:

- **Scan table** — one row per assumption: `#`, source (HUMAN / AGENT), one-line assumption, Cagan risk attacked (Value / Usability / Feasibility / Viability), confidence, which metric or statement is at risk if wrong.
- **Coach-session priority queue** — ordered, highest-leverage first, for the deliverables in this file.
- **Update protocol** — standard "update in place, do not silently delete" language from the primer.
- **Full entries** — Assumption / Hypothesis / How I'd test it / Confidence for each numbered entry.

Rules inherited from `CLAUDE.md` § *Prompt Authoring Conventions* apply verbatim:

- Every non-trivial claim is **[CITED]** (scenario text, named regulation, explicit prompt rule) or **[ASSUMED]** (numbered Assumption Log entry).
- **High** confidence requires coach-session validation; otherwise use **Medium** or **Low**.
- Unknowns are marked `[UNKNOWN]` and raised in the Assumption Log — never silently filled in.
- *Bluffing* is a named anti-pattern in Pack §7: confident claims about systems, data, or constraints the scenario did not state — and the participant did not mark as an assumption — will be challenged. If the scenario says SOAP and the design implicitly assumes REST, that is an assumption.

### 3. The Problem Being Solved

Per Pack §4 Deliverable 1, the problem must be framed from **both the claimant's perspective and the business's perspective**. Two short, evidence-anchored paragraphs — one per perspective. Every number must be `[CITED]` from the scenario or derived explicitly from one (e.g. `300/day × 22 min ÷ 60 ≈ 110 specialist-hours/day` — cite the inputs, show the arithmetic).

**Claimant perspective.** What the claimant experiences today: unstructured submission across email / phone transcript / web form, a 2-hour acknowledgement SLA that is breached on 31% of claims, and an 18% routing error rate that translates to misdirected adjusters and downstream re-work the claimant feels. Pack §7 *"Vanishing claimant"* applies directly — framing this purely as an efficiency story for the insurer is a fail. The scenario distinguishes claimant from customer; honour that distinction.

**Business perspective.** The shape of the work: 300 FNOLs/day, 12 specialists, 22-minute average handling time, 18% routing error, 31% SLA breach. Name the integration estate as the scenario gives it (modern CRM with APIs, legacy policy admin with SOAP endpoints, document management system, no AI infrastructure today).

Rules:
- Do not add a number the scenario does not give.
- Do not infer a pain metric (e.g. cost-per-claim, customer-churn, regulatory exposure) that is not stated — if you need one, mark it `[ASSUMED]` and add an Assumption Log entry.
- If the scenario file contains a stakeholder quote, include it verbatim with role attribution. (The Gate 1 scenario §3 does not contain one; do not invent one.)

### 4. Why Agentic, Why Now

Three short paragraphs — **Volume**, **Repeatability**, **Constraint** — each tied to the scenario numbers or cited framing. No generic business-speak. This is the *"why the problem is fit for an agent at all"* framing, not a sales pitch.

- **Volume:** 300 FNOLs/day × ~22 min ≈ specialist-hours of cognitive load per day [CITED inputs, derived total].
- **Repeatability:** triage by severity → coverage validation → routing → claimant acknowledgement is a fixed pipeline applied to every claim [CITED from §3 task list]. The judgment fraction the scenario flags ("high-value or ambiguous claims") is the explicit human-oversight boundary.
- **Constraint:** 2-hour SLA with 31% breach today [CITED] — this is latency-bound, not just cost-bound, which is the constraint that drives the agentic case.

### 5. Success Metrics

A single table. Columns:

| Metric | Current State | Target State | Measurement Method | Source |
|---|---|---|---|---|

Rules for the table:

- **Current State:** If the scenario gives a baseline, cite it (`22 min AHT [CITED]`, `18% routing error [CITED]`, `31% SLA breach [CITED]`, `12 specialists [CITED]`, `300 FNOLs/day [CITED]`). If it does not, write `[UNKNOWN — baseline needed]` and raise it as an Assumption Log entry (do not guess).
- **Target State:** Every target must be numeric and testable. If the threshold is invented, mark it `[ASSUMED]` and trace to a numbered entry. Do not claim a target is "Non-negotiable" unless it is [CITED] from the scenario or a named regulation.
- **Measurement Method:** Name the observable artefact or log that would produce the number in production (e.g. `claims_acknowledged_within_2h / total_claims_received`, `routing_decisions_overturned_by_adjuster / total_routed`, `claims_with_no_specialist_touch / total_claims`). No "we'll track it" hand-waving — Pack §7's *"Hand-waving verbs"* anti-pattern applies.
- **Source:** Use the exact labels a downstream stakeholder deck will inherit — `[CITED]`, `[ASSUMED] — A#`, or `(Non-negotiable)` where the scenario or regulation fixes the target. **Do not hide "needs validation" behind polished wording** — the primer's anti-pattern *"polished spec that dodges the riskiest unknown"* applies directly here.

Include at minimum:

1. A **SLA / latency** metric — % of FNOLs acknowledged to the claimant within the 2-hour window. Current `69% (= 100 − 31% breach) [CITED]`; target [ASSUMED] unless coach-validated.
2. A **routing-quality** metric — routing error rate (claims requiring re-routing after adjuster pickup). Current `18% [CITED]`; target [ASSUMED].
3. A **human-effort / throughput** metric — specialist time per claim, or % of claims fully handled without specialist touch. Current `22 min AHT [CITED]`; target [ASSUMED].
4. A **claimant-experience** metric — e.g. acknowledgement-to-claimant within SLA, or claimant-visible re-work rate. Anchored to the claimant perspective in §3 above. Pack §7 *"Vanishing claimant"* applies if this row is missing.
5. A **boundary-respect / non-negotiable** metric — every claim classified as *high-value or ambiguous* reaches a logged human decision; **zero silent agent decisions** on the human-oversight side of the boundary. This is Non-negotiable per the scenario's explicit *"insist on human oversight for high-value or ambiguous claims"* clause [CITED].

Below the table, a one-line note naming which rows rest on assumed baselines or assumed targets and must be converted to `[TESTED]` via a coach session — or, in the live walkthrough (Pack §5), defended as the participant's best-judged target with the trade-off named.

### 6. Out of scope for this deliverable

One short paragraph naming what this file deliberately does *not* cover:

- Delegation analysis (Deliverable 2).
- Agent specification (Deliverable 3).
- Validation design (Deliverable 4).
- The full assumptions & unknowns register (Deliverable 5).

Cross-link to the companion prompts in `Week1/Gate1/Prompts/` where relevant so a reviewer knows where the rest of the picture lives.

## Self-audit before declaring the output complete

- [ ] Every number in *The Problem Being Solved* is either `[CITED]` from the scenario file or a labelled derivation of a cited number.
- [ ] Both the **claimant** and **business** perspectives are framed (Pack §4 Deliverable 1 explicit requirement; Pack §7 *"Vanishing claimant"* anti-pattern not triggered).
- [ ] No invented stakeholder quote. If the scenario carries one, it is verbatim and attributed.
- [ ] Every target in the Success Metrics table is numeric, has a measurement method, and carries an honest source label.
- [ ] No `[ASSUMED]` target is implicitly presented as settled fact.
- [ ] Every `[ASSUMED]` or `[UNKNOWN]` in the body has a matching numbered entry in the Assumption Log.
- [ ] The boundary-respect / non-negotiable metric is present and correctly labelled (tied to the scenario's *"human oversight for high-value or ambiguous claims"* clause).
- [ ] File lives under `Week1/Gate1/Output/` and the filename follows the naming convention above.
- [ ] No invented infrastructure, integration shape, or capability language has leaked in from later deliverables. In particular, no implicit shift from the scenario's *SOAP* policy admin to REST without an inline `[ASSUMED]` marker (Pack §7 *"Bluffing"*).

## Regeneration

If the scenario file is edited — especially its HUMAN assumptions confidence ratings — regenerate this deliverable rather than hand-editing it. A divergence between the scenario file and this output is a defect, diagnosed the same way a divergence between spec and built software is diagnosed in the closed build loop.
