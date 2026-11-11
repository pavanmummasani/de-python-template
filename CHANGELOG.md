# Changelog

All notable changes to this template are listed here. The format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and versions
follow [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

Generated projects receive these changes with `uvx copier update`.

## [Unreleased]

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

[Unreleased]: https://github.com/pavanmummasani/de-python-template/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/pavanmummasani/de-python-template/releases/tag/v0.1.0
