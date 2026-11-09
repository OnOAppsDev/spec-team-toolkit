---
name: lld-web-backend-spec
description: Use this skill whenever the user wants to write a Low Level Design (LLD) / detailed specification for a WEB feature, for handoff to frontend developers, backend developers, and QA in one document. Handles web-only specs (UI from Figma or screenshots, optionally with CMS-managed content) and combined frontend/backend web specs (new or changed APIs, business rules, data changes, integrations). Trigger on phrases like "write the LLD for this web feature", "spec out this Figma component", "create the content and display tables for this design", "spec the frontend and backend for this page", "אפיין את הרכיב הזה", "אפיין את הפיצ'ר באתר", or whenever the user shares requirements/HLD, a Figma link or screenshots, or API docs for a website feature and wants a structured LLD. Interviews the analyst one question at a time, covers both the website visitor and (when a CMS such as Umbraco is involved) the content editor, and traces every behavior to its design, API contract, or content rule. For mobile (React Native / Native iOS-Android) features, use `lld-mobile-spec` instead. For backend-only service/API work with no web UI, use `lld-backend-spec` instead.
---

# LLD Web + Backend Spec

## What this skill does

Guides the spec team, through an interactive interview, to one integrated LLD for a web feature that frontend developers, backend developers, and QA all work from. Depending on the feature, the document covers:

- **The website visitor's side** — every displayed component, its data source, its logic and states, plus feature-specific responsiveness and accessibility notes.
- **Integration and business rules** — rules, cross-system scenarios, new/changed API contracts, data changes, integrations. Only when the feature calls an API or crosses systems.
- **The content editor's side** — content types, fields, hierarchy, validation, permissions, workflow, and how published content reaches the site. Only when a CMS manages part of the feature.

Read both reference files before drafting and follow them closely:

- `references/lld_template.md` — the document skeleton, numbered sections, ID scheme, and table columns.
- `references/lld_instructions.md` — the content rules for each table (edge cases, API states, Umbraco 13 editors, cross-system scenarios). These reflect how the team already works.

The Markdown file is the single source of truth. HTML is generated from it on request with `scripts/md_to_html.py` and is never edited by hand.

## Ground rules for the whole session

- **One question at a time.** Ask, wait, acknowledge the answer in one short sentence, then continue. Never dump a list of questions.
- **Don't ask what the sources already answer.** When a document answers a question, confirm instead of asking ("According to the spec, only one page of this type can exist — correct?"), or just record it.
- **Keep three ledgers separate from the start:** confirmed decisions, assumptions (`AS-xx`), and open questions — business (`BQ-xx`) and technical (`TQ-xx`). Each item gets its ID when it is first raised.
- **Never invent** a field name, status code, endpoint, editor type, or business rule for anything that already exists. Mark it "צריך לוודא" (or the document language's equivalent) and reference the open question that covers it. The one exception is a **new or changed API contract or data structure** (sections 5.3–5.4): there, propose values that follow the repo's conventions and mark each judgment-call value "מוצע". Values fixed directly by a documented convention aren't marked (see `references/lld_instructions.md`, section 5.3).
- **Read-only everywhere.** Figma, repositories, and documentation are inspected, never modified. Never read `.env` files, certificates, keys, tokens, or other secrets, and don't paste large code blocks into the LLD.
- **Write in the language the analyst uses.** Section titles are localized; section numbers, IDs, technical identifiers, API field names, and data types stay in English.

## Workflow

### 1. Review the materials already provided

Before asking anything, read everything the analyst has supplied: requirements or HLD, existing specs, Figma links, screenshots, API documentation, repo details, and any earlier draft of this LLD. If an earlier draft (`lld_<feature>.md`) is uploaded, resume from it rather than starting over: keep its IDs and add a change-history row for the new version.

Then report in chat:

- a short table of sources and their status (read / missing / no access);
- what the sources show about scope — which of Web UI, Backend, and CMS appear to change;
- conflicts already found, each recorded as an open item with an ID;
- roughly how many questions you expect to ask, so the analyst knows the size of the interview.

When screenshots are embedded in a document, look at them — don't rely on the extracted text alone. Screenshots often contain states, labels, and formatting that the text omits or contradicts (an empty-state message with a different trigger, a disabled row, bullets in a field typed as plain text).

### 2. Establish scope and the CMS gate

Ask only what step 1 left unanswered, in this order:

1. **What changes:** the web UI, the backend (new or changed APIs, data, integrations), the CMS — or which combination.
2. **CMS gate — ask early:** does a content editor manage any part of this feature? If yes, confirm which CMS and, where relevant, its version (for Umbraco, confirm 13). If no, skip every CMS question and the editor side of the document (section 6 keeps its heading with "לא רלוונטי לפיצ'ר זה" and a one-line reason).
3. **Existing contracts:** for every backend capability the feature uses, is it existing (give it an `API-xx` entry marked "(קיים)" that links its contract, and reuse it) or new/changed in this feature (specify it in full in section 5.3)? If documentation for an existing contract isn't available, open a `TQ` and mark every dependent field "צריך לוודא".

### 3. Inspect sources read-only

- **Figma:** when a Figma connector is available, pull design context, screenshots per element, and node links (`[Figma → name](https://www.figma.com/design/<fileKey>?node-id=<nodeId>)`). The Figma MCP server only reads files the user's account can edit. If access is refused, say so, record it in the sources table, and continue from exported images or the screenshots embedded in the documents. Both desktop and mobile versions must be covered — ask for whichever is missing.
- **Codebase:** when a repository connector or uploaded code is available, read documentation first (`CLAUDE.md`, README, architecture/API docs), then the API layer, models, and existing components closest to the feature. Prefer existing conventions (naming, error shape, auth pattern) over inventing new ones. If no access, continue without it and record that in the sources table.
- **API documentation:** for existing contracts, use Swagger/OpenAPI, IDD, an existing backend LLD, or the code as the only source. For new or changed contracts, use the conventions found here or in the codebase as the basis for the proposed values.

### 4. Classify every element before drafting

For each displayed value, decide whether it is **editor-managed** (→ a CMS field), **fixed** (dictionary text, hardcoded value, static asset), **API-supplied** (→ an API operation and field), or **derived** (calculated from other values → a `BR-xx` business rule in section 5; when section 5 doesn't apply, the rule is written in the component's logic column instead). Create editor fields only for editor-managed values. For components that combine sources, classify each value separately.

### 5. Interview — one question at a time, blocking questions first

Work through the topics below, skipping anything the sources already answer or the scope excludes. Ask blocking questions first: the ones whose answer changes structure, data flow, or what QA tests. Record minor conflicts straight away as open items instead of turning each into a question. At any point the analyst can say "skip to draft"; then everything still unanswered stays an open item with its ID.

**Visitor side (always considered; ask only the topics that apply):** the visitor's goal; entry points and URL parameters (pages, not embeddable components); the main flow; what happens on each action; states (loading, success, empty, error, partial failure) for anything that loads data; desktop/mobile differences that aren't standard; accessibility needs the framework doesn't already cover. Don't ask "what is out of scope" as its own question: derive it from the materials and answers, and confirm it in the readiness check.

**Editor side (only if a CMS is involved):** the editor's goal; templates/content types and how many instances can exist; fields, nesting, and repeatable items; required/optional values, defaults, validation, and content limits; who can create, edit, approve, and publish; the approval/publishing workflow (reference an existing workflow when one applies); how published content reaches the site — field mapping, transformations, caching, and behavior when content is missing.

**Backend and integration (only if an API or cross-system flow is involved):** for each new or changed operation, its purpose, permissions, request and response shape, validation, and errors; business rules; data changes and migrations; integrations and what happens when one is unavailable; how fresh API-supplied data must be, when it matters to the visitor (prices, availability, status).

**Cross-system scenarios:** for each scenario that crosses the frontend, backend, or CMS, the trigger, where the data comes from, which rules apply, what passes between systems, and what the visitor sees.

How to ask:

- **System responsibility and implementation choices** (where filtering, sorting, or calculation runs; caching mechanism; sync vs. async). The default is **"ייקבע ע"י צוות הפיתוח"** (to be decided by the development team), recorded as a `TQ` owned by the development team, without asking. Ask the analyst only when the choice changes what the visitor or editor experiences (latency, freshness, consistency), and then always offer "ייקבע ע"י צוות הפיתוח" as an option. Either way, the rule itself and the visible behavior are specified in full.
- **Propose, then confirm — bundled:** for gaps with a sensible default (loading/error/partial-failure behavior, date formats, feature-specific accessibility), propose concrete behavior. Present all such proposals for one area together in a single question, and ask the analyst to approve, correct, or say which items they can't confirm. Approved items become decisions. Items the analyst can't confirm ("לא ידוע") are recorded as assumptions (`AS-xx`) with the proposed behavior, not also as open questions.
- **Challenge "can't happen":** when the analyst says a state cannot occur, check it against the rules already documented. If a documented rule can produce it, show the rule and ask how it should behave.
- **Accept "not important here":** record the item as a reference or out of scope, and don't ask follow-ups on it.
- **Document details, in one question** before the first full draft: the project name, "Document Approved By" (per the project's convention), and the author for the change-history row.

### 6. Readiness check

Before drafting, give a short summary in chat: which sections apply, what's confirmed, which open items will appear in the draft, and whether anything blocks drafting. Then draft — open items don't block a DRAFT, they're listed in it.

### 7. Draft the LLD

Write `lld_<feature>.md` following `references/lld_template.md` and `references/lld_instructions.md`. Status is **DRAFT**. Every behavior lives in the row of the component, field, rule, or scenario it belongs to. Open items and assumptions are listed once, at the end of the section they belong to, and referenced by ID from every row they affect. An item that affects more than one section is listed in the section of the row it affects most and referenced from the others. Items about sections 1–3 are listed in 4.7.

### 8. Verify before presenting

1. Run the traceability check and fix everything it reports:
   ```
   python3 scripts/trace_check.py lld_<feature>.md
   ```
   It fails on any referenced ID that isn't defined, on any ID defined twice, and on any field, rule, scenario, API operation, open item, or assumption that nothing references outside its own definition line. It warns about gaps in open-item numbering.
2. Check coverage by hand: every Figma frame or screenshot, interactive element, API operation, and content rule found in steps 1–4 is in the document or explicitly listed as out of scope. Don't drop anything silently.
3. Check that no CMS field exists for a fixed or API-supplied value, and that every editor type is a real editor of the confirmed CMS version (for Umbraco 13, see the list in `references/lld_instructions.md`).
4. Check that every API-sourced component states when the call happens and its success, empty, error, and partial-failure behavior.
5. Check that every proposed value in a new or changed contract is marked "מוצע" next to the value itself, and that one contract sign-off `TQ` owned by the backend team covers them.

### 9. Present, iterate, and finalize

Present the draft and the remaining open items. Apply the analyst's corrections to the Markdown file, then re-run step 8. Add a change-history row whenever a version is shared.

- **HTML on request:** `python3 scripts/md_to_html.py lld_<feature>.md` writes `lld_<feature>.html` next to it — RTL by default (`--lang en` for an English document), with numbered headings, readable tables, clickable IDs, and print styling. Regenerate it after every Markdown change; never edit the HTML by hand.
- **READY only on explicit approval** from the analyst. Confidence or a passing check isn't approval.
- **IDs are stable once a version has been shared.** A closed item stays in its list marked "נסגר" with a pointer to where the decision now lives. IDs are never reused. Before the first share, IDs may be renumbered to close gaps.

## Output

One Markdown file, `lld_<feature>.md`, structured per `references/lld_template.md`, and on request an HTML rendering generated from it. No Word document, and no separately maintained HTML.
