# Prompt — System/Data Inventory

> **This is a lightweight trigger prompt.** The structural rules for Deliverable #5 are encoded in `../CLAUDE.md` § Deliverable Output Rules. Use `system-data-inventory-checklist.md` in this folder to verify your output after generation.

## Instruction

Produce **Deliverable #5 — System/Data Inventory** for the agent designed in Deliverable #4 (Agent Purpose Document).

**Input dependencies:** Load from the output folder:
- Deliverable #4 (Agent Purpose Document) — for the systems and data the agent needs
- The scenario file — for the tooling sketch and sample artefacts

For every system named in the scenario's tooling sketch **and** every system referenced in your Agent Purpose Document, produce an inventory entry. Pay particular attention to:

- **Systems with no real-time API** (e.g. batch-file-only legacy systems) — name the gap, the data lag, and its impact on agent design
- **Shadow systems** — lived-work tools not in the official tooling sketch (manual overrides, workarounds, informal channels)
- **Legacy or batch-only systems** — address constraints explicitly: export cadence, schema stability, modification turnaround, reconciliation lag. Don't hand-wave.

## Output location

- Practice: `../Output/system-data-inventory-{NNN}.md`
- Gate: `../Gate2/Output/system-data-inventory-{NNN}.md`

## After generation

1. Run through `system-data-inventory-checklist.md`
2. Check: does every system from the scenario tooling sketch appear?
3. Check: are shadow/unofficial systems from the artefacts included?
4. Feed forward into Deliverable #6 (Discovery Questions — system gaps are prime discovery targets)

