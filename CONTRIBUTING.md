## Prerequisites

- Python 3.10+
- Git, VS Code (recommended)
- Do not commit secrets: use `.env` and `.flaskenv` locally (both are gitignored)

## Local setup

1. Clone the repository and open it.
2. Create a virtual environment and install deps:
	- `pip install -r requirements.txt`
3. Create local env files if needed (both are gitignored):
	- `.env` for secrets/config
	- `.flaskenv` for Flask CLI (e.g., `FLASK_APP=wsgi:app`, `FLASK_ENV=development`)
4. Run the app:
	- `python -m flask run`

## Project structure 

- `app/` — Flask app package
  - `routes/` — Blueprints (routes/controllers)
  - `templates/` — Jinja templates
  - `static/` — CSS/JS/assets
- `wsgi.py` — Exposes `app` for WSGI servers and the Flask CLI
- `docs/` — Project documentation
- `tests/` — Testing