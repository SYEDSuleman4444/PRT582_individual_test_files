# Security Review Checklist

**Scope:** local authorised coursework copy only.  
**Date/environment/tool versions:** record after performing checks.

| ID | Check | Safe method | Result/evidence |
|---|---|---|---|
| SEC-01 | Weak-password policy | Use disposable test account and verify server-side rejection | Not run |
| SEC-02 | Booking history access control | Request private booking-history URL while signed out | Not run |
| SEC-03 | Search input handling | Try benign SQL-like text and harmless HTML/script text in local search; check that it is treated as input and not executed | Not run |
| SEC-04 | Brute-force protections | Review rate limits/lockout configuration; avoid high-volume attempts | Not run |
| SEC-05 | Debug configuration | Inspect settings and deployment checks; do not publish debug tracebacks | Not run |
| SEC-06 | Security headers/cookies | Inspect local response headers; evaluate in HTTPS deployment context | Not run |
| SEC-07 | Dependency support | Record framework versions and check for supported upgrade path | Not run |
| SEC-08 | Secrets in source control | Search repository for accidental credentials; never paste secret values into report/issues | Not run |

## Static analysis with Bandit
Run against Python source files and review findings manually:
```bash
bandit -r path/to/application -f txt -o bandit-results.txt
```
Do not include `.venv`, generated files or third-party packages. Keep the full output as local evidence if it contains sensitive paths; publish a sanitised report only.
