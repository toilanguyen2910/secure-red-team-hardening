# Example audit: local file boundary

This is a synthetic teaching example. It describes no real repository, credentials, or victim data.

## Authorized scope

- Local Python fixture only, using temporary text files.
- No production service, external host, or live user information.

## Finding

| Field | Value |
| --- | --- |
| ID | DEMO-001 |
| Severity | Medium in a hypothetical app; context-dependent |
| Location | A file-reading function accepting a user-controlled relative path |
| Evidence | A local test requests a sibling file via a parent directory component |
| Impact | Without root confinement, the function could read files outside the intended directory |
| Confidence | Illustrative, not a confirmed flaw in an external project |

## Defensive change

[path_safety.py](path_safety.py) resolves the trusted root and candidate file, verifies the resolved candidate stays within the root, and rejects directories. The checks also cover absolute paths and symlinks pointing outside the root.

## Verification

```sh
python -m unittest discover -s tests -v
```

The tests cover allowed reads, parent traversal, absolute external paths, symlink escapes, and directory inputs. They use only synthetic files under a temporary directory.

## Residual risk

This example does not address concurrent file replacement between validation and opening (TOCTOU), multi-user authorization, file-size limits, or sensitive content classification. A production design must handle those separately.
