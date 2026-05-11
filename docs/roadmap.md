---
project: oracle
version: 1
created: 2026-05-11
updated: 2026-05-12
---

# Roadmap

## Completed

### Framework Registry

- **Status:** done
- **Spec:** none
- **Summary:** JSON-based framework metadata with multi-extension and
  execution command support.
- **Blockers:** none
- **Plan:** none

### Intelligence Pipeline

- **Status:** done
- **Spec:** none
- **Summary:** Rule-based test classifier plus engineering framework
  recommender.
- **Blockers:** none
- **Plan:** none

### LLM Abstraction

- **Status:** done
- **Spec:** none
- **Summary:** Provider-agnostic factory (OpenAI, Mock) with lazy loading
  and thread-safe singleton client.
- **Blockers:** none
- **Plan:** none

### CLI Interface

- **Status:** done
- **Spec:** none
- **Summary:** `oracle generate` (with `--run`, `--json`,
  `--recommend-only`), `oracle run`, `oracle init`, `oracle version`.
- **Blockers:** none
- **Plan:** none

### Execution Feedback Loop

- **Status:** done
- **Spec:** none
- **Summary:** MVP self-healing with one retry attempt fed by execution
  error output.
- **Blockers:** none
- **Plan:** none

### Harness Integration

- **Status:** done
- **Spec:** none
- **Summary:** Full adoption of Bombshell engineering constraints and
  harness layer rules.
- **Blockers:** none
- **Plan:** none

### Oracle Init Scaffolding

- **Status:** done
- **Spec:** none
- **Summary:** TICKET-037 — `oracle init` command bootstraps
  Playwright/Vitest/Pytest/k6 suites.
- **Blockers:** none
- **Plan:** none

### Quality Gates

- **Status:** done
- **Spec:** none
- **Summary:** Passing security scans, architectural enforcement, and
  mechanical validation in CI.
- **Blockers:** none
- **Plan:** none

### Classifier Registry Contract

- **Status:** done
- **Spec:** none
- **Summary:** Enforce that every classifier `test_type` resolves to a
  registry framework; pytest now covers `api`. Merged in PR #1.
- **Blockers:** none
- **Plan:** none

## Provider Platform

### Multi-Provider LLM Support

- **Status:** in-progress
- **Spec:** none
- **Summary:** Bring Oracle's LLM provider matrix to parity with the
  harness toolchain. Add first-class providers for Claude (Anthropic)
  and Gemini (Google) alongside the existing OpenAI and Mock backends,
  plus a Codex provider to match the harness `codex` integration.
  Switch the default provider from OpenAI to Claude. Provider selection
  remains driven by `ORACLE_LLM_PROVIDER`. This is a prerequisite for
  the Project Intelligence work because context-aware prompts will
  exceed OpenAI free-tier context windows.
- **Blockers:** none
- **Plan:** none

## Project Intelligence

### Metadata Scanning

- **Status:** planned
- **Spec:** none
- **Summary:** TICKET-029 — detect local `package.json`, `tsconfig.json`,
  `requirements.txt` and align generation with project-specific library
  versions.
- **Blockers:** none
- **Plan:** none

### Pattern Matching

- **Status:** planned
- **Spec:** none
- **Summary:** TICKET-030 — analyze existing tests and match
  project-specific coding styles, naming, and helpers.
- **Blockers:** none
- **Plan:** none

### Recursive Domain Knowledge

- **Status:** planned
- **Spec:** none
- **Summary:** TICKET-031 — scan project directories to understand
  available components/APIs and inject domain context into prompts.
- **Blockers:** none
- **Plan:** none

## CI/CD and Ecosystem Integration

### GitHub Action

- **Status:** planned
- **Spec:** none
- **Summary:** TICKET-032 — official Oracle GitHub Action that
  auto-generates tests for new features/bug fixes on PR.
- **Blockers:** none
- **Plan:** none

### Standardized Reporting

- **Status:** planned
- **Spec:** none
- **Summary:** TICKET-033 — export execution results to JSON/SARIF for
  Datadog, SonarQube, and similar dashboards.
- **Blockers:** none
- **Plan:** none

### Headless Optimizations

- **Status:** planned
- **Spec:** none
- **Summary:** TICKET-034 — CI-specific execution flags and
  pipeline-friendly log output.
- **Blockers:** none
- **Plan:** none

## Advanced Self-Healing

### Multi-step Debugging

- **Status:** planned
- **Spec:** none
- **Summary:** TICKET-035 — iterative debugging across multiple fix
  attempts; search local code/docs to resolve complex failures.
- **Blockers:** none
- **Plan:** none

### Visual DOM Self-Healing

- **Status:** planned
- **Spec:** none
- **Summary:** TICKET-036 — use visual snapshots or DOM trees to fix
  brittle UI selectors automatically.
- **Blockers:** none
- **Plan:** none

## Developer Experience and Onboarding

### IDE Plugins

- **Status:** backlog
- **Spec:** none
- **Summary:** VS Code and JetBrains plugins exposing Oracle
  generation/execution.
- **Blockers:** none
- **Plan:** none

### Interactive Guided Onboarding

- **Status:** backlog
- **Spec:** none
- **Summary:** First-run guided experience for installing Oracle and
  configuring providers.
- **Blockers:** none
- **Plan:** none

<!-- fork-only:capillary -->
## Fork-Specific (Capillary)

> Items in this milestone live only in the Capillary fork and must never
> be merged upstream. They reference internal systems by name and
> location only — no proprietary content lives in this repo.

### Company Knowledge Integration

- **Status:** planned
- **Spec:** none
- **Summary:** Teach Oracle where to look for Capillary-internal context
  so AI agents can ground generation in company conventions. Stores
  pointers only (Confluence space keys, Jira project keys, internal doc
  URLs, MCP server identifiers) — no proprietary content is committed.
  AI agents retrieve the actual content at runtime via the configured
  MCP servers or authenticated tools.
- **Blockers:** none
- **Plan:** none

## Optum Test Ecosystem Integration (Capillary fork)

> Absorbs four Optum testing repos into Oracle as first-class skills so
> SDETs and manual testers can converse with `capillary-oracle` (and the
> upstream harness via Oracle reference) to find users, plan tests,
> execute them, and explore edges. Repos are referenced by path/URL —
> source is not vendored into this repo.
>
> **Source repos (pointers, not vendored):**
>
> - `optum/test-login-helper` — browser extension (background, popup,
>   content, shared, lib) that automates Optum login flows
> - `optum/optum-testing-api-library` — TypeScript API client/Managers
>   used by Playwright API suites; consumed via npm
> - `optum/optum-testing-user-library` — TypeScript test-user catalog
>   and helpers (per-env preconfigured users)
> - `optum/optum-testing-ui-library` — shared UI test components/helpers
>   for Playwright E2E
>
> **Personas served:** (1) SDET in an IDE/CLI extending an existing
> Playwright/API suite; (2) manual tester in a browser via LLM
> extension on `*.optumengage.com` with no IDE. Oracle infers persona
> from working dir, open tabs, and recent chat history (see
> `agent/core/orchestrator.py` context-gathering seam).

### Skill: optum-test-login-helper

- **Status:** planned
- **Spec:** none
- **Summary:** Wrap `test-login-helper` extension as an Oracle skill.
  Manual flow: detect Optum login page, call the extension to log in as
  a chosen user, return cookies/session for downstream steps. SDET
  flow: surface as a Playwright fixture/codegen helper. Skill metadata
  lists supported envs (stage, prod, etc.) and required permissions.
- **Blockers:** Company Knowledge Integration (env→base-URL mapping)
- **Plan:** none

### Skill: optum-test-user-catalog

- **Status:** planned
- **Spec:** none
- **Summary:** Wrap `optum-testing-user-library` as a queryable user
  catalog skill. Inputs: environment (inferred from active tab URL,
  `.env`, or repo config), domain (challenges, nudges, missions, …),
  required attributes (employerId, childId, biometrics-eligible, …).
  Outputs: candidate users with name, email, employer, employerId,
  childId, plus any UI/dev-handoff fields. Prefers a "common user"
  unless the test demands specifics. Flags gaps where preconfigured
  pools are incomplete and proposes filling them (see *Test Data
  Provisioning* below).
- **Blockers:** none
- **Plan:** none

### Skill: optum-api-library-bridge

- **Status:** planned
- **Spec:** none
- **Summary:** Expose `optum-testing-api-library` Managers/endpoints to
  Oracle's recommender so generated API tests (Playwright API context
  or Postman) call the canonical client instead of reinventing
  requests. Registry entry maps `test_type=api & domain=optum/*` to
  this library's calling convention.
- **Blockers:** Classifier↔registry contract (already enforced)
- **Plan:** none

### Skill: optum-ui-library-bridge

- **Status:** planned
- **Spec:** none
- **Summary:** Expose `optum-testing-ui-library` page objects/helpers to
  Oracle's UI generator so generated Playwright E2E tests compose the
  shared selectors/components instead of one-off locators.
- **Blockers:** none
- **Plan:** none

### Context-Aware Persona & Environment Detection

- **Status:** planned
- **Spec:** none
- **Summary:** Extend orchestrator context gathering to:
  (a) read active browser tab URL when invoked from an LLM browser
  extension; (b) parse `.env`, `playwright.config.*`, and other
  config for `BASE_URL`; (c) inspect cwd, open files, and recent chat
  history for SDET-vs-manual signal. Drives which Optum skills load
  and which user pool is queried.
- **Blockers:** none
- **Plan:** none

### Guided Test Planning & TCM Output

- **Status:** planned
- **Spec:** none
- **Summary:** From a feature description, brainstorm approaches using
  Optum skills + harness knowledge, then emit formatted test cases.
  Capwell-style output: Markdown files for AI-friendly TCM. Optum
  output: same Markdown plus a lightweight UI/preview so non-technical
  testers aren't overwhelmed. Core (Capillary) output: Markdown
  fallback until a TCM is identified.
- **Blockers:** Company Knowledge Integration
- **Plan:** none

### Test Run & Regression Compilation

- **Status:** planned
- **Spec:** none
- **Summary:** `oracle run` extensions to filter by domain and platform,
  execute automated suites, or compile a manual run-sheet (with test
  user info inlined, common user by default). Post-run: summarize
  results and offer next actions — file a bug ticket, start debugging,
  or open the failing test in the IDE.
- **Blockers:** Standardized Reporting (JSON/SARIF emitter)
- **Plan:** none

### Preconditions & Test Data Provisioning

- **Status:** planned
- **Spec:** none
- **Summary:** When a chosen user/test needs setup (mission check-in,
  enable biometrics, create private challenge, config flip), Oracle
  states the preconditions and either performs them via available
  skills or hands the user a checklist and waits. Stretch goal:
  programmatic test-data spin-up (new users, fresh state) — at minimum
  capture as a follow-up improvement on each test.
- **Blockers:** Company Knowledge Integration (locate the
  config-toggle tool referenced in the knowledge graph)
- **Plan:** none

### Exploratory Edge-Case Suggestions

- **Status:** planned
- **Spec:** none
- **Summary:** After test planning, propose super-edge cases (boundary
  data, race conditions, locale/timezone, accessibility, partial
  network) for exploratory sessions. Tailor depth to the user's
  coding/automation level — explain the *why* so manual testers learn
  alongside SDETs.
- **Blockers:** none
- **Plan:** none

### Pedagogical Reasoning Mode

- **Status:** planned
- **Spec:** none
- **Summary:** Track user skill signal (manual vs SDET, languages
  observed) and annotate Oracle's choices with reasoning — why a
  particular user was chosen, why an API test fits better than UI,
  what the recommender weighted. Off by default for senior SDETs,
  auto-on for first-time/manual testers.
- **Blockers:** none
- **Plan:** none
<!-- /fork-only -->
