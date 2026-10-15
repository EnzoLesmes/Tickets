"""FastAPI application entry point."""

from fastapi import FastAPI

from backend.routes.users import router as users_router

app = FastAPI()
app.include_router(users_router, prefix="/api")
