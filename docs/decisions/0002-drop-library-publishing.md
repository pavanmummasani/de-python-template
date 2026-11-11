# 0002: Drop library publishing, docs site and nox

**Status:** Accepted

**Context:** Cookie targets libraries published to PyPI with a hosted docs
site. Data engineering projects are deployed, not published.

**Decision:** Remove the CD workflow (PyPI upload), release notes config,
Read the Docs and Sphinx, nox, pylint (ruff `PL` rules cover it), PyPy, the
`.git_archival.txt` / `.gitattributes` pair and trove classifiers. `docs/`
holds decision records only.

**Consequence:** No package release path. The task runner is poe instead
of nox (record 0006).
