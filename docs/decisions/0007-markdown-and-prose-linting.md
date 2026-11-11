# 0007: Lint Markdown structure and prose

**Status:** Accepted

**Context:** Ruff and mypy check code only. READMEs and decision records
are read by reviewers first, and nothing checked them beyond spelling.
Cookie's markdown formatter, prettier, needs Node.js (record 0003).

**Decision:** Add two Python-installable pre-commit hooks, in the template
and in this repo: pymarkdown for Markdown structure (line length rule
`MD013` off, since tables and links run long), and Vale with a small
`Slop` style that rejects buzzwords, filler phrases and em dashes.
This repo reuses the template's Vale rules (`StylesPath`), so there is one
copy.

**Consequence:** Prose that fails a rule blocks the commit. To change what
counts as slop, edit `template/.vale/styles/Slop/`.
