---
name: lld-mobile-spec
description: >
  Use this skill whenever the mobile team needs a Low Level Design (LLD) / frontend specification document
  (called a SPAC by this team) for a React Native or Native iOS/Android feature.
  Triggers include: "write a SPAC", "create a SPAC", "new SPAC for", "generate spac", "I have requirements for a feature",
  "I have a Figma design and requirements", "write a spec for the mobile team", or any time someone
  describes a new mobile feature and wants to produce a structured spec file that developers can use to build
  and feed into Claude for technical DD generation. Even if they don't use the word "SPAC", if they're
  describing a mobile (React Native / Native iOS-Android) feature and providing business requirements, Figma links,
  screenshots, Backend DD, Bitbucket repository context, or codebase context — use this skill.
  For web components, use `lld-web-figma-spec` instead. For backend service/API specs, use `lld-backend-spec` instead.
---

# Create Frontend Spec Skill

This skill guides Claude through producing a high-quality `spac_<feature>.md` file for the frontend development team.

A SPAC is a frontend specification document used by the development team as a controlled input for:

* Frontend Technical DD
* Development task breakdown
* Claude Code implementation planning
* QA test case generation

The document is always created as **DRAFT** first, and only promoted to **READY** when the user explicitly says so.

The SPAC describes **what the frontend feature should do and how it should behave**.

It may reference existing app patterns, Figma frames, screenshots, backend contracts, repository documentation, and codebase conventions, but it should not replace the Frontend Technical DD or prescribe low-level implementation unless required for frontend behavior.

---

## Phase 1 — Identify Target Stack

Before writing anything, the **very first question** to ask is:

> "Which team is this SPAC for — **React Native** or **Native iOS/Android**?"

This determines the stack, language, and conventions used throughout the entire document.

Do not proceed until you have this answer.

Store it as `target_stack`:

* `react_native`
* `native_ios_android`

---

## Phase 2 — Gather Inputs

Once the target stack is confirmed, collect all available inputs conversationally — one ask at a time.

Do not list all required inputs at once. Ask for the most important thing first, then continue based on what the user provides.

### Suggested order

**First**, ask for the requirements and feature name if not already provided:
> "Do you have a requirements document or description I can start from? And what should we call this feature?"

**Then**, ask for the repository context:
> "Do you have the Bitbucket repo details handy — workspace, project, repo name, and branch?"

If they provide it, also ask:
> "Is there a relevant module or path inside the repo, and is there an existing screen or feature this is closest to?"

If they don't have it:
> "No problem — I'll continue without codebase context and mark that in the SPAC."

**Then**, ask about optional design and contract inputs:
> "Do you have a Figma link, any screenshots, or a Backend DD I can reference?"

Only ask about inputs that aren't already present in the conversation or as uploaded files.

### What to collect

**Required:**
* Business requirements — uploaded file, pasted text, or described in chat
* Feature name — used for the filename `spac_<feature_name>.md`

**Required project context (when available):**
* Bitbucket workspace, project key, repository name, target branch
* Relevant app/module path (required for monorepos)
* Closest existing screen or feature (if known)
* Relevant Jira issue / Epic / Story (optional)

**Optional but valuable:**
* Figma design — URL, exported PNG, or PDF
* Screen screenshots — from Figma, app, QA build, or production
* Backend DD / API Design Document
* Existing codebase files relevant to the feature area
* Existing project documentation — `CLAUDE.md`, README, architecture docs, existing SPACs or DDs

If repo details are missing, continue with available inputs and mark codebase confidence as unavailable.

---

## Phase 3 — Figma, Screenshot, and File Handling

### Figma handling

If the user provides a Figma URL, use the Figma MCP to inspect the design.

Extract:

* Screen/component names
* Layout structure and spacing notes
* Interactive states:

  * default
  * loading
  * error
  * empty
  * success
  * disabled
* Visible UI elements that need data mapping
* Any annotations or notes left by designers
* Conflicts between Figma and business requirements

### Figma node reference links

For every screen or component inspected via Figma MCP, record its Figma node link in this format:

```md
[Figma → Screen Name](https://www.figma.com/design/<fileKey>?node-id=<nodeId>)
```

These links must be embedded:

1. In the **UI Requirements** section, next to each screen heading.
2. In the **UI Element Data Mapping** section, in the `Screen / Frame` column or as a link on the screen heading.
3. In the **Project Context Used** section, under Figma frames inspected.

If a node link is not available for a specific component (e.g. only a parent frame was inspected), link to the closest parent frame and note it.

Do not embed raw node IDs without a clickable link — always use the full Figma URL format above so developers and designers can open the frame directly from the SPAC.

If Figma and requirements conflict, flag the conflict as an Open Question.

Figma is the source of truth for UI unless the user explicitly says otherwise.

### Screenshot handling

If Figma MCP is not available, ask the SPAC team to upload screenshots of the relevant screens.

For each screen or screenshot, identify:

* Visible text elements
* Buttons and actions
* Images, icons, and avatars
* Lists/cards
* Input fields
* Toggles, checkboxes, and selectors
* Badges, tags, and status indicators
* Counters, totals, dates, and formatted values
* Empty/loading/error/success-state elements
* Conditional elements shown only for specific roles, permissions, or data states

### File handling

If uploaded files are present, read them using the file-reading skill approach:

* `.md`, `.txt` files: read directly
* `.pdf` files: extract text
* Image files: inspect visually and extract visible UI elements
* Code files (`.ts`, `.tsx`, `.js`, `.jsx`, `.swift`, `.kt`, `.java`, etc.): read and analyze

---

## Phase 4 — Bitbucket MCP Connectivity Check

Before writing the SPAC, verify that Bitbucket MCP access is available when repo context was provided.

The goal is to make sure Claude can read the project repository as reference context for the SPAC.

### Required check

Use Bitbucket MCP to verify:

* The workspace is accessible
* The repository is accessible
* The target branch exists
* The relevant app/module path exists
* Claude can read files in the relevant area

### What to inspect first

Start with lightweight project discovery only:

* Repository root
* Package/module structure
* README or project documentation
* App entry points
* Navigation structure
* Feature folders
* Shared components/design system folders
* API/service layer folders
* i18n/localization folders

Do not perform a deep code scan yet.

### Connectivity result

After checking MCP access, report the result in chat:

```md
## Bitbucket MCP Connectivity Check

Status: Connected / Failed / Partial

Repository:
- Workspace: [workspace]
- Project: [project key]
- Repo: [repo name]
- Branch: [branch]
- Module/path: [path]

Verified:
- [ ] Workspace accessible
- [ ] Repository accessible
- [ ] Branch accessible
- [ ] Relevant module/path found
- [ ] Files readable

Notes:
- [short summary]

Fallback needed:
- Yes / No
```

### If Bitbucket MCP works

Continue with the Repository Documentation Context Scan and Codebase Context Scan later in the workflow.

### If Bitbucket MCP does not work

Do not block the SPAC completely.

Ask the SPAC team for one of these fallbacks:

* Uploaded relevant source files
* Uploaded `CLAUDE.md`, README, architecture docs, or feature docs
* Exported folder snapshot
* Screenshots of existing related screens
* Short explanation of existing app structure
* Links or pasted snippets from relevant files

Mark this in the SPAC header:

```md
**Codebase Context:** Not available — Bitbucket MCP failed / not configured
```

### Boundaries

Do not:

* Modify code
* Create commits
* Open pull requests
* Change branches
* Trigger pipelines
* Access secrets or environment files
* Read `.env`, certificates, keystores, tokens, private keys, or credentials
* Copy large source code blocks into the SPAC

The SPAC team should use Bitbucket MCP as read-only context.

---

## Phase 5 — Repository Documentation Context Scan

Before scanning source code, inspect available Markdown documentation files in the Bitbucket repository.

The goal is to understand the project rules, architecture, conventions, and existing feature documentation before writing the SPAC.

When Bitbucket MCP is available, Claude must inspect repository Markdown documentation before scanning source code.

### Files to look for

Use Bitbucket MCP to search for and read relevant documentation files such as:

* `CLAUDE.md`
* `README.md`
* `docs/**/*.md`
* `architecture.md`
* `coding-standards.md`
* `navigation.md`
* `api.md`
* `api-contracts.md`
* `design-system.md`
* `i18n.md`
* `rtl.md`
* `accessibility.md`
* `permissions.md`
* `security.md`
* `feature.md`
* `features/**/*.md`
* Any existing SPAC, spec, DD, or task files related to the same feature area

### What to extract

From these files, extract only information relevant to the SPAC:

* App architecture overview
* Navigation conventions
* Feature folder structure
* Existing screen/component naming conventions
* Design system and reusable component rules
* API/service layer conventions
* State management conventions
* i18n and RTL rules
* Accessibility rules
* Permission/security rules
* Platform-specific iOS/Android notes
* Existing feature behavior that overlaps with the new feature
* Any project-specific AI instructions from `CLAUDE.md`

### Priority order

Use documentation sources in this order:

1. `CLAUDE.md`
2. Project README
3. Architecture / coding standard docs
4. Feature-specific docs
5. Existing SPAC/spec/DD/task files
6. Source code files

### Boundaries

Do not copy large documentation sections into the SPAC.

Summarize only the rules and context that affect the feature behavior.

If documentation conflicts with business requirements, Figma, Backend DD, or code, flag it as an Open Question.

### Chat output format

After reading documentation files, summarize findings in chat only:

---

**📚 Repository Documentation Findings**

**Docs inspected:**

* `[path]` — [why it matters]

**Relevant project rules:**

* [rule]
* [rule]

**Feature-related context:**

* [context]
* [context]

**Potential conflicts or gaps:**

* [conflict/gap]
* [conflict/gap]

**Impact on the SPAC:**

* [what should be reflected in the SPAC]
* [what should stay for the Frontend DD]

---

Then continue to the Codebase Context Scan.

---

## Phase 6 — Requirements Interview

**Do not skip this phase.**

The goal is to reach approximately 90% confidence in the requirements before writing.

### Conversational rule — one question at a time

**Never dump a list of questions.** Ask one question, wait for the answer, then ask the next.

After each answer:
* Acknowledge what you understood in one short sentence.
* If the answer raises a follow-up, ask it before moving on.
* If the answer already covers the next planned question, skip it.
* If a question was already answered by uploaded documents, confirm instead of asking:
  > "Based on the requirements doc, this feature is for logged-in users only — is that right?"

Group questions naturally. When moving to a new topic area (e.g. from happy path to error states), use a short transition:
  > "Got it. Now let me ask about edge cases."

Keep the tone conversational — not formal, not robotic.

---

### Question sequence

Work through these topics in order, one question per turn. Skip any topic already answered by uploaded inputs.

**1. Problem & goal**
> "What problem does this feature solve for the user? One sentence is enough."

**2. Target user**
> "Who is this for — what role, auth state, and platform?"

**3. Happy path**
> "Can you walk me through the main flow from the user's perspective, step by step?"

**4. Entry point**
> "How does the user get to this feature — menu item, button, deep link, notification, or something else?"

**5. Success**
> "What does success look like? What should the user see or feel when it works perfectly?"

**6. Out of scope**
> "Is anything explicitly out of scope for this version?"

**7. Reuse**
> "Are there existing screens, components, or patterns this should reuse?"

**8. Technical constraints**
> "Any known technical constraints — must use existing API, no new dependencies, offline support, performance budget?"

**9. Platform**
> "Does this need to support iOS only, Android only, or both?"

**10. Empty state**
> "What should the user see when there's no data yet?"

**11. Error states**
> "What are the error cases — API failure, validation errors, permission denied, network unavailable, session expired?"

**12. Loading states**
> "Are there loading states to design, or does the data load fast enough to skip them?"

**13. Permissions**
> "Are there permission levels that affect what a user can see or do?"

**14. Backend / APIs**
> "Which backend services or APIs does this touch?"
Skip if fully covered by an uploaded Backend DD.

**15. Overlap**
> "Does this replace, extend, or overlap with any existing feature?"

**16. UI data mapping**
> "Does this feature display data from the backend? If so, I'll include a UI Element Data Mapping table for each screen."

If yes, continue:
> "Which screens need mapping?"
> "Is there a Backend DD or API contract I can use for the field names?"
> "Should unknown fields be marked as 'Need to verify'?"

If the feature is static or local-only, note: UI Element Data Mapping not required.

**17. Sensitive data**
> "Does this feature expose personal, financial, health, location, or private user data?"

If yes, continue:
> "Should any of it be masked, role-restricted, or audit-logged?"

**18. OS permissions**
> "Does this need any OS-level permissions — camera, photos, location, push notifications, contacts, microphone, Bluetooth?"

**19. Accessibility**
> "Are there accessibility requirements? Think screen readers, dynamic text size, icon-only buttons."

**20. RTL / localization**
> "Does this need Hebrew or RTL support? Should all strings go through the existing i18n system?"

**21. Analytics**
> "Is analytics or event tracking needed for this feature?"

Do not force analytics into the SPAC unless the user confirms it or the requirements mention it explicitly.

If yes, continue:
> "Which user actions should be tracked? Any required event names or properties?"

If no:
Note: Analytics / Tracking not required for this feature.

---

### Pacing

Not every question needs a full turn. If an answer clearly covers two topics at once, acknowledge both and move on. The goal is a natural conversation that covers all the ground — not a rigid 21-step form.

---

## Phase 7 — Confidence Gap Check + Write Approval

### Step 1 — Identify confidence gaps

Before summarizing, scan everything collected so far — requirements, Figma, Backend DD, codebase findings, and interview answers — and identify every point where confidence is below **High**.

Focus on gaps that would force you to invent something or leave a critical TBD:

* UI behavior or display rules that are ambiguous or missing
* API fields that are not confirmed in any source
* Error / empty / loading states that were not described
* Permissions or roles that are unclear
* Navigation entry points or exit points that are unspecified
* Platform behavior differences (iOS vs Android) that need a decision
* Data mapping rows that would be marked "Need to verify" for important elements
* Scope boundaries that are still ambiguous

**Do not ask about things that are merely nice-to-know.**
Only ask about gaps that would directly affect the correctness or completeness of the SPAC.

### Step 2 — Ask targeted gap-filling questions

If there are gaps, ask about them — **one question per turn**, in order of importance.

Use this framing:

> "Before I write, I want to fill in a few gaps I'm not confident about."

Then ask each gap question, waiting for the answer before moving to the next.

After each answer, acknowledge briefly and continue:
> "Got it. One more thing — ..."

When all important gaps are resolved (or the user says "continue with assumptions"), move to Step 3.

If there are **no gaps** — everything is confirmed — skip Step 2 entirely and go straight to Step 3.

### Step 3 — Summary + explicit write approval

Summarize your understanding in 3–5 sentences, then ask explicitly for permission to start writing:

> "Here's what I'm going to write:
>
> [3–5 sentence summary of: feature name, what it does, key screens, data sources, and open questions that will be marked TBD]
>
> Ready for me to start writing the SPAC?"

**Do not begin writing until the user confirms.**

Accepted confirmations: "yes", "go ahead", "כן", "תתחיל", "בסדר", or any clear affirmative.

If the user makes a correction before confirming, apply it, update your summary if needed, and ask again.

If the user says "quick draft" or "continue with assumptions" — skip the remaining gaps, note them as TBD/assumptions, and proceed.

---

## Phase 8 — Minimal Questions Mode

If the user says:

* "quick draft"
* "minimal questions"
* "draft with assumptions"
* "just create a first version"
* "continue with assumptions"

Then use Minimal Questions Mode.

In this mode, still ask one question at a time — just far fewer of them.

Ask only the 5 most critical missing questions, one per turn:

1. React Native or Native iOS/Android?
2. Who is the target user?
3. What is the main happy path?
4. Is there an existing backend API?
5. Is there Figma or screenshots, or should the SPAC describe behavior only?

Skip any of these already answered by uploaded inputs.

Fill everything else with clearly marked assumptions and continue.

Add to the document header:

```md
**Draft Mode:** Minimal Questions Mode
```

Keep the confidence score lower if important information is missing.

---

## Phase 9 — Codebase Context Scan

Use codebase context only to understand existing app patterns.

Do **not** use this phase to turn the SPAC into a low-level technical design document.

Before reading source files, Claude must first inspect repository Markdown documentation when available, especially `CLAUDE.md`, README files, architecture docs, feature docs, and existing SPAC/DD/task files.

### Uploaded code files

If the user uploaded relevant source files, analyze them before writing.

Look for:

* Existing components that could or should be reused
* State management patterns already in use:

  * Redux
  * Zustand
  * Context API
  * React Query
  * SWR
  * local component state
* API call conventions:

  * axios
  * fetch
  * generated API client
  * service layer
  * custom hooks
* Navigation patterns
* Naming conventions
* Folder structure patterns
* Styling conventions
* Anything that might conflict with the proposed feature
* Duplicate functionality
* Deprecated patterns
* Missing pieces the SPAC team may not have noticed

### Bitbucket / MCP code scan

If the project code is available through Bitbucket MCP, use it to inspect the existing frontend codebase before writing the SPAC.

Use the repo context already collected:

* Bitbucket workspace/project/repository name
* Target branch
* Relevant app/module/package name, if the repo is a monorepo
* Existing feature/screen/component that is closest to the requested feature
* Any folders the SPAC team already knows are relevant

Use Bitbucket MCP to inspect:

* Navigation structure
* Existing screens/views related to the feature
* Reusable components
* Form patterns
* List/detail patterns
* Modal/dialog patterns
* Loading, empty, error, and success-state patterns
* Permission/role checks
* API/service layer conventions
* i18n/RTL implementation
* Accessibility conventions
* Platform-specific iOS/Android handling
* Design system usage
* Existing feature overlap or duplicate functionality

### Code scan boundaries

Do not:

* Modify code
* Create commits
* Open pull requests
* Change branches
* Run destructive actions
* Reveal secrets, tokens, credentials, or private configuration values
* Read `.env`, certificates, keystores, tokens, private keys, or credentials
* Copy large code blocks into the SPAC
* Put detailed code scan findings inside the SPAC

The SPAC team’s Bitbucket access should be read-only for this workflow.

### Chat output format

Surface code findings in chat only.

Use this format:

---

**🔍 Codebase Context Findings**

**Relevant areas inspected:**

* `[path]` — [why it matters]

**Reusable components / patterns:**

* `<ComponentName>` in `[path]` — [how it may help]

**Existing conventions observed:**

* Navigation: [summary]
* Data fetching/API: [summary]
* State management: [summary]
* Styling/design system: [summary]
* i18n/RTL: [summary]
* Loading/error/empty states: [summary]

**Potential conflicts or risks:**

* [risk]
* [risk]

**Impact on the SPAC:**

* [what should be reflected in the SPAC]
* [what should stay for the Frontend DD]

---

After sharing findings, ask:

> "Should any of these code findings affect the SPAC before I write it?"

---

## Phase 10 — UI Element Data Mapping

For every data-driven screen, create a UI Element Data Mapping table.

This table maps each important visible UI element to its expected data source.

Use available sources in this order:

1. Figma MCP frames/components
2. Uploaded screenshots
3. Backend DD / API Design Document
4. Bitbucket/codebase MCP
5. Repository documentation files
6. Business requirements
7. SPAC team answers

If a Figma URL is available, use Figma MCP to inspect the relevant frames and identify visible elements.

If Figma is not available, ask the SPAC team to upload screenshots of the relevant screens.

If screenshots are not available, create the mapping from the written requirements and clearly mark confidence.

### What to map

Identify and map:

* Titles and labels
* User-facing text
* Images, icons, and avatars
* Buttons and actions
* Cards and list items
* Input fields
* Toggles, checkboxes, and selectors
* Badges, tags, and statuses
* Counters, totals, dates, and formatted values
* Empty/loading/error/success-state elements
* Conditional elements shown only for specific roles, permissions, or data states

### Required table format

Use this format inside the SPAC:

```md
## UI Element Data Mapping

### Screen: [Screen or Figma Frame Name] — [Figma link](https://www.figma.com/design/<fileKey>?node-id=<nodeId>)

| UI Element | Element Type | Screen / Frame | Display Rule | Data Source | Backend/API Field | Fallback / Empty Value | Confidence | Notes |
|---|---|---|---|---|---|---|---|---|
| [Element name] | [Text/Button/Image/etc.] | [Frame name] | [When it appears] | [Service/API/local/static] | [field path] | [fallback behavior] | [High/Medium/Low/Need to verify] | [notes] |
```

The Figma link on the screen heading must point directly to the node inspected. If multiple frames were used for one screen (e.g. default + empty state), list all links:

```md
### Screen: Request Form — [Default](https://figma.com/...) · [Empty state](https://figma.com/...) · [Error state](https://figma.com/...)
```

If no Figma link is available for a screen, write `(Figma: not available)` next to the heading.

### Confidence values

Use only these values:

* **High** — confirmed by Backend DD, codebase model/service, repository documentation, or explicit SPAC team answer
* **Medium** — likely source is known, but exact field/path needs confirmation
* **Low** — inferred from requirements or Figma only
* **Need to verify** — data source, field, or display rule is unknown

### Data source rules

* If the value comes from the backend, name the service/API and exact field when known.
* If the exact backend field is unknown, write `Need to verify`.
* If the service is unknown, write `TBD: Data source needs confirmation`.
* If the value is static text, write `Static / i18n`.
* If the value comes from navigation params, write `Navigation params`.
* If the value comes from local state, write `Local state`.
* If the value comes from device state or permissions, write `Device / OS state`.
* If the value is derived or calculated, write `Derived` and explain the calculation in Notes.
* If the value is conditional by role, permission, feature flag, or data state, describe the condition in Display Rule.
* If the value can be missing/null, define the fallback or empty behavior.

### Unknown mappings

Do not invent data mappings.

If Claude is not confident where the data comes from, write:

```md
Need to verify
```

For important unknowns, also add an item to Open Questions.

Example:

```md
- What is the source of the member status badge on the Profile screen?
- Is total distance calculated by the frontend or returned by the training details API?
```

---

## Phase 11 — Stack Adaptation Rules

Before writing, apply the following based on `target_stack`.

---

### If `react_native`

Add this to the document header:

```md
**Team:** React Native
```

Use React Native terminology:

* `View`
* `Text`
* `StyleSheet`
* `FlatList`
* `TouchableOpacity`
* `Pressable`
* hooks
* component state
* React Navigation
* native permissions
* iOS / Android platform behavior

Navigation:

* Reference React Navigation patterns where relevant:

  * stack navigator
  * tab navigator
  * drawer navigator
  * modal presentation
  * deep linking

Styling:

* Reference the styling approach used by the app if known:

  * StyleSheet
  * styled-components
  * NativeWind
  * design system components

Platform notes:

* Flag any `Platform.OS` differences needed between iOS and Android.
* Flag permission differences between iOS and Android.
* Flag native behavior differences where relevant.

State management:

* Reference the existing pattern if known.
* If unknown, avoid prescribing one and mark it as TBD or DD responsibility.

---

### If `native_ios_android`

Add this to the document header:

```md
**Team:** Native iOS / Android
```

Use platform-native terminology.

For iOS:

* `UIViewController`
* `SwiftUI`
* `UIView`
* `@State`
* `NavigationStack`
* `UIKit`
* `ViewModel`

For Android:

* `Activity`
* `Fragment`
* `Jetpack Compose`
* `ViewModel`
* `LiveData`
* `StateFlow`
* `Navigation Component`

Where behavior differs between iOS and Android, use clearly labeled subsections:

```md
#### iOS

#### Android
```

If the feature is one platform only, omit the irrelevant platform section.

---

### For both stacks

Avoid web/browser terminology in mobile SPACs.

Do not use:

* page
* DOM
* CSS
* responsive
* viewport
* browser

Use mobile terminology instead:

* screen
* view
* component
* layout
* native styling
* device size
* safe area

---

## Phase 12 — Readiness & Quality Gate

Before writing the SPAC, evaluate completeness of the inputs.

Produce a short readiness summary in chat.

Use this format:

```md
## SPAC Readiness Check

Confidence: [number]%
UI Data Mapping Confidence: [High / Medium / Low / Need to verify]
Codebase Context Confidence: [High / Medium / Low / Not available]
Documentation Context Confidence: [High / Medium / Low / Not available]

Ready to draft: Yes / No

Strong areas:
- [item]
- [item]

Missing or weak areas:
- [item]
- [item]

Assumptions needed:
- [item]
- [item]

Risks or conflicts:
- [item]
- [item]

Recommendation:
- [write DRAFT / ask more questions / resolve conflict first]
```

### Readiness rules

* If confidence is **90% or higher**:

  * Continue to write a detailed DRAFT.
* If confidence is **70–89%**:

  * Continue to write a DRAFT.
  * Clearly mark assumptions and open questions.
* If confidence is **below 70%**:

  * Do not write the full SPAC yet.
  * Ask only the minimum required questions first.
* Never mark the SPAC as READY based on confidence alone.
* READY requires explicit user approval.

### UI Data Mapping Confidence

Use this guidance:

* **High** — most visible dynamic elements have confirmed data sources
* **Medium** — main elements are mapped, but some secondary fields need confirmation
* **Low** — screen is visible, but backend/service mapping is mostly unknown
* **Need to verify** — most UI element sources are unknown

### Codebase Context Confidence

Use this guidance:

* **High** — Bitbucket MCP or uploaded code was available and relevant files were inspected
* **Medium** — partial code context was available
* **Low** — only limited code snippets or verbal explanation were available
* **Not available** — no codebase context was available

### Documentation Context Confidence

Use this guidance:

* **High** — `CLAUDE.md`, README, and relevant docs were inspected
* **Medium** — some documentation was inspected, but important docs were missing
* **Low** — only limited documentation was available
* **Not available** — no repository documentation was available

---

## Phase 13 — Write the SPAC

Create the file at:

```txt
/mnt/user-data/outputs/spac_<feature_name>.md
```

If the environment uses a different output convention, save according to the current workspace output convention.

Use the template in:

```txt
references/spac-template.md
```

Read this template before writing Phase 13.

---

## SPAC Writing Rules

The SPAC must be specific and unambiguous.

A developer should be able to understand the desired frontend behavior without asking basic product questions.

### General rules

* Do not invent requirements.
* Clearly mark unknown items as TBD.
* Clearly mark assumptions.
* **Never silently decide product/UI behavior.** If, in the absence of an explicit requirement, you decide how something should behave — including things like hiding a button, disabling an action, removing an element, defaulting a value, choosing an error message, or picking a state transition — that decision is an assumption. It must be written into the Assumptions section (Section 20) as its own line item, not just implied by how a screen or flow is described. The bar is: if you made a judgment call the user didn't give you, it goes in the list.
* Every UI state mentioned must describe what the user sees.
* Reference Figma frames/components by name if extracted, and always include a clickable Figma node link next to screen headings in UI Requirements and UI Element Data Mapping.
* Reference screenshots by filename or screen name if used.
* Reference backend endpoints by name/path if a Backend DD was provided.
* Include UI Element Data Mapping for every data-driven screen.
* Reference Bitbucket repository, branch, and module/path used as context.
* Reference repository documentation files used as context.
* If Figma and requirements conflict, list it in Open Questions.
* If repository documentation conflicts with business requirements, Figma, Backend DD, or code, list it in Open Questions.
* Keep code findings out of the SPAC document.
* Keep technical implementation details for the Frontend Technical DD unless they are required for frontend behavior.

### TBD format

Use this format inside the relevant section:

```md
> ⚠️ TBD: [description of what is missing]
```

### Assumption format

Use this format inline, at the point in the document where the assumption applies:

```md
> Assumption: [the assumed behavior]
```

Every inline Assumption marker used anywhere in the document must also have a matching line item in Section 20 (Assumptions). The inline marker shows *where* the assumption applies; the Assumptions section is the single place the user reviews and can push back on *all* of them. Never place an inline Assumption marker without also adding it to the list, and never add something to the Assumptions list without marking it inline where it affects the spec.

---

## Required Document Header

Every generated SPAC must start with:

```md
# SPAC: [Feature Name]

**Status:** 🟡 DRAFT
**Team:** [React Native | Native iOS / Android]
**Author:** [ask user for name if not known]
**Reviewer:** TBD
**Last Updated:** [today's date]
**Confidence:** [number]%
**UI Data Mapping Confidence:** [High / Medium / Low / Need to verify]
**Codebase Context:** [Bitbucket MCP connected / Uploaded files / Partial / Not available]
**Codebase Context Confidence:** [High / Medium / Low / Not available]
**Repository:** [workspace/project/repo or N/A]
**Branch:** [branch or N/A]
**Module/Path:** [path or N/A]
**Documentation Context:** [Available / Partial / Not available]
**Documentation Context Confidence:** [High / Medium / Low / Not available]
**Docs Used:** [`CLAUDE.md`, `README.md`, `docs/navigation.md`, etc. or N/A]
```

If Minimal Questions Mode was used, also add:

```md
**Draft Mode:** Minimal Questions Mode
```

---

## Required SPAC Sections

Use the structure from `references/spac-template.md`, but ensure the final SPAC includes these sections when relevant:

```md
## 1. Feature Overview

## 2. Target Users

## 3. Problem Statement

## 4. Goals

## 5. Out of Scope

## 6. Entry Points

## 7. User Flow

## 8. UI Requirements

## 9. UI Element Data Mapping

## 10. UI States

## 11. Data & Backend Dependencies

## 12. Validation Rules

## 13. Permissions

## 14. Security & Privacy

## 15. Accessibility

## 16. Localization & RTL

## 17. Analytics / Tracking

## 18. Platform Notes

## 19. Project Context Used

## 20. Assumptions

## 21. Open Questions

## 22. Developer Handoff Checklist

## 23. Downstream AI Usage
```

If a section is not relevant, write:

```md
Not required for this feature.
```

---

## Section Guidance

### UI Element Data Mapping

This section is required for every data-driven screen.

If the screen is static or local-only, write:

```md
Not required — static or local-only screen.
```

Example:

```md
## UI Element Data Mapping

### Screen: Training Details

| UI Element | Element Type | Screen / Frame | Display Rule | Data Source | Backend/API Field | Fallback / Empty Value | Confidence | Notes |
|---|---|---|---|---|---|---|---|---|
| Training title | Text | `Training Details` | Always visible | Training service | `training.title` | “Untitled training” | High | Field confirmed from Backend DD |
| Training date | Text | `Training Details` | Always visible | Training service | `training.training_date` | Hide date row | High | Format using app date localization |
| Coach name | Text | `Training Details` | Visible if coach exists | User/profile service | `coach.display_name` | “Coach” | Medium | Need to confirm exact object path |
| Total distance | Text | `Training Details` | Visible when exercises exist | Derived | `sum(exercises[].distance)` | `0m` | Medium | Derived in frontend or backend — Need to verify |
| Complete button | Button | `Training Details` | Visible if training is not completed | Completion state/API | `completion.status` | Hide if completed | Low | Need to verify source of completion status |
| Missed button | Button | `Training Details` | Visible if training date has passed and not completed | Completion state/API + date logic | `completion.status`, `training.training_date` | Hide | Low | Business rule needs confirmation |
| Exercise list | List | `Training Details` | Visible if exercises exist | Training service | `training.exercises[]` | Show empty state | High | Each item maps style, distance, reps, rest |
| Empty exercises message | Text | `Training Details` | Visible when exercises array is empty | Static / i18n | `training.details.emptyExercises` | N/A | High | Translation key required |
```

---

### Security & Privacy

Include this section when the feature touches:

* personal data
* private user data
* role-based data
* payment data
* location data
* health data
* children/minor data
* admin-only data
* group/school/customer-specific data

Describe:

* Who can see the data
* Who cannot see the data
* What data should be masked or hidden
* Permission-denied behavior
* Any audit or privacy expectations

Example:

```md
## Security & Privacy

Visible to:
- Group leaders
- Members of the same group

Not visible to:
- Users outside the group
- Unauthenticated users

Data visibility:
- Member name: visible
- Phone number: visible only if `share_phone = true`
- Email address: hidden from regular members

Permission denied behavior:
- Show a clear access-denied message.
- Do not show partial private data.
```

---

### Accessibility

Include this section for every user-facing feature unless truly not relevant.

Describe:

* screen reader labels
* icon-only buttons
* dynamic font size
* color contrast expectations
* avoiding color-only status indicators
* accessible error messages
* accessible loading states

Example:

```md
## Accessibility

- Icon-only actions must include clear accessibility labels.
- Error messages must be readable by screen readers.
- The feature must not rely only on color to communicate status.
- Text should support dynamic font size where possible.
```

---

### Localization & RTL

Include this section when the app supports multiple languages or Hebrew/RTL.

Describe:

* required language support
* i18n usage
* no hardcoded user-facing strings
* RTL alignment
* directional icon behavior
* date/time/number formatting

Example:

```md
## Localization & RTL

- All user-facing strings must use the existing i18n system.
- Hebrew layout must support RTL.
- Directional icons must flip when they represent navigation direction.
- Date and time values must use the app's existing localization format.
```

---

### Analytics / Tracking

This section is **not mandatory by default**.

The skill must ask the SPAC team whether analytics or tracking is needed.

If the SPAC team confirms analytics is needed, include:

```md
## Analytics / Tracking

### Event: [event_name]

Triggered when:
- [condition]

Properties:
- [property]
- [property]
```

If analytics is not needed, write:

```md
## Analytics / Tracking

Not required for this feature.
```

Do not invent analytics events unless the user confirms analytics is needed or the provided requirements explicitly mention analytics, reporting, BI, audit, monitoring, or conversion tracking.

---

### Project Context Used

Every SPAC must include this section.

Use this section to document what project context was used when writing the SPAC.

Example:

```md
## Project Context Used

### Repository Context

- Repository: `matrix-digital/MOBILE/customer-app`
- Branch: `develop`
- Module/path: `apps/mobile`
- Bitbucket MCP status: Connected

### Documentation Context

Docs inspected:
- `CLAUDE.md`
- `README.md`
- `docs/navigation.md`
- `docs/i18n.md`

Relevant project rules:
- Use existing design system components where possible.
- All user-facing strings must use i18n.
- Navigation must follow existing stack/tab structure.

### Codebase Context

Relevant areas inspected:
- `src/navigation`
- `src/features/profile`
- `src/components`
- `src/services`

Codebase context notes:
- Detailed code scan findings were surfaced in chat only.
- This SPAC reflects reusable patterns but does not prescribe low-level implementation.
```

If no project context was available, write:

```md
## Project Context Used

Repository context was not available.

Codebase Context: Not available  
Documentation Context: Not available

> ⚠️ TBD: SPAC should be reviewed against the actual repository before being marked READY.
```

---

### Assumptions

Include **every** assumption used to write the SPAC — anything decided without an explicit answer from the user, no matter how small it seems. This includes UI/behavior calls such as hiding a button, removing an element, disabling an action, or picking a default — these are exactly the kind of assumption that must surface here so the user can confirm or correct them.

Example:

```md
## Assumptions

- The feature is available only to authenticated users.
- Existing authentication/session handling will be reused.
- Backend authorization is handled by the existing API layer.
- The "Export" button is hidden for users without the manager role (no explicit requirement given; assumed from existing permission patterns).
```

Rules:

* Do not hide assumptions inside regular requirements — an assumption baked silently into a screen description (e.g. "the button is hidden for these users") does not count as documented unless it also appears as its own line here.
* Every assumption appears here — not only ones judged to be significant. Let the user decide what's significant; do not pre-filter.
* If an assumption is risky or reverses default/visible behavior (e.g. hiding or removing something a user might expect to see), also list it in Open Questions so it gets explicit sign-off, not just a silent read-through.

---

### Open Questions

Include unresolved questions that must be confirmed before the SPAC can be marked READY.

Example:

```md
## Open Questions

- Should users be able to edit their phone number?
- Is OTP verification required after phone number change?
- What is the exact backend endpoint for saving changes?
- What is the data source for the member status badge?
- Is total distance calculated by the frontend or returned by the training details API?
- Should the SPAC be reviewed against the Bitbucket repo before being marked READY?
```

---

### Developer Handoff Checklist

Every SPAC must include this checklist.

Use this format:

```md
## Developer Handoff Checklist

- [ ] Feature goal is clear
- [ ] Target user is defined
- [ ] Entry point is defined
- [ ] Happy path is defined
- [ ] Bitbucket repository reference is documented
- [ ] Target branch is documented
- [ ] Relevant module/path is documented
- [ ] Bitbucket MCP connectivity was checked
- [ ] Codebase context was used or marked as unavailable
- [ ] Repository documentation was checked when available
- [ ] `CLAUDE.md` was checked when available
- [ ] Relevant feature docs/specs/DDs were checked when available
- [ ] Documentation conflicts are listed in Open Questions
- [ ] UI Element Data Mapping is included for every data-driven screen
- [ ] Each visible dynamic element has a data source or is marked `Need to verify`
- [ ] Unknown data mappings are listed in Open Questions
- [ ] Static text is marked as `Static / i18n`
- [ ] Fallback behavior is defined for missing/null values
- [ ] Empty state is defined
- [ ] Loading state is defined
- [ ] Error states are defined
- [ ] Permissions are defined
- [ ] Security/privacy behavior is defined or marked as not required
- [ ] Accessibility behavior is defined or marked as not required
- [ ] Localization/RTL behavior is defined or marked as not required
- [ ] Backend/API dependencies are defined or marked as TBD
- [ ] Figma frames/components are referenced or marked as not provided
- [ ] Screenshots are referenced if Figma was not available
- [ ] Analytics/tracking is confirmed as required or not required
- [ ] Assumptions are listed
- [ ] Open questions are listed
```

---

### Downstream AI Usage

Every SPAC must include this section.

Use this format:

```md
## Downstream AI Usage

This SPAC is intended to be used as input for:

1. Frontend Technical DD
   Expected file:
   - `dd_<feature_name>.md`

2. Development task breakdown
   Expected file:
   - `tasks_<feature_name>.md`

3. Claude Code implementation planning
   Expected usage:
   - Claude Code should read this SPAC together with the Frontend Technical DD and task list before implementation.

4. QA test case generation
   Expected file:
   - `qa_<feature_name>_test_cases.md`
```

---

## Phase 14 — Final Review, Status & Handoff

Before presenting the SPAC file, perform a final review.

### Final review checklist

Verify that:

* [ ] Document header exists and includes:

  * Status
  * Team
  * Author
  * Reviewer
  * Last Updated
  * Confidence
  * UI Data Mapping Confidence
  * Codebase Context
  * Codebase Context Confidence
  * Repository
  * Branch
  * Module/Path
  * Documentation Context
  * Documentation Context Confidence
  * Docs Used
* [ ] Status is `🟡 DRAFT`
* [ ] All required SPAC sections are present
* [ ] Project Context Used section exists
* [ ] UI Element Data Mapping exists for every data-driven screen
* [ ] Every dynamic UI element has a data source or is marked `Need to verify`
* [ ] Important `Need to verify` items are also listed in Open Questions
* [ ] All assumptions are listed in the Assumptions section
* [ ] No judgment call (hidden/removed/disabled elements, defaults, fallback behavior, etc.) was made in the SPAC without a corresponding entry in the Assumptions section
* [ ] Analytics / Tracking is either defined or marked as not required
* [ ] Security & Privacy is defined or marked as not required
* [ ] Accessibility is defined or marked as not required
* [ ] Localization & RTL is defined or marked as not required
* [ ] Developer Handoff Checklist is included
* [ ] Downstream AI Usage is included
* [ ] No code scan findings were placed inside the SPAC
* [ ] No low-level implementation details were added unless required for frontend behavior
* [ ] The document was not marked READY without explicit approval

If anything is missing, fix the SPAC before presenting it.

After writing, tell the user in chat:

> "SPAC is saved as **DRAFT**. When you've reviewed it and it's ready for developers, just say 'mark it ready' and I'll update the status to ✅ READY, generate an HTML preview for stakeholder review, and create a DD starter file for the development team."

Always present the generated file to the user for download.

If the environment supports `present_files`, call `present_files`.

---

## Marking READY

When the user says:

* "mark it ready"
* "it's approved"
* "change status to ready"
* "approved for development"
* "ready for developers"

Then:

1. Re-open the file.
2. Change:

```md
**Status:** 🟡 DRAFT
```

to:

```md
**Status:** ✅ READY
```

3. Update `Last Updated` to today's date.
4. Ask:

> "Who reviewed it? I'll add the reviewer name."

5. If the reviewer name is provided, update:

```md
**Reviewer:** [name]
```

6. If the user does not provide a reviewer, keep:

```md
**Reviewer:** TBD
```

7. Save the updated SPAC file.
8. Run **Phase 15 — HTML Preview**.
9. Run **Phase 16 — DD Starter**.
10. Present all three files together using `present_files`:
    * `spac_<feature_name>.md` — the READY SPAC
    * `spac_<feature_name>.html` — human-readable preview
    * `dd_<feature_name>.md` — DD starter for the development team

Never mark READY on your own.

READY always requires explicit user approval.

---

## Phase 15 — HTML Preview

Generate a human-readable HTML version of the SPAC for stakeholder review.

This file is for **humans** — product managers, designers, QA leads, and business stakeholders who need to review and sign off on the feature spec. It is not a developer artifact.

### When to generate

Generate this file immediately after marking the SPAC as ✅ READY.

Do not generate it for DRAFT SPACs unless the user explicitly asks.

### Output path

```txt
/mnt/user-data/outputs/spac_<feature_name>.html
```

### Design rules

* Clean, readable layout — no heavy framework dependencies.
* Inline all CSS — single self-contained file, no external stylesheets or scripts.
* Responsive: readable on both desktop and mobile.
* Use a white background with good contrast. Body text: 16px, line-height 1.6.
* Use a clear visual hierarchy: feature name as the page `<h1>`, section numbers and names as `<h2>`, subsections as `<h3>`.
* Render the status badge prominently near the top:
  * 🟡 DRAFT — amber badge
  * ✅ READY — green badge
* Render the document header metadata (Team, Author, Reviewer, Confidence, etc.) as a styled info block near the top.
* Render the Developer Handoff Checklist as real HTML checkboxes (read-only, pre-checked based on SPAC content).
* Render UI Element Data Mapping tables as proper `<table>` elements with alternating row colors.
* Render TBD blocks as amber highlighted callouts.
* Render Assumption blocks as blue highlighted callouts.
* Render Open Questions as a numbered list with a distinct visual treatment (e.g. left border accent).
* Do not include raw Markdown syntax in the rendered output.
* Do not include any JavaScript except for a simple print button at the top.

### Structure

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>SPAC: [Feature Name]</title>
  <style>/* all styles inline */</style>
</head>
<body>
  <!-- Print button -->
  <!-- Status badge + header metadata block -->
  <!-- SPAC sections in order -->
  <!-- Footer: generated date, skill version note -->
</body>
</html>
```

### What to include

Render every section from the SPAC `.md` file in the same order.

For sections marked "Not required for this feature", render a muted placeholder rather than omitting the section entirely — this helps reviewers confirm the section was considered.

---

---

## Important Reminders

* Always ask the stack question first.
* Always ask for Bitbucket repository context when available.
* Always check Bitbucket MCP connectivity when repository context is provided.
* If Bitbucket MCP is unavailable, continue with fallback inputs and mark codebase context as unavailable or partial.
* Always inspect repository Markdown documentation before scanning source code when Bitbucket MCP is available.
* Always check `CLAUDE.md` when available.
* Never skip the requirements interview unless the user explicitly asks for Minimal Questions Mode.
* Never skip Phase 7 — always identify confidence gaps before writing.
* Never start writing the SPAC without explicit user approval at the end of Phase 7.
* Only ask gap questions that affect correctness — not nice-to-haves.
* Never mark READY without explicit approval.
* Never use web terminology in a mobile SPAC.
* Never invent requirements.
* Mark unknowns as TBD.
* Mark uncertain data mappings as `Need to verify`.
* Mark assumptions clearly.
* Never make a silent judgment call on UI/behavior (hiding a button, removing an element, disabling an action, choosing a default, etc.) — every one of these goes into the Assumptions section as its own line, so the user can confirm or correct it.
* Codebase scan findings go in chat, not in the SPAC.
* Repository documentation findings go in chat, not as long copied text inside the SPAC.
* UI Element Data Mapping goes inside the SPAC.
* Use Figma MCP to extract screens when available.
* If Figma is unavailable, ask for screenshots.
* Figma is the source of truth for UI unless the user says otherwise.
* If Figma and requirements conflict, flag it as an Open Question.
* Always embed a clickable Figma node link next to every screen heading in UI Requirements and UI Element Data Mapping — use the full URL format `https://www.figma.com/design/<fileKey>?node-id=<nodeId>`.
* If repository documentation conflicts with requirements, Figma, Backend DD, or code, flag it as an Open Question.
* Analytics / Tracking must be asked about, not forced.
* The SPAC should describe product and frontend behavior.
* The Frontend Technical DD should describe detailed implementation.
* After writing the SPAC, always present the file so the user can download it.
* When marking READY, always generate the HTML preview (Phase 15).
* Always present both files together on READY: the SPAC `.md` and the HTML preview.
* The HTML preview is for human stakeholder review — keep it clean, readable, and self-contained.

---

## Reference Files

* `references/spac-template.md` — The full SPAC document template. Read this before writing Phase 13.
* `references/html-preview-template.html` — The HTML preview template. Read this before writing Phase 15.
