"""Request and response schemas for the ticket system."""

from pydantic import BaseModel


class TicketCreate(BaseModel):
    title: str
    description: str


class TicketResponse(BaseModel):
    id: int
    title: str
    description: str
    status: str
    assignee: dict[str, object] | None
    created_at: str
    updated_at: str
