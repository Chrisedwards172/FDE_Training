# Prompt — Delegation Suitability Matrix

> **This is a lightweight trigger prompt.** The structural rules for Deliverable #2 are encoded in `../CLAUDE.md` § Deliverable Output Rules. Use `delegation-suitability-matrix-checklist.md` in this folder to verify your output after generation.

## Instruction

Produce **Deliverable #2 — Delegation Suitability Matrix** for the scenario in `../scenario-1.md`.

**Input dependency:** This deliverable takes the micro-task inventory from Deliverable #1 (Cognitive Load Map) as its primary input. Load your most recent Cognitive Load Map from `../Output/` before generating.

For every micro-task and JtD cluster identified in Deliverable #1, score on the 7 delegation suitability dimensions and assign a delegation archetype with written rationale.

**Critical check:** If every task cluster ends up as "fully agentic", stop and re-examine. This is the #1 Week 2 anti-pattern. At least 2 different archetypes must appear, with boundary rationale for each.

## Output location

`../Output/delegation-suitability-matrix-scenario-1-{NNN}.md`

## After generation

1. Run through `delegation-suitability-matrix-checklist.md`
2. Check: are at least 2 different delegation archetypes represented?
3. Check: does each archetype assignment have a written rationale citing specific dimension scores?
4. Feed forward into Deliverable #3 (Volume × Value Analysis) and Deliverable #4 (Agent Purpose Document)

