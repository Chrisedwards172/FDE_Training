# Prompt — Agentic Solution Architecture + ADRs (D#3)

> **This is a lightweight trigger prompt.** Use `solution-architecture-checklist.md` to verify output after generation.

## Instruction

Produce **Deliverable #3 — Agentic Solution Architecture** for the Gate 3 scenario, including **at least 2 Architecture Decision Records (ADRs)**.

**Input dependencies:**
- D#1 (Problem Framing) — problem statement and success metrics
- D#2 (Engagement Intake) — scope, constraints, risks
- Discovery session notes
- Marcus Reyes pushback memo
- ATX references (`Reference/atx/atx-*.md`) — delegation vocabulary still applies

**What this deliverable must contain:**

### Solution Architecture
1. **Which parts of the workflow become agentic** — map each workflow element to a delegation level (fully agentic / agent-led + oversight / human-led + agent support / human-only / RPA-automation)
2. **Why each delegation level** — brief rationale per element (not a full D2-style matrix, but the logic must be visible)
3. **System diagram** — Mermaid flowchart showing agent boundaries, human touchpoints, external systems, and data flows
4. **Integration points** — what systems the agent reads from, writes to, and how (API / batch / manual)

### Architecture Decision Records (≥ 2)
Each ADR must follow this structure:
- **Title** — the decision in one sentence
- **Status** — Proposed / Accepted / Superseded
- **Context** — what forces are at play, including the CEO's constraints
- **Decision** — what you chose
- **Alternatives considered** — at least 2 alternatives with pros/cons
- **Consequences** — what happens because of this decision (good and bad)
- **Reversibility** — can this be changed later, at what cost?

**Critical check:** The solution must be **genuinely AI-native** — agents are the primary mechanism for delivering value, not a feature bolted onto a traditional matching algorithm. Coaches will ask: "Show me the agent decision in your design — the specific point where reasoning over context determines an outcome that a rule-based system couldn't reach."

**ADR critical check:** ADRs must not read as justifications ("We chose X because it's right"). They must name real alternatives, real trade-offs, and conditions under which the decision would be revisited.

## Output Location

- Interim (Thursday EOD): `../Gate3/Output/solution-architecture-{NNN}.md`
- Gate (Friday): `../Gate3/Output/solution-architecture-{NNN}.md`

## After Generation

1. Run through `solution-architecture-checklist.md`
2. Check: can you point to a specific agent decision that a rule-based system couldn't make?
3. Check: do your ADRs name at least 2 alternatives each with genuine trade-offs?
4. Check: is the Mermaid diagram ≤ 25 nodes?
5. Feed forward into D#4 (two capability specs built from this architecture)

