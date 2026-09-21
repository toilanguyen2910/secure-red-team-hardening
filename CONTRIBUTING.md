# Contributing

Thanks for helping improve this defensive security skill.

1. Open an issue describing the documentation gap or defensive use case. For a possible vulnerability in this repository, follow [SECURITY.md](SECURITY.md) instead of a public issue.
2. Keep examples local, synthetic, non-destructive, and free of credentials or personal data. Do not add stealth, exfiltration, persistence, bypass, or live-target scanning features.
3. Keep `SKILL.md` focused on instructions for the agent. Put long examples in `examples/` or `docs/`.
4. Run `python -m unittest discover -s tests -v` before proposing a change. Explain the use case, test results, and any limitations in the pull request.
5. Avoid adding dependencies unless necessary; document why and pin them when added.

Maintainers may decline contributions outside the authorized, defensive scope.
