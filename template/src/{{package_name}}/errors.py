"""Project exception hierarchy.

Catch ``ProjectError`` to handle any error this package raises on purpose.
Add one subclass per failure kind (e.g. ``SourceError``, ``LoadError``).
"""


class ProjectError(Exception):
    """Base class for errors raised by this project."""


class ConfigError(ProjectError):
    """Settings are missing or invalid."""
