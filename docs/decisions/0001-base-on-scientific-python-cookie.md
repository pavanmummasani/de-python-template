# 0001: Base the template on scientific-python/cookie

**Status:** Accepted

**Context:** A Python project template needs a well-known, maintained
standard to start from, with a checker that proves conformance.

**Decision:** Start from `scientific-python/cookie` (Copier, `uv_build`
backend) and its development guide. Keep its pytest, mypy, ruff and GitHub
Actions settings unless another record here says otherwise.

**Consequence:** `sp-repo-review` runs in every generated project's CI and
must pass. Each check we turn off is listed in `[tool.repo-review] ignore`
with a record.
