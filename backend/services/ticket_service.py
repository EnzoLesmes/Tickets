"""Ticket business operations and ticket and user existence validation."""

FIXED_USERS: list[dict[str, object]] = [
    {"id": 1, "name": "Juan Perez"},
    {"id": 2, "name": "Ana Garcia"},
]


def create_ticket(title: str, description: str) -> dict[str, object]:
    raise NotImplementedError


def list_tickets() -> list[dict[str, object]]:
    raise NotImplementedError


def change_ticket_status(ticket_id: int, status: str) -> dict[str, object]:
    raise NotImplementedError


def assign_ticket(ticket_id: int, user_id: int | None) -> dict[str, object]:
    raise NotImplementedError


def list_users() -> list[dict[str, object]]:
    raise NotImplementedError


def get_ticket_for_suggestion(ticket_id: int) -> dict[str, object]:
    raise NotImplementedError
