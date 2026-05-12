# Checklist — Two Production-Grade Capability Specifications (D#4)

> Use **after** generating your Capability Specs to verify completeness. Also run `../SupportingDocs/Reference/production-spec-checklist.md` against each spec.

## Per-Spec Completeness Check (run for EACH of the 2 specs)

### Core Structure

- [ ] Capability name and one-sentence purpose
- [ ] Trigger clearly defined (what event/condition initiates this capability)
- [ ] Inputs listed with: data field, source system, format, required/optional
- [ ] Processing logic is step-by-step (not narrative)
- [ ] Decision points have explicit branching (if X → do A; if Y → do B)
- [ ] Edge cases identified (at least 2 per spec)
- [ ] Outputs defined with: field, format, destination system

### Validation & Error Handling

- [ ] Validation rules stated for each output (how to know it's correct)
- [ ] Error handling covers: bad input, system down, timeout, unexpected data
- [ ] Each error has: detection method, response action, escalation path

### Integration Points

- [ ] Each external system integration has: system name, operation, auth method, endpoint/method
- [ ] Failure mode per integration (what happens when unavailable)
- [ ] Data format specified (JSON schema, field types, required fields)

### Worked Examples

- [ ] At least 1 **happy path** example with concrete data (not placeholders)
- [ ] At least 1 **edge case** example with concrete data
- [ ] Examples show input → processing steps → expected output
- [ ] Examples use realistic domain values (not "John Doe, 123 Main St")

### Assumptions

- [ ] Every ambiguity marked `[ASSUMED]` with confidence level
- [ ] Assumptions are specific ("credential expiry is checked against state board API") not vague ("system handles credentials")

## Cross-Spec Consistency Check

- [ ] Shared entity names match (same name = same structure in both specs)
- [ ] Shared entity schemas are identical or one extends the other
- [ ] No conflicting definitions of the same concept
- [ ] If both specs reference the same system, integration details are consistent

## Agent-Buildability Check

- [ ] Could Claude Code build this without asking clarifying questions?
- [ ] No "TBD" or "to be determined" in any field
- [ ] No "as appropriate" or "as needed" — every decision point has explicit criteria
- [ ] Processing logic does not skip steps with "etc." or "and so on"

## Anti-Pattern Self-Check

| Anti-pattern | Signal | Fix |
|---|---|---|
| **Narrative spec** | Processing logic reads like a paragraph | Convert to numbered steps with explicit branching |
| **Missing edge cases** | Only happy path is specified | Add: what if input is missing? What if system is down? What if data conflicts? |
| **Vague validation** | "Output should be correct" | Define: correct means field X matches Y within tolerance Z |
| **Placeholder examples** | "e.g., a nurse named Jane" | Use concrete data: "Nurse ID NRS-2847, RN license #IL-RN-44821, expires 2026-09-15" |

## Feed-Forward

One of these specs is the input to D#9 (self-spec build-loop reflection). Choose the one you're most confident in — or the one you suspect has the most interesting ambiguities for honest diagnosis.

