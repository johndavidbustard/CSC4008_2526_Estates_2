# Minimal Flask scaffold

[![CI](https://github.com/johndavidbustard/CSC4008_2526_Estates_2/actions/workflows/ci.yml/badge.svg)](https://github.com/johndavidbustard/CSC4008_2526_Estates_2/actions/workflows/ci.yml)

- App entrypoint: `wsgi.py`
- App factory: `app.create_app()`
- Routes: `app/routes/main.py`
- Templates: `app/templates/`
- Static files: `app/static/`

## Local setup

- Create `.env` if you need local secrets (gitignored).
- Create `.flaskenv` for Flask CLI (gitignored). Example:
	- FLASK_APP=wsgi:app
	- FLASK_DEBUG=1
- Install pre-commit and enable hooks:
	- pip install pre-commit
	- pre-commit install
- A local virtual environment folder like `.venv/` is gitignored.

## Quality checks

- Pre-commit (Ruff lint/format): `pre-commit install` (should run automatically)
- Tests: `pytest -q`
