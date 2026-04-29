# Prompt — Cognitive Load Map

> **This is a lightweight trigger prompt.** The structural rules for Deliverable #1 are encoded in `../CLAUDE.md` § Deliverable Output Rules. Use `cognitive-load-map-checklist.md` in this folder to verify your output after generation.

## Instruction

Produce **Deliverable #1 — Cognitive Load Map** for the scenario in `../scenario-1.md`.

**Work streams to cover:** Select the 2 work streams with the richest sample artefacts in the scenario. For the practice scenario (HR Onboarding Coordination), this is likely:

- **New-hire system & access setup** (grounded by Artefact 1.1 email thread + Artefact 1.2 master tracker)
- **Compliance training assignment & tracking** (grounded by Artefact 1.3 flowchart fragment + tracker footnotes)

Ground your lived-process narrative in the sample artefacts. Where the scenario doesn't give you enough, mark `[ASSUMED]` and log it.

## Output location

`../Output/cognitive-load-map-scenario-1-{NNN}.md` — replace `{NNN}` with the next available 3-digit run suffix.

## After generation

1. Run through `cognitive-load-map-checklist.md` — tick every box
2. Check: does the micro-task inventory have score variance? (If it's all `M`, decompose further)
3. Check: does every JtD name a *decision*, not just an action?
4. Feed the micro-task inventory forward to Deliverable #2 (Delegation Suitability Matrix)
