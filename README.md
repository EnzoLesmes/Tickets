# Sistema de tickets de soporte

Proyecto de práctica del módulo "Ingeniería IA-First": un sistema simple de
tickets de soporte. Permite crear tickets, listarlos, cambiar su estado,
asignarlos a un usuario y generar un borrador de respuesta sugerida.

La respuesta sugerida es simulada (una plantilla): no usa IA real ni claves de
API, y una persona siempre la revisa antes de usarla.

## Estado del proyecto

Se construye por etapas:

1. **Backend** (FastAPI, datos en memoria): en curso.
2. **Base de datos** (PostgreSQL en Docker): pendiente.
3. **Frontend** (React + Vite): pendiente.

Endpoints del contrato (`API_CONTRACT.md`):

| Endpoint | Estado |
|---|---|
| `GET /api/users` | Listo |
| `POST /api/tickets` | Listo |
| `GET /api/tickets` | Pendiente |
| `PATCH /api/tickets/{ticket_id}/status` | Pendiente |
| `PATCH /api/tickets/{ticket_id}/assignee` | Pendiente |
| `POST /api/tickets/{ticket_id}/suggestion` | Pendiente |

## Cómo correrlo

Requiere Python 3.11 o superior. Desde la raíz del repositorio:

    python -m venv venv
    source venv/Scripts/activate      # Git Bash en Windows
    pip install -r backend/requirements.txt
    python -m uvicorn backend.main:app --reload

La API queda en `http://localhost:8000`, y la documentación automática en
`http://localhost:8000/docs`.

## Tests

    python -m pytest

## Estructura

    backend/
      main.py            punto de entrada de FastAPI
      schemas.py         esquemas de entrada y salida de la API
      routes/            capa HTTP: recibe pedidos y responde
      services/          lógica de negocio y validaciones
      repositories/      acceso a los datos
    tests/               pruebas automáticas
    API_CONTRACT.md      contrato de la API (fuente de verdad)
    AGENTS.md            reglas para trabajar con asistentes de IA