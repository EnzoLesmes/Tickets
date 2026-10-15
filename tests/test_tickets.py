import re

import pytest
from fastapi.testclient import TestClient

from backend.main import app
from backend.repositories.ticket_repository import clear_tickets

client = TestClient(app)


@pytest.fixture(autouse=True)
def reset_tickets():
    clear_tickets()


def test_create_ticket_returns_complete_ticket():
    response = client.post(
        "/api/tickets",
        json={
            "title": "  No puedo acceder al sistema  ",
            "description": "  El sistema rechaza mi contraseña.  ",
        },
    )

    assert response.status_code == 201
    assert response.json() == {
        "id": 1,
        "title": "No puedo acceder al sistema",
        "description": "El sistema rechaza mi contraseña.",
        "status": "open",
        "assignee": None,
        "created_at": response.json()["created_at"],
        "updated_at": response.json()["created_at"],
    }


def test_create_ticket_timestamps_are_utc_iso_strings_without_microseconds():
    response = client.post(
        "/api/tickets",
        json={"title": "Título", "description": "Descripción"},
    )

    timestamp = response.json()["created_at"]
    assert response.json()["updated_at"] == timestamp
    assert re.fullmatch(
        r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z", timestamp
    )


def test_create_ticket_ids_increment():
    first_response = client.post(
        "/api/tickets",
        json={"title": "Primero", "description": "Descripción"},
    )
    second_response = client.post(
        "/api/tickets",
        json={"title": "Segundo", "description": "Descripción"},
    )

    assert second_response.json()["id"] == first_response.json()["id"] + 1


def test_create_ticket_with_empty_title_returns_bad_request():
    response = client.post(
        "/api/tickets",
        json={"title": "", "description": "Descripción"},
    )

    assert response.status_code == 400
    assert response.json() == {"detail": "El título no puede estar vacío."}


def test_create_ticket_with_blank_description_returns_bad_request():
    response = client.post(
        "/api/tickets",
        json={"title": "Título", "description": "   "},
    )

    assert response.status_code == 400
    assert response.json() == {"detail": "La descripción no puede estar vacía."}


def test_create_ticket_without_body_returns_unprocessable_entity():
    response = client.post("/api/tickets")

    assert response.status_code == 422
    assert isinstance(response.json()["detail"], list)


def test_create_ticket_with_missing_field_returns_unprocessable_entity():
    response = client.post(
        "/api/tickets",
        json={"title": "Título"},
    )

    assert response.status_code == 422
    assert isinstance(response.json()["detail"], list)


def test_create_ticket_with_invalid_type_returns_unprocessable_entity():
    response = client.post(
        "/api/tickets",
        json={"title": 123, "description": "Descripción"},
    )

    assert response.status_code == 422
    assert isinstance(response.json()["detail"], list)
