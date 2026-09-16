# Spec Team Toolkit

Four skills for the spec team's document workflow, bundled into one plugin: one upstream HLD builder, and three team-specific LLD builders (web, mobile, backend).

## Skills

### `hld-builder`
Builds the High Level Design — the customer-facing scoping document that goes to product customers for approval.

- Built incrementally across sessions from two durable artifacts — `scope-list.md` (entities, personas, journeys, adjacent systems) and `hld-draft.md` (the working document, with per-section status tags and a change-tracking table) — that the user re-uploads to resume where they left off.
- Runs discovery from a fixed question script (`references/discovery_questions.md`), not improvised questions, so every analyst gets the same process; conditional sections are only asked about when the signal for them appears.
- Drafts into the team's real HLD template (`references/hld_template_structure.md`, exact Hebrew headers) following the status-tag and change-log conventions in `references/draft_conventions.md`.
- On finalize (only when asked), renders the draft as a Word document and self-reviews it against the full 10-part QA checklist (bundled in `references/hld_qa_review.md`), fixing Critical/High issues before handing it over.

### `lld-web-figma-spec`
Builds the Low Level Design for the **frontend web** team — the developer/QA-facing component spec derived from a Figma design.

- Pulls real data from Figma via connected Figma MCP tools (design context, screenshots, variable definitions) rather than asking the user to describe the design by hand.
- Produces the team's existing two-part format: a content-entry table (Umbraco 13 editor types, API-sourced fields excluded) and a display/behavior table (logic, edge cases, responsiveness, accessibility), following the exact rules in `references/lld_instructions.md`.

### `lld-mobile-spec`
Builds the Low Level Design for the **frontend mobile** team (React Native / Native iOS-Android) — called a SPAC by that team.

- Asks the target stack (React Native vs. Native iOS/Android) first, then gathers requirements, Figma, Backend DD, and Bitbucket repo context conversationally, one question at a time.
- Reads the actual repo (via Bitbucket MCP) and its Markdown docs (`CLAUDE.md`, README, architecture docs) before writing, to reuse existing patterns instead of prescribing new ones.
- Every silent judgment call (hiding a button, picking a default, etc.) must be marked inline **and** listed in the Assumptions section — nothing is decided silently.
- Produces a `spac_<feature>.md` in DRAFT status; on explicit approval, updates it to READY and generates an HTML stakeholder-review preview plus a DD-starter file for developers.

### `lld-backend-spec`
Builds the Low Level Design for the **backend** team — service/API/data-model specs, designed from scratch for this toolkit (no prior team template).

- No Figma equivalent: sources context from the relevant HLD/requirements and, where available, a read-only codebase scan to match existing API style, naming, and error conventions rather than inventing new ones.
- Produces endpoint contracts (request/response/error shapes), a data model table, and explicit business-rule/edge-case coverage (empty input, not-found, permission-denied, concurrent writes, partial failure), following `references/lld_backend_template.md`.

## Notes

- `scope-list.md` and `hld-draft.md` produced by `hld-builder` are meant to be downloaded and re-uploaded at the start of the next session, since the HLD is built across conversations rather than in one sitting.
- `lld-mobile-spec` was ported in from an existing, already-used skill (`create-frontend-spec`) with only its name/description updated to fit alongside the other skills — its process is otherwise unchanged.
- `lld-backend-spec` is brand new and unvalidated — there was no existing backend spec template to codify, so try it on a real backend change before relying on it.
- None of the four skills has been run through formal test evaluations yet — try each on a real project before rolling out broadly.
