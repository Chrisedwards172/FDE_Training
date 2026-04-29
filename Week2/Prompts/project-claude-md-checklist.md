# Checklist — Project CLAUDE.md (Deliverable #7)

> Use this **after** generating your project CLAUDE.md to verify completeness.

## Completeness check

### Project identity

- [ ] **Project purpose** stated — what the agent system does and why it exists
- [ ] **Agent's Job to be Done** encoded (from Deliverable #4)
- [ ] **Business context** — which organisation, department, and process

### Domain entities

- [ ] Key entities named and defined (e.g. Hire, Onboarding Case, Compliance Path, Buddy Assignment)
- [ ] Entity relationships described enough that a developer understands the domain model
- [ ] Entities match those used in Deliverables #1–4 (no new entities invented without justification)

### System integrations and constraints

- [ ] Every system from Deliverable #5 listed with integration status
- [ ] API-less systems flagged with constraints (e.g. "Saba LMS — no API; compliance training assignment requires human fallback")
- [ ] Shadow systems acknowledged (e.g. Excel Master Tracker)
- [ ] Data quality constraints noted (e.g. "Workday is not real-time — tracker is the live source during onboarding")

### Delegation boundaries and autonomy rules

- [ ] Autonomy matrix from Deliverable #4 encoded as rules (not just a reference to another document)
- [ ] "The agent may" and "The agent may not" sections present
- [ ] Escalation triggers encoded
- [ ] Monetary or risk thresholds explicit

### Conventions

- [ ] Source-tagging rules (how assumptions and citations are marked in project artefacts)
- [ ] Naming conventions for files, entities, or outputs
- [ ] Output placement rules (where generated artefacts go)

### Scope boundaries

- [ ] What is **in scope** for the agent (the primary work stream)
- [ ] What is **out of scope** (other work streams, adjacent systems, future phases)
- [ ] What should be **escalated** vs **refused** vs **deferred**

## Quality check

- [ ] A developer reading only this CLAUDE.md would understand the agent's purpose, boundaries, and constraints
- [ ] The file does not contradict Deliverables #4 or #5
- [ ] Conventions are actionable (not vague aspirations like "follow best practices")

## Anti-pattern check

| Anti-pattern | How to detect | Fix |
|---|---|---|
| **Copy of Week2/CLAUDE.md** | References FDE program, gates, peer review | This is a *project* CLAUDE.md, not a training CLAUDE.md — rewrite for a developer audience |
| **No autonomy rules** | Missing "may/may not" or escalation encoding | Translate Deliverable #4's autonomy matrix into CLAUDE.md rules |
| **Generic conventions** | "Follow standard naming" with no specifics | Name the actual conventions for this project |
| **Missing system constraints** | Systems listed but no integration status or gaps | Pull Gap/Risk column from Deliverable #5 |

