<!-- CLAUDE CODE CONTEXT FILE
  Read this file together with spac_<feature_name>.md before starting implementation.
  All TODO sections require developer input before coding begins.
  Do not implement sections marked ⚠️ TODO without explicit developer guidance.
-->

# Frontend Technical DD: [Feature Name]

**Status:** 🔴 NOT STARTED
**SPAC:** `spac_<feature_name>.md`
**Team:** [React Native | Native iOS / Android]
**Author:** TBD
**Reviewer:** TBD
**Last Updated:** [YYYY-MM-DD]
**Based on SPAC confidence:** [n]%

---

## 1. Overview

[Copy the Feature Overview and Problem Statement from the SPAC verbatim.]

---

## 2. Target stack & conventions

**Stack:** [from SPAC]
**Repository:** [workspace/project/repo from SPAC]
**Branch:** [branch from SPAC]
**Module/Path:** [path from SPAC]

> ⚠️ TODO: Document the specific files, folders, navigation structure, and component patterns to use for this feature. Reference the Bitbucket repository and branch above.

---

## 3. Screens & navigation

[List every screen from the SPAC User Flow and UI Requirements sections, one per bullet:]

- [Screen name] — [one-line description of purpose]
- [Screen name] — [one-line description of purpose]

> ⚠️ TODO: For each screen, define:
> - Component file path (e.g. `src/features/<feature>/screens/<ScreenName>.tsx`)
> - Navigator registration (stack name, route name, params type)
> - Screen params (if any)

---

## 4. State management

> ⚠️ TODO: Define the state management approach for this feature.
> - Which store/hook/context will own the feature state?
> - What data needs to persist across navigation?
> - What data is local to the screen?
> - Reference the existing pattern from the codebase scan if available.

---

## 5. API integration

[Copy the Data & Backend Dependencies table from the SPAC:]

| Service / API | Endpoint | Method | Purpose | Contract source |
|---|---|---|---|---|
| [Service] | [/path] | [GET/POST] | [purpose] | [Backend DD / TBD] |

> ⚠️ TODO: For each endpoint, define:
> - Service file path (e.g. `src/services/<ServiceName>.ts`)
> - Hook or query name (e.g. React Query key, custom hook)
> - Error handling strategy (toast, inline error, retry)
> - Loading state handling
> - Cache/stale time if applicable

---

## 6. UI components

[List all UI elements from the UI Element Data Mapping section of the SPAC:]

- [Element name] — [type, screen, data source summary]
- [Element name] — [type, screen, data source summary]

> ⚠️ TODO: For each element, define:
> - Use existing component or build new?
> - If existing: component name and file path
> - If new: proposed name, file path, and required props
> - Design system tokens to use (if applicable)

---

## 7. Validation

[Copy the Validation Rules table from the SPAC:]

| Field | Rule | Error message |
|---|---|---|
| [Field] | [Rule] | [Message or i18n key] |

> ⚠️ TODO: Define:
> - Where validation runs (client-side, server-side, or both)
> - How errors are surfaced to the user (inline, toast, modal)
> - Which validation library or pattern to use (if applicable)

---

## 8. Permissions & security

[Copy the Permissions section from the SPAC:]

| Permission | Required | Behavior if denied |
|---|---|---|
| [Permission] | [Yes/No] | [behavior] |

[Copy the Security & Privacy section from the SPAC.]

> ⚠️ TODO: Define the implementation approach for each permission check and data visibility rule.

---

## 9. Accessibility

[Copy the Accessibility section from the SPAC.]

> ⚠️ TODO: Define implementation approach:
> - Accessibility labels for icon-only actions
> - Dynamic font size support
> - Screen reader testing plan
> - Color contrast verification

---

## 10. Localization & RTL

[Copy the Localization & RTL section from the SPAC.]

> ⚠️ TODO:
> - List all i18n keys needed for this feature
> - Define RTL layout adjustments (flipped icons, mirrored layouts)
> - Confirm date/time/number formatting approach

---

## 11. Analytics

[Copy the Analytics / Tracking section from the SPAC.]

> ⚠️ TODO: Define:
> - Analytics service call location (component? hook? middleware?)
> - Confirm final event names with the data team
> - Define which properties are required vs optional

---

## 12. Platform notes

[Copy the Platform Notes section from the SPAC.]

> ⚠️ TODO: Define any platform-specific implementation differences not already covered above.

---

## 13. Open questions

[Copy all Open Questions from the SPAC. These must be resolved before implementation begins.]

1. [Open question from SPAC]
2. [Open question from SPAC]

> ⚠️ TODO: Each question above must be answered and the answer documented here before coding begins. Remove questions as they are resolved.

---

## 14. Task breakdown

> ⚠️ TODO: Break this DD into implementation tasks.
> Expected output file: `tasks_<feature_name>.md`
>
> Suggested task categories:
> - Navigation setup
> - Screen scaffolding
> - API integration
> - UI components
> - State management
> - Validation
> - Accessibility & i18n
> - Testing

---

## 15. Testing notes

> ⚠️ TODO: Define:
> - Unit test scope (which functions/hooks need unit tests?)
> - Integration test scope (which flows need integration tests?)
> - Manual QA checklist (happy path, error states, edge cases)
>
> Expected output file: `qa_<feature_name>_test_cases.md`
