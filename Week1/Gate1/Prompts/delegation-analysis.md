# Prompt — Delegation Analysis (Gate 1 Deliverable 2)

This prompt produces **Deliverable 2** of the Gate 1 timed exercise, as defined in [`Week1/Gate1/SupportingDocs/Gate1-Participant-Pack.md`](../SupportingDocs/Gate1-Participant-Pack.md) §4:

> **Delegation analysis** — *For each part of FNOL processing, decide: fully agentic / agent-led with human oversight / human-led with agent support / human only. Justify each boundary. Arbitrary boundaries ("this feels like a human decision") will be challenged.*

It is intentionally scoped to that one deliverable. It does **not** produce the problem statement, agent specification, validation design, or the full assumptions & unknowns register — those are separate prompts under `Week1/Gate1/Prompts/`.

The "why" column is the point of this deliverable. A row that lists a classification without a defensible rationale rooted in the scenario, a named regulation, or a numbered Assumption Log entry is a failed row — both per the primer's anti-pattern *"arbitrary splits you couldn't defend against a coach's 'why there?'"* and per Pack §6.2 *"Are delegation boundaries justified with clear rationale, not drawn arbitrarily? Is the codifiability of each agentic step addressed?"*.

---

## Inputs

- **Scenario file (required):** [`Week1/Gate1/gate-scenario.md`](../gate-scenario.md). Contains the §3 scenario text verbatim plus any HUMAN assumptions captured during the timed exercise (Assumption / Hypothesis / Test / Confidence). **There is no coach session inside the Gate 1 window** (Pack §2 — 2.5 hours, scenario unseen, submission closes before the Live Walkthrough). Treat everything that is not directly cited from the scenario or the Pack as an **assumption**. No assumption in this deliverable can carry **High** confidence. The Live Walkthrough (Pack §5) is a post-submission challenge, not a coach session that can elevate the document's confidence ratings before submission.
- **Gate 1 Participant Pack (authoritative):** [`Week1/Gate1/SupportingDocs/Gate1-Participant-Pack.md`](../SupportingDocs/Gate1-Participant-Pack.md). Pack §4 fixes the four-classification vocabulary; §6.2 fixes the rationale bar; §7 *"Hand-waving verbs"* and *"Bluffing"* anti-patterns apply directly to this deliverable.
- **Companion deliverable (if produced):** the most recent problem statement under `Week1/Gate1/Output/problem-statement-{{scenario-slug}}-{NNN}.md`. The boundary-respect metric in §7 below must align with the M5 row in that document.
- **Standing sources** inherited per `CLAUDE.md` § *Prompt Authoring Conventions* (applied automatically, not restated):
  - `CLAUDE.md` — repository structure, Core Entities, diagram rules.
  - `SupportingDocs/Week1-Thinking-Discipline-Primer.md` — reasoning and documentation style.
  - `SupportingDocs/production-spec-checklist.md` — quality bar.
  - `SupportingDocs/spec-ambiguity-vs-builder-mistakes.md` — diagnostic taxonomy.
  - `SupportingDocs/the-fde.md` — FDE role framing; specifically the ATX *Delegation Archetypes* (Full delegation / Human-in-the-loop / AI assistance / Hybrid) and *Cognitive Zones*. The Pack's four labels map onto these archetypes — see §3 below.

If the scenario file is not specified at run time, default to `Week1/Gate1/gate-scenario.md`.

## Output

Write a new file at:

```
Week1/Gate1/Output/delegation-analysis-{{scenario-slug}}-{random-3-digits}.md
```

where `{{scenario-slug}}` is the scenario filename without the `.md` extension (e.g. `gate-scenario`). Do not overwrite a previous run — always create a new file so iterations remain auditable.

## Required structure of the output

The output file must contain, in order:

### 1. Front-matter block

- Submission ID (filename without extension).
- Source scenario file path (relative link).
- Date produced (`DD.MM.YYYY`).
- Status line — *"Gate 1 timed-exercise draft, no coach-session validation possible per Pack §2."* All assumptions in §2 sit at **Medium** or **Low** by construction; **High** is not available for this deliverable.
- Cross-links to companion deliverables under `Week1/Gate1/Output/` if they exist (problem statement, agent spec).

### 2. Assumption Log (at the top, per primer)

Same shape as in the other Gate 1 prompts, scoped to assumptions that load-bear on the delegation boundary only:

- **Scan table** — one row per assumption: `#`, source (HUMAN / AGENT), one-line assumption, Cagan risk attacked (Value / Usability / Feasibility / Viability), confidence, which row or hard constraint is at risk if wrong.
- **Walkthrough / client-validation priority queue** — ordered, highest-leverage first. The assumption whose resolution would *move rows in the work inventory* ranks highest. This is the queue the participant defends in the Live Walkthrough (Pack §5) and would take into a real client conversation; under gate conditions none of these get resolved before submission.
- **Update protocol** — standard "update in place, do not silently delete" language from the primer. If an assumption is refuted, leave strikethrough and add a new numbered entry for the replacement.
- **Full entries** — Assumption / Hypothesis / How I'd test it / Confidence for each numbered entry.

Rules inherited from `CLAUDE.md` § *Prompt Authoring Conventions* apply verbatim, with one Gate 1-specific tightening:

- Every non-trivial claim is **[CITED]** (scenario text, named regulation, explicit prompt rule) or **[ASSUMED]** (numbered Assumption Log entry).
- **There is no coach session inside the Gate 1 window.** **High** confidence is therefore not available for any assumption in this deliverable — use **Medium** or **Low**. Treat anything not directly traceable to the scenario or the Pack as an assumption.
- Unknowns are marked `[UNKNOWN]` and raised in the Assumption Log — never silently filled in.
- The HUMAN / AGENT distinction still applies, but in practice the scenario file's HUMAN assumptions section is empty under gate conditions, so most or all entries will be **AGENT**. Do not invent HUMAN assumptions to give the impression of validation.
- Pack §7 *"Bluffing"* applies: confident classifications about systems, data, or constraints the scenario did not state — and the participant did not mark as an assumption — will be challenged.

### 3. Delegation Framework (brief)

Three to five sentences naming the classification vocabulary used in the work inventory table. Use the **Pack §4 four-label vocabulary verbatim**, mapped to the ATX archetypes from `SupportingDocs/the-fde.md`:

- **FULLY AGENTIC** — agent executes end-to-end without per-instance human action; rule-governed, reversible, deterministic against named systems. (ATX *Full delegation*.)
- **AGENT-LED WITH HUMAN OVERSIGHT** — agent drafts / proposes / prepares; a named human must act (approve, confirm, sign off) before the system state changes externally. (ATX *Human-in-the-loop*.)
- **HUMAN-LED WITH AGENT SUPPORT** — a human decides; the agent surfaces evidence, drafts options, or compiles context, but does not take the decision. (ATX *AI assistance*.)
- **HUMAN ONLY** — no agent involvement; the work is reserved to humans by regulation, accountability, or scenario constraint. (Outside the ATX delegation continuum.)

State explicitly that classification is applied at the **task / decision** level, not at the capability level — a single FNOL pipeline step (e.g. routing) can contain rows in more than one category (e.g. routine routing FULLY AGENTIC; high-value routing AGENT-LED WITH HUMAN OVERSIGHT). Do not invent synonyms; the Pack's labels are the labels reviewers will look for.

### 4. Work Inventory (the main table)

A single table with the following columns:

| Step / Task / Decision | Classification | Rationale (why) | Source |
|---|---|---|---|

Rules for the table:

- **One row per task or per decision** — not per system, not per capability. If a pipeline step has a routine execution path and a judgment-call path, it produces two rows (e.g. *Triage by severity — routine* vs. *Triage by severity — high-value or ambiguous*).
- Decompose the scenario's named pipeline exhaustively. The Gate 1 scenario explicitly names four steps [CITED Pack §3]:
  1. **Triage by severity**
  2. **Validate against policy coverage**
  3. **Route to the appropriate adjuster**
  4. **Acknowledge to the claimant**
  Plus the implicit upstream / cross-cutting work the agent will inherit: intake-channel ingestion (email / phone transcript / web form), entity extraction from unstructured text, identity / policy lookup, escalation classification (the *"high-value or ambiguous"* test [CITED]), and audit-trail logging of every human decision.
- **Classification** uses one of the four labels from §3. No hybrids inside a cell — split into two rows instead.
- **Rationale** must name *why* in terms Pack §6.2 and the primer would accept:
  - What makes a FULLY AGENTIC row safe to delegate (rule-governed, reversible, named system of record, deterministic filter, codifiable threshold)?
  - What accountability or tacit judgement keeps a HUMAN-LED or HUMAN-ONLY row out of the agent's hands (regulatory exposure, irreversible payout decision, silent-error cost, the scenario's *"high-value or ambiguous"* clause [CITED])?
  - What is the specific human action a row in AGENT-LED WITH HUMAN OVERSIGHT requires, and what system state does it gate?
  - For HUMAN-LED WITH AGENT SUPPORT, what evidence does the agent compile, and what decision remains with the human?
- **Source** labels each row with **[CITED]** (scenario quote, named regulation, explicit prompt rule) or **[ASSUMED] — A#** (numbered Assumption Log entry). A row classified without a source label is not finished. Under gate conditions, **no row may be labelled as "settled" on the strength of a HUMAN assumption** — the scenario file's HUMAN section is empty in the timed exercise, and even where the participant adds one, no coach session is available to lift it to **High**.

Below the table, a short paragraph naming the rows that will move if the open tensions in the Assumption Log resolve the other way — per primer, make the conditional visible rather than quietly picking a side. The most common candidates in this scenario: the *high-value or ambiguous* threshold definition [scenario text is qualitative] and the SOAP coverage-validation latency / availability [Pack §7 *"Integration hand-wave"* applies if silently designed-around].

### 5. Hard Constraints on the Boundary

A second, smaller table listing the non-negotiable constraints that fix the classification of specific rows regardless of design preference:

| Constraint | Source | Effect on the boundary |
|---|---|---|

Include at minimum:

- **Human oversight for high-value or ambiguous claims.** [CITED] from Pack §3 *"open to full automation where appropriate but insist on human oversight for high-value or ambiguous claims"*. Fixes the classification of every escalated row to AGENT-LED WITH HUMAN OVERSIGHT or stricter.
- **2-hour acknowledgement SLA.** [CITED] from Pack §3. Forces the *Acknowledge to claimant* row toward FULLY AGENTIC for the bulk path — any human-in-loop step on the routine ack would consume the SLA budget and breach by design.
- **No silent agent decisions on the human-oversight side of the boundary.** Derived directly from the previous two and the boundary-respect metric in §7. [CITED] in spirit; the metric definition is the contract.

If the participant cites a specific named regulation (e.g. an applicable state insurance code, a DOI prompt-pay rule, a NAIC model act, a privacy regime such as HIPAA for medical-claim handling, or an internal audit-retention policy), it belongs in this table with the citation in the *Source* column. Do **not** invent a regulation: Pack §7 *"Bluffing"* applies. If a regulation is asserted but the participant cannot pin the citation, demote it to an Assumption Log entry instead of a hard constraint.

Every row in this table must be **[CITED]**. Hard constraints are not [ASSUMED] — if you cannot cite one, it is not a hard constraint, it is a design choice and belongs in the work inventory rationale.

### 6. Delegation Boundary Diagram (conditional)

Include a Mermaid diagram iff one or more of the `CLAUDE.md` § *Diagrams* triggers fires — most commonly, the work inventory has more than ~10 rows *or* a boundary test needs to show a veto / override path visually (the *"high-value or ambiguous"* escalation is exactly such a path).

When included:

- Follow `CLAUDE.md` § *Diagrams* verbatim: Mermaid only, `flowchart` (direction to be chosen), `classDef agent` / `classDef human`, dashed escalation edges with `ESC-*` labels, human-led node labels suffixed with `(human)`.
- Group external systems into named subgraphs (CRM, Policy Admin (SOAP), DMS, Email / SMS / Portal) where integration calls cross the boundary — these are the systems the scenario names verbatim [CITED].
- Caption immediately below the code block: `*Figure N — delegation boundary (work inventory §4)*`.
- The diagram must not introduce a task, decision, escalation, or integration that is not already named in §4 or §5. Diagram is a reader aid, not a source of new facts.

If none of the diagram triggers fire, state explicitly: *"No diagram — work inventory table is short enough that prose + table carry the structure."*

### 7. Boundary-Respect Metric (hand-off to Deliverable 1)

One short paragraph naming the single non-negotiable metric that the delegation analysis forces into the success metrics table of Deliverable 1:

> *100% of claims classified as **high-value or ambiguous** reach a logged `HumanDecision` before any irreversible action (routing-finalised, payout-initiated, claimant-comms-sent on the escalated branch). Zero silent agent decisions on the human-oversight side of the boundary.*

This exists so that when the problem-statement deliverable is regenerated, the boundary-respect row (M5 in the metrics table) does not drift or soften. Cite it back to §5 so the linkage is visible, and confirm it matches the M5 row in the most recent `problem-statement-{{scenario-slug}}-{NNN}.md` if one exists — divergence is a defect.

### 8. Out of scope for this deliverable

One short paragraph naming what this file deliberately does *not* cover:

- Problem statement and success metrics (Deliverable 1).
- Agent specification — inputs, outputs, business rules, decision thresholds, state machines, integration contracts (Deliverable 3).
- Validation design, edge cases, failure modes, *quiet-failure* detection (Deliverable 4).
- The full assumptions & unknowns register (Deliverable 5).

Cross-link to the companion prompts in `Week1/Gate1/Prompts/` so a reviewer knows where the rest of the picture lives.

## Self-audit before declaring the output complete

- [ ] Every row in the work inventory has a classification, a rationale, and a source label — no row is finished without all three.
- [ ] The four classification labels match Pack §4 verbatim (FULLY AGENTIC / AGENT-LED WITH HUMAN OVERSIGHT / HUMAN-LED WITH AGENT SUPPORT / HUMAN ONLY); no invented synonyms.
- [ ] No HUMAN assumption has been used to move a row from HUMAN-LED to FULLY AGENTIC without surfacing the tension in the Assumption Log. (No HUMAN assumption can carry **High** confidence in this deliverable; coach-session validation is unavailable per Pack §2.)
- [ ] No assumption in §2 carries **High** confidence; all entries sit at **Medium** or **Low** by construction.
- [ ] All four named pipeline steps (triage, coverage validation, routing, claimant acknowledgement) are present in the table, decomposed into routine vs. escalated rows where the scenario's *"high-value or ambiguous"* clause applies.
- [ ] Every hard constraint in §5 is **[CITED]**; none are **[ASSUMED]**. No invented regulations (Pack §7 *"Bluffing"*).
- [ ] The boundary-respect metric in §7 is present and named exactly as it will appear in the success metrics table of Deliverable 1 (M5 alignment).
- [ ] The ATX delegation archetype vocabulary from `SupportingDocs/the-fde.md` is mapped to the Pack §4 labels in §3, not used as a replacement vocabulary.
- [ ] If a Mermaid diagram is included, it follows `CLAUDE.md` § *Diagrams* conventions and introduces no new facts.
- [ ] Every `[ASSUMED]` or `[UNKNOWN]` in the body has a matching numbered entry in the Assumption Log.
- [ ] File lives under `Week1/Gate1/Output/` and the filename follows the naming convention above.
- [ ] No agent-spec language (state machines, idempotency keys, retry policies, SOAP request/response bodies, REST endpoints) has leaked in from later deliverables. Pack §7 *"Integration hand-wave"* applies the other way too — naming a SOAP boundary is fine, specifying the WSDL is Deliverable 3's job.

## Regeneration

If the scenario file is edited — e.g. a new HUMAN assumption is added during the timed window, or an existing entry is reframed — regenerate this deliverable rather than hand-editing it. A row moving from HUMAN-LED to FULLY AGENTIC (or vice versa) is exactly the kind of change that must be visible in a fresh run, with the old run kept on disk for the audit trail. Confidence ratings cannot move to **High** within the Gate 1 window (no coach session per Pack §2); regeneration in this gate is therefore driven by *new or revised* assumptions and by *cited* corrections, not by validation upgrades.
