# Prompt — Problem Framing & Success Metrics (D#1)

> **This is a lightweight trigger prompt.** Structural rules are in `../CLAUDE.md`. Use `problem-framing-checklist.md` to verify output after generation.

## Instruction

Produce **Deliverable #1 — Problem Framing & Success Metrics** for the Gate 3 scenario.

**Input dependencies:**
- Gate 3 Participant Pack (scenario brief)
- Discovery session notes (from Thursday live session)
- Marcus Reyes CEO pushback memo (Friday AM — revise against this before finalising)

**What this deliverable must answer:**
1. **What is actually broken?** Not the stated request ("10x without 10x-ing") — the real operational problem underneath it. Translate the CEO's aspiration into concrete breakdowns in the current workflow.
2. **Who experiences the broken thing?** Map success from three perspectives: the business (MedFlex), the customers (hospitals), and the workers (nurses). Each has different success criteria.
3. **What does success look like?** Measurable. Not "improve efficiency" — specific metrics with baselines, targets, and measurement methods.

**Structure:**
- Current-state problem statement (grounded in discovery evidence, not assumptions)
- Stakeholder-specific success criteria (MedFlex / hospitals / nurses)
- Measurable KPIs with baseline → target → how measured
- What this is NOT about (explicit scope exclusions surfaced by framing)

**Critical check:** The problem framing must address the **real problem**, not the stated request. "10x without 10x-ing the coordinators" is a business aspiration — your framing translates it into what the agentic system actually needs to achieve.

## Output Location

- Interim (Thursday EOD): `../Gate3/Output/problem-framing-{NNN}.md`
- Gate (Friday): `../Gate3/Output/problem-framing-{NNN}.md`

## After Generation

1. Run through `problem-framing-checklist.md`
2. Check: is every success metric measurable (baseline + target + method)?
3. Check: does the framing distinguish between the stated request and the real problem?
4. Check: have you revised against Marcus's pushback memo?
5. Feed forward into D#2 (Engagement Intake & Scope) and D#3 (Architecture)

