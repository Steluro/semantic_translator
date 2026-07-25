from dataclasses import dataclass
from datetime import UTC, datetime
from enum import StrEnum


class TraceEventType(StrEnum):
    DEBUG = "debug"
    INFO = "info"
    WARNING = "warning"
    ERROR = "error"
    CRITICAL = "critical"


@dataclass
class TraceEvent:
    timestamp: datetime
    event_type: TraceEventType
    message: str


class Trace:
    def __init__(self):
        self.events = []

    def debug(self, message: str) -> None:
        self.events.append(TraceEvent(datetime.now(UTC), TraceEventType.DEBUG, message))

    def info(self, message: str) -> None:
        self.events.append(TraceEvent(datetime.now(UTC), TraceEventType.INFO, message))

    def warning(self, message: str) -> None:
        self.events.append(TraceEvent(datetime.now(UTC), TraceEventType.WARNING, message))

    def error(self, message: str) -> None:
        self.events.append(TraceEvent(datetime.now(UTC), TraceEventType.ERROR, message))

    def critical(self, message: str) -> None:
        self.events.append(TraceEvent(datetime.now(UTC), TraceEventType.CRITICAL, message))
