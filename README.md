# Minimal Flask scaffold

[![CI](https://github.com/johndavidbustard/CSC4008_2526_Estates_2/actions/workflows/ci.yml/badge.svg)](https://github.com/johndavidbustard/CSC4008_2526_Estates_2/actions/workflows/ci.yml)

- App entrypoint: `wsgi.py`
- App factory: `app.create_app()`
- Routes: `app/routes/main.py`
- Templates: `app/templates/`
- Static files: `app/static/`

## Quick start

- Install dependencies:
  - `pip install -r requirements.txt`
- Run the app:
  - `python -m flask run`

For full developer setup, see [CONTRIBUTING.md](CONTRIBUTING.md).

## Local setup

- Optional local config: use `.env` for secrets and `.flaskenv` for Flask CLI (both are gitignored). Example:
	- FLASK_APP=wsgi:app
	- FLASK_DEBUG=1
- A local virtual environment folder like `.venv/` is gitignored.

## Quality checks

- Linting/formatting and tests are documented in [CONTRIBUTING.md](CONTRIBUTING.md).
