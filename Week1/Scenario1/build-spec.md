## Prompt 1 — buildable spec from a scenario

Please use the Respository structure and Core Entities defined in the CLAUDE.md to understand where to store outputs and how to refer to concepts. 
Use the thinking-discipline principles from the Week 1 primer to guide your reasoning and documentation style. 

Use the 'How to work with your chosen scenario' section in @ `SupportingDocs/README-Participants-Week1-Scenarios.md` to understand how to approach the scenario and what the expectations are for your spec output. The main sections of the output document should be:
Assumption Log (with scan table, coach-session queue, update protocol, and detailed entries) followed by the five deliverables:
1. **A problem statement and success metrics** tied to the numbers given in your scenario (not generic business-speak)
2. **A delegation analysis** that names which parts of the work become fully agentic, agent-led with human oversight, or stay human-led — and **why**. The "why" is the skill being tested.
3. **A first-draft capability specification** for the agentic part: purpose, scope, inputs/outputs, decision logic, escalation triggers, integration points. Target 6–10 requirements minimum. Precise enough that an AI coding agent could start building from it.
4. **A first-draft validation design** with at least 3 scenarios spanning happy path, edge case, and failure mode — including at least one failure scenario that tests the delegation boundary itself.
5. **An honest assumptions & unknowns section** — at least 5 genuine unknowns, not filler. What are you assuming about the client's data, systems, and organisation? What must be validated before building?

The goal for this prompt is to satisfy the week 1 agenda which can be found in @ `SupportingDocs/README-Participants-Intro-Week1.md` but is also copied below:

Week 1 - AI-Native Specification - Given a business problem, design an agentic solution and write a spec an AI coding agent can build from.

The scenario being used is Scenario 1 — HR Onboarding Coordination, which can be found in @ `SupportingDocs/README-Participants-Week1-Scenarios.md` but is also copied below:

---
## Scenario 1 — HR Onboarding Coordination

> A regional professional-services firm (1,200 employees, 220+ hires per year) runs new-hire onboarding through a 3-person HR Ops team. 
> Each onboarding spans ~40 tasks across 2 weeks: IT provisioning, benefits enrolment, compliance training assignment, buddy matching, welcome materials, 30-day checkpoint scheduling, and manager handoff. 
> Tasks originate from 6 different systems. Roughly 15% require judgment calls — which compliance track applies to a contractor versus a full employee, whether a buddy assignment crosses seniority norms, whether a late I-9 triggers a hold.
>
> The HR Ops lead says: "Most of this is paperwork my team should not be touching, but every time we try to automate, something falls through the cracks because the edge cases never look the same twice." 
>Their stack is:
>  - Workday for core HR
>  - ServiceNow for IT requests
>  - a separate LMS for compliance training
>  - email for everything the other three don't cover. 
>  
> They have no AI infrastructure today.
>
> Design the agentic solution.
---

Human assumptions are listed below, but you should also review the scenario text itself for any additional assumptions you may be making that aren't explicitly stated. Mark these agent made assumptions as 'AGENT' and the human assumptions as 'HUMAN'.
Remember to follow the rules outlined in the Week 1 thinking-discipline primer, and to document all assumptions in the Assumption Log at the top of your spec.

```
Human Assumptions:
1. **HUMAN Assumption:** The HR Ops team is open to adopting an AI agent for onboarding coordination.
   - **Hypothesis:** If the HR Ops team is open to AI adoption, then they will be willing to collaborate on defining the agent's capabilities and providing feedback during development, because they have expressed frustration with current automation efforts.
   - **How I'd test it:** In a coach session, I would role-play with the HR Ops lead to gauge their enthusiasm and willingness to engage in the design process for an AI solution.
   - **Confidence:** Medium — while the HR Ops lead has expressed frustration with current automation efforts, it's not guaranteed that they will be receptive to an AI-based solution without further discussion.
2. **HUMAN Assumption:** The 15% of onboarding tasks that require judgment calls are consistent enough that an AI agent could learn to handle them effectively.
    - **Hypothesis:** If the judgment calls in onboarding tasks follow identifiable patterns, then an AI agent could be trained to make similar decisions, because many HR processes have established guidelines that could be codified into the agent's decision-making framework.
    - **How I'd test it:** I would ask the HR Ops team for examples of the judgment calls they encounter and analyze them for commonalities. In a coach session, I would present these examples and ask the coach to evaluate whether they seem like they could be systematized for an AI agent to learn from.
    - **Confidence:** Low — without seeing the specific judgment calls, it's difficult to assess whether they are consistent enough for an AI agent to handle, especially given the variability implied by "the edge cases never look the same twice."
3. **HUMAN Assumption:** The existing systems (Workday, ServiceNow, LMS) have APIs or integration points that an AI agent could use to coordinate tasks effectively. Email has SMTP or a transactional API for sending messages.
    - **Hypothesis:** If the existing systems have APIs or integration points, then an AI agent could be designed to interact with these systems to automate task coordination, because modern enterprise software typically includes some form of API access for integration purposes.
    - **How I'd test it:** I would ask the HR Ops team for documentation on the APIs or integration capabilities of Workday, ServiceNow, and the LMS. For email, I would inquire about how they currently send emails (e.g., through an SMTP server or a transactional email service) to understand how the AI agent could integrate with their email system. In a coach session, I would discuss the implications of these integration capabilities for the design of the AI agent.
    - **Confidence:** Medium — while it's common for enterprise systems to have APIs, there can be variability in their availability and functionality. The email integration is also uncertain without knowing their current setup.
4. **HUMAN Assumption** Buddy assignments are determined by three codifiable factors — seniority, department, and location. Also you can only be a buddy to one person, so take this into consideration. The agent auto-assigns when a candidate passes all these factors. If multiple matches are found, prioritise in order of department, location and seniority. If still multiple matches, pick at random. If no candidate is available, the agent escalates to HR for manual assignment.
    - **Hypothesis:** If the three-factor filter (seniority + department + location) yields at least one eligible candidate, the agent can auto-assign without further judgment. If it yields zero, HR takes over — because capacity, leave, and pool gaps are facts HR already manages for the team.
    - **How I'd test it:** Tested in coach session — coach confirmed the three-factor model and the HR-manual-escalation-on-unavailability rule. Remaining operational probes (not confidence-blocking but build-blocking): (a) what exactly counts as "not available" — zero-match vs. capacity-exhausted vs. on-leave; (b) tie-break rule when multiple candidates pass the filter.
    - **Confidence:** High — coach-confirmed on the three-factor model and the escalation rule. The two operational details above are carried forward as AGENT assumptions in the spec, not as open HUMAN assumptions.
5. **HUMAN Assumption:** The 2 unnamed systems in "6 systems" are benefits system and payroll/time system, and they have similar integration capabilities as the named systems.
    - **Hypothesis:** If the unnamed systems are benefits and payroll/time systems with similar integration capabilities, then the AI agent could potentially integrate with them in the same way it would with Workday, ServiceNow, and the LMS, because many HR-related systems are designed to be interoperable.
    - **How I'd test it:** I would ask the HR Ops team to identify the unnamed systems and research their integration capabilities. In a coach session, I would discuss with the coach the implications of these systems' integration capabilities for the overall design of the AI agent.
    - **Confidence:** High — Coach session confirms the unnamed systems are benefits and payroll/time systems, and it's reasonable to assume they have similar integration capabilities given their role in HR processes.
6 **HUMAN Assumption** The HR Ops team are fully open to an AI driven solution and will provide the necessary access and support for integration with existing systems.
    - **Hypothesis:** If the HR Ops team is fully open to an AI-driven solution, then they will facilitate access to the necessary systems and provide support during the integration process, because they have expressed a desire to move away from manual coordination and have no AI infrastructure today, suggesting a willingness to explore new solutions.
    - **How I'd test it:** In a coach session, I would role-play with the HR Ops lead to discuss the level of access and support they would be willing to provide for integrating an AI agent with their existing systems. I would also ask about any potential barriers or concerns they might have regarding this level of involvement.
    - **Confidence:** High — Agreed in coach session that HR Ops is open to an AI-driven solution and will provide necessary access and support, given their expressed frustration with current automation efforts and lack of existing AI infrastructure.
7 **HUMAN Assumption** The term "late I-9 triggers a hold" implies that there are compliance-related tasks that require immediate attention and may have legal implications if not handled correctly.
    - **Hypothesis:** If "late I-9 triggers a hold" means that there are compliance-related tasks with legal implications, then the AI agent would need to be designed with strict rules and escalation protocols for handling these situations, because compliance tasks often have specific requirements and consequences that must be managed carefully.
    - **How I'd test it:** I would ask the HR Ops team to clarify what "late I-9 triggers a hold" means in their context and what the specific requirements and consequences are for these compliance-related tasks. In a coach session, I would discuss with the coach how to design the AI agent's handling of these tasks to ensure compliance and mitigate risks.
    - **Confidence:** Medium — while it's reasonable to infer that "late I-9 triggers a hold" refers to compliance-related tasks, without further clarification it's difficult to fully understand the implications for the AI agent's design and how critical it is to get this aspect right.
```


Use the below rules and the scenario to produce a buildable specification as a new file at `Week1/Scenario1/Output/`. The filename should be in the format template: 'critique-pool-Sahil2-1-{random-3-digits}.md'

```
Rules:
- Every non-trivial claim must be one of: [CITED] from the scenario or a
  named regulation, or [ASSUMED]
  and recorded in a numbered entry in the Assumption Log.
- The Assumption Log goes at the TOP of the document, not the bottom, per
  SupportingDocs/Week1-Thinking-Discipline-Primer.md.
- The Assumption Log must contain: a scan table (one line per assumption
  with confidence and Cagan risk attacked), a coach-session priority
  queue, an update protocol, and full Assumption/Hypothesis/Test/Confidence
  entries.
- A Contractor vs a Full Employee is defined by the Workday system's employee 
  classification, which the HR Ops team uses to determine compliance training tracks. 
  Escalation to HR is needed if this cannot be determined reliably by the agent.
- Any assumption that is marked as High has been discussed in a coach session and is supported by the coach's feedback. These can be assumed true for the purpose of the first draft spec. 
  Medium and Low confidence assumptions have not yet been tested in a coach session.
- Do not invent values the scenario does not give. Mark unknowns as
  [UNKNOWN] and raise them in the Assumption Log.
- Do not claim High confidence on any assumption until it has been tested
  in a coach session.
```

## Prompt 2 — Generate a non-technical stakeholder deck from a spec

Use this when you need a 10-slide PowerPoint for sponsors (HR Ops leadership, compliance, finance, anyone who will sponsor or block the build).

Please use the repository structure and naming conventions defined in `CLAUDE.md`. Use the thinking-discipline principles from `SupportingDocs/Week1-Thinking-Discipline-Primer.md` — the deck must not hide assumptions under polish. Every non-trivial claim on a slide must be traceable to a section in the source spec; if the spec marks something `[ASSUMED]` or `[UNKNOWN]`, the deck must say so too.

```
Using the spec at Week1/Scenario1/Output/{{spec-filename}}.md (produced by
Prompt 1) as the single source of truth, generate a 10-slide
stakeholder overview as a PowerPoint file.

Output file-naming convention:
- Generator script: Week1/Scenario1/Presentation/build_{{spec-slug}}_deck.py
  (where {{spec-slug}} is the spec filename without the .md extension)
- Output deck:      Week1/Scenario1/Presentation/{{spec-slug}}.pptx
- The script is the source of truth. The .pptx is a build artefact.
  Do not hand-edit the .pptx — regenerate it.

Design language (Claude-inspired, applied consistently across every
Week{N}/Scenario{M}/Presentation/ folder so decks look like a family):
- Typography-first; no clip-art, no gradients, no shadows, no icons
- Single warm accent: #D97757 (Claude coral) — use sparingly on
  kickers, hairlines, and big numbers only
- Deep ink text: #1F1F1E on warm off-white canvas: #F5F4EE
- Muted secondary text: #6B6A66
- 16:9; Calibri (or Inter / Söhne if installed)
- Generous whitespace

Structure (10 slides, one concept per slide):

1. Title
   - Project name + one-line sub-heading anchored in scenario numbers.
   - Footer: "Stakeholder overview · {{spec-slug}} · {{month}} {{year}}".

2. The problem
   - Three statistics as big coral numbers (pulled directly from the
     scenario — do not invent).
   - Stakeholder quote verbatim from the scenario (with attribution to
     the named role).
   - No interpretation. Let the numbers and quote land.

3. Why agentic, why now
   - Two columns: WHAT FITS (the routine portion) vs. WHAT DOESN'T
     (the judgment portion).
   - Use the spec's §1.2 volume / repeatability / constraint arguments.
   - Footer: note which split is [CITED] vs. [ASSUMED] per the spec.

4. The proposal
   - The capabilities from spec §3, numbered, one line each.
   - No capability introduced on this slide that is not in §3.

5. The delegation boundary
   - Two columns: AGENT HANDLES vs. HUMANS ALWAYS DECIDE.
   - Pull directly from spec §2.1 (work inventory) and §2.2 (hard
     constraints).
   - Footer: name the audit-trail retention ("every human decision is
     logged … — 7-year retention" or whatever the spec says).

6. What success looks like
   - The metrics from spec §1.3 as big coral numbers.
   - CRITICAL: preserve the source labels from §1.3 exactly.
     If a metric is marked "Target — needs validation" or
     "Non-negotiable" in the spec, that label appears on the slide.
     Do not hide "needs validation" behind polished marketing.
   - This is the primer's anti-pattern "polished spec that dodges the
     riskiest unknown" translated to slide design.

7. What we still need to validate
   - The top 3 from the spec's Assumption Log coach-session priority
     queue, in the order the spec ranks them.
   - Each item: short title + 2-sentence body explaining why it
     matters for the build.
   - Footer: count of assumptions in the log (e.g., "Full assumption
     log — 11 items: 2 HUMAN + 9 AGENT — in the spec").

8. What could go wrong
   - 4 failure modes drawn from spec §6.3 (Failure Modes) and §6.4
     (Delegation Boundary Test).
   - For each, a one-line description of how the design absorbs it
     (the "Agent response" / "Recovery" columns in the spec, compressed).
   - Avoid hand-waving like "we'll handle it" — every row must name a
     specific mechanism (queue, escalation, audit, logged decision).

9. What we're asking for
   - 3 specific, ordered asks.
   - Each ask must be something a stakeholder can say yes or no to in
     the meeting. Not "engagement" or "alignment" — specific actions
     with specific outcomes.
   - Draw from the spec's §8 overall / recommended next step.

10. Close
    - Single line: "Questions, reactions, objections."
    - Sub-line: "The spec is a draft. Your pushback is what turns it
      into something buildable."
    - Footer: link back to the spec file path.

Slide-level rules:
- Every slide has a kicker (uppercase, 11pt, coral) + a title
  (32pt bold, ink). Slide number bottom-right, muted.
- No slide crosses the delegation boundary — the agent should not
  appear to be "deciding" things marked HUMAN-LED in the spec.
- No invented numbers. If the spec marks something [UNKNOWN], the
  slide either omits the number or labels it as TBD / baseline needed.
- Quotes are verbatim. If the spec does not contain a quote, do not
  invent one.

Self-audit before declaring the deck complete:
- [ ] Every metric on slide 6 carries the same source label the spec
      gives it in §1.3.
- [ ] Slides 7 items match the spec's coach-session priority queue
      order exactly; no reordering for "flow".
- [ ] No assumption marked [ASSUMED] in the spec is presented as
      [CITED] or settled fact on a slide.
- [ ] The stakeholder quote on slide 2 is verbatim from the scenario,
      attributed to the named role.
- [ ] Generator script and .pptx file names match the {{spec-slug}}
      naming convention above.
- [ ] The script runs end-to-end with `py build_{{spec-slug}}_deck.py`
      and produces the .pptx without warnings.

Regeneration: after any spec change that affects §1.3 (metrics), §2
(delegation), §3 (capabilities), §6.3 (failure modes), or the
Assumption Log priority queue, regenerate the deck. Treat a divergence
between spec and deck the same way the closed-build-loop treats a
divergence between spec and built software — as a gap to diagnose,
not paper over.
```

## Prompt 3 — Build System from the spec
Using the spec at `Week1/Scenario1/Output/{{spec-filename}}.md` as the single source of truth, build the system using Claude Code. 

