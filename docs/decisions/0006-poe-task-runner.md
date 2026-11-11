# 0006: poe as the task runner

**Status:** Accepted

**Context:** The guide expects a task runner (`sp-repo-review` check
`PY007`). nox builds its own virtual environments, which duplicates uv.

**Decision:** Define `[tool.poe.tasks]` in `pyproject.toml`: `lint`,
`types`, `test`, `review`, and `check`, which runs all four in the same
order as CI. Tasks run inside the uv environment (`uv run poe <task>`).

**Consequence:** One local command matches CI. poethepoet is a locked dev
dependency.
