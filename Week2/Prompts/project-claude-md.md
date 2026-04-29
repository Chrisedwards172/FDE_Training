# Prompt — Project CLAUDE.md

> **This is a lightweight trigger prompt.** The structural rules for Deliverable #7 are encoded in `../CLAUDE.md` § Deliverable Output Rules. Use `project-claude-md-checklist.md` in this folder to verify your output after generation.

## Instruction

Produce **Deliverable #7 — `CLAUDE.md` for the project** — a CLAUDE.md file that would sit at the root of the agent project being designed in Deliverables #1–6.

**This is not a copy of `Week2/CLAUDE.md`.** It is a project-level CLAUDE.md for the *agent system you've been designing* — demonstrating that you can encode workflow discipline, agent constraints, and project context into a format that shapes AI-assisted development.

**Input dependencies:** Load your most recent versions of Deliverables #4 (Agent Purpose Document) and #5 (System/Data Inventory) from `../Output/`. These contain the agent's purpose, scope, autonomy rules, and system constraints that the CLAUDE.md must encode.

**The CLAUDE.md should include:**
- Project purpose and the agent's Job to be Done
- Key entities in the domain (from the scenario)
- System integrations and constraints (from Deliverable #5)
- Delegation boundaries and autonomy rules (from Deliverable #4's autonomy matrix)
- Source-tagging and assumption-logging conventions
- What the agent may and may not do (scope boundaries)
- Naming, output, and formatting conventions for the project

**Reference:** `../../Week1/SupportingDocs/claude-md-examples-guide.md` for structural patterns.

## Output location

`../Output/project-claude-md-scenario-1-{NNN}.md`

## After generation

1. Run through `project-claude-md-checklist.md`
2. Check: does it encode the autonomy matrix from Deliverable #4?
3. Check: would a developer loading this file understand the agent's boundaries without reading your other deliverables?

