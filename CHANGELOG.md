# Changelog

All notable changes to this template are listed here. The format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and versions
follow [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

Generated projects receive these changes with `uvx copier update`.

## [Unreleased]

## [0.2.1] - 2026-11-12

### Fixed

- Push runs on `main` are no longer cancelled by a newer push, so every
  pushed commit gets its secret scan. Only superseded pull request runs are
  cancelled.
- CI fails when the TruffleHog action tag and scanner `version:` differ.
- Generated README has a repository setup section: security features and
  branch protection.
- Decision record 0009 states what fails the secret scan: keys confirmed
  live, or whose live check errored. Keys confirmed dead are not reported.

## [0.2.0] - 2026-11-12

### Added

- TruffleHog secret scan as a separate CI job in generated projects and in
  this repo. See decision record 0009.
- README setup step: turn on GitHub secret scanning and push protection.

## [0.1.2] - 2026-11-12

### Fixed

- `.gitattributes` (`* text=auto eol=lf`) in the template repo and in
  generated projects. On Windows with `core.autocrlf=true`, `copier update`
  produced CRLF files, and the mixed-line-ending hook failed after local edits.
  See decision record 0008.

### Upgrade notes

Only for projects generated on Windows before 0.1.2. From a clean working
tree (commit first), before running `copier update`:

```bash
git config --global core.autocrlf input      # once per Windows machine
git rm --cached -r -q . && git reset --hard  # rewrite working files with LF
uvx copier update --defaults
```

`git reset --hard` discards uncommitted changes, so commit everything first.

## [0.1.1] - 2026-11-11

### Added

- Generated README explains where decision records go.

### Changed

- `.env.example` shows the copy command on its first line.
- pymarkdown allows repeated headings under different parents, so a
  Keep a Changelog file passes.

## [0.1.0] - 2026-11-11

### Added

- Copier template built from scientific-python/cookie, with questions for
  project name, package name, GitHub owner and Python version (3.12 or 3.13).
- Starter package: typed settings from `.env` (pydantic-settings), a
  project exception hierarchy and standard-library logging setup, with tests.
- uv environment with a committed lock file and `.python-version`.
- poe tasks `lint`, `types`, `test`, `review` and `check`; CI runs `check`.
- Pre-commit hooks: Ruff, mypy strict, detect-secrets, pymarkdown, Vale,
  codespell, schema validation and zizmor.
- Coverage gate at 80% and sp-repo-review in CI.
- `integration` pytest marker: such tests are skipped by `poe test` and CI
  and run with `poe test-integration`.
- Dependabot for GitHub Actions, pre-commit hooks and uv.
- Template self-test workflow for each Python version.
- Decision records 0001 to 0007.

[Unreleased]: https://github.com/pavanmummasani/de-python-template/compare/v0.2.1...HEAD
[0.2.1]: https://github.com/pavanmummasani/de-python-template/compare/v0.2.0...v0.2.1
[0.2.0]: https://github.com/pavanmummasani/de-python-template/compare/v0.1.2...v0.2.0
[0.1.2]: https://github.com/pavanmummasani/de-python-template/compare/v0.1.1...v0.1.2
[0.1.1]: https://github.com/pavanmummasani/de-python-template/compare/v0.1.0...v0.1.1
[0.1.0]: https://github.com/pavanmummasani/de-python-template/releases/tag/v0.1.0
