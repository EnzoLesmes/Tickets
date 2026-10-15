"""Ticket business operations and ticket and user existence validation."""

from backend.repositories.ticket_repository import create_ticket as save_ticket

FIXED_USERS: list[dict[str, object]] = [
    {"id": 1, "name": "Juan Pérez"},
    {"id": 2, "name": "Ana García"},
]


class TicketValidationError(Exception):
    """Raised when ticket data violates a business rule."""


def create_ticket(title: str, description: str) -> dict[str, object]:
    clean_title = title.strip()
    clean_description = description.strip()

    if not clean_title:
        raise TicketValidationError("El título no puede estar vacío.")
    if not clean_description:
        raise TicketValidationError("La descripción no puede estar vacía.")

    return save_ticket(clean_title, clean_description)


def list_tickets() -> list[dict[str, object]]:
    raise NotImplementedError


def change_ticket_status(ticket_id: int, status: str) -> dict[str, object]:
    raise NotImplementedError


def assign_ticket(ticket_id: int, user_id: int | None) -> dict[str, object]:
    raise NotImplementedError


def list_users() -> list[dict[str, object]]:
    return [dict(user) for user in FIXED_USERS]


def get_ticket_for_suggestion(ticket_id: int) -> dict[str, object]:
    raise NotImplementedError
