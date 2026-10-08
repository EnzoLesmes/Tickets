"""Stable persistence interface for ticket data."""


def create_ticket(title: str, description: str) -> dict[str, object]:
    raise NotImplementedError


def list_tickets() -> list[dict[str, object]]:
    raise NotImplementedError


def get_ticket(ticket_id: int) -> dict[str, object] | None:
    raise NotImplementedError


def update_ticket_status(ticket_id: int, status: str) -> dict[str, object]:
    raise NotImplementedError


def update_ticket_assignee(
    ticket_id: int, user_id: int | None
) -> dict[str, object]:
    raise NotImplementedError
