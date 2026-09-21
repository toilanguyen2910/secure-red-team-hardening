# Secure Red Team Hardening

An ethical, evidence-first security skill for reviewing **software you own or are authorized to test**, implementing defensive fixes, and verifying that the fixes hold.

> No stealth, data collection, credential theft, live exploitation, or unauthorized scanning. Findings must be reproducible with harmless local tests and reported transparently.

## What it does

1. Maps entry points, trust boundaries, sensitive data, dependencies, and existing tests.
2. Prioritizes likely weaknesses in access control, injection, sessions, file handling, SSRF, secrets, and configuration.
3. Validates findings with minimal non-destructive local reproductions.
4. Makes reviewable fixes and adds regression tests.
5. Reports evidence, changes, test results, and residual risk.

This is a **workflow skill**, not an autonomous penetration-testing tool or a guarantee that a project is secure.

## Get started

Copy this repository's `SKILL.md`, `agents/`, `references/`, and `assets/` into a skill directory named `secure-red-team-hardening` in an environment that supports SKILL.md-based skills. Then invoke the skill by name with your project:

```text
Use secure-red-team-hardening to review this authorized repository.
Scope: local source and tests only. Identify the three highest-risk confirmed issues,
fix safe ones, add regression tests, and summarize residual risk.
```

Start with a disposable branch and test data. Specify the scope and any production systems that must not be touched. The skill will ask before changes to authentication policy, data models, deployment settings, or secrets.

## Example

The [local path-handling demo](examples/path_safety.py) shows a defensive boundary around a file-reading operation. It is deliberately small, runs without network access, and uses synthetic files only.

```sh
python -m unittest discover -s tests -v
```

See [example audit](examples/example-audit.md) for a sample finding and [report template](docs/report-template.md) for the output format. The [defensive checklist](references/security-checklist.md) is a prompt for review, not a pass/fail certification.

## Repository map

| Path | Purpose |
| --- | --- |
| [SKILL.md](SKILL.md) | Agent workflow and guardrails |
| [agents/openai.yaml](agents/openai.yaml) | Skill interface metadata |
| [references/security-checklist.md](references/security-checklist.md) | Optional review checklist |
| [examples/path_safety.py](examples/path_safety.py) | Safe, runnable defensive example |
| [examples/example-audit.md](examples/example-audit.md) | Synthetic audit walkthrough |
| [docs/report-template.md](docs/report-template.md) | Reusable finding and verification format |
| [tests/](tests/) | Local regression and repository checks |

## Safety and contributions

Test only assets you own or have explicit permission to assess. Never submit real secrets, personal data, stealth features, or exploit payloads. Read [SECURITY.md](SECURITY.md) before reporting a vulnerability and [CONTRIBUTING.md](CONTRIBUTING.md) before opening a change.

## License

No reuse license has been selected yet. Public visibility lets people read the repository; it does **not** automatically grant permission to redistribute or modify it. The owner can add a license after choosing the terms.
