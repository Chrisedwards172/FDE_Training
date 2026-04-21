# Integration Spec Template

## How to Use This Template

This template is designed to be handed to an AI agent alongside a scenario. Fill in the **[bracketed prompts]** or leave them as instructions to the agent. The agent will produce a buildable specification structured to pass the `production-spec-checklist.md` criteria.

**Recommended usage pattern:**

```
"Using the scenario below and the structure in integration-spec-template.md,
produce a complete buildable specification. Flag any section where the scenario
does not supply enough information to complete the field — mark those [ASSUMPTION:
<your assumption>] or [UNKNOWN: <what needs validation>] rather than guessing."
```

Paste the scenario text after that instruction. The agent will populate the template. You then review, diagnose gaps, and iterate.

> **This template is for spec-generation, not spec-storage.** The output is a new file in your working directory — not an edit to this template. Name the output `spec-<scenario-slug>.md`.

---

## Part 1 — Problem Statement

### 1.1 The Problem Being Solved

> State the problem precisely: what is breaking, for whom, at what volume, at what cost. Use the numbers from the scenario. Do not use generic business-speak.

**[Agent instruction: Write 3–5 sentences. Ground every claim in a number or constraint from the scenario. Do not introduce numbers not in the scenario.]**

### 1.2 Why Agentic, Why Now

> Explain what makes this a viable candidate for an agentic solution, and what the trigger or urgency is.

**[Agent instruction: Identify: (a) the volume argument — why human effort at this scale is the wrong tool; (b) the repeatability argument — which parts of the work are rule-governed enough for an agent to handle; (c) the constraint argument — what hard constraints exist that prevent full automation.]**

### 1.3 Success Metrics

> Define what "working" means — quantitatively. Success metrics must be testable, not aspirational.

| Metric | Current State | Target State | Measurement Method |
|---|---|---|---|
| [e.g., time-to-first-decision] | [current value from scenario] | [target value] | [how measured] |
| [e.g., accuracy rate] | [current] | [target] | [how measured] |
| [e.g., human review volume] | [current] | [target] | [how measured] |

**[Agent instruction: Use the numbers given in the scenario. Do not invent baselines. If the scenario does not give a current metric, mark it [UNKNOWN: baseline not provided — flag for client validation].]**

---

## Part 2 — Delegation Analysis

### 2.1 Work Inventory

> Map out every identifiable task or decision in the process and classify it.

| Task / Decision | Classification | Rationale |
|---|---|---|
| [task name] | [FULL DELEGATION / HUMAN-IN-LOOP / HUMAN-LED] | [why — cite the specific constraint] |

Classification definitions:
- **FULL DELEGATION** — Agent handles end-to-end; consequence of error is reversible or low-stakes; no compliance, clinical, legal, or reputational constraint on the outcome.
- **HUMAN-IN-LOOP** — Agent acts, human verifies before effect takes place; used where the action is consequential or governed by a hard constraint.
- **HUMAN-LED** — Human decides; agent assists only (provides information, drafts options, surfaces context). Used where judgment is genuinely non-rule-governed or the hard constraint explicitly requires a named human.

**[Agent instruction: Be exhaustive. Do not collapse multiple distinct decisions into a single row. The delegation boundary is the most important design decision in the spec — each row must be justifiable from the scenario constraints.]**

### 2.2 Hard Constraints on the Boundary

> List every constraint that prevents full automation. These are non-negotiable; the boundary cannot be drawn past them.

| Constraint | Source | Effect on Boundary |
|---|---|---|
| [e.g., "no permit decision without named human reviewer"] | [scenario quote or regulatory source] | [what it forbids the agent from doing] |

**[Agent instruction: Quote the constraint from the scenario verbatim where possible. If the constraint comes from a regulation (HIPAA, GDPR, PCI-DSS, etc.), name the regulation and the specific rule, not just "regulatory compliance".]**

---

## Part 3 — Capability Specification

> One section per capability. A capability is a bounded, independently buildable and testable unit of agent behaviour. For Week 1, aim for 1–3 capabilities in the agentic portion of the solution.

### Capability [N]: [Capability Name]

#### 3.N.1 Purpose

> One sentence. What does this capability do and why does it exist?

#### 3.N.2 Scope

**In scope:**
- [explicit statement of what this capability handles]

**Out of scope:**
- [explicit statement of what this capability does NOT handle — prevents scope creep during build]

#### 3.N.3 Inputs

| Input | Type | Required / Optional | Validation Rule | Source |
|---|---|---|---|---|
| [field name] | [string / int / enum / etc.] | [R / O] | [exact rule, not "valid input"] | [where it comes from] |

#### 3.N.4 Outputs

| Output | Type | Condition | Destination |
|---|---|---|---|
| [field name] | [type] | [when this output is produced] | [where it goes] |

#### 3.N.5 Business Rules

> Every rule must be testable. Use "must," "will," "cannot" — not "should," "may," "might."

1. **[Rule name]:** [Exact rule statement. If conditional: state the condition, the action, and the outcome for each branch.]
2. **[Rule name]:** [...]

**[Agent instruction: For every rule that has a threshold (dollar amount, time window, count, score), make the threshold explicit and numeric. For every rule with a condition, write it as: IF [condition] THEN [action] ELSE [action].]**

#### 3.N.6 Escalation Triggers

> When does this capability stop and hand off to a human?

| Trigger | Condition | Who Is Notified | What the Human Must Do | SLA |
|---|---|---|---|---|
| [name] | [exact condition] | [role] | [explicit action required] | [time limit] |

#### 3.N.7 Decision Log

> What must the agent log at each decision point?

| Decision Point | Fields Logged | Storage Location | Retention |
|---|---|---|---|
| [decision name] | [field list] | [system / table] | [duration] |

---

## Part 4 — Entity Model

> Define every data entity the capability creates, reads, updates, or deletes.

### Entity: [Name]

**Attributes:**

| Attribute | Type | Required | Constraints | Notes |
|---|---|---|---|---|
| id | UUID | Yes | Primary key, immutable, generated on creation | |
| [attribute] | [type] | [Y/N] | [exact constraints: max length, min value, enum values, format] | |
| created_at | ISO 8601 timestamp (UTC) | Yes | Immutable | Set on creation |
| updated_at | ISO 8601 timestamp (UTC) | Yes | Updated on any modification | |

**State Machine** (if applicable):

```
[STATE_A] → [STATE_B]   Trigger: [what causes this transition]   Guard: [conditions that must be true]
[STATE_A] → [STATE_C]   Trigger: [...]                           Guard: [...]
[STATE_B] → [STATE_D]   Trigger: [...]                           Guard: [...]
[STATE_C] is terminal
```

**Immutability Rules:**
- [List attributes that cannot be changed after creation]

**Delete Behaviour:**
- [Soft delete / hard delete / restricted — and why]

---

## Part 5 — Integration Contracts

> One section per external system the capability calls.

### Integration: [System Name]

| Property | Value |
|---|---|
| **Purpose** | [what this integration does for the capability] |
| **Endpoint** | `[METHOD] [URL or URL pattern]` |
| **Authentication** | [type and credential location — e.g., "Bearer token, stored in env var SYSTEM_API_KEY"] |
| **Timeout** | [N seconds] |
| **Retry logic** | [on what HTTP codes; how many retries; backoff strategy] |
| **Rate limit** | [requests/minute or requests/day] |

**Request format:**
```json
{
  "field": "type (required/optional) — description"
}
```

**Success response (HTTP 200):**
```json
{
  "field": "type — description"
}
```

**Error responses:**

| HTTP Code | Meaning | Agent Action |
|---|---|---|
| 4xx | [what it means] | [exact action: reject, log, escalate, retry — not "handle gracefully"] |
| 5xx | [what it means] | [exact action] |
| Timeout | Request exceeded [N]s | [exact action] |

**Fallback behaviour:**
> If this integration is unavailable, the agent must: [exact action — not "degrade gracefully"].

**Data mapping:**

| Internal Field | Direction | External Field |
|---|---|---|
| [entity.attribute] | → | [system.field] |
| [entity.attribute] | ← | [system.field] |

---

## Part 6 — Validation Design

### 6.1 Happy Path

> One end-to-end scenario where everything works. Concrete inputs → concrete expected outputs.

**Scenario:** [Name]
**Input state:** [exact starting conditions]
**Steps:** [numbered sequence of what happens]
**Expected output:** [exact result — field values, state changes, notifications sent]

### 6.2 Edge Cases

> Minimum 5. Cover: empty/null inputs, boundary values, concurrent actions, unexpected states, timing.

| # | Scenario | Input | Expected Outcome | Pass / Fail / Escalate |
|---|---|---|---|---|
| EC-1 | [name] | [exact input] | [exact expected outcome] | [P/F/E] |
| EC-2 | | | | |
| EC-3 | | | | |
| EC-4 | | | | |
| EC-5 | | | | |

### 6.3 Failure Modes

> Minimum 3. For each: what breaks, what the agent does, how recovery happens.

| # | Failure | Agent Response | Recovery Path |
|---|---|---|---|
| FM-1 | [what fails] | [exact agent action] | [how the system recovers or how a human resolves it] |
| FM-2 | | | |
| FM-3 | | | |

### 6.4 Delegation Boundary Test

> At least one scenario that tests the boundary itself — what happens at the edge of the agent's authority.

**Scenario:** [Name — e.g., "Case that is borderline between full delegation and human review"]
**Input:** [exact conditions that put the case on the boundary]
**Expected agent behaviour:** [what the agent must do — escalate, act, log, ask]
**What a failure looks like:** [agent acts when it shouldn't, or escalates when it doesn't need to]

---

## Part 7 — Assumptions and Unknowns

> Minimum 5 genuine unknowns. Every assumption that could invalidate a business rule, integration contract, or delegation boundary must appear here.

| # | Assumption or Unknown | Why It Matters | What Breaks If Wrong | Status |
|---|---|---|---|---|
| A1 | [statement] | [what design decision it underlies] | [exact failure mode] | [KNOWN / ASSUMED / FLAG FOR VALIDATION] |
| A2 | | | | |
| A3 | | | | |
| A4 | | | | |
| A5 | | | | |

**Validation questions for flagged assumptions** (to be raised with the client or coach):

- A[N]: [Exact question. Who answers it. What you will do with the answer.]

---

## Part 8 — Spec Self-Audit

Before treating this spec as buildable, confirm:

- [ ] Every business rule uses "must / will / cannot" — no "should / may / might"
- [ ] Every threshold is numeric (no "large," "soon," "frequently")
- [ ] Every conditional has an explicit IF/THEN/ELSE
- [ ] Every entity has a primary key, timestamps, and state machine (if stateful)
- [ ] Every integration has: endpoint, auth, timeout, retry, rate limit, fallback, data mapping
- [ ] Delegation boundary has at least one hard constraint cited from the scenario
- [ ] Validation design has ≥ 1 happy path, ≥ 5 edge cases, ≥ 3 failure modes
- [ ] Every [UNKNOWN] and [ASSUMPTION] item is in the Assumptions Register (Part 7)
- [ ] No open [TODO] markers remain — either resolve, descope, or move to Assumptions

> A spec that does not pass this self-audit is not ready to hand to an AI coding agent. Failing items are spec gaps, not build problems — fix the spec first.

