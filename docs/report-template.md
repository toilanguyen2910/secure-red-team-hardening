# Security review report template

## Scope and authorization

- Project / revision:
- Owner and explicit authorization:
- Test environment and allowed methods:
- Out-of-scope assets:
- Baseline test command and result:

## Executive summary

Write 2–4 sentences on confirmed risk, fixes, and what remains unverified. Never equate a clean scan with proof of security.

## Findings

| ID | Severity | Status | Location | Evidence | Impact | Fix |
| --- | --- | --- | --- | --- | --- | --- |
| F-001 | High / Medium / Low | Confirmed / Suspected / Fixed | File and line | Harmless local reproduction | Concrete consequence | Change and test |

For each confirmed issue, record prerequisites, safe reproduction inputs, affected trust boundary, before/after behavior, and limitations. Remove tokens and personal data from all evidence.

## Changes

- Files and rationale:
- Compatibility or migration considerations:
- Controls added:

## Verification

| Check | Command or method | Result |
| --- | --- | --- |
| Focused regression |  | Pass / Fail / Not run |
| Existing test suite |  | Pass / Fail / Not run |
| Static/dependency review |  | Pass / Fail / Not run |

## Residual risk and next steps

- Open questions:
- Deferred fixes and owner:
- Production rollout / monitoring plan (if authorized):

Clearly distinguish observed evidence from inference.
