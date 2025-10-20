Minimal Flask scaffold.

- App entrypoint: `wsgi.py`
- App factory: `app.create_app()`
- Routes: `app/routes/main.py`
- Templates: `app/templates/`
- Static files: `app/static/`

Local setup:

- Create `.env` if you need local secrets (gitignored).
- Create `.flaskenv` for Flask CLI (gitignored). Example:
	- FLASK_APP=wsgi:app
	- FLASK_ENV=development
- A local virtual environment folder like `.venv/` is gitignored.