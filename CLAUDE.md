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
├── CLAUDE.md                          ← this file (project constitution)
├── SupportingDocs/                    ← reference material used across all weeks
│   ├── README-Participants.md         ← documentation index (start here)
│   ├── README-Participants-Intro-Week1.md  ← orientation + Week 1 guide
│   ├── README-Participants-Week1-Scenarios.md  ← 7 practice scenarios
│   ├── Week1-Thinking-Discipline-Primer.md    ← Week 1 thinking-discipline primer
│   ├── claude-md-examples-guide.md    ← CLAUDE.md examples (3 quality tiers)
│   ├── production-spec-checklist.md   ← what makes a spec buildable
│   ├── spec-ambiguity-vs-builder-mistakes.md  ← build-loop diagnostic taxonomy
│   └── the-fde.md                     ← FDE role definition (canonical source)
├── Week1/                             ← Week 1 working area
│   ├── Scenario1/                     ← scenario-specific working folder (one per chosen scenario)
│   │   ├── build-spec.md              ← reusable prompts for this scenario (Prompt 1 spec, Prompt 2 deck, Prompt 3 build)
│   │   ├── Output/                    ← generated spec artefacts (e.g. critique-pool-*.md)
│   │   └── Presentation/              ← generated stakeholder decks (.pptx) and their generator scripts
│   └── Gate1/                         ← Gate 1 deliverables (populated during gate exercise)
```

> Note: Week 2–5 working areas (`Week2/` through `Week5/`) and their scenario-specific subfolders are expected to appear alongside `Week1/` as the cohort progresses. Weekly participant READMEs for Weeks 2–5 are expected in `SupportingDocs/` following the `README-Participants-Week{N}.md` pattern. If they are missing, flag the gap rather than creating placeholder content.

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

