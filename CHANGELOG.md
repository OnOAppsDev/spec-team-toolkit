# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

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
