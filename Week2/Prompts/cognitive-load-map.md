# Prompt — Cognitive Load Map

> **This is a lightweight trigger prompt.** The structural rules for Deliverable #1 are encoded in `../CLAUDE.md` § Deliverable Output Rules. Use `cognitive-load-map-checklist.md` in this folder to verify your output after generation.

## Instruction

Produce **Deliverable #1 — Cognitive Load Map** for the scenario provided.

**Work streams to cover:** Select the 2 work streams with the **richest sample artefacts** in the scenario. Choose based on artefact density (emails, tracker excerpts, call transcripts, flowchart fragments) — not on which work stream seems most important. Artefacts ground your lived-work claims; without them, you're mapping the SOP.

Ground your lived-process narrative in the sample artefacts. Where the scenario doesn't give you enough, mark `[ASSUMED — AN]` and add the entry to the Agent Purpose Document's consolidated Assumption Log.

## Output location

- Practice: `../Output/cognitive-load-map-{NNN}.md`
- Gate: `../Gate2/Output/cognitive-load-map-{NNN}.md`

## After generation

1. Run through `cognitive-load-map-checklist.md` — tick every box
2. Check: does the micro-task inventory have score variance? (If it's all `M`, decompose further)
3. Check: does every JtD name a *decision*, not just an action?
4. Feed the micro-task inventory forward to Deliverable #2 (Delegation Suitability Matrix)
