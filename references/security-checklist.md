# Defensive security checklist

- Scope and authorization documented
- Secrets absent from source, logs, fixtures, and error responses
- Authentication and session lifecycle protected
- Authorization checked server-side for every sensitive operation
- Inputs validated by type, length, format, and business constraints
- Queries parameterized; templates and output safely encoded
- File paths canonicalized and confined to intended directories
- Uploads constrained by size, type, storage, and execution policy
- CSRF, CORS, cookies, headers, and TLS configured deliberately
- SSRF and outbound network access restricted
- Rate limits, timeouts, pagination, and body-size limits present
- Dependencies pinned and patched; lockfile reviewed
- Logs structured, useful, access-controlled, and redacted
- Security regression tests cover every confirmed finding
- Backups, alerting, and incident response ownership identified
