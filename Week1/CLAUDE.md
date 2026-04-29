# CLAUDE.md — Week 1: AI-Native Specification

> **Inherits:** [`../CLAUDE.md`](../CLAUDE.md) (root project constitution). Load both files when executing any prompt from `Week1/Prompts/`.

## Week 1 Context

Week 1 teaches the foundational FDE skill: **given a business problem, design an agentic solution and produce a specification precise enough for an AI coding agent to build from.** The output is a written spec — not a slide deck, not a strategy memo. If a builder would have to guess what you meant, the spec is not yet done.

- **FDE Level targeted:** Level 1 — Buildable Specification (single capability, close guidance)
- **Practice:** participant picks 1 of 7 scenarios at Virtual Monday orientation and works against it all week
- **Gate 1:** 2.5-hour timed exercise on a previously unseen scenario, followed by a ~10-minute live walkthrough

## Week 1 Directory Structure

```
Week1/
├── CLAUDE.md                          ← this file
├── scenario-1.md                      ← practice scenario (selected at orientation)
├── Prompts/                           ← prompts for producing practice deliverables
│   ├── problem-statement.md
│   ├── delegation-analysis.md
│   ├── capability-specification.md    (Week 1 term; becomes "agent specification" at gate)
│   ├── validation-design.md
│   ├── assumptions-and-unknowns.md
│   ├── concatonate-and-review.md
│   └── Presentation/
├── Output/
│   └── Scenario1/                     ← generated artefacts from practice prompts
├── Gate1/
│   ├── gate-scenario.md               ← sealed gate scenario (released at gate start)
│   ├── Gate1-Chris-Edwards.md         ← gate submission
│   ├── Prompts/                       ← prompts used during the gate exercise
│   ├── Output/                        ← intermediate gate artefacts
│   ├── Final/                         ← final consolidated gate deliverables
│   └── SupportingDocs/
│       └── Gate1-Participant-Pack.md
└── SupportingDocs/                    ← Week 1 reference material
    ├── README-Participants.md
    ├── README-Participants-Intro-Week1.md
    ├── README-Participants-Week1-Scenarios.md
    ├── Week1-Thinking-Discipline-Primer.md
    ├── claude-md-examples-guide.md
    ├── production-spec-checklist.md
    ├── spec-ambiguity-vs-builder-mistakes.md
    └── the-fde.md
```

## Standing Sources

When executing any prompt from `Week1/Prompts/` (or `Week1/Gate1/Prompts/`), load **all** of the following in addition to the root `../CLAUDE.md`:

| # | Source | Path (relative to `Week1/`) | Purpose |
|---|---|---|---|
| 1 | Thinking Discipline Primer | `./SupportingDocs/Week1-Thinking-Discipline-Primer.md` | Reasoning-discipline constitution. Applies **every week**, not just Week 1. Frame claims as Assumption → Hypothesis → Test → Confidence. Surface the Assumption Log at the top. Obey the primer's anti-patterns. Apply the Cagan four-risk lens. |
| 2 | Participant README (Intro + Week 1) | `./SupportingDocs/README-Participants-Intro-Week1.md` | What the deliverables are and how they'll be reviewed |
| 3 | Week 1 Scenarios | `./SupportingDocs/README-Participants-Week1-Scenarios.md` | The 7 practice scenarios |
| 4 | Production Spec Checklist | `./SupportingDocs/production-spec-checklist.md` | The buildability bar any spec must clear |
| 5 | Build-Loop Diagnostic Taxonomy | `./SupportingDocs/spec-ambiguity-vs-builder-mistakes.md` | Diagnostic taxonomy for build-loop review |
| 6 | FDE Role Definition | `./SupportingDocs/the-fde.md` | Role framing and level definitions. **Canonical; never modified.** |
| 7 | CLAUDE.md Examples Guide | `./SupportingDocs/claude-md-examples-guide.md` | Three quality tiers for CLAUDE.md authoring |
| 8 | Scenario file | `./scenario-1.md` (practice) or `./Gate1/gate-scenario.md` (gate) | Scenario text and participant HUMAN assumptions |

For **Gate 1 prompts** specifically, also load:
- `./Gate1/SupportingDocs/Gate1-Participant-Pack.md` — the gate brief, deliverable list, evaluation criteria, and anti-patterns

## Output Placement

| Artefact type | Path |
|---|---|
| Practice spec artefacts | `Week1/Output/Scenario1/` — filename encodes deliverable + 3-digit run suffix |
| Gate intermediate artefacts | `Week1/Gate1/Output/` |
| Gate final deliverables | `Week1/Gate1/Final/` |
| Stakeholder decks | `Week1/Prompts/Presentation/` |

## Week 1 Deliverables (5)

| # | Deliverable | What it tests |
|---|---|---|
| 1 | Problem statement & success metrics | Dual-perspective framing (claimant + business), measurable outcomes, scenario-specific numbers |
| 2 | Delegation analysis | Boundary justification, codifiability reasoning, not arbitrary |
| 3 | Agent specification (capability spec in practice) | Entities, state machines, integration contracts, decision logic, escalation triggers, error handling |
| 4 | Validation design | Happy path, edge cases, failure modes, **quiet failure detection** |
| 5 | Assumptions & unknowns | Honest identification, ≥ 5 genuine unknowns, no filler |

## Week 1 Anti-Patterns

These are the failure modes coaches watch for (from Gate 1 Participant Pack §7):

- **Hand-waving verbs** — "handles", "manages", "processes" with no inputs/outputs/logic
- **Implicit state** — referencing claim states without defining transitions
- **Integration hand-wave** — "integrates with X" without endpoint/auth/request/response/timeout/retry/fallback
- **Generic problem framing** — could have been written without reading the scenario
- **Vanishing claimant** — framing purely from efficiency perspective, losing the claimant
- **Filler assumptions** — platitudes instead of testable claims
- **Bluffing** — confident claims about things the scenario didn't state, unmarked as assumptions

## Closed Build Loop

The Week 1 build loop tests whether the spec is buildable:

1. Hand the spec to Claude Code with: *"Build from this spec. Tell me what you can build confidently, what you need to clarify, and what you can't build."*
2. Review: (a) what it built — faithful or drifted? (b) what questions it asked — each is a spec gap (c) what it couldn't build — each is a buildability gap
3. Diagnose each gap against `spec-ambiguity-vs-builder-mistakes.md`
4. Revise the spec and re-run

