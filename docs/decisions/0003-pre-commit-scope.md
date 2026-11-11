# 0003: Pre-commit runs fast checks only

**Status:** Accepted

**Context:** Slow commit hooks get skipped. Cookie also uses prettier
(needs Node.js), shellcheck and rST hooks (no shell or rST files here), and
configures pre-commit.ci, which duplicates our own CI.

**Decision:** Hooks: ruff lint and format, mypy (local hook, locked uv
environment), detect-secrets, plus sub-second hygiene hooks (pre-commit-hooks,
codespell, validate-pyproject, check-jsonschema, zizmor). Tests run in CI
only. Dependabot updates hook revs.

**Consequence:** `sp-repo-review` checks `PC140` (only recognises
mirrors-mypy), `PC170`, `PC180` and `PC901`–`PC903` are ignored, with
reasons in the generated `pyproject.toml`.
