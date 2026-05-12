# Prompt — Volume × Value Analysis

> **This is a lightweight trigger prompt.** The structural rules for Deliverable #3 are encoded in `../CLAUDE.md` § Deliverable Output Rules. Use `volume-value-analysis-checklist.md` in this folder to verify your output after generation.

## Instruction

Produce **Deliverable #3 — Volume × Value Analysis** for the scenario provided.

**Input dependency:** Load Deliverable #2 (Delegation Suitability Matrix) from the output folder. You also need the volume/frequency data from the scenario's four work streams.

Plot **all 4 work streams** on the Volume × Value grid (not just the 2 you decomposed in Deliverable #1). Use the scenario's stated volumes and your delegation analysis to score each.

**Scoring:** Use the 1–5 scales from `atx-scoring.md` § Step 2:
- Y-axis: Execution Frequency (cases/day or week)
- X-axis: Non-Deterministic Decision Effort (how much reasoning beyond rules)

Identify the **primary agentic target** and justify why it wins. If a work stream lands top-left (high volume, low non-determinism), name it as a rules/RPA candidate — not an agent.

## Output location

- Practice: `../Output/volume-value-analysis-{NNN}.md`
- Gate: `../Gate2/Output/volume-value-analysis-{NNN}.md`

## After generation

1. Run through `volume-value-analysis-checklist.md`
2. Check: does the 2×2 grid include all 4 work streams?
3. Check: is the primary agentic target justified with both volume AND non-determinism reasoning?
4. The primary target feeds forward into Deliverable #4 (Agent Purpose Document)

