# Prompt — Two Production-Grade Capability Specifications (D#4)

> **This is a lightweight trigger prompt.** Use `capability-specs-checklist.md` to verify output after generation. Reference `../SupportingDocs/Reference/production-spec-checklist.md` and `../SupportingDocs/Reference/integration-spec-template.md` for spec quality standards.

## Instruction

Produce **Deliverable #4 — Two Production-Grade Capability Specifications** for the Gate 3 scenario.

**Input dependencies:**
- D#3 (Solution Architecture) — which agent components exist and at what delegation level
- D#2 (Engagement Intake) — scope constraints
- `Reference/production-spec-checklist.md` — spec quality criteria
- `Reference/integration-spec-template.md` — integration spec structure

**Requirements:**

1. Produce **two** capability specifications, each for a distinct agent capability from your D#3 architecture
2. Both specs must be **precise enough for Claude Code to build from** without guessing at intent
3. **Shared entities must be consistent across both specs** — if both reference a "Shift" or "Nurse" entity, the schema matches
4. Where ambiguity is unavoidable, name it as an assumption with a confidence level

**Each capability spec must include:**
- Capability name and purpose (one sentence)
- Trigger (what initiates this capability)
- Inputs — exact data, source system, format
- Processing logic — step-by-step, with decision points and edge cases
- Outputs — what the capability produces, format, destination
- Validation rules — how to know the output is correct
- Error handling — what happens when inputs are bad, systems are down, or edge cases hit
- Integration points — per `integration-spec-template.md` structure
- Worked examples — at least 1 happy path + 1 edge case per spec, with concrete data

**Critical check:** One of these two specs will be run through Claude Code for D#9 (self-spec build-loop reflection). Write them as if they will be built — because one will be.

## Output Location

- Gate (Friday): `../Gate3/Output/capability-spec-{A|B}-{NNN}.md`

## After Generation

1. Run through `capability-specs-checklist.md`
2. Run through `../SupportingDocs/Reference/production-spec-checklist.md` for each spec
3. Check: could Claude Code build this without asking clarifying questions?
4. Check: are shared entities consistent across both specs?
5. Choose one spec for D#9 (self-spec build-loop reflection)

