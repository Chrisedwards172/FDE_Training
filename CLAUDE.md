# CLAUDE.md — FDE Accelerated Development Program

## Project Purpose

This repository contains the participant-facing documentation, source materials, and supporting resources for the **Forward Deployed Engineer (FDE) Accelerated Development Program** — a 5-week intensive training program that develops practitioners who direct AI agents to build software systems through precise specification, rather than writing code themselves.

The primary audience is program participants (FDE trainees), coaches, and squad leads. The primary outputs are markdown documentation files: weekly README guides, scenario files, reference materials, and supporting methodology artifacts.

## What This Repository Is

- A **documentation repository** — all content is Markdown (`.md` files)
- A **living curriculum** — files are iteratively refined as the program evolves
- A **reference library** — participants use these files daily during the 5-week program
- **Not** a software project — there is no application code, build system, or deployment pipeline

## Repository Structure

```
FDE_Training/
├── CLAUDE.md                          ← this file (shared project constitution)
├── Week1/
│   ├── CLAUDE.md                      ← Week 1 context, standing sources, output rules
│   ├── scenario-1.md                  ← practice scenario
│   ├── Prompts/                       ← prompts used during Week 1 practice
│   ├── Output/                        ← generated spec artefacts
│   ├── Gate1/                         ← Gate 1 deliverables
│   └── SupportingDocs/                ← Week 1 reference material
│       ├── README-Participants.md
│       ├── README-Participants-Intro-Week1.md
│       ├── README-Participants-Week1-Scenarios.md
│       ├── Week1-Thinking-Discipline-Primer.md
│       ├── claude-md-examples-guide.md
│       ├── production-spec-checklist.md
│       ├── spec-ambiguity-vs-builder-mistakes.md
│       └── the-fde.md
├── Week2/
│   ├── CLAUDE.md                      ← Week 2 context, ATX methodology, standing sources, output rules
│   └── SupportingDocs/                ← Week 2 reference material
│       ├── README-Participants-Week2.md
│       ├── discovery-questioning-patterns.md
│       ├── enriched_scenarios.md
│       ├── spec-ambiguity-vs-builder-mistakes.md
│       └── references/                ← ATX framework references
│           ├── atx-concepts.md
│           ├── atx-assessment.md
│           ├── atx-agent-mapping.md
│           ├── atx-scoring.md
│           └── atx-economics.md
```

> Note: Week 3–5 working areas and their `CLAUDE.md` files are expected to appear as the cohort progresses. Each `Week{N}/CLAUDE.md` inherits this root file and adds week-specific context. If a week folder exists without a `CLAUDE.md`, flag the gap rather than creating placeholder content.

## CLAUDE.md Inheritance Model

This root file is the **shared constitution** — naming conventions, diagram rules, authoring rules, and programme-wide entities. Each `Week{N}/CLAUDE.md` inherits everything here and adds:

- **Week-specific context** — what the week is about, its methodology, its deliverables
- **Standing sources** — which `SupportingDocs/` files prompts in that week must load
- **Output placement** — where artefacts for that week are written
- **Week-specific anti-patterns** — failure modes specific to that week's skill

When executing a prompt from `Week{N}/Prompts/`, load **both** this root `CLAUDE.md` and `Week{N}/CLAUDE.md`. If they conflict, flag the conflict — do not silently pick a side.

## Core Entities (Documentation Domain)

### Program
- 5-week accelerated development program
- Week structure: Intro + Week 1 combined, then Weeks 2–5 individually
- Calendar convention: **virtual days** (Mon–Fri labels) map to **physical dates** (actual calendar dates, adjusted for public holidays and cohort schedule)
- Key public holidays affecting the calendar: **1 May** and **14 May**

### Participant
- A trainee in the FDE program
- Progresses through 5 weekly gates (Gate 1–5), with rubrics sealed until gate begins
- Exception: Capstone rubric (Week 5) is shared at the start of Virtual Monday of Week 5
- Week 1: picks one of 7 practice scenarios at Virtual Monday orientation; works against it all week

### Gate / Deliverable
- Each week ends with a gate requiring specific deliverables (defined per weekly README)
- Rubrics are sealed until the gate begins — **do not invent rubric details** if they are not documented

### FDE Level Progression
Defined in `SupportingDocs/the-fde.md`:
- **Level 1**: Buildable Specification (single capability, close guidance)
- **Level 2**: Multi-Capability Systems (3–5 interconnected capabilities, decreasing oversight)
- **Level 3**: Independent End-to-End Engagement (client-facing, owns full lifecycle)
- **Level 4**: Governance and Strategy (multi-engagement quality, economics, mentoring)
- **Level 5**: Program Leadership and Methodology (program design, methodology authorship)

### Key Contacts (as documented)
| Role | Who |
|---|---|
| Program Lead | Aliaksandr Kaliadka |
| Resource Librarian / credit & tooling contact | Klimentiy Misyuchenko |
| Coach | Assigned at Week 1 orientation |
| Squad Lead | Assigned at Week 1 orientation |

## Naming and Formatting Conventions

- All files: lowercase with hyphens, `.md` extension (e.g., `production-spec-checklist.md`)
- Weekly participant READMEs: `README-Participants-Week{N}.md` (PascalCase prefix is intentional)
- Headings: Title Case for H1 and H2; sentence case acceptable for H3+
- Calendar references: always show physical date first, virtual day in brackets — e.g., `Fri 17.04.2026 ("Monday, Week 1")`
- Dates: `DD.MM.YYYY` format for physical calendar dates
- Tables: use Markdown pipe tables; align columns for readability
- Cross-references: use relative Markdown links — `[text](./filename.md)` or `[text](./filename.md#section)`

## Diagrams

Diagrams belong in the spec when prose alone cannot carry the structure — not for decoration. Use them sparingly and consistently so that across scenarios and weeks the outputs look like one programme.

### When to include a diagram

Include a diagram when the spec describes any of the following, and prose is costing the reader more than a glance:

- **Entity relationships** — more than two entities with non-obvious cardinality (e.g. `Onboarding`, `Task`, `BuddyAssignment`, `HumanDecision`).
- **State machines** — any entity with more than three states or a non-linear transition graph.
- **Sequence / orchestration flows** — where timing, external system calls, and escalation branches interact (e.g. the Onboarding Orchestrator day −7 → day 14 timeline).
- **Delegation boundary** — the agent-vs-human split when the table in §2.1 has more than ~10 rows or when a boundary test needs to show a veto / override path visually.
- **Integration topology** — when the spec touches four or more external systems with distinct auth, retry, and fallback profiles.

If none of the above holds, a well-structured Markdown table is usually the right artefact. Do not add a diagram to hit a quota.

### Tooling — Mermaid only

- **All diagrams must be authored in [Mermaid](https://mermaid.js.org/) fenced code blocks** inside the Markdown spec. No external image files, no PNG / SVG exports checked in, no draw.io XML.
- Rationale: Mermaid renders natively in GitHub, JetBrains, and VS Code previews; it is text, so it diffs cleanly; and it keeps the spec the single source of truth. A PNG next to a spec is a divergence risk — treat it the same way we treat a hand-edited `.pptx`.
- Prefer these Mermaid diagram types, in this order: `flowchart` (orchestration, delegation), `stateDiagram-v2` (entity lifecycles), `sequenceDiagram` (integration calls + escalations), `erDiagram` (entity model only when >3 entities with FK relationships), `classDiagram` (avoid unless entity attributes are genuinely load-bearing and already in a table).

### Style conventions

- **Direction:** `flowchart` defaults to top-to-bottom (`TD`). Use `LR` only when the graph reads more naturally left-to-right (typical for sequence-style orchestration).
- **Node labels:** sentence case, ≤ 6 words. Avoid acronyms the spec has not defined.
- **Agent vs. human:** when a diagram crosses the delegation boundary, mark agent-driven nodes and human-driven nodes distinctly — e.g. a `classDef agent` and `classDef human` with short, consistent class names. Keep the palette restricted (one colour for agent, one for human, one for external system). Do not rely on colour alone — suffix human-led nodes with `(human)` in the label so the diagram survives monochrome rendering.
- **Escalations:** render every escalation edge with a dashed arrow and the escalation code as the edge label (e.g. `-. ESC-CLASS .->`).
- **External systems:** represent as subgraphs named after the system (Workday, ServiceNow, LMS, Email, Benefits, Payroll). Keep integration calls inside the subgraph so the diagram shows the boundary without cluttering the internal flow.
- **State machines:** always mark the initial state with `[*]` and terminal states with `-->[*]`. List guard conditions on the transition label, not in prose beneath the diagram.
- **Size:** if a diagram exceeds ~25 nodes it is doing too much. Split it — one diagram per capability, or one per lifecycle phase.

### Cross-referencing

- Every diagram must have a caption line immediately below the code block (`*Figure N — short description*`).
- Reference the figure by number from the prose that depends on it (`see Figure 2`).
- A diagram may not introduce an entity, state, escalation, or integration that is not also named in the spec text. The spec text remains authoritative; the diagram is a reader aid, not a source of new facts.

## Prompt Authoring Conventions

Files under any `Week{N}/Prompts/` folder are *prompts* — instructions executed against this repository to produce deliverables (specs, decks, builds) elsewhere in the tree. This section is the standing contract every such prompt inherits. Individual prompt files should not restate it; they refer to it by name.

### Standing sources every prompt must load

When executing any prompt from a `Week{N}/Prompts/` folder, load and apply **all** of the following before producing output:

1. **This file** (`CLAUDE.md` at root) — repository structure, Core Entities, naming conventions, diagram rules, authoring rules.
2. **`Week{N}/CLAUDE.md`** — week-specific context, standing sources list, output placement rules.
3. **All sources listed in `Week{N}/CLAUDE.md` § Standing Sources** — these are the week-specific reference materials that prompts must load. Each week's CLAUDE.md enumerates them with paths relative to `Week{N}/SupportingDocs/`.

Prompts may quote small fragments of the above for reader convenience, but must not contradict them. If a prompt and a standing source disagree, the standing source wins and the conflict is flagged back to the user — do not silently pick a side.

### Source tagging and confidence rules (inherited by every prompt output)

- Every non-trivial claim must be either **[CITED]** (scenario text, named regulation, explicit rule in the prompt) or **[ASSUMED]** (traced to a numbered entry in the Assumption Log).
- The **Assumption Log goes at the top** of the output document — scan table, coach-session priority queue, update protocol, and full Assumption/Hypothesis/Test/Confidence entries.
- **High** confidence is reserved for coach-session-validated assumptions. **Medium** and **Low** are the defaults until a coach session confirms.
- Unknowns are marked `[UNKNOWN]` in the body and raised as a numbered Assumption Log entry. Never silently fill them in.
- Where assumptions are tagged, distinguish **HUMAN** (participant-supplied, from the scenario file) from **AGENT** (identified during drafting).

### Output placement

Output placement rules are defined in each `Week{N}/CLAUDE.md`. The general pattern is:

- Spec artefacts: `Week{N}/Output/Scenario{M}/` with a filename that encodes the deliverable and a 3-digit run suffix to keep iterations side-by-side.
- Stakeholder decks and their generators: `Week{N}/Scenario{M}/Presentation/`.
- Gate deliverables: `Week{N}/Gate{N}/`.
- Prompts must never write into `SupportingDocs/` and must never modify `the-fde.md` in any week's `SupportingDocs/`.

### Diagrams in prompt outputs

Diagram rules from § *Diagrams* apply unchanged. Use diagrams only where the triggers in that section are met, Mermaid-only, with captions cross-referenced from the prose that depends on them.

## Authoring Rules

### Content Precision
- **Participant-facing docs must be unambiguous**: trainees act on these instructions in time-pressured gates. Vague instructions cause real confusion.
- **Rubrics are sealed**: never add rubric detail (criteria, weights, pass thresholds) to weekly READMEs unless it is explicitly part of the source material. Sealed = omit entirely or say "shared at gate start."
- **Capstone rubric exception**: the Capstone (Week 5) rubric *is* shared at Virtual Monday of Week 5 — this is intentional and correct.
- **Scenario content**: do not invent scenario details. If a scenario file exists, use it. If not, flag the gap.

### What This Agent Should NOT Do
- Never fabricate gate rubric details — they are intentionally sealed
- Never add physical calendar dates beyond what is in the source material (dates shift per cohort)
- Never modify `SupportingDocs/the-fde.md` — it is a canonical role definition, not a living doc for editing
- Never create application code, scripts, or non-markdown files unless explicitly instructed
- Never remove the "rubrics are sealed" notice from weekly READMEs
- Never change the calendar convention format (physical date → virtual day in brackets)

### Structural Integrity
- `README-Participants.md` is the index. Every participant-facing file should be reachable from it.
- If adding a new reference material file, add it to the "Supporting material" table in `README-Participants.md`
- Week N READMEs must cover: week goal, calendar, deliverables, what coaches are looking for

## Handling Ambiguity and Escalation

1. **Missing source material** (e.g., Week 3–5 READMEs don't exist yet): Do not fabricate. State what is missing and ask whether to create a skeleton from the documented structure pattern.

2. **Conflicting information between files**: Flag the conflict explicitly. State which file is the likely authoritative source (e.g., `the-fde.md` is authoritative for FDE level definitions). Do not silently pick one.

3. **Calendar date requests**: Do not assign physical dates to virtual days. Physical dates are cohort-specific and communicated via Teams. If asked to populate a calendar, ask for the confirmed physical date mapping first.

4. **Rubric content requests**: If asked to write a rubric, clarify whether this is coach-side internal content (where detail is appropriate) or participant-facing (where it must be sealed). Do not mix the two.

5. **Scope expansion** (e.g., "add a Week 6"): Flag that no Week 6 exists in the program structure per source material. Ask for confirmation before creating new program structure.

## When to Decide vs When to Ask

**Decide alone:**
- Formatting fixes (broken links, malformed tables, heading hierarchy)
- Typo and grammar corrections
- Adding cross-reference links between existing documented files
- Normalising date format to `DD.MM.YYYY`
- Restructuring existing content for clarity without changing substance

**Ask before acting:**
- Adding new weeks, scenarios, or program structure not in source material
- Any change to gate deliverable lists
- Any change to key contacts
- Any modification to `SupportingDocs/the-fde.md`
- Creating content that will be participant-facing during a live gate

