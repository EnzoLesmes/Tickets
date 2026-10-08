# AGENTS.md — Support System

## Project context

A simple support ticket system. Users can create tickets, list them,
change their status, assign them to a user, and get a suggested reply
draft for a ticket. It is a learning project for the "Ingeniería
IA-First" module of a full-stack course. A person always reviews the
suggested reply; it is never sent automatically.

## Tech stack and constraints

Built in stages. Do not work on a later stage until asked.

- **Stage 1 — Backend**: Python 3 + FastAPI.
- **Stage 2 — Database**: PostgreSQL running in Docker. Until this stage,
  keep database access isolated so the database can be swapped without
  touching business logic.
- **Stage 3 — Frontend**: React (with Vite).
- **Suggested replies**: simulated. Do NOT call any external AI API and
  do NOT use API keys. Build it as a separate component with a clear
  interface (for example, a "reply suggester") that returns a draft from
  a template, so it can be replaced by a real AI later without changing
  the rest of the system.
- **No authentication or roles** for now.
- **Do NOT** add any library, framework, ORM, or tool beyond the stack
  above unless explicitly approved. List the library and why before
  adding it to `requirements.txt` or `package.json`.
- Never commit secrets, passwords, or `.env` files. Keep `.env` in
  `.gitignore`.

## Project structure

To be defined after the architecture is reviewed and approved.
Do not create files or folders before that without asking first.

## Agent behavior rules

- Do not invent features that were not requested.
- Do not add libraries or dependencies without explicit approval.
- Do not make architectural decisions silently — ask before assuming.
- Keep the code simple and readable; avoid unnecessary abstractions,
  design patterns, or premature optimization.
- Only implement what is asked for the current stage/step. Do not get
  ahead of the requested scope.
- When asked for a plan or design, do not write code. Give the plan,
  then critique it: risks and weak points.
- Explain the reason for each separation of responsibilities.
- If a request conflicts with this file, point out the conflict instead
  of silently resolving it.
- Do not change existing files that are not related to the current task.

## Architecture principles

- Keep responsibilities separated: HTTP layer, business logic, data
  access, and the reply suggester are different components.
- The HTTP layer does not contain SQL. The business logic does not know
  about HTTP.
- Validation that protects the data lives in the backend, even if the
  frontend also validates.

## Code conventions

- All code — variable names, function names, comments — in **English**.
- User-facing text (messages, labels, errors shown to the user) in
  **Spanish**.
- Python: `snake_case` for variables and functions (PEP 8).
- React: `PascalCase` for components, `camelCase` for variables and
  functions.
- Validate every input from the user before saving it.
- Use specific error types and proper HTTP status codes (201 created,
  400 invalid data, 404 not found, 422 malformed request).
- Prefer plain functions over classes unless there is a clear reason.

## Definition of done (per stage)

A stage is complete when:
- All features for that stage work as intended.
- Invalid input does not crash the app: it returns a clear message.
- Code is organized in the correct place per its responsibility.
- There are tests for the main behavior, and they pass.
- The feature was verified by running it, not just by reading the code.
