"""HTTP routes for users."""

from fastapi import APIRouter

from backend.services.ticket_service import list_users

router = APIRouter()


@router.get("/users")
def get_users() -> list[dict[str, object]]:
    return list_users()
