# Checklist — Cognitive Load Map (Deliverable #1)

> Use this **after** generating your Cognitive Load Map to verify completeness, and **before** the Thursday peer review submission. This is a review tool, not an execution prompt.

## Completeness check

### Assumption Log (top of document)

- [ ] Log appears **before** Section 1, not at the bottom
- [ ] Every entry has: #, Type (AGENT/HUMAN), Assumption, Confidence (Low/Medium/High), Test
- [ ] Every `[ASSUMED]` tag in the body has a matching numbered entry
- [ ] No assumption is marked High confidence unless validated by a coach session

### Section 1 — Lived-Process Narrative

- [ ] Covers **≥ 2 of the 4 work streams**
- [ ] Grounded in sample artefacts (emails, tracker excerpts, flowchart annotations) — not restating the SOP
- [ ] Names at least one **documented ↔ lived divergence** per work stream (e.g. "Workday is system of record but Priya updates the tracker first")
- [ ] Identifies cognitive hotspots: where the worker pauses, checks a reference, calls someone, or makes a judgment call

### Section 2 — Jobs to be Done Decomposition

- [ ] Each JtD has all 8 fields: ID, Trigger, Actor, Goal/Outcome, Key decisions, Key systems, Expected output, Primary type
- [ ] JtDs are **cognitive contracts** (what must be *decided*), not task lists (what must be *done*)
- [ ] Primary type is one of: Decision-making / Execution / Synthesis / Communication / Exception-handling
- [ ] At least one JtD per work stream is primarily Decision-making or Exception-handling (not all Execution)

### Section 3 — Cognitive Zones and Breakpoints

- [ ] Micro-tasks grouped into named zones (e.g. Intent Understanding, Data Retrieval, Diagnosis, Decision, Action, Documentation)
- [ ] At least **one breakpoint per work stream** identified
- [ ] Each breakpoint labelled with format: `BP-X.Y: [shift type] — [description]`
- [ ] Shift types include at least one **Rule → Judgment** transition (every work stream has one)
- [ ] Breakpoints are specific — not "sometimes judgment is needed" but "compliance path selection diverges when hire type = contractor-to-FTE conversion"

### Section 4 — Micro-Task Inventory

- [ ] Every micro-task from Section 3 appears in the scoring table
- [ ] Scored on all 8 ATX dimensions: Cognitive Load, Input Structure, Decision Determinism, Exception Frequency, Turn-Taking Degree, Latency Constraint, Compliance/Risk Sensitivity, Tool/API Availability
- [ ] Scores are **not uniform** — if most tasks score the same, decomposition is too coarse
- [ ] Uncertain scores use `?` suffix (e.g. `M?`) with a matching assumption log entry
- [ ] Tool/API Availability uses inverted scale (H = available = favours delegation)

### Section 5 — Process Topology Diagram (optional)

- [ ] Include **only if** ≥ 3 zones with non-obvious handoffs
- [ ] Mermaid `flowchart TD` format
- [ ] Zones as subgraphs, micro-tasks as nodes, breakpoints as annotated edges
- [ ] Caption line below the code block (`*Figure N — short description*`)
- [ ] ≤ 25 nodes; split if larger

## Source-tagging check

- [ ] Claims grounded in artefacts tagged `[Artefact 1.1]`, `[Artefact 1.2]`, `[Artefact 1.3]` etc.
- [ ] Inferences from scenario brief (not artefacts) tagged `[INFERRED — scenario brief]`
- [ ] Unknowns tagged `[ASSUMED]` with log entry
- [ ] No untagged factual claims about how work happens

## Anti-pattern self-check

| Anti-pattern | How to detect | Fix |
|---|---|---|
| **Documented-process-as-lived-work** | Your narrative reads like the SOP flowchart | Rewrite grounding in artefact evidence — what does Priya *actually* do? |
| **Flat decomposition** | JtDs are verb-noun pairs ("send email", "update Workday") | Reframe as cognitive contracts: what *decision* does this resolve? |
| **Missing breakpoints** | No `BP-` labels in Section 3 | Re-examine where rule-following stops and judgment begins |
| **Uniform scoring** | Micro-task table is a wall of `M` | Split coarse tasks into finer micro-tasks; score again |
| **Bluffing domain knowledge** | Claims about system behaviour or stakeholder priorities without artefact evidence | Convert to `[ASSUMED]` with confidence level and test |

## Feed-forward

The micro-task inventory (Section 4) is the **direct input** to Deliverable #2 (Delegation Suitability Matrix). Each micro-task's 8-dimension scores map to delegation suitability dimensions. If Section 4 is thin, Deliverable #2 will be thin.

