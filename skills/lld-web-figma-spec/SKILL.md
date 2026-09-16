---
name: lld-web-figma-spec
description: Use this skill whenever the user wants to write a Low Level Design (LLD) / component-level specification for a WEB UI component based on a Figma design, for handoff to the frontend web team and QA. Trigger on phrases like "write the LLD for this component", "spec out this Figma component", "create the content and display tables for this design", "אפיין את הרכיב הזה", or whenever the user shares a Figma link/file for a web component and wants an editor-content spec plus a display/behavior spec produced from it. Produces the two-part Umbraco-CMS-oriented content-entry and display-behavior specification this team already uses, pulling real data from Figma via the Figma MCP tools when connected rather than asking the user to describe the design by hand. For mobile (React Native / Native iOS-Android) features, use `lld-mobile-spec` instead. For backend service/API specs, use `lld-backend-spec` instead.
---

# LLD Web Figma Component Spec

## What this skill does

Turns a Figma UI component design (desktop + mobile) into a two-part specification document for developers and QA:

- **Part 1 — Content entry**: tables of the fields a content editor fills in. The CMS is Umbraco 13, so field types must map to real Umbraco editors, not generic types.
- **Part 2 — Display & behavior**: tables of every displayed element, its content source, display logic (including edge cases), responsiveness, and accessibility notes.

The exact rules for both parts — table columns, wording conventions, and several hard rules about what belongs in Part 1 vs Part 2 — are in `references/lld_instructions.md`. Read it before drafting and follow it closely; it reflects how this team already works, not a generic template.

## Workflow

1. **Get the design.** If a Figma connector is available, use it to pull real data rather than guessing from a description:
   - design-context / metadata tools for the structure and content of the component
   - a screenshot tool for a visual of each element, to place alongside its spec row (the instructions require a visual reference per row)
   - variable-definition tools if you need to confirm whether something is a fixed style vs. an actual editable value
   If no Figma connector is available, or the user gives a link that can't be opened, ask for exported images or screenshots of both the desktop and mobile versions — the instructions require both to be covered.

2. **Classify every piece of content before drafting.** For each element, decide up front whether it is: editor-entered (→ a Part 1 field), fixed/hardcoded (→ noted in Part 1 as fixed, not as an editable field), or sourced from an external API (→ excluded from Part 1 entirely; API-sourced elements are only characterized in Part 2's display table, per the instructions). Getting this classification right first avoids rework later, since the two parts have different rules for the same underlying content.

3. **Draft Part 1** using the field-table columns and rules in the reference file (field ID, name, type as a real Umbraco editor, description, required?, recommended validation, notes for the content editor). Give each list of repeating sub-components its own table.

4. **Draft Part 2** using the element-table columns in the reference file (element description, content source, logic including edge cases, responsiveness, accessibility, visual reference). Cover the required edge cases explicitly: empty content, overlong content, malformed content. Only note responsiveness where Desktop↔Mobile genuinely differs, and only note accessibility for things Figma or the dev environment doesn't already enforce automatically (heading tag levels, disabled-state behavior, skip-to-content, and similar — not color contrast or text size if those are already handled in the Figma design).

5. **Apply the special-content rules** from the reference file wherever relevant:
   - Lists with pagination, horizontal scroll, or carousels — spec the responsive and accessible behavior of the paging mechanism explicitly, not just the content it paginates.
   - Dates/times — include the human-readable conversion logic with Hebrew examples (e.g. "לפני 3 שעות", "אתמול").

6. **No appendices.** Every note belongs inside the Part 1 or Part 2 table it's relevant to. A note parked at the end of the document leaves the developer guessing which element it applies to — fold it into the right row instead.

## Output

A single document with both parts, in Markdown, using tables, with the Figma screenshot/reference for each row inlined where the instructions call for it (Part 2's last column). If a given task calls for a Word version instead, that's fine too — keep the same structure and rules.
