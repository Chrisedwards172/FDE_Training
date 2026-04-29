# Prompt — Agent Purpose Document

> **This is a lightweight trigger prompt.** The structural rules for Deliverable #4 are encoded in `../CLAUDE.md` § Deliverable Output Rules. Use `agent-purpose-document-checklist.md` in this folder to verify your output after generation.

## Instruction

Produce **Deliverable #4 — Agent Purpose Document** for the primary agentic target identified in Deliverable #3 (Volume × Value Analysis).

**Input dependencies:** Load from `../Output/`:
- Deliverable #1 (Cognitive Load Map) — for JtDs, micro-tasks, and breakpoints
- Deliverable #2 (Delegation Suitability Matrix) — for archetype assignments and boundary rationale
- Deliverable #3 (Volume × Value Analysis) — for the primary target identification

The Agent Purpose Document is the Week 2 equivalent of Week 1's capability spec. It must be precise enough to hand to Claude Code in the closed build loop (see `../CLAUDE.md` § Closed Build Loop).

**Structure** follows the template in `atx-agent-mapping.md` § Agent Purpose Document + § Autonomy Matrix:
- Agent Name, Job to be Done, Business context
- Primary objectives, KPIs (accuracy, coverage, throughput, cost per case, HITL rate)
- Failure modes (what bad output looks like, consequences, recovery path)
- Delegation archetype + rationale
- Escalation triggers (at least 3, each with a target role)
- Autonomy matrix (4 tiers: decides alone / acts then notifies / proposes for approval / human takes over)

## Output location

`../Output/agent-purpose-document-scenario-1-{NNN}.md`

## After generation

1. Run through `agent-purpose-document-checklist.md`
2. Check: could you hand this document to Claude Code and get a faithful build? If not, where are the ambiguities?
3. Check: does the autonomy matrix have entries in at least 3 of the 4 tiers?
4. **Run the closed build loop** before Thursday 14:15 — this is the artefact you hand to Claude Code
5. Feed forward into Deliverable #5 (System/Data Inventory)

