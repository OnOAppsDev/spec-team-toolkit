---
name: lld-backend-spec
description: Use this skill whenever the user wants to write a Low Level Design (LLD) / detailed technical specification for a backend service, API, or data-model change, for handoff to backend developers and QA. Trigger on phrases like "write the backend LLD for X", "spec out this API", "detailed design for this service change", "אפיין את השירות הזה", or whenever someone describes a backend feature (new endpoint, schema change, integration) and wants a structured spec covering the contract, data model, business rules, and edge cases. For web UI components, use `lld-web-figma-spec` instead. For mobile features, use `lld-mobile-spec` instead.
---

# LLD Backend Spec

## What this skill does

Turns a backend feature or change (new/modified API, schema change, service integration) into a single developer/QA-facing specification: exact request/response contracts, data model changes, business rules and edge cases, and non-functional behavior. There is no Figma equivalent here — the source of truth is the HLD (if one exists), any existing API/data-model docs, and the codebase itself, not a visual design.

The structure and section rules are in `references/lld_backend_template.md`. Read it before drafting and follow it closely.

## Workflow

1. **Gather context first, don't invent an API shape from scratch.**
   - Ask for (or read from an uploaded/linked doc) the relevant HLD section or business requirements this LLD is scoping.
   - If a repo/codebase connector is available, use it read-only to find: the existing API style (REST/GraphQL/RPC), naming and versioning conventions, the current data model for entities this feature touches, and error-response conventions already in use. Prefer matching existing conventions over inventing new ones.
   - If no codebase access is available, ask the user for these conventions directly rather than guessing.
   - Ask which of the following are actually in play, since not every feature has all of them: new/changed endpoints, schema/migration changes, dependency on other services, async/event flow.

2. **Classify every endpoint and field before drafting**, same reasoning as the web/mobile LLDs: know whether each request/response field is new, reused from an existing model, or coming from a downstream integration — this determines whether it belongs in the Data Model section, the Endpoint Contract section, or is just referenced as an external dependency.

3. **Draft the Endpoint Contracts** using the table/block format in the reference file: method, path, auth requirement, request schema, response schema (success and error), status codes.

4. **Draft the Data Model section**: new tables/fields/collections, types, constraints, and any migration implications for existing data.

5. **Draft Business Logic & Edge Cases** as explicit rules, not prose paragraphs — validation rules, calculation logic, and the required edge cases: empty/missing input, invalid input, not-found, permission-denied, concurrent-write/race conditions, and partial-failure behavior for any multi-step operation.

6. **Cover the cross-cutting sections** from the template: security & permissions (who can call this, data visibility rules), non-functional notes (rate limits, idempotency, retries, expected latency/throughput if known), backward compatibility (if changing an existing contract), and dependencies on other services.

7. **Mark unknowns honestly.** Don't invent a status code, field name, or business rule that wasn't given or found in the codebase — mark it `TBD` or `Need to verify` and add it to Open Questions.

## Output

A single Markdown document following `references/lld_backend_template.md`, with tables for endpoint contracts and data model fields, and explicit bullet lists for business rules, edge cases, and open questions. If a Word version is requested instead, keep the same structure.
