from enum import StrEnum


class IncidentStatus(StrEnum):
    """Статусы Инцидента."""

    TODO = "todo"
    IN_PROGRESS = "in_progress"
    DONE = "done"


class Source(StrEnum):
    """Источник Статусов."""

    OPERATOR = "operator"
    MONITORING = "monitoring"
    PARTNER = "partner"
