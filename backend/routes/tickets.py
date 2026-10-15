"""HTTP route signatures for the ticket system."""

from fastapi import APIRouter

from backend.schemas import TicketCreate, TicketResponse
from backend.services.ticket_service import create_ticket as create_ticket_service

router = APIRouter()


@router.post("/tickets", response_model=TicketResponse, status_code=201)
def create_ticket(ticket: TicketCreate) -> dict[str, object]:
    return create_ticket_service(ticket.title, ticket.description)


def list_tickets() -> list[dict[str, object]]:
    raise NotImplementedError


def change_ticket_status(ticket_id: int, status: str) -> dict[str, object]:
    raise NotImplementedError


def assign_ticket(ticket_id: int, user_id: int | None) -> dict[str, object]:
    raise NotImplementedError


def generate_suggestion(ticket_id: int) -> dict[str, object]:
    raise NotImplementedError
