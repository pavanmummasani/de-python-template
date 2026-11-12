# 0009: Layered secret scanning

**Status:** Accepted (since 0.2.0)

**Context:** detect-secrets runs at commit time, but a commit made with
`--no-verify`, from another machine, or before hooks were installed skips
it. Projects will hold API keys for FRED, Tiingo, Alpha Vantage and cloud
platforms.

**Decision:** Three layers. detect-secrets in pre-commit (blocks locally).
TruffleHog in CI as its own job (scans every commit in a push or pull
request and checks whether a found key is live; verified or unverifiable
results fail the build). GitHub secret scanning with push protection
(rejects known key types at push). gitleaks is not added: it overlaps with
detect-secrets.

**Consequence:** The TruffleHog action tag and its `version:` input must
move together; Dependabot bumps only the tag. The TruffleHog pre-commit hook
is not used because it needs a separate binary or Docker.
