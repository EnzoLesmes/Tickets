"""FastAPI application entry point."""

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from backend.routes.tickets import router as tickets_router
from backend.routes.users import router as users_router
from backend.services.ticket_service import TicketValidationError

app = FastAPI()


@app.exception_handler(TicketValidationError)
async def handle_ticket_validation_error(
    request: Request, exc: TicketValidationError
) -> JSONResponse:
    return JSONResponse(status_code=400, content={"detail": str(exc)})


app.include_router(tickets_router, prefix="/api")
app.include_router(users_router, prefix="/api")
