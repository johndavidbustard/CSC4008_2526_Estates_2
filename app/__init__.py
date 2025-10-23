import os
from flask import Flask, render_template


def create_app(test_config: dict | None = None) -> Flask:
    """Create and configure the Flask app."""
    app = Flask(__name__, instance_relative_config=True)

    # Load environment-based settings
    from .config import DevelopmentConfig, ProductionConfig, TestingConfig

    env = os.getenv("FLASK_ENV") or os.getenv("APP_ENV") or "production"
    if test_config is not None and test_config.get("TESTING"):
        app.config.from_object(TestingConfig)
    elif str(env).lower().startswith("dev"):
        app.config.from_object(DevelopmentConfig)
    else:
        app.config.from_object(ProductionConfig)

    # Allow instance config or explicit overrides
    if test_config is None:
        app.config.from_pyfile("config.py", silent=True)
    else:
        app.config.update(test_config)

    from .routes.main import bp as main_bp

    app.register_blueprint(main_bp)

    @app.get("/healthz")
    def healthz():
        return {"status": "ok"}

    # Error pages
    @app.errorhandler(404)
    def not_found(_):
        return render_template("errors/404.html"), 404

    @app.errorhandler(500)
    def server_error(_):
        return render_template("errors/500.html"), 500

    return app
