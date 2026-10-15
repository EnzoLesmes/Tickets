"""In-memory persistence interface for ticket data."""

from copy import deepcopy
from datetime import datetime, timezone

_tickets: list[dict[str, object]] = []
_next_ticket_id = 1


def create_ticket(title: str, description: str) -> dict[str, object]:
    global _next_ticket_id

    timestamp = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
    timestamp = timestamp.replace("+00:00", "Z")
    ticket = {
        "id": _next_ticket_id,
        "title": title,
        "description": description,
        "status": "open",
        "assignee": None,
        "created_at": timestamp,
        "updated_at": timestamp,
    }
    _tickets.append(ticket)
    _next_ticket_id += 1
    return deepcopy(ticket)


def clear_tickets() -> None:
    global _next_ticket_id

    _tickets.clear()
    _next_ticket_id = 1


def list_tickets() -> list[dict[str, object]]:
    return deepcopy(_tickets)


def get_ticket(ticket_id: int) -> dict[str, object] | None:
    raise NotImplementedError


def update_ticket_status(ticket_id: int, status: str) -> dict[str, object]:
    raise NotImplementedError


def update_ticket_assignee(
    ticket_id: int, user_id: int | None
) -> dict[str, object]:
    raise NotImplementedError
