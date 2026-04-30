# Discovery Responses — Priya Aggarwal, HR Ops Lead

> **Persona:** Priya Aggarwal, HR Ops Lead at Aldridge & Sykes. 6 years with the firm, 3 in the current role. Knows the operation inside-out but hasn't had time to step back and document it properly. Pragmatic, slightly defensive about her tracker, willing to talk honestly if she trusts the interviewer isn't trying to eliminate her role.

---

## Q1: Silent routing failure frequency

> "When Tom's laptop ticket got stuck because the consulting spec changed — how often does that happen?"

**Priya's answer:**

"More than I'd like. Consulting is the worst — they change specs roughly twice a year, and nobody tells us until something breaks. Last year it happened three times that I noticed. But honestly? I suspect it's happened more and we just didn't catch it because the hire didn't complain loudly enough. Tax and audit are more stable — their specs haven't changed in over a year. The problem is that the change gets approved at divisional level, Procurement updates the order catalogue, but nobody thinks to tell HR Ops or update the ServiceNow routing rules. We find out when tickets go to the wrong queue."

**Follow-up — is it always consulting?**

"Mostly. Although — actually, Birmingham office had a thing last spring where building access was being routed to Manchester facilities because someone set up the location codes wrong when Birmingham moved floors. That took two weeks to sort out. It's not always equipment specs — sometimes it's routing rules being stale in general."

**Design impact:** Confirms this is a recurring problem (~3–5 times/year, primarily consulting). Validates the spec repository concept. Also surfaces a *location-based* routing failure not in the current design — the OPC may need to validate location codes as well as equipment specs.

---

## Q2: Tracker as source of truth — team access and format stability

> "Do your two coordinators see the hidden columns? And how often does the tracker format change?"

**Priya's answer:**

"The coordinators can see the full tracker if they un-hide the columns, but they don't usually bother. They work from the visible columns — Name, Start, Type, status. The hidden columns are really my notes to myself. Risk flags, buddy overrides, that sort of thing. I wouldn't say I *hide* them from the team, it's more that the information is context I carry — they'd have to ask me anyway to understand what 'Director's hire from Deloitte, sensitive about onboarding speed' means in practice."

**Follow-up — format stability?**

"I add a column maybe once or twice a year. I added the Risk flag column about eighteen months ago when we started getting more consulting hires and I needed to track which ones were politically sensitive. I haven't moved columns in a long time though — the basic layout has been the same for about two years. What I *do* change is the dropdown values in some columns. Like, 'Pending IT — laptop' used to just be 'Pending IT' until I needed to distinguish laptop from software from access."

**Design impact:** Column layout is reasonably stable (~2-year consistency). Hidden columns are Priya's private context layer — coordinators don't routinely use them. Agent reading hidden columns would surface knowledge the coordinators don't currently have access to, which could change team dynamics. Format changes are minor (dropdown values, rare new columns) — header-based reading should be robust enough.

---

## Q3: Escalation priority — rules or pure judgment?

> "When you decide whether a stuck ticket is Amber or Red — is there a pattern?"

**Priya's answer:**

"There's definitely a pattern, even if I've never written it down. Red is when the hire's start date is at risk and someone senior is already asking about it. Amber is when we've missed an internal SLA but nobody external knows yet. Green is... everything is where it should be.

Consulting hires almost always start at Amber just because the consulting directors are more demanding. If a partner is involved in the hiring decision — like Tom, who was poached from Deloitte — that's Red from day one regardless of ticket status, because I know I'll get a call the moment anything slips.

Tax and audit are more straightforward. They'll tolerate a day or two of delay without escalating. The exception is anyone in the Dublin office — there's something about being remote that makes delays feel worse to them, and the Country Manager there has a short fuse."

**Design impact:** There ARE patterns — Priya articulated them clearly once asked:
- **Red:** start date at risk + senior stakeholder already asking, OR partner-sponsored hire
- **Amber:** internal SLA missed but no external visibility yet
- **Consulting default:** Amber baseline
- **Dublin:** treat as higher sensitivity (like consulting)

These can be partially codified in the priority escalation scoring. The agent could auto-flag consulting + Dublin hires as elevated sensitivity. Partner-sponsored hires would need keyword detection in notes (as the current ET-3 design proposes).

---

## Q4: Non-standard hire classification — conversion/rehire volume and patterns

> "How often do you get rehires or contractor-to-FTE conversions?"

**Priya's answer:**

"Conversions — maybe 15–20 a year? It's been growing because consulting hires a lot of contractors for project work and then converts the good ones. The pain point is always the same: Workday creates a fresh FTE record but the contractor record stays there. Compliance history doesn't carry over. If I'm lucky, the coordinator remembers to check, but if it's someone new on the team, they wouldn't know to look.

Rehires are less frequent — maybe 8–10 a year? Those are the messy ones. If someone left less than a year ago, Workday usually lets us reactivate. Over a year and we often have to create new, especially if their old record was from a different entity or a different role. IT sometimes flags it as a duplicate — that's what happened with James."

**Follow-up — is there a rule for reactivate vs create new?**

"There's no written rule. I use a year as my rough guideline — under a year, try reactivate first. Over a year, create new and link the old record in the notes. But honestly, it depends on IT's mood. Sometimes they'll reactivate a two-year-old record if the data is clean, sometimes they'll refuse a six-month one because they've already archived it. I usually just ask them."

*[Priya pauses]*

"Actually, the Dublin ones are always new records regardless. Something to do with the Irish entity being set up separately in Workday. I forgot about that."

**Design impact:** Confirms the ET-1 classification rule is roughly right but needs refinement:
- Conversions: ~15–20/yr, growing — compliance history gap is the consistent issue
- Rehires: ~8–10/yr — Priya's <1 year / >1 year heuristic is a candidate for codification, BUT IT's response is inconsistent
- Dublin: always new record regardless of gap (entity-level constraint)
- Agent could classify with the heuristic and propose, but IT sign-off makes this human-led regardless. HITL rate estimate of 15–20% holds.

---

## Q5: Who updates ServiceNow routing rules when specs change?

> "When the consulting laptop spec changed last quarter, who was supposed to update ServiceNow routing?"

**Priya's answer:**

"That's the problem — nobody is 'supposed to.' Procurement updates the order catalogue when a spec changes. IT manages ServiceNow routing rules. HR Ops raises tickets. None of us are talking to each other about it. When consulting changed to the new ThinkPad spec last quarter, Procurement updated the catalogue, but nobody told IT to update the routing rules — and nobody told me until Tom's ticket landed in the wrong queue five days later.

I raised it with IT afterwards and they said 'we need a change request form' — but there's no process for triggering that form when Procurement changes a spec. It just... falls between the cracks."

**Follow-up — could you update ServiceNow routing directly?**

"No. We don't have admin access to ServiceNow routing configuration. We can create tickets, modify priority, add comments — but the routing rules are IT-managed. If the agent needed to change routing, it would need IT to grant access or build an automated handoff. That's a conversation I haven't had with them."

**Design impact:** Critical governance gap confirmed. The spec repository solves part of this (the agent can detect mismatches), but the *fix* for stale routing rules requires IT action. This means:
- The OPC can detect and work around routing failures (override ticket parameters)
- But the OPC cannot fix the root cause (update routing rules)
- A governance process (quarterly routing review triggered by spec changes) is outside the agent's scope but should be recommended as an organisational change
- Confirms D5 assumption: HR Ops can modify tickets but not routing config

---

## Q6: Workday sync timing and consequences

> "Has a stale Workday record ever caused a problem downstream?"

**Priya's answer:**

"Once — about eight months ago. Payroll pulled data from Workday before I'd updated it, and a new hire's bank details were missing because I was still processing them in the tracker. The hire didn't get paid on time. That was a bad day.

But it's rare. Payroll runs mid-month, and I usually have Workday up to date by then. The risk is the first two weeks after a start date, when everything is still in flux. By the time Workday matters for downstream systems — payroll, benefits, compliance reporting — the onboarding is usually settled."

**Follow-up — could the agent sync more often?**

"I wouldn't mind daily sync for the critical fields — status, start date, that sort of thing. But not everything. Some of the notes and flags in the tracker are messy drafts — I wouldn't want those going into Workday. A selective daily sync for 'hard' data and a weekly full reconciliation would be fine."

**Design impact:** Stale Workday is a real risk but rare (~1 incident in 8 months). Priya's suggestion aligns well: daily sync for status/start date fields, weekly full reconciliation. Revise the Operating Triggers section to add a lightweight daily sync (status + start date only) alongside the end-of-week full sync.

---

## Q7: What triggers a hire becoming "high sensitivity"?

> "How do you know which hires are sensitive?"

**Priya's answer:**

"It's a mix. Some I know from the requisition — if the hiring manager is a partner or a division director, that tells me the hire is visible. The recruiter sometimes gives me a heads-up: 'this one came from a competitor, the partner really wants a smooth landing.' That's how I knew about Tom.

Consulting hires above manager level are almost always sensitive. Tax and audit are less political, but if someone is coming in to lead a new service line or a practice area, that's high profile too.

The other one that catches me out is client-facing roles. If a new hire is going straight onto a client engagement and they don't have their laptop or access on day one, the client notices. That's happened twice this year — both consulting."

**Follow-up — do you flag these at the start or react as things happen?**

"I try to flag at the start. When I create the tracker row, if I know it's sensitive, I put a note in. But sometimes I don't know until the hiring manager's PA calls me asking where the laptop is. Like Tom — I knew he was a Deloitte poach, but I didn't flag Amber until day three when the emails started."

**Design impact:** Confirms that sensitivity is partially articulable:
- Partner/director sponsor → always sensitive
- Consulting above manager level → default sensitive
- New service line / practice lead → sensitive
- Client-facing with day-one engagement → sensitive
- But some sensitivity only emerges reactively (PA calls, hiring manager emails)

The auto-inference rules in ET-3 cover the first two. The agent should also flag "client-facing = true" if that attribute is available in Workday. Reactive sensitivity (discovered mid-onboarding) means the agent should monitor for incoming stakeholder communications as a secondary sensitivity signal.

---

## Q8: Previous automation attempts

> "What was tried before, and what broke?"

**Priya's answer:**

"Two things. First, about three years ago, someone in IT built a Power Automate flow that was supposed to auto-create ServiceNow tickets from Workday hire records. It worked for standard FTEs but completely broke for contractors — different ticket categories, different approval flows. It generated a bunch of wrong tickets and we spent a week cleaning up. After that nobody wanted to touch it again.

Second, the ServiceNow auto-routing itself — that's been there since we adopted ServiceNow. It works fine for most tickets, but it's based on role codes and location codes, and when either of those gets out of sync with reality, it routes to the wrong team. The Tom situation was that — routing rules pointing to an old hardware spec.

We haven't tried anything with AI. The CFO asked me to 'look at AI options' but what he really means is 'make the consulting directors stop complaining about onboarding.' He doesn't have a specific solution in mind."

**Design impact:** Previous automation failed because it didn't handle non-standard hire types (contractors). This directly validates the OPC's delegation architecture — the "everything is fully agentic" approach was already tried (via Power Automate) and failed. The lesson: the agent must not auto-create tickets for non-standard types without human confirmation. Current design already addresses this (ET-1 escalation for non-standard). The CFO's motivation is political (consulting complaints) not technical — this frames the OPC's success metrics around the consulting division's experience.

---

## Q9: Badge and building access — same system or separate?

> "Does badge ordering go through ServiceNow?"

**Priya's answer:**

"Badges go through ServiceNow — same as IT equipment. Building access is a bit different. Manchester and Leeds use ServiceNow for building access too, but Birmingham has a separate facilities management company that handles their building, and I have to email them directly. Dublin is so small that building access is just... the office manager adds you to the fob system, and I send her an email."

**Design impact:** Not uniform. Manchester/Leeds = ServiceNow. Birmingham = separate email-based process. Dublin = informal email to office manager. The OPC needs:
- ServiceNow integration for Manchester/Leeds building access (already in design)
- Email-based request for Birmingham (Outlook integration, or flag for human)
- Email to Dublin office manager (Outlook integration)

This adds complexity to the "Request badge ordering and building access" item in the autonomy matrix — it's not a single ServiceNow action. The agent would need location-aware logic. For Wave 1, the simplest approach: auto-raise ServiceNow for Manchester/Leeds, draft emails for Birmingham/Dublin for coordinator review.

---

## Q10: Coordinator workload distribution

> "How do you and the coordinators split the work?"

**Priya's answer:**

"Loosely by division. Sarah handles audit and tax — they're more predictable, fewer edge cases. Dev handles consulting and Dublin — he's been here longer and can deal with the more demanding hiring managers. I handle the edge cases directly, plus I review everything before it goes to Workday.

When someone's on leave, the other coordinator picks up their work, but they're usually slower because they don't know the division contacts as well. If both are out — which happened once last Christmas — I do everything, and things slip."

**Design impact:** Cases ARE assigned to specific coordinators by division:
- Sarah: audit + tax
- Dev: consulting + Dublin
- Priya: edge cases + oversight

This means OPC escalation targets should be case-specific:
- ET-1 / ET-4 for consulting/Dublin → Dev
- ET-1 / ET-4 for audit/tax → Sarah
- Edge cases / Red flags → always Priya

Revise escalation triggers from generic "HR Coordinator" to division-based routing. Also surfaces a bus-factor risk: if Dev is absent, consulting onboardings (the highest-sensitivity ones) are handled by Sarah, who is less familiar with consulting contacts.

---

## Questions Priya couldn't fully answer

### Workday API field availability (from various assumptions)

"You'd need to ask IT about that. I know Workday has APIs because we were told that during the implementation, but I've never used them. I don't know which fields are exposed. Our HRIS analyst might know — his name is Raj, he sits in the Manchester IT team."

### ServiceNow API access permissions for HR Ops

"I can create tickets and change priority through the web interface. Whether we have API access... I genuinely don't know. That's an IT question. I've never asked because we've never needed it."

### Saba LMS integration possibilities (bulk upload, CSV, RPA)

"There might be a bulk upload? I've never looked. We've always assigned training one by one through the interface. It's slow but it works. If there's a shortcut, nobody's told us about it."

---

## Key takeaways for OPC design revision

1. **Routing failures are recurring (~3–5/yr) and cross-division** — validates spec repository; also need to cover location-code mismatches, not just equipment specs
2. **Priya's escalation patterns are codifiable** — consulting + Dublin = elevated baseline; partner/director sponsor = Red from day one; client-facing day-one engagement = elevated
3. **Rehire/conversion classification has a heuristic (<1yr reactivate, >1yr new), but IT is the wild card** — keep as human-led with agent proposal
4. **Nobody owns the routing-update governance chain** — OPC can detect and work around, but fixing root cause requires organisational change
5. **Building access is location-dependent** — Birmingham and Dublin are email-based, not ServiceNow
6. **Coordinator assignment is division-based** — escalation routing should be case-specific, not generic
7. **Daily lightweight sync + weekly full reconciliation** — Priya's preference, replaces current weekly-only design
8. **Power Automate failure is the ghost in the room** — it failed on non-standard hires; our design must visibly address this or Priya won't trust it

