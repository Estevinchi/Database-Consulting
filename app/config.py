from datetime import timedelta
import os

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "contraseña-ejemplo")
    DEBUG = False
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = "Lax"
    PERMANENT_SESSION_LIFETIME = timedelta(hours=1)

class DevConfig(Config):
    DEBUG = True
    SESSION_COOKIE_SECURE = False

class ProdConfig(Config):
    DEBUG = False
    SESSION_COOKIE_SECURE = True

