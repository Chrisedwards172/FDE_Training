# Scenario 1 — HR Onboarding Coordination

> Extracted from [`SupportingDocs/README-Participants-Week1-Scenarios.md`](../SupportingDocs/README-Participants-Week1-Scenarios.md) for reuse across Week 1 prompts. The scenario text below is verbatim; the HUMAN assumptions that follow are the participant-supplied assumptions lifted from [`../Scenario1/build-spec.md`](../Scenario1/build-spec.md).

---

## Scenario text (verbatim)

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
>
> Design the agentic solution.

---

## HUMAN Assumptions

> Tag every assumption you carry into a spec as **HUMAN** (participant-supplied) or **AGENT** (agent-identified during drafting). Per the prompt rules in [`../Scenario1/build-spec.md`](../Scenario1/build-spec.md): 
> **High** confidence means coach-validated and may be treated as true for a first draft; 
> **Medium** / **Low** have not yet been tested in a coach session.

1. **HUMAN Assumption:** The HR Ops team is open to adopting an AI agent for onboarding coordination.
   - **Hypothesis:** If the HR Ops team is open to AI adoption, then they will be willing to collaborate on defining the agent's capabilities and providing feedback during development, because they have expressed frustration with current automation efforts.
   - **How I'd test it:** In a coach session, I would role-play with the HR Ops lead to gauge their enthusiasm and willingness to engage in the design process for an AI solution.
   - **Confidence:** Medium — while the HR Ops lead has expressed frustration with current automation efforts, it's not guaranteed that they will be receptive to an AI-based solution without further discussion.

2. **HUMAN Assumption:** The 15% of onboarding tasks that require judgment calls are consistent enough that an AI agent could learn to handle them effectively.
   - **Hypothesis:** If the judgment calls in onboarding tasks follow identifiable patterns, then an AI agent could be trained to make similar decisions, because many HR processes have established guidelines that could be codified into the agent's decision-making framework.
   - **How I'd test it:** I would ask the HR Ops team for examples of the judgment calls they encounter and analyse them for commonalities. In a coach session, I would present these examples and ask the coach to evaluate whether they seem like they could be systematised for an AI agent to learn from.
   - **Confidence:** Low — without seeing the specific judgment calls, it's difficult to assess whether they are consistent enough for an AI agent to handle, especially given the variability implied by *"the edge cases never look the same twice."*

3. **HUMAN Assumption:** The existing systems (Workday, ServiceNow, LMS) have APIs or integration points that an AI agent could use to coordinate tasks effectively. Email has SMTP or a transactional API for sending messages.
   - **Hypothesis:** If the existing systems have APIs or integration points, then an AI agent could be designed to interact with these systems to automate task coordination, because modern enterprise software typically includes some form of API access for integration purposes.
   - **How I'd test it:** I would ask the HR Ops team for documentation on the APIs or integration capabilities of Workday, ServiceNow, and the LMS. For email, I would inquire about how they currently send emails (e.g., through an SMTP server or a transactional email service) to understand how the AI agent could integrate with their email system. In a coach session, I would discuss the implications of these integration capabilities for the design of the AI agent.
   - **Confidence:** Medium — while it's common for enterprise systems to have APIs, there can be variability in their availability and functionality. The email integration is also uncertain without knowing their current setup.

4. **HUMAN Assumption:** Buddy assignments are determined by three codifiable factors — seniority, department, and location. Also you can only be a buddy to one person, so take this into consideration. The agent auto-assigns when a candidate passes all these factors. If multiple matches are found, prioritise in order of department, location and seniority. If still multiple matches, pick at random. If no candidate is available, the agent escalates to HR for manual assignment.
   - **Hypothesis:** If the three-factor filter (seniority + department + location) yields at least one eligible candidate, the agent can auto-assign without further judgment. If it yields zero, HR takes over — because capacity, leave, and pool gaps are facts HR already manages for the team.
   - **How I'd test it:** Tested in coach session — coach confirmed the three-factor model and the HR-manual-escalation-on-unavailability rule. Remaining operational probes (not confidence-blocking but build-blocking): (a) what exactly counts as "not available" — zero-match vs. capacity-exhausted vs. on-leave; (b) tie-break rule when multiple candidates pass the filter.
   - **Confidence:** High — coach-confirmed on the three-factor model and the escalation rule. The two operational details above are carried forward as AGENT assumptions in the spec, not as open HUMAN assumptions.

5. **HUMAN Assumption:** The 2 unnamed systems in "6 systems" are benefits system and payroll/time system, and they have similar integration capabilities as the named systems.
   - **Hypothesis:** If the unnamed systems are benefits and payroll/time systems with similar integration capabilities, then the AI agent could potentially integrate with them in the same way it would with Workday, ServiceNow, and the LMS, because many HR-related systems are designed to be interoperable.
   - **How I'd test it:** I would ask the HR Ops team to identify the unnamed systems and research their integration capabilities. In a coach session, I would discuss with the coach the implications of these systems' integration capabilities for the overall design of the AI agent.
   - **Confidence:** High — Coach session confirms the unnamed systems are benefits and payroll/time systems, and it's reasonable to assume they have similar integration capabilities given their role in HR processes.

6. **HUMAN Assumption:** The HR Ops team are fully open to an AI-driven solution and will provide the necessary access and support for integration with existing systems.
   - **Hypothesis:** If the HR Ops team is fully open to an AI-driven solution, then they will facilitate access to the necessary systems and provide support during the integration process, because they have expressed a desire to move away from manual coordination and have no AI infrastructure today, suggesting a willingness to explore new solutions.
   - **How I'd test it:** In a coach session, I would role-play with the HR Ops lead to discuss the level of access and support they would be willing to provide for integrating an AI agent with their existing systems. I would also ask about any potential barriers or concerns they might have regarding this level of involvement.
   - **Confidence:** High — Agreed in coach session that HR Ops is open to an AI-driven solution and will provide necessary access and support, given their expressed frustration with current automation efforts and lack of existing AI infrastructure.

7. **HUMAN Assumption:** The term "late I-9 triggers a hold" implies that there are compliance-related tasks that require immediate attention and may have legal implications if not handled correctly.
   - **Hypothesis:** If "late I-9 triggers a hold" means that there are compliance-related tasks with legal implications, then the AI agent would need to be designed with strict rules and escalation protocols for handling these situations, because compliance tasks often have specific requirements and consequences that must be managed carefully.
   - **How I'd test it:** I would ask the HR Ops team to clarify what "late I-9 triggers a hold" means in their context and what the specific requirements and consequences are for these compliance-related tasks. In a coach session, I would discuss with the coach how to design the AI agent's handling of these tasks to ensure compliance and mitigate risks.
   - **Confidence:** Medium — while it's reasonable to infer that "late I-9 triggers a hold" refers to compliance-related tasks, without further clarification it's difficult to fully understand the implications for the AI agent's design and how critical it is to get this aspect right.

