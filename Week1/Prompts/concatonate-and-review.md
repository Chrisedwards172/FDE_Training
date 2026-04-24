# Prompt — Concatenate Scenario 1 Outputs and Review Against Production Spec Checklist

## Standing sources

Apply the standing contract defined in `CLAUDE.md` under *Prompt Authoring Conventions → Standing sources every prompt must load* before producing output. In particular: this prompt inherits the source tagging, Assumption Log, and diagram rules from that section — do not restate them, do not contradict them.

## Purpose

Produce a **single consolidated Gate 1 spec document** for Scenario 1 by concatenating the five deliverable files already generated in `Week1/Output/Scenario1/`, in the exact deliverable order specified by the Gate 1 section of `SupportingDocs/README-Participants-Intro-Week1.md`, then review and revise the result against `SupportingDocs/production-spec-checklist.md`.

## Inputs

Read all five files from `Week1/Output/Scenario1/`:

- `problem-statement-scenario-1-201.md`
- `delegation-analysis-scenario-1-202.md`
- `capability-specification-scenario-1-203.md`
- `validation-design-scenario-1-204.md`
- `assumptions-and-unknowns-scenario-1-205.md`

If any of the five is missing, stop and flag the gap — do not fabricate content to fill it.

## Concatenation order (authoritative)

The order is taken from the Gate 1 deliverable list in `SupportingDocs/README-Participants-Intro-Week1.md` (*Part 5 — Week 1 → Gate 1 — what you'll hand in*):

1. **Problem statement & success metrics** — from `problem-statement-scenario-1-201.md`
2. **Delegation analysis** — from `delegation-analysis-scenario-1-202.md`
3. **Agent specification** — from `capability-specification-scenario-1-203.md`
4. **Validation design** — from `validation-design-scenario-1-204.md`
5. **Assumptions & unknowns** — from `assumptions-and-unknowns-scenario-1-205.md`

If the README and this prompt ever disagree on the order, the README wins — re-read it and adjust.

## How to concatenate

- Produce one Markdown file with a single top-level `# H1` title for the consolidated Gate 1 spec, followed by the five deliverables as `## H2` sections in the order above. Demote the source files' own headings by one level so the output has a clean hierarchy (source `#` → `##`, source `##` → `###`, and so on).
- Preserve all substantive content, tables, Mermaid diagrams, figure captions, and citation / assumption tags (`[CITED]`, `[ASSUMED]`, `[UNKNOWN]`, `HUMAN`, `AGENT`) exactly as written in the source files.
- **Pay close attention to removing duplicate information.** The five source files were authored independently and will restate the same scenario framing, personas, entities, success metrics, assumptions, and integration details. Consolidate duplicates so each fact appears **once** in the most appropriate section, and replace later occurrences with a short in-document cross-reference (e.g. *"see §2 Delegation analysis, Table 2.1"*). When two versions of the "same" fact disagree, do not silently merge — surface the conflict as a new numbered Assumption Log entry and keep the stronger-evidenced version in the body.
- Merge the five Assumption Logs into a **single Assumption Log at the top of the output**, renumbered sequentially, preserving HUMAN/AGENT tags and confidence levels. Where the same assumption appears in more than one source log, keep one entry and list all sections that depend on it.
- Keep Mermaid diagrams Mermaid-only, with their captions, per the *Diagrams* section of `CLAUDE.md`. If two diagrams cover the same structure, keep the clearer one and delete the other rather than showing both.

## Output placement

Write the consolidated file to:

`Week1/Output/Scenario1/critique-pool-Sahil2-1-{NNN}.md`

where `{NNN}` is a 3-digit run suffix. Pick the next unused suffix by scanning the folder for existing `critique-pool-Sahil2-1-*.md` files and incrementing past the highest numeric suffix present (so iterations sit side-by-side per `CLAUDE.md` → *Output placement*). Do not overwrite previous runs.

## Execution mode — write in stages

The consolidated output runs to roughly 900–1,800 lines once the five sources are combined, deduplicated, and extended with the checklist-review appendix. A single-turn write of that size can hit the model's output-token ceiling and return an empty response, producing no file at all. To make this prompt resilient, **the producer must write the output file in sequential stages**, appending to the same file rather than emitting the whole document in one generation:

1. **Stage 1 — Header + merged Assumption Log.** Create the file with the top-level `# H1` title, a short dated header (submission IDs consolidated, source scenario, date produced, status), and the single merged Assumption Log (scan table, coach-session priority queue, update protocol, full entries).
2. **Stage 2 — §1 Problem statement & success metrics.** Append the problem-statement deliverable with its per-file front-matter and its own §2 Assumption Log stripped (those now live at the top). Preserve M1–M4.
3. **Stage 3 — §2 Delegation analysis.** Append, stripping the file's front-matter, §2 Assumption Log, and "Out of scope" block. Preserve the work inventory, hard constraints C1–C4, Figure 1, and the boundary-respect metric hand-off.
4. **Stage 4 — §3 Agent specification.** Append, stripping front-matter, §2 Assumption Log, self-audit section, and "Out of scope" block. Preserve the entity model, Figures 2–4, and every Cap-A / Cap-B / Cap-C rule.
5. **Stage 5 — §4 Validation design.** Append, stripping front-matter, §2 Assumption Log, self-audit, and "Out of scope". Preserve HP-1, EC-1…EC-7, FM-1…FM-6, BT-1, BT-2, and the trace matrix.
6. **Stage 6 — §5 Assumptions & unknowns (compact).** Append only what is *not* already in the top Assumption Log: §4 Coach-session priority queue, §7 Genuine unknowns list, §8 What must be validated before building. Replace §3 scan table and §6 full entries with a cross-reference to the top log.
7. **Stage 7 — Appendix A — Production spec checklist review.** Append the audit-trail table described in *Post-concatenation review* below. Any in-body revisions made to close checklist gaps must already be in place by this stage; Appendix A records what was changed.

Each stage is one file-write operation. If any stage returns an empty response, retry only that stage — do not regenerate earlier stages and do not rewrite the file from scratch.

## Post-concatenation review — against the production spec checklist

Once the consolidated file is written, review it against `SupportingDocs/production-spec-checklist.md` and update the file in place so that it clears the checklist's buildability bar. Specifically:

1. Walk the checklist top-to-bottom. For each item, decide **Met / Partially met / Not met** against the consolidated document.
2. For every **Partially met** or **Not met** item, revise the relevant section of the consolidated file to close the gap. Do not invent facts — if closing the gap requires information not present in the source files or the scenario, raise it as a new numbered entry in the Assumption Log (tagged `AGENT`, Low or Medium confidence) and mark the body `[UNKNOWN]` or `[ASSUMED #N]` accordingly.
3. Append a final `## Appendix A — Production spec checklist review` section to the consolidated file containing a table with columns: *Checklist item | Status (Met / Partial / Not met) | Section(s) addressing it | Change made in this revision (if any)*. This appendix is the audit trail for the review pass.
4. Re-check the document against the *Authoring Rules* and *Diagrams* sections of `CLAUDE.md` before finishing. Fix any violations silently (formatting, naming, figure captions); flag any substantive conflicts back to the user rather than resolving them unilaterally.

## Done criteria

- One new file exists at `Week1/Output/Scenario1/critique-pool-Sahil2-1-{NNN}.md`.
- Its section order matches the Gate 1 deliverable order in `README-Participants-Intro-Week1.md`.
- Duplicated content across the five sources appears once, with cross-references where helpful.
- A single merged Assumption Log sits at the top.
- Appendix A documents the production-spec-checklist review and the revisions made in response.
- No content has been written to `SupportingDocs/`, and `SupportingDocs/the-fde.md` is untouched.

