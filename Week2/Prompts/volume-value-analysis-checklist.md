# Checklist — Volume × Value Analysis (Deliverable #3)

> Use this **after** generating your Volume × Value Analysis to verify completeness.

## Completeness check

### Assumption Log

- [ ] Appears at top of document
- [ ] Volume estimates sourced from scenario tagged `[Artefact]` or `[INFERRED — scenario brief]`
- [ ] Non-determinism scores justified — not guessed

### Scoring table

- [ ] **All 4 work streams** scored (not just the 2 from Deliverable #1)
- [ ] Execution Frequency scored 1–5 using `atx-scoring.md` scale
- [ ] Non-Deterministic Decision Effort scored 1–5 using `atx-scoring.md` scale
- [ ] Agentic Value Score calculated (Volume × Non-Determinism, 1–25 scale)
- [ ] Each score has a short justification grounded in scenario evidence

### 2×2 Grid

- [ ] All 4 work streams plotted visually (Mermaid quadrant chart or text-based grid)
- [ ] Quadrants labelled: Top-right (primary agentic targets), Top-left (rules/RPA), Bottom-right (selective agentic), Bottom-left (not worth automating)
- [ ] Each work stream's position matches its scores

### Primary agentic target

- [ ] One work stream identified as the primary target
- [ ] Justification cites **both** volume and non-determinism — not just one axis
- [ ] Justification addresses why the target wins over the second-strongest candidate
- [ ] Any work stream scoring ≥ 15 is flagged as a strong candidate
- [ ] Any work stream scoring < 8 is flagged as rule-based or not worth automating

### Suitability gate cross-check

- [ ] The primary target passed the suitability gate in Deliverable #2
- [ ] If the highest-scoring work stream failed the suitability gate, the second-highest is selected and the conflict is noted

## Anti-pattern check

| Anti-pattern | How to detect | Fix |
|---|---|---|
| **All 4 in the same quadrant** | Scores cluster together | Re-examine — the scenario gives different volumes and complexity levels per stream |
| **Edge-case resolution scored as high volume** | Scenario says 30–50/yr for edge cases | Use scenario's stated volumes, not impressions |
| **Non-determinism score ignores lived-work evidence** | Score based on SOP rather than artefacts | Revisit Deliverable #1 narratives for judgment-call frequency |
| **Missing the "not an agent" call** | Every work stream positioned as agentic | Some work streams are rules/RPA — name them |

## Feed-forward

- Primary agentic target becomes the focus of **Deliverable #4** (Agent Purpose Document)
- Volume and cost-per-case estimates feed into preliminary TCO thinking (used more in Week 4)

