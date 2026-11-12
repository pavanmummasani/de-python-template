# 0009: Layered secret scanning

**Status:** Accepted (since 0.2.0)

**Context:** detect-secrets runs at commit time, but a commit made with
`--no-verify`, from another machine, or before hooks were installed skips
it. Data projects hold third-party API keys and cloud credentials.

**Decision:** Three layers. detect-secrets in pre-commit (blocks locally).
TruffleHog in CI as its own job, scanning every commit in a push or pull
request with `--results=verified,unknown`: a key confirmed live, or one
whose live check errored, fails the build; keys confirmed dead
(`unverified`) are not reported, which keeps false alarms low. GitHub
secret scanning with push protection rejects known key types at push.
gitleaks is not added: it overlaps with detect-secrets.

**Consequence:** Push runs are never cancelled, so no pushed commit skips
the scan. A guard step fails CI when the action tag and the scanner
`version:` drift apart (Dependabot bumps only the tag). Branch protection
blocks force-pushes to `main`; after a deliberate history rewrite, rerun the
workflow manually. The TruffleHog pre-commit hook is not used because it
needs a separate binary or Docker.
