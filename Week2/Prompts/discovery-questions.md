# Prompt — Discovery Questions

> **This is a lightweight trigger prompt.** The structural rules for Deliverable #6 are encoded in `../CLAUDE.md` § Deliverable Output Rules. Use `discovery-questions-checklist.md` in this folder to verify your output after generation.

## Instruction

Produce **Deliverable #6 — Discovery Questions for the Main Stakeholder** based on the scenario provided and your outputs from Deliverables #1–5.

**Input dependencies:** Load your most recent versions of Deliverables #1–5 from the output folder. Each deliverable will have surfaced gaps, assumptions, and tensions. The discovery questions should target those — not generic process questions.

**Key reference:** `../SupportingDocs/discovery-questioning-patterns.md` — especially the Funnel Pattern (Level 3: Probe) and the "Lived vs Documented" probe technique.

**Structure each question as:**
1. The question itself
2. **What tension or gap it targets** — the specific item from your analysis (e.g. "A3 from assumption log", "Saba LMS no-API gap from Deliverable #5", "delegation boundary for compliance path selection")
3. **What design decision changes if the answer is X vs Y** — if the answer wouldn't change your design, it's not a real discovery question

**The gate 2 live clarification round is 10 minutes.** You'll get to ask ~5–7 questions. Prioritise ruthlessly — lead with the questions whose answers would cause the largest design changes.

## Output location

- Practice: `../Output/discovery-questions-{NNN}.md`
- Gate: `../Gate2/Output/discovery-questions-{NNN}.md`

## After generation

1. Run through `discovery-questions-checklist.md`
2. Check: does every question name a specific design decision it would change?
3. Check: are the top 5 questions ordered by design impact (highest first)?
4. Prepare for the live clarification round — the stakeholder is impatient and sceptical

