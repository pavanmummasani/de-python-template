"""Typed settings read from environment variables and a local ``.env`` file.

Environment variables win over ``.env``. Field names are case-insensitive,
so ``log_level`` reads ``LOG_LEVEL``. Put secrets in ``SecretStr`` fields so
they never print in logs or tracebacks.

``.env`` is read from the current working directory, so run commands from
the project root. Deployed jobs should set environment variables instead.
"""

from functools import cache
from typing import Annotated, Literal

from pydantic import BeforeValidator, ValidationError
from pydantic_settings import BaseSettings, SettingsConfigDict, SettingsError

from .errors import ConfigError
from .logging_setup import LogLevel


def _upper(value: object) -> object:
    return value.upper() if isinstance(value, str) else value


class Settings(BaseSettings):
    """Project settings. Mirror every field in ``.env.example``."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    app_env: Literal["dev", "prod"] = "dev"
    log_level: Annotated[LogLevel, BeforeValidator(_upper)] = "INFO"


@cache
def get_settings() -> Settings:
    """Load settings once per process.

    Raises:
        ConfigError: a value is missing, has the wrong type, or ``.env``
            cannot be parsed.
    """
    try:
        return Settings()
    except (ValidationError, SettingsError, UnicodeDecodeError) as exc:
        msg = "Invalid settings; compare your .env with .env.example"
        raise ConfigError(msg) from exc
