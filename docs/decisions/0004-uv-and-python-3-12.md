# 0004: uv with a lock file; Python 3.12 by default

**Status:** Accepted

**Context:** CI and every developer machine must install identical
versions. Projects also run on Databricks serverless and next to dbt.

**Decision:** Use uv with `.python-version` and a committed `uv.lock`; CI
runs `uv sync --locked`. Default to Python 3.12 (offer 3.13). Dev tools
(mypy, poe, pre-commit, pytest, sp-repo-review) are locked in the `dev`
group. Ruff is not: it runs only from its pinned pre-commit hook, so there
is one Ruff version. The template does not ship `uv.lock`; the user runs
`uv lock` once after generation (no Copier `_tasks`, so `--trust` is never
needed).

**Consequence:** Dependabot keeps `uv.lock` and the hook revs current. For
ad hoc Ruff use, run `uvx ruff`.
