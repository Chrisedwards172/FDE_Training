# Prompt — Engagement Intake & Scope (D#2)

> **This is a lightweight trigger prompt.** Use `engagement-intake-checklist.md` to verify output after generation.

## Instruction

Produce **Deliverable #2 — Engagement Intake & Scope** for the Gate 3 scenario.

**Input dependencies:**
- D#1 (Problem Framing) — for problem statement and success criteria
- Gate 3 Participant Pack (scenario brief + artefacts)
- Discovery session notes
- Marcus Reyes pushback memo (revise scope against this)

**What this deliverable must contain:**

1. **Business context** — who is MedFlex, what do they do, how big, what's the market
2. **Stakeholder map** — who has authority, who has influence, who will resist, who must be consulted. Include at least: CEO, coordinators, hospital administrators, nurses. Note conflicting incentives.
3. **Constraints** — technical, regulatory (healthcare staffing compliance), timeline (CEO wants 8 weeks), budget, team capacity
4. **Risks** — what could go wrong, likelihood, impact, mitigation. Include adoption risk (two failed AI projects)
5. **MVP scope** — what's IN for the first delivery. Be specific: which workflows, which user groups, which geographic scope
6. **Out of scope** — what's explicitly NOT in MVP and why. This is where you hold boundary against the CEO's scope pressure.

**Critical check:** The CEO will push on scope and timeline. Your intake must hold boundary without alienating. "Everything the CEO asked for in 8 weeks" is not a credible scope — name what's achievable and what moves to Phase 2.

## Output Location

- Interim (Thursday EOD): `../Gate3/Output/engagement-intake-{NNN}.md`
- Gate (Friday): `../Gate3/Output/engagement-intake-{NNN}.md`

## After Generation

1. Run through `engagement-intake-checklist.md`
2. Check: does the stakeholder map name at least one conflicting incentive?
3. Check: is the out-of-scope section specific enough that the CEO can't claim you agreed to include it?
4. Check: does the risk register include adoption risk from prior AI failures?
5. Feed forward into D#3 (Architecture) and D#6 (Client Feedback Response)

