import os


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "dev")
    TESTING = False
    DEBUG = False


class DevelopmentConfig(Config):
    DEBUG = True
    TEMPLATES_AUTO_RELOAD = True


class ProductionConfig(Config):
    DEBUG = False


class TestingConfig(Config):
    TESTING = True
    DEBUG = False