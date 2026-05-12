# Checklist — System/Data Inventory (Deliverable #5)

> Use this **after** generating your System/Data Inventory to verify completeness.

## Completeness check

### Assumption Log

- [ ] Every `[ASSUMED]` tag references a numbered entry in the **Agent Purpose Document's** consolidated Assumption Log
- [ ] API availability assumptions clearly flagged (many will be inferred, not stated)

### Inventory table

- [ ] Columns present: System, Data needed, Access type (Read/Write/Both), Availability, Gap/Risk
- [ ] **Every system from the scenario tooling sketch** has an entry (Workday, ServiceNow, Saba LMS, SharePoint, Outlook for the practice scenario)
- [ ] **Shadow/unofficial systems** from sample artefacts included (e.g. the Excel Master Tracker on OneDrive)
- [ ] Access type is specific: Read, Write, or Read/Write — not just "Yes"

### API and integration reality

- [ ] Systems with **available APIs** noted with specifics (REST, SOAP, etc.) where the scenario provides them
- [ ] Systems with **no API** flagged explicitly (e.g. Saba LMS → "no API" per scenario) with impact on agent design
- [ ] **Batch-only or manual-only** systems flagged with workaround options noted
- [ ] Integration effort estimated (Low/Medium/High) per system where possible — tag as `[ASSUMED]` if not scenario-given

### Shadow systems and lived-work data

- [ ] Unofficial tools identified from sample artefacts (e.g. tracker Excel, desk-printed flowcharts, email threads as coordination tools)
- [ ] For each shadow system: what data does it hold that the official systems don't?
- [ ] Risk of shadow system flagged (single point of failure, no backup, no audit trail)

### Gap/Risk column

- [ ] Each entry has a substantive gap or risk statement (not just "none" or "OK")
- [ ] Risks are specific to the agent design (e.g. "agent cannot assign compliance training without Saba API — requires human fallback or screen-scraping workaround")
- [ ] Data quality risks noted where artefacts show them (e.g. "Workday not updated in real-time — Priya updates tracker first, refreshes Workday end-of-week" from Artefact 1.2)

## Anti-pattern check

| Anti-pattern | How to detect | Fix |
|---|---|---|
| **Only official systems listed** | Shadow tools from artefacts missing | Re-read artefacts — where does Priya *actually* go for information? |
| **Hand-waving integration gaps** | "Saba LMS: will need integration" with no detail | Name the constraint (no API), the impact (agent can't assign training), and the workaround options |
| **Availability column says "Yes" everywhere** | No differentiation between well-integrated and hard-to-reach systems | Score availability honestly — some systems are easy (REST API), some are blocked |
| **No data quality risks** | Every system treated as clean and reliable | Review artefacts for evidence of stale data, manual updates, or dual sources of truth |

## Feed-forward

- System gaps and missing APIs are prime candidates for **Deliverable #6** (Discovery Questions)
- Available integrations inform the compounding roadmap (which shared assets get built in Wave 1)

