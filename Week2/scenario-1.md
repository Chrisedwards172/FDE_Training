# Scenario 1 — HR Onboarding Coordination

> Extracted from [`SupportingDocs/README-Participants-Week1-Scenarios.md`](SupportingDocs/README-Participants-Week1-Scenarios.md) for reuse across Week 1 prompts. The scenario text below is verbatim; the HUMAN assumptions that follow are the participant-supplied assumptions lifted from [`../Scenario1/build-spec.md`](../Scenario1/build-spec.md).

---

## Week 1 Scenario text (verbatim)

> A regional professional-services firm (1,200 employees, 220+ hires per year) runs new-hire onboarding through a 3-person HR Ops team.
> Each onboarding spans ~40 tasks across 2 weeks: IT provisioning, benefits enrolment, compliance training assignment, buddy matching, welcome materials, 30-day checkpoint scheduling, and manager handoff.
> Tasks originate from 6 different systems. Roughly 15% require judgment calls — which compliance track applies to a contractor versus a full employee, whether a buddy assignment crosses seniority norms, whether a late I-9 triggers a hold.
>
> The HR Ops lead says: *"Most of this is paperwork my team should not be touching, but every time we try to automate, something falls through the cracks because the edge cases never look the same twice."*
>
> Their stack is:
> - Workday for core HR
> - ServiceNow for IT requests
> - a separate LMS for compliance training
> - email for everything the other three don't cover.
>
> They have no AI infrastructure today.

---

## Scenario 1 (enriched) — HR Onboarding Coordination

*Original brief in `README-Participants-Week1-Scenarios.md` § Scenario 1.*

## Week 2 Enriched Scenario text (verbatim)


### The company

**Aldridge & Sykes** — Manchester-headquartered regional professional services firm (UK). 1,200 employees across audit, tax, and consulting; offices in Manchester, Leeds, Birmingham, and a small Dublin team. ~85% FTE, ~15% contractors / secondments / rehires. 220+ hires/year, with strong growth in the consulting division.

### The function

3-person HR Ops team supporting all hires across the firm: an HR Ops Lead and 2 HR Coordinators.

### The four work streams

- **New-hire system & access setup** (~190/yr; effective handling ~3 hrs/case spread across 2 weeks). Workday record creation, IT requests, badge ordering, payroll setup, building access.
- **Compliance training assignment & tracking** (~220/yr; ~45 min/case for assignment plus chasing). Choosing the right LMS path based on role, country (UK vs Republic of Ireland), prior employment certifications.
- **Buddy matching & welcome cadence** (~220/yr; ~30 min initial + ~60 min across the first 30 days). Buddy assignment, 30-day check-in scheduling, welcome materials, manager handoff.
- **Edge-case resolution** (~30–50/yr; ~4 hrs/case but unpredictable). Late right-to-work checks (Home Office share-code / passport verification), expired visa work permits, missing reference checks, contractor-to-FTE conversions, rehires with frozen records.

### Tooling sketch

- **Workday** (core HR, modern, REST APIs available)
- **ServiceNow** (IT requests, robust auto-routing)
- **Saba LMS** (compliance training, no API)
- **SharePoint** (onboarding doc library)
- **Outlook** (most stakeholder communication)

### Stakeholder

**Priya Aggarwal**, HR Ops Lead. Recently asked by the CFO to "look at AI options" after onboarding delays surfaced as a complaint from the consulting division.

### What you're expected to elicit through the week

You do not have the full picture. Bring questions to your coach (who role-plays Priya) about:

- What automation has been tried at Aldridge & Sykes before, and what happened?
- How does the team's actual practice differ from the documented onboarding SOP?
- What tools does Priya rely on that aren't in the system list above?
- What does she fear about an AI-driven approach?
- Where do contractors, secondments, and rehires fit in real practice — not just on paper?

### Sample artefacts

#### Artefact 1.1 — Email thread, delayed laptop

*Subject: RE: RE: RE: New consultant Tom Reeves — Day 5 with no laptop. Between Mike Tehrani (Consulting Director's PA) and Priya Aggarwal (HR Ops Lead). 5 messages over 5 days.*

**Day 1, 09:14 — Mike → Priya:**
> "Morning Priya — Tom Reeves started Monday, the senior consulting hire from the Deloitte poach. He's been here three days and hasn't received his laptop. Anyone in your team handling this? Mike."

**Day 1, 16:48 — Priya → Mike:**
> "Sorry Mike — checking now. ServiceNow ticket #INC-44102 is open, sitting with IT for hardware allocation. Will chase. P."

**Day 3, 11:02 — Mike → Priya:**
> "Hi Priya, status? It's Wednesday now, Tom's on a loaner from reception that security need back tomorrow. The director is not happy."

**Day 3, 15:30 — Priya → Mike:**
> "Reset the ticket priority and pinged IT directly. ServiceNow ETA tomorrow. Apologies for the delay — the consulting laptop spec changed last quarter and the auto-routing didn't pick it up."

**Day 5, 08:45 — Mike → Priya:**
> "Still nothing. The director has emailed the CFO. Please escalate."

#### Artefact 1.2 — Master Tracker excerpt

*Selected row from Priya's "Onboarding Master Tracker" (Excel, OneDrive). Some hidden columns un-hidden for this excerpt.*

| Hire | Start | Type | Workday status | Visible status | (hidden) Notes | (hidden) Risk flag | (hidden) Buddy override |
|---|---|---|---|---|---|---|---|
| Tom Reeves | 14.10 | FTE | Active | Pending IT — laptop | Director's hire from Deloitte; sensitive about onboarding speed | Amber — laptop ETA missed | Paired with Sarah J (peer level), not Anna (rule says senior pair) |
| Maria Costa | 14.10 | Contractor → FTE Q1 | Active (FTE record only) | On track | Originally contractor June; FTE conversion record didn't pull contractor compliance history | Green | Default rule |
| James O'Connor | 21.10 | Returning hire | Pending Workday reactivation | On hold | Was contractor 2022; old record frozen, IT thinks duplicate | Red — start delayed | n/a until live |

*Workday is the "system of record" but Priya updates the tracker first and refreshes Workday end-of-week.*

#### Artefact 1.3 — Compliance Training Routing Flowchart fragment

*From SharePoint > HR Ops > Onboarding > "Compliance Training Routing v4.2" (last revised October 2023).*

```
[Hire Type?] → [FTE]                    → Path A (Standard FTE Pack)
            → [Contractor]              → Path B (Reduced — see below)
            → [Secondment]              → Path C (Client-specific)

[Path B — Contractor]
  ├─ Role code = CONS-A,B,C  → assign 6-module compliance pack
  ├─ Role code = CONS-D       → assign 4-module compliance pack
  └─ Role code = TEMP-EXT     → no assignment (out of scope)
```

*Footnote pencilled on the printed copy on Priya's desk: "TEMP-EXT retired 2024-Q1 — these now route as CONS-D. Update flowchart sometime."*

---

