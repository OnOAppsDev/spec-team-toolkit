# Backend LLD Template

Use this structure for every backend LLD. Omit a section only by writing `Not required for this feature.` under its heading — never delete the heading.

```md
# LLD: [Feature / Service Change Name]

**Status:** DRAFT
**Author:** [name]
**Reviewer:** TBD
**Last Updated:** [date]
**Related HLD/Requirements:** [link or N/A]
**Service(s) affected:** [service name(s)]
**API style:** [REST / GraphQL / RPC / event-driven]

## 1. Overview

One paragraph: what this change does and why, in plain terms.

## 2. Scope

What's in scope. What's explicitly out of scope for this change.

## 3. Endpoint Contracts

One subsection per endpoint. Not required for schema-only or event-only changes.

### `[METHOD] /path`

- **Auth:** [required role/scope, or "none"]
- **Request:**
  \`\`\`json
  { }
  \`\`\`
- **Response — success ([status code]):**
  \`\`\`json
  { }
  \`\`\`
- **Response — errors:**

| Status | Condition | Body |
|---|---|---|
| 400 | [condition] | [shape] |
| 403 | [condition] | [shape] |
| 404 | [condition] | [shape] |

## 4. Data Model

Table per new or changed entity. Mark whether a field is new, existing, or sourced from another service.

### `[entity_name]`

| Field | Type | Constraints | New/Existing | Notes |
|---|---|---|---|---|
| [field] | [type] | [required, unique, FK, etc.] | [New/Existing] | [notes] |

Migration implications for existing data (backfill needed, nullable during rollout, etc.), or `None`.

## 5. Business Logic & Edge Cases

Explicit rules, not prose. Must cover, where applicable:

- Empty / missing input
- Invalid input (validation failures)
- Not-found
- Permission-denied
- Concurrent write / race condition behavior
- Partial-failure behavior for any multi-step or multi-service operation

## 6. Dependencies

Other services, queues, external APIs this feature calls or is called by. What happens if a dependency is unavailable.

## 7. Security & Permissions

Who can call each endpoint / trigger this logic. What data is restricted and to whom. Any audit-logging expectations.

## 8. Non-Functional Notes

Rate limits, idempotency requirements, retry behavior, expected latency/throughput if known. Write `Not specified` rather than inventing a number.

## 9. Backward Compatibility

Only if modifying an existing contract: what breaks, what's versioned, deprecation plan if any. Otherwise `N/A — new contract`.

## 10. Project Context Used

Repo(s)/branch inspected, existing conventions followed (naming, error format, auth pattern), and which HLD/requirements doc this was scoped from.

## 11. Assumptions

Every judgment call made without an explicit answer — a default value, an inferred status code, an assumed permission rule — as its own line, marked inline where it applies with `> Assumption: [...]` and listed here.

## 12. Open Questions

Unresolved items that must be confirmed before this LLD can be marked READY.
```

## Rules

- Do not invent field names, status codes, or business rules — mark `TBD` or `Need to verify` and add to Open Questions.
- Prefer matching existing codebase conventions (naming, error shape, auth pattern) over introducing new ones; note the convention source in Project Context Used.
- Every endpoint's error table must cover at least validation failure and not-found/permission-denied where relevant — don't leave error behavior undefined.
- Keep code-scan findings summarized here only as "Project Context Used" — don't paste large code blocks into the LLD.
