# Contrato de la API — Sistema de tickets

Base URL: `/api`
Formato de intercambio: `application/json`

Este documento es la fuente de verdad para implementar el backend.
No agregar endpoints ni campos que no estén acá sin aprobación.

## Formato de errores

Los errores usan el formato estándar de FastAPI:

- Errores que lanza el servicio (400, 404, 500): `{"detail": "Descripción del error."}`
- Errores automáticos de validación (422): `detail` es una lista de objetos
  (`type`, `loc`, `msg`). El frontend debe manejar ambos formatos.

## Reglas generales de códigos HTTP

- **200 OK**: operación exitosa que devuelve un recurso o una lista.
- **201 Created**: se creó un recurso nuevo.
- **422 Unprocessable Entity**: formato o valor inválido (cuerpo mal formado,
  tipos incorrectos, IDs no numéricos, estado fuera de la lista permitida,
  campo obligatorio ausente).
- **400 Bad Request**: solo para reglas de negocio que valida el servicio
  (por ejemplo, título o descripción vacíos después de quitar espacios).
- **404 Not Found**: el ticket o el usuario solicitado no existe.
- **500 Internal Server Error**: fallo inesperado, con el mismo formato.
- La verificación de existencia de ticket y usuario pertenece al servicio,
  no a FastAPI.

## Reglas de implementación

- No usar `min_length` en los esquemas de título y descripción. Todo texto
  vacío o de solo espacios debe rechazarse desde el servicio con 400, para
  que el cliente vea un solo error para el mismo problema.
- En la asignación, `user_id` es obligatorio pero acepta `null`. Omitir el
  campo da 422. Enviar `null` significa quitar la asignación.
- Los estados permitidos son `open`, `in_progress`, `resolved` y `closed`,
  con transiciones libres.
- Los tickets nacen sin asignar y en estado `open`.
- Los IDs son enteros.
- La lista de usuarios es fija y vive en el código del backend por ahora.

## Endpoints

### Crear ticket

`POST /api/tickets`

Cuerpo:

```json
{
  "title": "No puedo acceder al sistema",
  "description": "El sistema rechaza mi contraseña."
}
```

Respuesta `201 Created`:

```json
{
  "id": 1,
  "title": "No puedo acceder al sistema",
  "description": "El sistema rechaza mi contraseña.",
  "status": "open",
  "assignee": null,
  "created_at": "2026-10-08T14:30:00Z",
  "updated_at": "2026-10-08T14:30:00Z"
}
```

Errores:
- 422: cuerpo ausente, campos faltantes, tipos incorrectos o formato inválido.
- 400: `title` o `description` quedan vacíos después de quitar los espacios.

### Listar tickets

`GET /api/tickets`

Sin cuerpo. Respuesta `200 OK`: lista de tickets con el mismo formato de
arriba. Si no hay tickets, devuelve `[]`.

Errores:
- 500: fallo inesperado del repositorio.

### Cambiar el estado

`PATCH /api/tickets/{ticket_id}/status`

Cuerpo:

```json
{
  "status": "in_progress"
}
```

Respuesta `200 OK`: el ticket actualizado.

Errores:
- 422: `ticket_id` no numérico, cuerpo mal formado, `status` ausente o
  estado fuera de la lista permitida.
- 404: ticket inexistente.
- 500: fallo inesperado del repositorio.

### Asignar ticket

`PATCH /api/tickets/{ticket_id}/assignee`

Cuerpo para asignar:

```json
{
  "user_id": 2
}
```

Cuerpo para quitar la asignación:

```json
{
  "user_id": null
}
```

Respuesta `200 OK`: el ticket actualizado, con `assignee` como
`{"id": 2, "name": "Ana García"}` o `null`.

Errores:
- 422: `ticket_id` no numérico, cuerpo mal formado, `user_id` omitido o con
  un tipo inválido. El valor `null` es válido.
- 404: ticket inexistente, o `user_id` distinto de `null` que no existe.
- 500: fallo inesperado del repositorio.

### Listar usuarios asignables

`GET /api/users`

Sin cuerpo. Respuesta `200 OK`:

```json
[
  { "id": 1, "name": "Juan Pérez" },
  { "id": 2, "name": "Ana García" }
]
```

Errores:
- 500: fallo inesperado al cargar los usuarios.

No hay creación, edición ni eliminación de usuarios.

### Generar sugerencia de respuesta

`POST /api/tickets/{ticket_id}/suggestion`

Sin cuerpo. Respuesta `200 OK`:

```json
{
  "ticket_id": 1,
  "draft": "Hola. Recibimos tu solicitud sobre No puedo acceder al sistema. Estamos revisando el problema y te daremos una respuesta pronto.",
  "generated_at": "2026-10-08T15:10:00Z"
}
```

Reglas:
- Usa un saludo genérico: la respuesta va dirigida a quien creó el ticket,
  no a la persona asignada, y debe funcionar con tickets sin asignar.
- Se genera bajo demanda, no se persiste y no cambia el ticket.
- Es un borrador simulado (plantilla). No llama a APIs externas ni usa
  claves.
- No incluye ninguna operación de envío: lo revisa una persona.

Errores:
- 422: `ticket_id` no numérico.
- 404: ticket inexistente.
- 500: fallo inesperado del generador o del repositorio.
