# Prompt — Delegation Analysis (Week 1 Deliverable 2)

This prompt produces **Deliverable 2** of the Week 1 task, as defined in `SupportingDocs/README-Participants-Week1-Scenarios.md` § *How to work with your chosen scenario*:

> *A delegation analysis that names which parts of the work become fully agentic, agent-led with human oversight, or stay human-led — and **why**. The "why" is the skill being tested.*

It is intentionally scoped to that one deliverable. It does **not** produce the problem statement, capability spec, validation design, or the full assumptions register — those are separate prompts under `Week1/Prompts/`.

The "why" column is the point of this deliverable. A row that lists a classification without a defensible rationale rooted in the scenario, a named regulation, or a numbered Assumption Log entry is a failed row — per the primer's anti-pattern *"arbitrary splits you couldn't defend against a coach's 'why there?'"*.

---

## Inputs

- **Scenario file (required):** a prompt-scoped scenario file in the same `Prompts/` folder — e.g. `Week1/Prompts/scenario-1.md`. Contains the scenario text verbatim plus HUMAN assumptions with Assumption / Hypothesis / Test / Confidence.
- **Standing sources** inherited per `CLAUDE.md` § *Prompt Authoring Conventions* (applied automatically, not restated):
  - `CLAUDE.md` — repository structure, Core Entities, diagram rules.
  - `SupportingDocs/Week1-Thinking-Discipline-Primer.md` — reasoning and documentation style.
  - `SupportingDocs/README-Participants-Week1-Scenarios.md` — Week 1 expectations.
  - `SupportingDocs/production-spec-checklist.md` — quality bar.
  - `SupportingDocs/spec-ambiguity-vs-builder-mistakes.md` — diagnostic taxonomy.
  - `SupportingDocs/the-fde.md` — FDE role framing; specifically the ATX delegation archetypes (Full delegation / Human-in-the-loop / AI assistance / Hybrid) and Cognitive Zones.

If the scenario file is not specified at run time, default to `Week1/Prompts/scenario-1.md`.

## Output

Write a new file at:

```
Week1/Output/Scenario{M}/delegation-analysis-{{scenario-slug}}-{random-3-digits}.md
```

where `{{scenario-slug}}` is the scenario filename without the `.md` extension and `{M}` matches the scenario number. Do not overwrite a previous run — always create a new file so iterations remain auditable.

## Required structure of the output

The output file must contain, in order:

### 1. Front-matter block

- Submission ID (filename without extension).
- Source scenario file path (relative link).
- Date produced (`DD.MM.YYYY`).
- Status line — e.g. *"first draft, pre-coach-session"* or note which HUMAN assumptions from the scenario file are already coach-validated (**High**).
- Cross-links to companion deliverables under `Week1/Output/Scenario{M}/` if they exist (problem statement, capability spec).

### 2. Assumption Log (at the top, per primer)

Same shape as in `build-spec.md` Prompt 1, scoped to assumptions that load-bear on the delegation boundary only:

- **Scan table** — one row per assumption: `#`, source (HUMAN / AGENT), one-line assumption, Cagan risk attacked (Value / Usability / Feasibility / Viability), confidence, which row or hard constraint is at risk if wrong.
- **Coach-session priority queue** — ordered, highest-leverage first. The assumption whose resolution would *move rows in the work inventory* ranks highest.
- **Update protocol** — standard "update in place, do not silently delete" language from the primer. If an assumption is refuted, leave strikethrough and add a new numbered entry for the replacement.
- **Full entries** — Assumption / Hypothesis / How I'd test it / Confidence for each numbered entry.

Rules inherited from `CLAUDE.md` § *Prompt Authoring Conventions* apply verbatim:

- Every non-trivial claim is **[CITED]** (scenario text, named regulation, explicit prompt rule) or **[ASSUMED]** (numbered Assumption Log entry).
- **High** confidence requires coach-session validation; otherwise use **Medium** or **Low**.
- Unknowns are marked `[UNKNOWN]` and raised in the Assumption Log — never silently filled in.
- Any tension between a HUMAN assumption and the scenario text must be surfaced as an AGENT assumption with *"Medium-high that the tension exists; unknown which way it resolves"* — do not silently pick a side.

### 3. Delegation Framework (brief)

Three to five sentences naming the classification vocabulary used in the work inventory table, anchored in `SupportingDocs/the-fde.md` § *Delegation Archetypes* and § *Cognitive Zones*:

- **FULL DELEGATION** — agent executes end-to-end; routine, rule-governed, reversible.
- **HUMAN-IN-LOOP** — agent drafts / proposes / prepares; a named human must act (approve, confirm, sign off) before the system state changes.
- **HUMAN-LED** — a human decides; the agent may detect, flag, or compile evidence, but must not take the decision itself.

Make clear that the classification is applied at the **task / decision** level, not at the capability level — a single capability can contain rows in all three categories.

### 4. Work Inventory (the main table)

A single table with the following columns:

| Task / Decision | Classification | Rationale (why) | Source |
|---|---|---|---|

Rules for the table:

- **One row per task or per decision** — not per system, not per capability. If a task family has a routine execution and a judgment decision, it produces two rows (see Buddy matching: propose vs. final assign).
- Decompose the scenario's named task families exhaustively. For Scenario 1 that means IT provisioning, benefits enrolment, compliance training assignment, buddy matching, welcome materials, 30-day checkpoint scheduling, manager handoff, plus any judgment call the scenario names explicitly (classification, seniority-norm check, late-I-9 hold).
- **Classification** uses one of the three labels from § 3. No hybrids inside a cell — split into two rows instead.
- **Rationale** must name *why* in terms the primer would accept:
  - What makes a FULL row safe to delegate (rule-governed, reversible, named system of record, deterministic filter)?
  - What accountability or tacit judgement keeps a HUMAN-LED row out of the agent's hands (regulatory exposure, social norm, irreversible consequence, silent-error cost)?
  - What is the specific human action a HUMAN-IN-LOOP row requires, and what system state does it gate?
- **Source** labels each row with **[CITED]** (scenario quote, named regulation, explicit prompt rule) or **[ASSUMED] — A#** (numbered Assumption Log entry). A row classified without a source label is not finished.
- Where a HUMAN assumption in the scenario file is **High** (coach-validated), the resulting row may treat the classification as settled — but the rationale must still cite the specific assumption number (e.g. **H4** for the buddy three-factor filter).

Below the table, a short paragraph naming the rows that will move if the open tensions in the Assumption Log resolve the other way — per primer, make the conditional visible rather than quietly picking a side.

### 5. Hard Constraints on the Boundary

A second, smaller table listing the non-negotiable constraints that fix the classification of specific rows regardless of design preference:

| Constraint | Source | Effect on the boundary |
|---|---|---|

Include at minimum:

- Employment classification (contractor vs. full employee) — [CITED] prompt rule + IRS common-law test / ACA 30-hour rule / state ABC tests.
- I-9 Section 2 within 3 business days; hold decisions are human — [CITED] scenario + IRCA (8 U.S.C. § 1324a).
- Any scenario-specific "no permit decision without a named human plan reviewer"-style non-negotiable if the scenario names one.
- Audit-trail retention for human decisions (e.g. "every human decision is logged — 7-year retention"). This is the line the stakeholder deck will inherit on its delegation slide; it must exist and be sourced.

Every row in this table must be **[CITED]**. Hard constraints are not [ASSUMED] — if you cannot cite one, it is not a hard constraint, it is a design choice and belongs in the work inventory rationale.

### 6. Delegation Boundary Diagram (conditional)

Include a Mermaid diagram iff one or more of the `CLAUDE.md` § *Diagrams* triggers fires — most commonly, the work inventory has more than ~10 rows *or* a boundary test needs to show a veto/override path visually.

When included:

- Follow `CLAUDE.md` § *Diagrams* verbatim: Mermaid only, `flowchart` (direction to be chosen), `classDef agent` / `classDef human`, dashed escalation edges with `ESC-*` labels, human-led node labels suffixed with `(human)`.
- Group external systems into named subgraphs (Workday, ServiceNow, LMS, Email, Benefits, Payroll) where integration calls cross the boundary.
- Caption immediately below the code block: `*Figure N — delegation boundary (work inventory §4)*`.
- The diagram must not introduce a task, decision, escalation, or integration that is not already named in §4 or §5. Diagram is a reader aid, not a source of new facts.

If none of the diagram triggers fire, state explicitly: *"No diagram — work inventory table is short enough that prose + table carry the structure."*

### 7. Boundary-Respect Metric (hand-off to Deliverable 1)

One short paragraph naming the single non-negotiable metric that the delegation analysis forces into the success metrics table:

> *100% of judgment-classified tasks reach a logged `HumanDecision` before the task state can become `COMPLETE`. Zero silent agent decisions.*

This exists so that when the problem-statement deliverable is regenerated, the boundary-respect row does not drift or soften. Cite it back to §5 so the linkage is visible.

### 8. Out of scope for this deliverable

One short paragraph naming what this file deliberately does *not* cover:

- Problem statement and success metrics (Deliverable 1).
- Capability specification — inputs, outputs, business rules, state machines, integration contracts (Deliverable 3).
- Validation design, edge cases, failure modes, boundary tests (Deliverable 4).
- The full assumptions / unknowns register (Deliverable 5).

Cross-link to the companion prompts (`problem-statement.md`, `build-spec.md`, `assumptions-and-unknowns.md`, etc.) so a reviewer knows where the rest of the picture lives.

## Self-audit before declaring the output complete

- [ ] Every row in the work inventory has a classification, a rationale, and a source label — no row is finished without all three.
- [ ] No HUMAN assumption marked **Low** or **Medium** in the scenario file has been used to move a row from HUMAN-LED to FULL DELEGATION without surfacing the tension as an AGENT assumption.
- [ ] Every **High**-confidence HUMAN assumption used to settle a row cites the assumption number in the rationale column.
- [ ] Every hard constraint in §5 is **[CITED]**; none are **[ASSUMED]**.
- [ ] The boundary-respect metric in §7 is present and named exactly as it will appear in the success metrics table.
- [ ] The ATX delegation archetype vocabulary from `SupportingDocs/the-fde.md` is used — not invented synonyms.
- [ ] If a Mermaid diagram is included, it follows `CLAUDE.md` § *Diagrams* conventions and introduces no new facts.
- [ ] Every `[ASSUMED]` or `[UNKNOWN]` in the body has a matching numbered entry in the Assumption Log.
- [ ] File lives under `Week1/Output/Scenario{M}/` and the filename follows the naming convention above.
- [ ] No capability-spec language (state machines, idempotency keys, retry policies, API endpoints) has leaked in from later deliverables.

## Regeneration

If the scenario file is edited — especially when a HUMAN assumption's confidence rating changes from Medium to High or a new HUMAN assumption is added — regenerate this deliverable rather than hand-editing it. A row moving from HUMAN-LED to FULL DELEGATION (or vice versa) is exactly the kind of change that must be visible in a fresh run, with the old run kept on disk for the audit trail.

