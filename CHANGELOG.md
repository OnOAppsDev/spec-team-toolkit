# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.5.0] - 2026-11-09

### Changed

- `lld-web-figma-spec` renamed to `lld-web-backend-spec` and reworked into one integrated LLD for web features, serving frontend developers, backend developers, and QA. It handles both web-only specs and combined frontend/backend specs.
- `lld-web-backend-spec`: interviews the analyst one question at a time (adapted from `lld-mobile-spec`), after reviewing the provided materials and embedded screenshots, and skips questions the sources already answer. The CMS question comes early: when no content is CMS-managed, the CMS questions and the editor side are skipped. System-responsibility questions always offer "to be decided by the development team".
- `lld-web-backend-spec`: new numbered document structure (`references/lld_template.md`) with localized section titles and fixed numbering:
  - a mandatory change-history table and a single "Document Approved By" field;
  - a component table with separate source and logic columns;
  - responsiveness and accessibility moved out of the table into a feature-specific section;
  - visitor-side and editor-side user stories with acceptance criteria;
  - an integration section covering business rules, cross-system scenarios, API contracts, data changes, and integrations.
- `lld-web-backend-spec`: CMS support is now conditional rather than assumed. Umbraco 13 fields must use the exact property-editor names, and table layout for nested or repeating content is left to the analyst.
- `lld-web-backend-spec`: contract sources depend on the contract. Existing contracts come only from verified sources, and missing details are flagged as open questions. For new or changed contracts, the skill proposes paths, fields, status codes, and error codes that follow repo conventions, marks each value "proposed", and opens one sign-off item for the backend team.
- `lld-web-backend-spec`: when a Figma link is shared but no Figma connector is available, the skill says so once and offers to continue from screenshots. The README now lists the connectors the skill can use; none are bundled with the plugin.
- `lld-web-backend-spec`: open questions and assumptions get unique IDs, are listed once per section, and are referenced from the rows they affect instead of duplicated.

### Added

- `lld-web-backend-spec/scripts/trace_check.py`: fails when a referenced ID isn't defined, when an ID is defined twice, or when a defined field, rule, scenario, API operation, or open item is never referenced. Runs before every draft is presented.
- `lld-web-backend-spec/scripts/md_to_html.py`: renders the Markdown LLD to a standalone RTL HTML page (numbered headings, clickable IDs, print styling) instead of a Word document. The Markdown remains the single source of truth.
- `lld-web-backend-spec/scripts/selftest.py`: self-check for both scripts.

## [0.4.2] - 2026-10-07

### Changed

- `hld-builder`: existing-state, business-process, and entity (מאגרי מידע) sections now offer to render a diagram via the draw.io connector when one would help, asking the specialist a yes/no question before generating rather than assuming — with the outcome recorded inline so the offer isn't repeated next session.
- `lld-mobile-spec`: the State Transitions subsection's draw.io/Figma diagram rendering is now gated behind the same ask-first question instead of generating automatically.
- `lld-backend-spec`: the Dependencies section now offers a sequence diagram via the draw.io connector for multi-service/async flows, asking before generating.

## [0.4.1] - 2026-10-06

### Changed

- Version bump only; no functional changes.

## [0.4.0] - 2026-09-27

### Changed

- `lld-mobile-spec`: the HTML preview is now generated alongside every DRAFT write, not only after marking READY — the HTML is the artifact reviewers actually approve, so it no longer waits for READY.
- `lld-mobile-spec`: marking a feature READY is now blocked if a critical backend dependency has no real contract (IDD, OpenAPI/Swagger, other API doc, or a full request/response) — it's kept as an Open Question instead.
- `lld-mobile-spec`: User Flow (§7) now requires each step to name the user action, the app's response, any backend call, and the resulting state/UI effect, instead of a plain screen-to-screen sequence; added an optional State Transitions subsection (Mermaid `stateDiagram-v2`) for complex, state-heavy screens.
- `lld-mobile-spec`: UI Requirements (§8) now requires every interactive element to state exactly what happens on activation, not just its type.
- `lld-mobile-spec`: Data & Backend Dependencies (§11) and UI States → Error State (§10) now require invocation timing, request/response handling, response-transformation logic, and functional error behavior (data preservation, retry, navigation blocking) instead of just an endpoint list and error message.
- `lld-mobile-spec` and `lld-web-figma-spec`: both now require a final coverage-verification pass against all in-scope source material before presenting the document for approval.
- `lld-web-figma-spec`: API-sourced display elements now require invocation timing and success/empty/error/partial-failure behavior in the logic column, in addition to the existing empty/overlong/malformed content edge cases.

## [0.3.0] - 2026-09-16

### Changed

- `lld-figma-spec` renamed to `lld-web-figma-spec` for naming parity with the other team-specific LLD skills; content and behavior unchanged.

### Added

- `lld-mobile-spec` skill: LLD/SPAC builder for the mobile team (React Native / Native iOS-Android), ported in from an existing, already-used skill (`create-frontend-spec`) with only its name and trigger description updated to fit alongside the other skills. Interviews for requirements one question at a time, reads the repo via Bitbucket MCP to match existing conventions, and requires every silent judgment call to be marked as an explicit assumption.
- `lld-backend-spec` skill: LLD builder for the backend team, designed from scratch (no prior team template existed). Produces endpoint contracts, a data model table, and explicit business-rule/edge-case coverage, sourcing context from the relevant HLD and a read-only codebase scan instead of a visual design tool.

## [0.2.0] - 2026-07-08

### Changed

- `hld-builder` skill reworked around incremental, multi-session drafting: the HLD is now built from two durable artifacts (`scope-list.md` and `hld-draft.md`) that carry state between sessions, with a session-start protocol that resumes from existing files instead of restarting discovery.
- Discovery questions are now a fixed script (`references/discovery_questions.md`) so the process is identical across analysts, with conditional sections gated by signals from the answers.
- Drafting now follows the team's real HLD template (`references/hld_template_structure.md`, with the exact Hebrew section headers) and its status-tag / change-tracking conventions (`references/draft_conventions.md`), instead of a generic Business/Functional/Information-Model structure.
- QA self-review against the checklist now runs only when the draft is finalized for delivery, rather than as part of a single one-shot generation.

### Added

- `skills/hld-builder/references/discovery_questions.md` — the fixed discovery question script.
- `skills/hld-builder/references/draft_conventions.md` — status tags, open-question notes, and change-log conventions for the working draft.
- `skills/hld-builder/references/hld_template_structure.md` — the team's real HLD section structure and headers.

## [0.1.0] - 2026-07-07

### Added

- Initial release of the spec-team-toolkit plugin.
- `hld-builder` skill: discovers and scopes a High Level Design (HLD) through guided conversation, self-reviews it against the team's QA checklist, and produces a customer-facing Word document ready for approval.
- `lld-figma-spec` skill: turns a Figma web component design into the team's two-part Low Level Design spec — an Umbraco CMS content-entry spec and a display/behavior spec — for handoff to developers and QA, pulling design data directly from Figma via MCP.
