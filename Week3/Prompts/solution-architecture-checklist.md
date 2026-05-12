# Checklist — Agentic Solution Architecture + ADRs (D#3)

> Use **after** generating your Architecture to verify completeness.

## Completeness Check

### Solution Architecture

- [ ] Every workflow element from D#2 scope is mapped to a delegation level
- [ ] Delegation levels use ATX vocabulary: fully agentic / agent-led + oversight / human-led + agent support / human-only / RPA-automation
- [ ] Each delegation assignment has a brief rationale (1–2 sentences)
- [ ] At least one element is **not** fully agentic (avoid "everything is agentic" anti-pattern)
- [ ] At least one element shows genuine agent reasoning (not just lookup/match/template)

### System Diagram

- [ ] Mermaid `flowchart` format
- [ ] Shows: agent components, human touchpoints, external systems, data flows
- [ ] Agent vs human nodes visually distinguished (classDef or label suffix)
- [ ] ≤ 25 nodes; split if larger
- [ ] Caption line below code block
- [ ] Referenced from prose ("see Figure N")

### Integration Points

- [ ] Every external system named with: what data flows, direction (read/write/both), method (API/batch/manual)
- [ ] Auth/credential approach mentioned per integration
- [ ] Failure mode per integration (what happens when it's down?)

### ADRs (≥ 2)

- [ ] Each ADR has: Title, Status, Context, Decision, Alternatives, Consequences, Reversibility
- [ ] **Alternatives** section lists at least 2 genuine alternatives (not straw men)
- [ ] Each alternative has pros AND cons stated
- [ ] **Consequences** section names both positive and negative consequences
- [ ] **Reversibility** states cost/difficulty of changing the decision later
- [ ] At least one ADR addresses a CEO-relevant concern (timeline, scope, prior failures)

### AI-Native Check

- [ ] Can you point to a specific point where **agent reasoning over context** determines an outcome?
- [ ] That outcome could NOT be reached by a rule-based system or deterministic matcher
- [ ] The agent's reasoning is explained — what inputs, what reasoning, what output

## Anti-Pattern Self-Check

| Anti-pattern | Signal | Fix |
|---|---|---|
| **AI-as-a-feature** | Architecture is a matcher with LLM call appended | Redesign: where does the agent reason about ambiguous context? |
| **Decision theatre ADRs** | "We chose X because it is the right choice" | Add genuine alternatives with real trade-offs and reversal cost |
| **Everything is agentic** | No human-only or human-led elements | Revisit — which decisions carry liability, compliance, or political risk? |
| **Missing integration failures** | Integrations listed without "what if it's down" | Add degradation strategy per integration |

## Feed-Forward

Architecture constrains D#4 (capability specs implement the agent components you've designed here). ADR decisions constrain D#7 (validation plan tests the consequences you've predicted).

