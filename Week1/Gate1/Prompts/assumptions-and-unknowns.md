# Prompt — Assumptions and Unknowns (Gate 1 Deliverable 5)

This prompt produces **Deliverable 5** of the Gate 1 timed exercise, as defined in [`Week1/Gate1/SupportingDocs/Gate1-Participant-Pack.md`](../SupportingDocs/Gate1-Participant-Pack.md) §4:

> **Assumptions & unknowns** — *What are you assuming about the client's data, systems, and organisation? What must be validated before building? At least 5 genuine unknowns, not filler.*

It is intentionally scoped to that one deliverable. It does **not** produce the problem statement, delegation analysis, agent specification, or validation design — those are separate prompts under `Week1/Gate1/Prompts/`.

This deliverable is the one where the primer's rule *"hidden assumptions are the failure mode; stated assumptions are discovery"* lands hardest. A plausible-sounding five entries will not pass — Pack §6.5 *"Are at least five genuine unknowns surfaced? Are they real (things the participant truly does not know), not filler?"* and Pack §7 *"Filler unknowns"* are the explicit bar. *"I don't know"* beats a confident guess, provided it is paired with a plan to find out.

---

## Inputs

- **Scenario file (required):** [`Week1/Gate1/gate-scenario.md`](../gate-scenario.md). Contains the §3 scenario text verbatim plus any HUMAN assumptions captured during the timed exercise. **There is no coach session inside the Gate 1 window** (Pack §2 — 2.5 hours, scenario unseen, submission closes before the Live Walkthrough). Treat everything that is not directly cited from the scenario or the Pack as an **assumption**. **No assumption in this deliverable can carry High confidence**, because the gate provides no validation channel that could move a rating to High before submission.
- **Gate 1 Participant Pack (authoritative):** [`Week1/Gate1/SupportingDocs/Gate1-Participant-Pack.md`](../SupportingDocs/Gate1-Participant-Pack.md). Pack §4 fixes the deliverable's required content (≥ 5 genuine unknowns, *"client's data, systems, and organisation"* coverage, *"what must be validated before building"*); Pack §6.5 fixes the rationale bar; Pack §7 names *"Filler unknowns"* (e.g. *"we'd need to confirm the exact UI"*) as a fail mode.
- **Upstream deliverables (strongly preferred — this deliverable is a consolidator, not an inventor):** the most recent runs under `Week1/Gate1/Output/` of
  - `problem-statement-{{scenario-slug}}-{NNN}.md` (Deliverable 1 — each row with an `[ASSUMED]` source label is an assumption to consolidate here, plus the existing A1–A7 register),
  - `delegation-analysis-{{scenario-slug}}-{NNN}.md` (Deliverable 2 — D1–D7 register; HC1–HC4 hard constraints; any open tension between a HUMAN assumption and the scenario text),
  - `agent-specification-{{scenario-slug}}-{NNN}.md` (Deliverable 3 — every `[UNKNOWN]` in integration contracts, every `[ASSUMED]` threshold in business rules, every S-anchor with a build-blocking dependency),
  - `validation-design-{{scenario-slug}}-{NNN}.md` (Deliverable 4 — V1–V7 register; assumptions about baseline behaviour, synthetic test data, sample sizes, detection windows; *"named accepted risks"* enumerated under §7).

  If any upstream file is missing, **flag the gap in the consolidated log rather than silently re-deriving**. The point of this deliverable is to *consolidate* the assumptions already surfaced across the other four into one register, not to re-invent them. Any genuinely new assumption that surfaces during consolidation is tagged AGENT and annotated *"surfaced during consolidation"* with the section that triggered it.

- **Standing sources** inherited per `CLAUDE.md` § *Prompt Authoring Conventions* (applied automatically, not restated):
  - `CLAUDE.md` — repository structure, Core Entities, diagram rules.
  - `SupportingDocs/Week1-Thinking-Discipline-Primer.md` — **reasoning and documentation style; this deliverable is the primer's most direct expression.** The Assumption / Hypothesis / Test / Confidence shape is mandatory. The Cagan four-risk lens (Value / Usability / Feasibility / Viability) categorises every entry.
  - `SupportingDocs/production-spec-checklist.md` — a `[UNKNOWN]` in the spec that is not consolidated here is a defect.
  - `SupportingDocs/spec-ambiguity-vs-builder-mistakes.md` — when the closed build loop surfaces a gap, this log is the first place to look.
  - `SupportingDocs/the-fde.md` — FDE Level 1 framing.

If the scenario file is not specified at run time, default to `Week1/Gate1/gate-scenario.md`.

## Output

Write a new file at:

```
Week1/Gate1/Output/assumptions-and-unknowns-{{scenario-slug}}-{random-3-digits}.md
```

where `{{scenario-slug}}` is the scenario filename without the `.md` extension (e.g. `gate-scenario`). Do not overwrite a previous run — always create a new file so iterations remain auditable.

## Required structure of the output

The output file must contain, in order:

### 1. Front-matter block

- Submission ID (filename without extension).
- Source scenario file path (relative link).
- Links to the upstream Deliverable 1–4 files consolidated, with their run suffixes. If any were not used, say so explicitly and name the gap as an Assumption Log entry.
- Date produced (`DD.MM.YYYY`).
- Status line — *"Gate 1 timed-exercise draft, no coach-session validation possible per Pack §2."* No assumption sits at **High**; entries are **Medium** or **Low** by construction. The Live Walkthrough (Pack §5) is a post-submission challenge, not a validation channel that can elevate confidence ratings before submission.

### 2. Scope and stance

Three to five sentences naming:

- This deliverable is the **single consolidated assumption register** for the Gate 1 scenario. Every `[ASSUMED]` or `[UNKNOWN]` referenced anywhere in Deliverables 1–4 must trace to a numbered entry here.
- Each entry is tagged **HUMAN** (participant-supplied, e.g. captured directly in `gate-scenario.md` during the timed exercise) or **AGENT** (identified during drafting; not settled by the scenario text or Pack rules).
- Confidence is **Low / Medium**. **High** is unavailable per Pack §2. An entry rated High in this deliverable is a defect — `CLAUDE.md` § *Prompt Authoring Conventions* reserves High for coach-session-validated assumptions, and the gate has no coach session.
- Pack §7 *"Bluffing"* and *"Filler unknowns"* anti-patterns apply directly. An assumption that reads *"we'd need to confirm the exact UI"* without naming the specific decision it gates is filler. Each entry must name the decision, threshold, integration shape, or rule that breaks if the assumption is wrong.

### 3. Scan table

Quick-read summary — one row per assumption. Every row in every upstream deliverable's Assumption Log must be represented.

| # | Source | Assumption (one line) | Cagan risk | Confidence | Upstream sections at risk if wrong |
|---|---|---|---|---|---|

Rules:

- **One line per assumption.** If an upstream log has the same assumption recorded twice (e.g. once in Deliverable 1 as A3 and once in Deliverable 2 as D1 — the *high-value or ambiguous* trigger codifiability is a worked example), consolidate to a single `#` and reference both upstream entries plus their sections in the final column.
- **Cagan risk** uses **Value / Usability / Feasibility / Viability** — the primer's four-risk lens. Multiple risks allowed; list the load-bearing one first.
- **Upstream sections at risk** names the specific section(s) of the specific file(s) that would need to change if the assumption were refuted (e.g. *"D3 §5.B.5 R-B-6; D4 §8 BV-1"*). This is the column a reviewer scans to see the blast radius.
- **Numbering scheme.** Use a single consolidated `#` (e.g. `U1`, `U2`, …) and cross-reference upstream entries in the body text. Do **not** reuse upstream prefixes (A/D/V) as primary keys — the consolidated register owns its own numbering, with upstream traceability captured in the rightmost column. (This avoids ambiguity when the same physical assumption appears as A3 in D1 and D1 in D2.)

Below the table:

- A one-line **overall read** stating how many entries are HUMAN vs AGENT, how many are Medium vs Low, and how many are open tensions (AGENT entries where a HUMAN assumption contradicts the scenario text, *or* where two upstream deliverables silently disagreed and the consolidation surfaced the disagreement). Per Pack §2, no entry is High.

### 4. Walkthrough / client-validation priority queue

A numbered list, highest-leverage first. Each item names the assumption number(s) and one sentence on *why* it ranks there. Under gate conditions none of these get resolved before submission — the queue is what the participant defends in the Live Walkthrough (Pack §5) and would take into a real client conversation.

Rules for prioritisation:

1. **Open tensions first.** An AGENT entry surfacing a HUMAN-vs-scenario-text contradiction, or a silent disagreement between two upstream deliverables, ranks above everything — resolving it redraws delegation rows, changes business rules, or invalidates a validation scenario.
2. **Build-blocking unknowns next.** A `[UNKNOWN]` that prevents a capability from being built end-to-end — for the FNOL scenario, the canonical examples are the SOAP WSDL for the legacy policy admin (request/response shape, latency, availability), the CRM tenant URL and OAuth scopes, the DMS API and retention policy, and the ack-channel SDK identity (transactional email vendor, SMS gateway, claimant portal). Pack §4 explicitly permits a *"named scope-out with a concrete plan to resolve"* — silent omission is not the same as an honest scope-out.
3. **Boundary-respect probes.** Anything affecting M5 — the *high-value or ambiguous* trigger codifiability (D1/A3), the boundary-violation detector mechanism (upstream §5.C.6), the audit-trail retention regime.
4. **Routing / ownership questions.** Which team owns the CRM write for the routing-rule table; who is the named on-call for `ESC-SOAP-DOWN`, `ESC-CRM-DOWN`, `ESC-ACK-FAIL`, `ESC-DMS-DOWN`, `ESC-BOUNDARY-VIOLATION`; who has authority to declare a `branch = ESCALATED` claim resolved.
5. **Value-risk probes.** The assumptions behind the headline success metrics M1 (SLA), M2 (routing-quality), M3 (specialist effort), M4 (claimant-experience), M5 (boundary-respect) — particularly any baseline that was `[ASSUMED]` rather than `[CITED]` (e.g. the `69% = 100 − 31% breach` derivation).
6. **Implementation-shape questions.** API specifics, rate limits, idempotency-key conventions per system, transactional-vs-async send semantics for the ack channels.
7. **Lower-urgency confirmations.** Severity rubric edge cases, peril-enum completeness, regional / state-level regulatory amendments not named in the scenario.

Treat the queue as a **scarce-interview-slot plan** per the primer: arrive at the next client conversation with a prioritised list of hypotheses to test, not open-ended chat. **No item moves to High in the gate window** — the queue is the bridge to the next conversation, not a record of validations performed.

### 5. Update protocol

Standard language, gate-aware:

> Update assumptions in place — never silently delete. If a Live Walkthrough challenge surfaces new evidence, leave the entry with strikethrough and append a dated `→ [REVISED]` annotation, plus a new numbered entry pointing at the replacement. **Confidence ratings cannot move to High within the Gate 1 window.** If a post-gate coach session subsequently validates an entry, raise the confidence in place and add a dated coach-session note; the `[ASSUMED]` tag remains on the original entry so the audit trail is preserved.
>
> If an assumption no longer traces to a HUMAN anchor (e.g. because a HUMAN assumption was refined and its operational details were lifted to new AGENT entries), retire with strikethrough and a footnote — do not delete.
>
> Any entry tagged *"surfaced during consolidation"* must name the upstream section that triggered the surfacing. Pack §7 *"Bluffing"* applies — an entry that asserts a regulator-mandated requirement (e.g. NAIC model act, state insurance code, HIPAA) without a citable section number is downgraded to `[UNKNOWN]` rather than carried as a hard constraint.

### 6. Full entries

One subsection per assumption, in the order they appear in the scan table. Each subsection uses the primer shape verbatim:

**U# — <one-line title>** _(HUMAN | AGENT — <Medium | Low>)_

- **Upstream traceability:** which upstream entries this consolidates (e.g. *"A3 (D1 §2.1); D1 (D2 §2.1)"*) — or *"surfaced during consolidation, triggered by D4 §9 *Spec gaps surfaced* item 1"*.
- **Assumption:** what is being taken as given.
- **Hypothesis:** *If [X is true], then [Y will happen], because [reasoning].*
- **How I'd test it:** the literal client-conversation question, prototype probe, or data check that would confirm or refute. For a client-conversation probe, write the literal question in quotes — *"Can you walk me through five recent claims your specialists flagged as 'ambiguous', and tell me what tipped each one over?"*. For a data probe, name the observable signal.
- **Confidence:** Low or Medium — **and why.** A bare rating is not sufficient; name the reason the rating is not higher (Pack §2 ceiling on High plus the specific evidentiary gap).

Required coverage — the entries must, at minimum, include assumptions about each of the following categories (per Pack §4's *"client's data, systems, and organisation"* framing):

- **Data** — extraction confidence distribution and per-broker drift; severity-rubric calibration; representativeness of synthetic test data used in Deliverable 4 happy-path / edge cases / failure modes; baseline-metric retrievability (the cited 31% / 18% / 22-min figures — what calculation produced them?).
- **Systems** — identity and shape of every system touched, including ack channels (the scenario names CRM with APIs, legacy policy admin with SOAP, document management; ack channels are implied by §3's intake list but not specified). For each: API availability and auth flavour; rate limits; tenant-specific endpoints; webhook availability; idempotency-key conventions; transactional vs. async semantics.
- **Organisation** — who owns which write in which system; named on-call for each `ESC-*` code; who has authority to declare a `branch = ESCALATED` claim resolved; willingness-to-adopt vs. willingness-to-provision-access (these are distinct); regulatory reach (state insurance code prompt-acknowledgement language; SIU / fraud workflow triggers; NAIC model acts; HIPAA on medical-claim PHI; jurisdictional workers'-comp rules) — none asserted as hard constraints unless cited (Pack §7 *"Bluffing"* applies).
- **Problem shape** — any open tension between a HUMAN assumption and the scenario text; any threshold in a success metric, business rule, or detection rule that is load-bearing and was `[ASSUMED]`; specifically the *high-value or ambiguous* trigger codifiability as the load-bearing tension for M5.

Any genuine unknown that does not fit those categories is welcome — the four are the floor, not a ceiling.

### 7. Genuine unknowns — the "I don't know" list

A short, explicit enumeration of questions to which the honest answer today is *"I don't know"*, even after consolidating the upstream assumption logs. Each item is one line, numbered, and references the consolidated entry in §6 that formalises it (every item must have an entry in §6).

Per Pack §4, **≥ 5 items**. Per Pack §6.5 and §7 *"Filler unknowns"*, every item must be a real thing the participant does not know — not *"we'd need to confirm the exact UI"*-shaped filler. A reviewer should be able to read this section alone and see where the spec is load-bearing on things that have not been tested.

For the FNOL scenario the canonical floor (each must have a §6 entry) is:

1. The codifiable definition of *high-value or ambiguous* — the scenario's only qualitative phrase, load-bearing for M5 and the entire escalated branch.
2. The legacy policy admin SOAP shape — WSDL, latency / availability, fault semantics, idempotency for any write paths.
3. The CRM tenant identity and OAuth scope catalogue — endpoint paths, rate limits, webhook availability, system-of-record for claim records vs. policy admin.
4. The ack-channel inventory and vendor identity — transactional email, SMS gateway, claimant portal: which is one system, which is three, and what each costs in tokens / dollars per send.
5. The audit-trail retention regime — no scenario citation, no inferred regulatory cover (Pack §7 *"Bluffing"*); the regime drives `HumanDecision` table sizing, log retention, and FQ-* sample-audit cadence.
6. The historical baseline distribution for `severity_band × peril` — the comparator behind the FQ-3 KL-divergence detector, build-blocking if it does not exist.

Add scenario-specific items beyond this floor as upstream deliverables surface them. Filler additions are penalised — Pack §7 names this anti-pattern explicitly.

### 8. What must be validated before building

Three subsections, each a short list. Pack §4 *"What must be validated before building?"* is the explicit prompt question — answer it in plain language, with citations.

- **Blocking — cannot start building until resolved.** Typically build-blocking integration unknowns (SOAP WSDL, CRM tenant URL + OAuth, DMS API, ack-channel vendor identity) and any open HUMAN-vs-scenario tension that would redraw the delegation boundary or invalidate a Deliverable 4 boundary test.
- **Soft-blocking — can start building around, but a specific capability or branch depends on resolution.** Typically the *high-value or ambiguous* trigger codifiability (D1/A3) — Capabilities A and C build cleanly; the escalated branch in Capability B and BV-1 / BV-2 in Deliverable 4 depend on it. Also: rate limits per integration; sample-audit capacity (V5).
- **Non-blocking but load-bearing — build can proceed; validation changes the confidence of the business case, not the architecture.** Typically baseline-metric accuracy (M1–M3 baselines); ack-channel send-rate cost economics; severity-rubric calibration; threshold values in detection rules (FQ-1 sample %, FQ-3 KL-divergence threshold, FQ-5 confidence-drift window).

Each item cites the consolidated assumption number(s) from §6 and the upstream section(s) it would force a revision to.

Close §8 with a one-line **recommended next client-conversation probe** — the single highest-leverage question to ask, drawn from the top of the priority queue in §4. This is what a stakeholder sees first if they scan the deliverable.

### 9. Diagrams

No diagrams in this deliverable — the Assumption Log is a text artefact by design, and no trigger in `CLAUDE.md` § *Diagrams* fires. State explicitly: *"No diagram — the log is the artefact."*

If a later revision genuinely needs a diagram (e.g. a dependency graph between assumptions, where resolving U2 unblocks U7 which unblocks Capability B), raise it first rather than adding one silently.

### 10. Self-audit (against Pack §6.5 / §7)

A checklist the draft must pass before the file is declared complete. Tick `[x]` only if honestly true.

- [ ] Every `[ASSUMED]` or `[UNKNOWN]` reference in upstream Deliverable 1–4 files has a matching numbered entry in §6 (with explicit upstream traceability per entry).
- [ ] Every entry is tagged **HUMAN** or **AGENT**.
- [ ] Every entry has Upstream traceability, Assumption, Hypothesis, How I'd test it, and Confidence — none are skipped.
- [ ] **No entry is rated High** (Pack §2 ceiling).
- [ ] Every open tension between a HUMAN assumption and the scenario text — and every silent disagreement between two upstream deliverables surfaced during consolidation — is captured as a distinct AGENT entry, not silently resolved.
- [ ] The scan table in §3 and the full entries in §6 are consistent — same `#`, same tag, same confidence, same one-line summary.
- [ ] The Pack §4 floor of **≥ 5 genuine unknowns** is cleared by the §7 list. Each item is real (not Pack §7 *"filler"*) and references a §6 entry.
- [ ] The walkthrough / client-validation priority queue in §4 is ordered by leverage, not by entry number.
- [ ] The "what must be validated before building" section in §8 is split into Blocking / Soft-blocking / Non-blocking with explicit citations to §6 entries.
- [ ] No `[TODO]` markers remain open. Where time has run out, the gap is *named as a scope-out* (Pack §4) — not silently omitted (Pack §7).
- [ ] No upstream deliverable was silently re-derived here — where an upstream file is missing, the gap is flagged in the Assumption Log, not filled.
- [ ] No regulatory citation is asserted as a hard constraint without a section / model-act / code reference (Pack §7 *"Bluffing"*).

Close §10 with a one-paragraph **overall assumption-register read** — whether a reviewer could confidently scan this log and know where the spec is load-bearing, whether the Pack §6.5 question *"are at least five genuine unknowns surfaced — real, not filler?"* can be honestly answered yes, and which one entry is the highest-leverage open question for the Live Walkthrough.

### 11. Out of scope for this deliverable

One short paragraph naming what this file deliberately does *not* cover:

- Problem statement and success metrics (Deliverable 1).
- Delegation analysis (Deliverable 2).
- Agent specification (Deliverable 3).
- Validation design (Deliverable 4).

Cross-link to the companion prompts in `Week1/Gate1/Prompts/` so a reviewer knows where the rest of the picture lives.

## Self-audit before declaring the output complete

(Prompt-level audit, distinct from the in-document §10 audit. Both must pass.)

- [ ] The output sits under `Week1/Gate1/Output/` with the naming convention above, and does not overwrite a prior run.
- [ ] Every upstream Deliverable 1–4 file present on disk was loaded and its Assumption Log entries consolidated.
- [ ] No new assumption has been invented in this deliverable that was not already implicit in an upstream `[ASSUMED]` / `[UNKNOWN]` marker — if genuinely new assumptions surfaced during consolidation, they are tagged AGENT and noted as *"surfaced during consolidation"* with the triggering upstream section.
- [ ] No upstream deliverable was edited as a side-effect of this prompt — if this log reveals an upstream inconsistency, the inconsistency is flagged here and the upstream prompt is re-run, not patched by hand.
- [ ] `SupportingDocs/the-fde.md` was not modified.
- [ ] The Cagan four-risk vocabulary is used verbatim — not invented synonyms.
- [ ] No Pack §7 anti-pattern (Bluffing, Filler unknowns, Hand-waving verbs) is triggered in the body of the deliverable.

## Regeneration

If any upstream deliverable changes — particularly when a new HUMAN assumption is added to the scenario file, when an agent-spec `[UNKNOWN]` is resolved or a new one is surfaced, or when Deliverable 4 surfaces a new spec gap — regenerate this deliverable rather than hand-editing it. The consolidated log is the cheapest place in the gate to notice drift between the four upstream deliverables, and the closed build loop depends on it staying honest. A divergence between this log and the upstream source of a given assumption is a defect, diagnosed the same way per `SupportingDocs/spec-ambiguity-vs-builder-mistakes.md`. Confidence ratings cannot move to **High** within the Gate 1 window (no coach session per Pack §2); regeneration is therefore driven by *new or revised* assumptions and *new or revised upstream entries*, not by validation upgrades.
