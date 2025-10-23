## Prerequisites

- Python 3.10+
- Git, VS Code (recommended)
- Do not commit secrets: use `.env` and `.flaskenv` locally (both are gitignored)

### Recommended dev tooling

- Pre-commit hooks (lint/format): `pip install pre-commit` then `pre-commit install`
- Pytest for tests: `pip install pytest`

## Local setup

1. Clone the repository and open it.
2. Create a virtual environment and install deps:
	- `pip install -r requirements.txt`
   - Optional dev tools: `pip install -U pre-commit pytest`
3. Create local env files if needed (both are gitignored):
	- `.env` for secrets/config
	- `.flaskenv` for Flask CLI (e.g., `FLASK_APP=wsgi:app`, `FLASK_DEBUG=1`)
4. Run the app:
	- `python -m flask run`

## Linting and formatting

This repo uses pre-commit with Ruff hooks for linting and formatting.

- One-time: `pre-commit install`
- Run on-demand: `pre-commit run --all-files`

CI also runs pre-commit to enforce checks.

## Project structure

- `app/` — Flask app package
  - `routes/` — Blueprints (routes/controllers)
  - `templates/` — Jinja templates
  - `static/` — CSS/JS/assets
- `wsgi.py` — Exposes `app` for WSGI servers and the Flask CLI
- `docs/` — Project documentation
- `tests/` — Testing

## Running tests

- Execute all tests: `pytest -q`
- Add tests in `tests/` following the existing style.
