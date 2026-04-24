# Prompt — Problem Statement and Success Metrics (Week 1 Deliverable 1)

This prompt produces **Deliverable 1** of the Week 1 task, as defined in `SupportingDocs/README-Participants-Week1-Scenarios.md` § *How to work with your chosen scenario*:

> *A problem statement and success metrics tied to the numbers given in your scenario (not generic business-speak).*

It is intentionally scoped to that one deliverable. It does **not** produce the delegation analysis, capability spec, validation design, or the full assumptions section — those are separate prompts under `Week1/Prompts/`.

---

## Inputs

- **Scenario file (required):** a prompt-scoped scenario file in the same `Prompts/` folder — e.g. `Week1/Prompts/scenario-1.md`. The scenario file contains the scenario text verbatim plus the HUMAN assumptions with Assumption / Hypothesis / Test / Confidence.
- **Standing sources** inherited per `CLAUDE.md` § *Prompt Authoring Conventions* (do not restate them — they are applied automatically):
  - `CLAUDE.md` — repository structure, Core Entities, diagram rules.
  - `SupportingDocs/Week1-Thinking-Discipline-Primer.md` — reasoning and documentation style.
  - `SupportingDocs/README-Participants-Week1-Scenarios.md` — output expectations for Week 1.
  - `SupportingDocs/production-spec-checklist.md` — quality bar.
  - `SupportingDocs/spec-ambiguity-vs-builder-mistakes.md` — diagnostic taxonomy.
  - `SupportingDocs/the-fde.md` — FDE role and Level 1 framing.

If the scenario file is not specified at run time, default to `Week1/Prompts/scenario-1.md`.

## Output

Write a new file at:

```
Week1/Output/Scenario{M}/problem-statement-{{scenario-slug}}-{random-3-digits}.md
```

where `{{scenario-slug}}` is the scenario filename without the `.md` extension (e.g. `scenario-1`) and `{M}` matches the scenario number. Do not overwrite a previous run — always create a new file so iterations remain auditable.

## Required structure of the output

The output file must contain, in order:

### 1. Front-matter block

- Submission ID (filename without extension).
- Source scenario file path (relative link).
- Date produced (`DD.MM.YYYY`).
- Status line — e.g. *"first draft, pre-coach-session"* or note which HUMAN assumptions from the scenario file are already coach-validated (**High**).

### 2. Assumption Log (at the top, per primer)

Same shape as in `build-spec.md` Prompt 1, scoped to assumptions that load-bear on the problem statement and success metrics only:

- **Scan table** — one row per assumption: `#`, source (HUMAN / AGENT), one-line assumption, Cagan risk attacked (Value / Usability / Feasibility / Viability), confidence, which metric or statement is at risk if wrong.
- **Coach-session priority queue** — ordered, highest-leverage first, for the deliverables in this file.
- **Update protocol** — standard "update in place, do not silently delete" language from the primer.
- **Full entries** — Assumption / Hypothesis / How I'd test it / Confidence for each numbered entry.

Rules inherited from `CLAUDE.md` § *Prompt Authoring Conventions* apply verbatim:

- Every non-trivial claim is **[CITED]** (scenario text, named regulation, explicit prompt rule) or **[ASSUMED]** (numbered Assumption Log entry).
- **High** confidence requires coach-session validation; otherwise use **Medium** or **Low**.
- Unknowns are marked `[UNKNOWN]` and raised in the Assumption Log — never silently filled in.

### 3. The Problem Being Solved

A tight, evidence-anchored paragraph. Every number in this section must be `[CITED]` from the scenario file or derived explicitly from one (e.g. `220 × 40 ≈ 8,800 tasks/year` — cite the ratio, show the arithmetic).

- Name the organisation shape (employees, annual hire volume, team size owning the work).
- Name the work shape (how many tasks, over what duration, across how many systems).
- Name the judgment-vs-routine split as given.
- Include the **stakeholder quote verbatim** from the scenario with role attribution.
- Do not add a number the scenario does not give. Do not infer a pain metric that is not stated.

### 4. Why Agentic, Why Now

Three short paragraphs — **Volume**, **Repeatability**, **Constraint** — each tied to the scenario numbers or cited framing. No generic business-speak. This is the *"why the problem is fit for an agent at all"* framing, not a sales pitch.

### 5. Success Metrics

A single table. Columns:

| Metric | Current State | Target State | Measurement Method | Source |
|---|---|---|---|---|

Rules for the table:

- **Current State:** If the scenario gives a baseline, cite it. If it does not, write `[UNKNOWN — baseline needed]` and raise it as an Assumption Log entry (do not guess).
- **Target State:** Every target must be numeric and testable. If the threshold is invented, mark it `[ASSUMED]` and trace to a numbered entry. Do not claim a target is "Non-negotiable" unless it is [CITED] from the scenario or a named regulation.
- **Measurement Method:** Name the observable artefact or log that would produce the number in production (e.g. `onboardings_with_no_incomplete_task_at_day_14 / total_onboardings`). No "we'll track it" hand-waving.
- **Source:** Use the exact labels the stakeholder deck will inherit — `[CITED]`, `[ASSUMED] — A#`, or `(Non-negotiable)` where the scenario or regulation fixes the target. **Do not hide "needs validation" behind polished wording** — the primer's anti-pattern *"polished spec that dodges the riskiest unknown"* applies directly here.

Include at minimum:

1. A **routine-delegation** metric (% of routine tasks executed with no human action).
2. A **human-effort** metric (time-per-onboarding or equivalent cost measure).
3. A **quality / "fell through the cracks"** metric tied to the scenario's own pain language.
4. A **boundary-respect** metric expressed as a non-negotiable (every judgment-classified task reaches a logged human decision; zero silent agent decisions). This is Non-negotiable per the scenario's judgment-call framing and, where applicable, named regulation.

Below the table, a one-line note naming which rows rest on assumed baselines and must be converted to `[TESTED]` via a coach session before the spec is treated as business-aligned.

### 6. Out of scope for this deliverable

One short paragraph naming what this file deliberately does *not* cover:

- Delegation analysis (Deliverable 2).
- Capability specification (Deliverable 3).
- Validation design (Deliverable 4).
- The full assumptions / unknowns register (Deliverable 5).

Cross-link to the companion prompts in `Week1/Prompts/` where relevant (`build-spec.md`, `assumptions-and-unknowns.md`, etc.) so a reviewer knows where the rest of the picture lives.

## Self-audit before declaring the output complete

- [ ] Every number in *The Problem Being Solved* is either `[CITED]` from the scenario file or a labelled derivation of a cited number.
- [ ] The stakeholder quote is verbatim and attributed to the named role in the scenario.
- [ ] Every target in the Success Metrics table is numeric, has a measurement method, and carries an honest source label.
- [ ] No `[ASSUMED]` target is implicitly presented as settled fact.
- [ ] Every `[ASSUMED]` or `[UNKNOWN]` in the body has a matching numbered entry in the Assumption Log.
- [ ] The boundary-respect / non-negotiable metric is present and correctly labelled.
- [ ] File lives under `Week1/Output/Scenario{M}/` and the filename follows the naming convention above.
- [ ] No invented infrastructure, integration shape, or capability language has leaked in from later deliverables.

## Regeneration

If the scenario file is edited — especially its HUMAN assumptions confidence ratings — regenerate this deliverable rather than hand-editing it. A divergence between the scenario file and this output is a defect, diagnosed the same way a divergence between spec and built software is diagnosed in the closed build loop.

