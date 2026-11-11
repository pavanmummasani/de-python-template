import pytest


def pytest_sessionfinish(session: pytest.Session, exitstatus: int) -> None:
    """Let `poe test-integration` pass while a project has no integration tests."""
    if (
        exitstatus == pytest.ExitCode.NO_TESTS_COLLECTED
        and session.config.option.markexpr == "integration"
    ):
        session.exitstatus = pytest.ExitCode.OK
