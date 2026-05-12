# Week 3 — CLAUDE.md

> **Status:** Active — Week 3 materials loaded.

## Week Context

- **Week:** 3 of 5
- **Theme:** End-to-End AI-Native Engagement
- **Gate:** Gate 3 (Friday afternoon, 3.5 hours + 10-minute verbal defense)
- **Prerequisite:** Gate 2 passed
- **Scenario:** MedFlex — healthcare staffing agency, 200 employees, CEO wants to "10x the business without 10x-ing the coordinators"

## What This Week Covers

Week 3 combines Weeks 1 and 2 into a full engagement arc:
- Messy discovery → production-grade specification → build-loop correction → stakeholder management
- First time diagnosing actual build output against a partial spec
- Classifying build failures: spec gap / builder misread / unjustified addition / test-environment issue / legitimate unknown
- AI-native solution design (agents as primary mechanism, not bolted-on feature)
- Architecture Decision Records (ADRs) with trade-off analysis
- Client pushback handling (scope discipline, not capitulation)

## Inheritance

This file inherits all rules from `../CLAUDE.md` (root):
- Naming conventions, diagram rules, authoring rules, prompt conventions
- Source tagging ([CITED], [ASSUMED], [UNKNOWN])
- Assumption log placement and confidence rules
- Calendar convention (physical date first, virtual day in brackets)

## Standing Sources

When executing prompts from `Week3/Prompts/`, load:

1. **Root `CLAUDE.md`** — repository structure, Core Entities, naming/diagram/authoring rules
2. **This file** (`Week3/CLAUDE.md`) — week-specific context below
3. **All sources listed below:**

| Source | Path | Purpose |
|---|---|---|
| Participant README | `Week3/SupportingDocs/README-Participants-Week3.md` | Week structure, deliverables, calendar, coaching guidance |
| Spec ambiguity vs builder mistakes | `Week3/SupportingDocs/Reference/spec-ambiguity-vs-builder-mistakes.md` | Build-loop diagnostic taxonomy — read before Wednesday |
| Production spec checklist | `Week3/SupportingDocs/Reference/production-spec-checklist.md` | Spec quality criteria |
| Integration spec template | `Week3/SupportingDocs/Reference/integration-spec-template.md` | Template for integration specs |
| Discovery questioning patterns | `Week3/SupportingDocs/Reference/discovery-questioning-patterns.md` | Discovery session prep (carried from Week 2) |
| ATX references | `Week3/SupportingDocs/Reference/atx/atx-*.md` | ATX vocabulary still used in Gate 3 |

## Output Placement

| Deliverable type | Path |
|---|---|
| Practice artefacts (build-loop exercises, prep work) | `Week3/Output/` |
| Gate 3 deliverables | `Week3/Gate3/` |
| Prompts | `Week3/Prompts/` |

## Week 3 Calendar Summary

| Virtual day | Main event |
|---|---|
| Monday | Coach-led orientation (1h); self-directed prep |
| Tuesday | Continue prep; production-spec-checklist audit |
| Wednesday AM | Whole-cohort build-review walkthrough (Coffee Subscription Credit Handler) |
| Wednesday PM | Solo build-loop exercise (Cascade Public Libraries Hold Queue) |
| Thursday AM | Gate 3 scenario released; live discovery session (60 min) |
| Thursday PM | Specification work; interim design due EOD |
| Friday AM | Personalised client feedback (Marcus Reyes pushback); finalise design |
| Friday PM | **Gate 3 timed exercise (3.5h)** + 10-minute verbal defense |

## Gate 3 Deliverables (9 total)

1. Problem framing & success metrics
2. Engagement intake & scope
3. Agentic solution architecture (incl. ≥2 ADRs)
4. Two production-grade capability specifications
5. Build-loop response memo (Cascade Libraries fixture)
6. Client feedback response
7. Validation plan
8. Reflection document
9. Self-spec build-loop reflection (1 page)

## Week 3 Anti-Patterns

- **AI-as-a-feature** — deterministic matcher with LLM sprinkled on top; must show genuine agent decision points
- **First-impression diagnosis** — naming surface signal without reading spec alongside code
- **Client appeasement** — caving to CEO timeline pressure without honest replanning
- **Defensive self-reflection** — "mostly got it right" when the build is clearly broken
- **Decision theatre ADRs** — "We chose X because it is right" without alternatives/consequences/reversibility
- **Build-loop stops at classification** — must include the corrective response in the right tone per category
