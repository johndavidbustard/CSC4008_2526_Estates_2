from app import create_app

app = create_app()

# Expose the WSGI callable for servers and development tools
# For example: gunicorn wsgi:app
+
