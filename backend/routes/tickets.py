"""HTTP route signatures for the ticket system."""


def create_ticket(title: str, description: str) -> dict[str, object]:
    raise NotImplementedError


def list_tickets() -> list[dict[str, object]]:
    raise NotImplementedError


def change_ticket_status(ticket_id: int, status: str) -> dict[str, object]:
    raise NotImplementedError


def assign_ticket(ticket_id: int, user_id: int | None) -> dict[str, object]:
    raise NotImplementedError


def generate_suggestion(ticket_id: int) -> dict[str, object]:
    raise NotImplementedError
