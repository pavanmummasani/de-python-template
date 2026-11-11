# 0005: Generated-project CI on Linux with one Python version

**Status:** Accepted

**Context:** Cookie tests on Linux, Windows and macOS across several Python
versions, which suits libraries. Our projects deploy to Linux runtimes at
one pinned Python version.

**Decision:** A generated project's CI is one job on `ubuntu-latest`, Python
from `.python-version`. No Codecov (it needs a token and an outside
service); coverage `fail_under = 80` fails the test step instead. This
record covers generated projects only. The template's own self-test runs a
matrix over every `python_version` choice, because each choice must render
and pass.

**Consequence:** Code must stay cross-platform by convention (pathlib, no
shell-specific helpers). Add a matrix only if a project ships to more
platforms.
