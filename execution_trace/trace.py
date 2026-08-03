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

    def to_json(self) -> dict:
        """Convert trace to JSON-serializable dictionary"""
        trace_data = []
        for event in self.events:
            trace_data.append(
                {
                    "timestamp": event.timestamp.isoformat(),
                    "event_type": event.event_type,
                    "message": event.message,
                }
            )
        return {"trace": trace_data}

    def to_string(self) -> str:
        """Convert trace to human-readable string representation"""
        lines = []
        for event in self.events:
            time_str = event.timestamp.strftime("%H:%M:%S")
            lines.append(f"{time_str} {event.event_type.upper()} - {event.message}")
        return "\n".join(lines)
