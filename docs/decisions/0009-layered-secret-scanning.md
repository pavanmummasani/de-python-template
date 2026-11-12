# 0009: Layered secret scanning

**Status:** Accepted (since 0.2.0; scan moved to `secrets.yml` in 0.2.2)

**Context:** detect-secrets runs at commit time, but a commit made with
`--no-verify`, from another machine, or before hooks were installed skips
it. Data projects hold third-party API keys and cloud credentials.

**Decision:** Three layers. detect-secrets in pre-commit (blocks locally).
TruffleHog in its own workflow, `secrets.yml`, scanning every commit in a
push or pull request with `--results=verified,unknown`: a key confirmed
live, or one whose live check errored, fails the build; keys that fail the
live check are not reported, which keeps false alarms low. GitHub secret
scanning with push protection rejects known key types at push. gitleaks is
not added: it overlaps with detect-secrets.

**Consequence:** In `secrets.yml`, each push has its own concurrency group
(keyed by commit), so no push scan is cancelled or dropped; a newer commit
on a pull request cancels the older PR scan, which the new run covers. The action tag and the scanner
`version:` input are pinned to the same release; Dependabot bumps only the
tag, so its pull request must also update `version:`. Branch protection
blocks force-pushes to `main`; after a deliberate history rewrite, start a
new run with "Run workflow" (re-running the old run reuses the missing
commit). The TruffleHog pre-commit hook is not used because it needs a
separate binary or Docker.
