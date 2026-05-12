# Prompt — Gate Presentation Deck

> **This is a lightweight trigger prompt.** It generates a PowerPoint presentation for the live clarification round using `python-pptx`. The presentation structure adapts to the scenario and deliverables produced earlier in the gate exercise.

## Instruction

Produce a **PowerPoint presentation** for the live clarification round described in the Gate Participant Pack (§ "Live clarification round" and "Hints From Coaches").

**Input dependencies:** Load from the output folder:
- Deliverable #1 (Cognitive Load Map) — for the "before" view of current process
- Deliverable #2 (Delegation Suitability Matrix) — for archetype assignments and delegation defence
- Deliverable #3 (Volume × Value Analysis) — for work stream scoring and primary target justification
- Deliverable #4 (Agent Purpose Document) — for agent identity, KPIs, failure modes, autonomy matrix
- Deliverable #5 (System/Data Inventory) — for system constraints and assumptions
- Deliverable #6 (Discovery Questions) — for top questions to ask COO and coach Q&A prep
- Gate Participant Pack — for scenario context, live round format, and "Hints From Coaches" section

## Presentation Structure

The deck must cover **three sections** matching the live round format:

### Section 1 — Presentation (4 minutes)

| Slide | Content | Source |
|---|---|---|
| Title | Agent name, scenario, prepared for [stakeholder name] | D4, scenario |
| Work stream summary | All work streams assessed with V×V scores; why primary target wins | D3 |
| BEFORE | Current process for primary target — lived work, not SOP. Bottlenecks, failures, cognitive load | D1 |
| AFTER | Redesigned process with agent — three columns: agent decides alone / human-led + agent support / human-only | D2, D4 |
| Agent identity & KPIs | Agent name, job to be done, KPI targets, why this avoids prior failure modes | D4, scenario |
| Delegation defence | Pre-prepared Q&A: "why is X delegated?", "why isn't Y agentic?" | D2 rationale |
| Secondary work stream | Why it was mapped but NOT chosen as primary target; Wave 2 plan | D1, D3 |

### Section 2 — COO Question (3 minutes)

| Slide | Content | Source |
|---|---|---|
| The question | The single question whose answer would most change the design; why it matters; what changes based on each possible answer | D6 (Priority 1 question) |
| Follow-up probes | How to push if stakeholder hedges, deflects, or pushes back | D6, D4 assumptions |

### Section 3 — Coach Q&A (3 minutes)

| Slide | Content | Source |
|---|---|---|
| Top discovery questions | 5 ranked questions with design-impact rationale | D6 |
| Assumptions to defend | Key assumptions with confidence levels and "if wrong, what breaks" | D4, D5 assumption logs |
| Honest gaps & trade-offs | Known gaps, deliberate trade-offs, what changes based on stakeholder answers | All deliverables |

## Output Format

Generate a Python script using `python-pptx` that:
- Uses widescreen format (13.333" × 7.5")
- Dark navy background (`#1B2A4A`) with accent colours for section headers
- Colour-codes sections: green for "after"/agent, red for "before"/problems, amber for warnings/trade-offs, teal for neutral/identity
- Includes human-readable text at presentation sizes (12–42pt)
- Saves to the gate output folder

## Output Location

- Practice: `../Scripts/generate_deck.py` → saves `.pptx` to `../Output/`
- Gate: `../Gate{N}/generate_gate{N}_deck.py` → saves `.pptx` to `../Gate{N}/`

## Design Principles

1. **Content mirrors the "Hints From Coaches" section exactly** — before/after, delegation defence, COO question with design-change thinking, coach Q&A
2. **Every slide has a source deliverable** — no content invented for the deck that isn't traceable to D1–D7
3. **Delegation defence is pre-prepared** — anticipate "why is X fully delegated?" and "why isn't Y agentic?" based on D2 rationale
4. **COO question is design-breaking, not generic** — the answer would materially change the agent architecture, KPIs, or scope
5. **Follow-up probes handle evasion** — stakeholder hedges, contradicts, or pushes back; each probe has a rationale
6. **Honest gaps are named, not hidden** — known gaps and deliberate trade-offs show FDE judgment, not perfection

## After Generation

1. Run the script to verify it produces a valid `.pptx` without errors
2. Open the deck and check: could you present this in 4 minutes without reading from notes?
3. Check: does the delegation defence cover every archetype boundary in D2?
4. Check: does the COO question have "what changes based on the answer" for at least 3 possible responses?
5. Check: are assumptions referenced by their log IDs (A1, S1, etc.) for traceability?

