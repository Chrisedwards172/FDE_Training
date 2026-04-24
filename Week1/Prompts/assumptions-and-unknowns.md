# Prompt — Assumptions and Unknowns (Week 1 Deliverable 5)

This prompt produces **Deliverable 5** of the Week 1 task, as defined in `SupportingDocs/README-Participants-Week1-Scenarios.md` § *How to work with your chosen scenario*:

> *An honest assumptions & unknowns section — at least 5 genuine unknowns, not filler. What are you assuming about the client's data, systems, and organisation? What must be validated before building?*

It is intentionally scoped to that one deliverable. It does **not** produce the problem statement, delegation analysis, capability spec, or validation design — those are separate prompts under `Week1/Prompts/`.

This deliverable is the one where the primer's rule *"hidden assumptions are the failure mode; stated assumptions are discovery"* lands hardest. A plausible-sounding five entries will not pass. *"I don't know"* beats a confident guess, provided it is paired with a plan to find out.

---

## Inputs

- **Scenario file (required):** a prompt-scoped scenario file in the same `Prompts/` folder — e.g. `Week1/Prompts/scenario-1.md`. Contains the scenario text verbatim plus HUMAN assumptions with Assumption / Hypothesis / Test / Confidence.
- **Upstream deliverables (strongly preferred):** the most recent runs under `Week1/Output/Scenario{M}/` of
  - `problem-statement-*.md` (Deliverable 1 — each row with an `[ASSUMED]` source label is an assumption to consolidate here),
  - `delegation-analysis-*.md` (Deliverable 2 — each open tension between a HUMAN assumption and the scenario text surfaces as a load-bearing entry),
  - `capability-specification-*.md` (Deliverable 3 — every `[UNKNOWN]` in integration contracts, every invented threshold in business rules),
  - `validation-design-*.md` (Deliverable 4 — any assumption about baseline behaviour or synthetic test data).

  If any upstream file is missing, flag the gap in the consolidated log rather than silently re-deriving. The point of this deliverable is to *consolidate* the assumptions already surfaced across the other four, not to re-invent them.

- **Standing sources** inherited per `CLAUDE.md` § *Prompt Authoring Conventions* (applied automatically, not restated):
  - `CLAUDE.md` — repository structure, Core Entities, diagram rules.
  - `SupportingDocs/Week1-Thinking-Discipline-Primer.md` — **reasoning and documentation style; this deliverable is the primer's most direct expression.** The Assumption/Hypothesis/Test/Confidence shape is mandatory. The Cagan four-risk lens (Value / Usability / Feasibility / Viability) categorises every entry.
  - `SupportingDocs/README-Participants-Week1-Scenarios.md` — Week 1 expectations; *"at least 5 genuine unknowns, not filler"* is the floor, not the target.
  - `SupportingDocs/production-spec-checklist.md` — a `[UNKNOWN]` in the spec that is not consolidated here is a defect.
  - `SupportingDocs/spec-ambiguity-vs-builder-mistakes.md` — when the closed build loop surfaces a gap, this log is the first place to look.
  - `SupportingDocs/the-fde.md` — FDE Level 1 framing.

If the scenario file is not specified at run time, default to `Week1/Prompts/scenario-1.md`.

## Output

Write a new file at:

```
Week1/Output/Scenario{M}/assumptions-and-unknowns-{{scenario-slug}}-{random-3-digits}.md
```

where `{{scenario-slug}}` is the scenario filename without the `.md` extension and `{M}` matches the scenario number. Do not overwrite a previous run — always create a new file so iterations remain auditable.

## Required structure of the output

The output file must contain, in order:

### 1. Front-matter block

- Submission ID (filename without extension).
- Source scenario file path (relative link).
- Links to the upstream Deliverable 1–4 files consolidated, with their run suffixes. If any were not used, say so explicitly and name the gap.
- Date produced (`DD.MM.YYYY`).
- Status line — e.g. *"first draft, pre-coach-session"* or *"second draft, post-coach-session of 23.04.2026 (H4, H5, H6 moved to High)"*.

### 2. Scope and stance

Three to five sentences naming:

- This deliverable is the **single consolidated assumption register** for the scenario. Every `[ASSUMED]` or `[UNKNOWN]` referenced anywhere in Deliverables 1–4 must trace to a numbered entry here.
- Each entry is tagged **HUMAN** (participant-supplied, from the scenario file) or **AGENT** (identified during drafting; not settled by the scenario text or prompt rules).
- Confidence is **Low / Medium / High**. **High** is reserved for coach-session-validated assumptions per `CLAUDE.md` § *Prompt Authoring Conventions*. An AGENT entry rated High without a dated coach-session note is itself a red flag per the primer anti-pattern *"confusing 'I decided' with 'I validated'."*

### 3. Scan table

Quick-read summary — one row per assumption. Every row in every upstream deliverable's Assumption Log must be represented.

| # | Source | Assumption (one line) | Cagan risk | Confidence | Upstream sections at risk if wrong |
|---|---|---|---|---|---|

Rules:

- **One line per assumption.** If an upstream log has the same assumption recorded twice (e.g. once in Deliverable 1 and once in Deliverable 3), consolidate to a single `#` and reference both sections in the final column.
- **Cagan risk** uses **Value / Usability / Feasibility / Viability** — the primer's four-risk lens. Multiple risks allowed; list the load-bearing one first.
- **Upstream sections at risk** names the specific section(s) of the specific file(s) that would need to change if the assumption were refuted (e.g. *"Deliverable 3 §5.2 rule 2; Deliverable 4 EC-5"*). This is the column a reviewer scans to see where the blast radius is.

Below the table:

- A one-line **overall read** stating how many entries are HUMAN vs AGENT, how many are High / Medium / Low, and how many are open tensions (AGENT entries where a HUMAN assumption contradicts the scenario text). Per `CLAUDE.md`, no AGENT entry is rated High without coach-session validation.

### 4. Coach-session priority queue

A numbered list, highest-leverage first. Each item names the assumption number(s) and one sentence on *why* it ranks there.

Rules for prioritisation:

1. **Open tensions first.** An AGENT entry surfacing a HUMAN-vs-scenario-text contradiction ranks above everything — resolving it redraws delegation rows or changes business rules.
2. **Build-blocking unknowns next.** A `[UNKNOWN]` that prevents a capability from being built end-to-end (e.g. LMS vendor identity blocking webhook contract) ranks above thresholds and weights.
3. **Routing / ownership questions.** E.g. which team at HR Ops owns the Workday write for `employment_class` — wrong target makes an escalation route nowhere.
4. **Value-risk probes.** The assumptions behind the headline success metrics (routine-delegation %, time-per-onboarding reduction).
5. **Implementation-shape questions.** API specifics, rate limits, catalog-bundle vs. per-asset provisioning.
6. **Lower-urgency confirmations.** Role taxonomy size, state-level regulatory amendments, ranking weights.

Treat the queue as a **scarce-interview-slot plan** per the primer: arrive at the next coach session with a prioritised list of hypotheses to test, not open-ended chat.

### 5. Update protocol

Standard language, verbatim:

> After each coach session, update the affected entry **in place**: raise or lower confidence, add a dated note, and change any dependent spec prose in the upstream deliverables.
>
> **Do not silently delete an assumption.** If an assumption is refuted, leave it with strikethrough and add a new numbered entry pointing at the replacement. If an assumption no longer traces to a HUMAN anchor (e.g. because a HUMAN assumption was refined and its operational details were lifted to new AGENT entries), retire with strikethrough and a footnote — do not delete.
>
> `[ASSUMED]` items do not migrate to a new source tag after a coach session. The original entry carries a dated confirmation note; the `[ASSUMED]` tag remains so the audit trail is preserved for Friday peer review.

### 6. Full entries

One subsection per assumption, in the order they appear in the scan table. Each subsection uses the primer shape verbatim:

**H#/A# — <one-line title>** _(HUMAN | AGENT — <confidence>)_

- **Assumption:** what is being taken as given.
- **Hypothesis:** *If [X is true], then [Y will happen], because [reasoning].*
- **How I'd test it:** the coach session question, prototype probe, or data check that would confirm or refute. For a coach-session probe, write the literal question in quotes — *"Who on your team has Workday write access to `workerType`, and what is your standard turnaround?"*. For a data probe, name the observable signal.
- **Confidence:** Low / Medium / High — **and why.** A bare rating is not sufficient; name the reason it is not higher (or, for coach-validated Highs, name the date and substance of the validation).

Required coverage — the entries must, at minimum, include assumptions about each of the following categories (per the Week 1 brief's *"client's data, systems, and organisation"* framing):

- **Data** — role taxonomy shape and stability; baseline-metric retrievability; representativeness of synthetic test data.
- **Systems** — identity of every system touched (including unnamed ones in the scenario); API availability and auth flavour per system; rate limits; tenant-specific endpoints; catalog / bundle structures; webhook availability.
- **Organisation** — who owns which write in which system; who is the correct escalation target for each ESC-* code; willingness-to-adopt vs. willingness-to-provision-access (these are distinct); regulatory reach (federal-only vs. state amendments).
- **Problem shape** — any open tension between a HUMAN assumption and the scenario text; any threshold in a success metric or business rule that is load-bearing and was not cited.

Any genuine unknown that does not fit those categories is welcome — the four are the floor, not a ceiling.

### 7. Genuine unknowns — the "I don't know" list

A short, explicit enumeration of questions to which the honest answer today is *"I don't know"*, even after consolidating the upstream assumption logs. Each item is one line, numbered, and references the Assumption Log entry that formalises it (every item must have an entry in §6).

Per the Week 1 brief, ≥ 5 items. Per the primer, *"I don't know" beats a plausible-sounding guess* — the purpose of this section is to make the unknowns impossible to miss on a glance. A reviewer should be able to read this section alone and see where the spec is load-bearing on things that have not been tested.

### 8. What must be validated before building

Three subsections, each a short list.

- **Blocking — cannot start building until resolved.** Typically build-blocking integration unknowns (LMS vendor, auth flavours, tenant URLs) and any open HUMAN-vs-scenario tension that would redraw the delegation boundary.
- **Soft-blocking — can start building around, but a specific capability or branch depends on resolution.** Typically catalog-bundle shape, rate limits, state-level regulatory amendments, role-taxonomy stability.
- **Non-blocking but load-bearing — build can proceed; validation changes the confidence of the business case, not the architecture.** Typically adoption willingness, baseline-metric accuracy, threshold values in success metrics.

Each item cites the assumption number(s) from §6 and the upstream section(s) it would force a revision to.

Close §8 with a one-line **recommended next coach-session probe** — the single highest-leverage question to ask, drawn from the top of the priority queue in §4. This is what a stakeholder sees first if they scan the deliverable.

### 9. Diagrams

No diagrams in this deliverable — the Assumption Log is a text artefact by design, and no trigger in `CLAUDE.md` § *Diagrams* fires. State explicitly: *"No diagram — the log is the artefact."*

If a later revision genuinely needs a diagram (e.g. a dependency graph between assumptions, where resolving A8 unblocks A10 which unblocks a capability), raise it first rather than adding one silently.

### 10. Self-audit

A checklist the draft must pass before the file is declared complete. Tick `[x]` only if honestly true.

- [ ] Every `[ASSUMED]` or `[UNKNOWN]` reference in the upstream Deliverable 1–4 files has a matching numbered entry in §6.
- [ ] Every entry is tagged **HUMAN** or **AGENT**.
- [ ] Every entry has Assumption, Hypothesis, How I'd test it, and Confidence — none are skipped.
- [ ] No AGENT entry is rated **High** unless a dated coach-session note justifies it.
- [ ] Every open tension between a HUMAN assumption and the scenario text is surfaced as a distinct AGENT entry, not silently resolved in favour of either side.
- [ ] The scan table in §3 and the full entries in §6 are consistent — same `#`, same tag, same confidence, same one-line summary.
- [ ] The Week 1 floor of ≥ 5 genuine unknowns is cleared by the §7 list, and none of the items are filler.
- [ ] The coach-session priority queue in §4 is ordered by leverage, not by entry number.
- [ ] The "what must be validated before building" section in §8 is split into Blocking / Soft-blocking / Non-blocking with explicit citations to Assumption Log entries.
- [ ] No `[TODO]` markers remain open.
- [ ] No upstream deliverable was silently re-derived here — where an upstream file is missing, the gap is flagged, not filled.

Close §10 with a one-paragraph **overall assumption-register read** — whether a reviewer could confidently scan this log and know where the spec is load-bearing, and whether the Week 1 self-check question *"would a reviewer be able to challenge my thinking because I've exposed it, rather than in spite of hiding it?"* can be honestly answered yes.

### 11. Out of scope for this deliverable

One short paragraph naming what this file deliberately does *not* cover:

- Problem statement and success metrics (Deliverable 1).
- Delegation analysis (Deliverable 2).
- Capability specification (Deliverable 3).
- Validation design (Deliverable 4).

Cross-link to the companion prompts in `Week1/Prompts/` so a reviewer knows where the rest of the picture lives.

## Self-audit before declaring the output complete

(Prompt-level audit, distinct from the in-document §10 audit. Both must pass.)

- [ ] The output sits under `Week1/Output/Scenario{M}/` with the naming convention above, and does not overwrite a prior run.
- [ ] Every upstream Deliverable 1–4 file present on disk was loaded and its Assumption Log entries consolidated.
- [ ] No new assumption has been invented in this deliverable that was not already implicit in an upstream `[ASSUMED]` / `[UNKNOWN]` marker — if genuinely new assumptions surfaced during consolidation, they are tagged AGENT and noted as "surfaced during consolidation" in the entry.
- [ ] No upstream deliverable was edited as a side-effect of this prompt — if this log reveals an upstream inconsistency, the inconsistency is flagged here and the upstream prompt is re-run, not patched by hand.
- [ ] `SupportingDocs/the-fde.md` was not modified.
- [ ] The Cagan four-risk vocabulary is used verbatim — not invented synonyms.

## Regeneration

If any upstream deliverable changes — particularly when an assumption's confidence rating moves after a coach session, when a new HUMAN assumption is added to the scenario file, or when a capability-spec `[UNKNOWN]` is resolved — regenerate this deliverable rather than hand-editing it. The consolidated log is the cheapest place in the programme to notice drift between the four upstream deliverables, and the closed build loop depends on it staying honest. A divergence between this log and the upstream source of a given assumption is a defect, diagnosed the same way per `SupportingDocs/spec-ambiguity-vs-builder-mistakes.md`.

