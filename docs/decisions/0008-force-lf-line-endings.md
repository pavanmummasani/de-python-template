# 0008: Force LF line endings

**Status:** Accepted (since 0.1.2)

**Context:** Git on Windows defaults to `core.autocrlf=true`, so Copier,
which reads the template through git, wrote CRLF files. Lines added later
with LF made files mixed, and the `mixed-line-ending` hook failed. Linux CI
never saw the problem.

**Decision:** Add `.gitattributes` with `* text=auto eol=lf` to this repo
and to `template/`, so every checkout and every rendered file uses LF on
every OS. Recommend `core.autocrlf=input` on Windows machines, which also
keeps tags older than 0.1.2 rendering as LF.

**Consequence:** Projects generated on Windows before 0.1.2 need a one-time
rewrite of their working files before updating (see the 0.1.2 entry in
`CHANGELOG.md`).
