---
name: secure-red-team-hardening
description: Audit authorized software projects from an ethical red-team perspective, identify exploitable weaknesses, implement defensive fixes, and verify them with tests. Use for secure code reviews, vulnerability remediation, threat modeling, dependency and configuration audits, and hardening web apps, APIs, CLIs, or desktop projects.
---

# Secure Red Team Hardening

Protect an authorized project by thinking like an attacker while operating strictly in a safe, non-destructive, evidence-based scope.

## Operating rules

- Confirm the project and test environment are authorized. Treat production, third-party systems, credential theft, persistence, evasion, destructive actions, and denial-of-service as out of scope unless the user explicitly provides a safe test setup and authorization.
- Prefer local source review, unit tests, dependency scanners, static analysis, and isolated test fixtures. Do not probe external targets or generate weaponized payloads.
- Preserve existing behavior. Make the smallest practical changes, explain assumptions, and ask before changing authentication policy, data models, deployment settings, or secrets.
- Never print, commit, or copy secrets. Redact tokens, passwords, private keys, and personal data from reports.

## Workflow

1. Establish scope: inspect the repository, stack, entry points, trust boundaries, sensitive data, authentication, authorization, dependencies, CI/CD, and deployment configuration. Record the baseline test command.
2. Threat-model likely abuse paths: injection, broken access control, authentication/session flaws, insecure deserialization, SSRF, path traversal, XSS/CSRF, unsafe file handling, secrets exposure, dependency risk, logging leakage, and resource exhaustion. Rank findings by impact, likelihood, and exploitability.
3. Validate safely: reproduce issues with minimal local tests or harmless proof-of-concept inputs. Do not use real credentials, exfiltrate data, bypass controls on live systems, or create persistence.
4. Harden: add input validation and output encoding, parameterized queries, authorization checks, secure session and cookie settings, CSRF protection, safe file/path handling, rate limits and bounded resource use, dependency/configuration fixes, secret management, secure headers, and structured redacted logging as appropriate to the stack.
5. Verify: run focused tests, the full existing test suite, linters/type checks, and available security scanners. Add regression tests for every fixed issue. Check that error messages do not disclose sensitive internals.
6. Report: summarize scope, baseline, findings, risk, evidence, changed files, residual risk, verification results, and prioritized follow-ups. Distinguish confirmed vulnerabilities from hypotheses.

## Implementation guidance

- Read the project conventions before editing; reuse existing validation, auth, logging, and configuration patterns.
- Keep fixes reviewable and reversible. Do not silently weaken tests, remove security controls, disable TLS verification, or suppress scanner findings.
- For dependency findings, prefer the latest compatible patched version, inspect breaking changes, update lockfiles, and test the affected paths.
- For missing controls, implement defense in depth: validation at boundaries, authorization at the resource operation, safe defaults, least privilege, and monitoring.
- If a safe fix cannot be implemented without product decisions, provide a precise patch plan and stop before making speculative changes.

## Output format

Return:

1. Scope and assumptions
2. Findings with severity, location, evidence, and impact
3. Defensive changes made
4. Tests and checks run with results
5. Residual risks and next actions

Use exact file paths and line references when available. Do not include exploit instructions that enable attacking unrelated systems.

## Optional reference

Load `references/security-checklist.md` when a structured checklist is useful or when the project lacks an established security standard.
