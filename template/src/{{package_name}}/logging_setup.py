"""Logging setup using the standard library.

Call ``configure_logging()`` once at program start (CLI entry point, job
main). Library code only does ``logger = logging.getLogger(__name__)``.
"""

import logging
from typing import Literal

LogLevel = Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
LOG_FORMAT = "%(asctime)s %(levelname)s %(name)s: %(message)s"


def configure_logging(level: LogLevel = "INFO") -> None:
    """Send log records at ``level`` and above to stderr."""
    logging.basicConfig(level=level, format=LOG_FORMAT, force=True)
