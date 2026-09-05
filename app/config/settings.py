import os
from dotenv import load_dotenv

# Cargar variables desde el archivo .env
load_dotenv()

class Settings:
    APP_NAME = os.getenv("APP_NAME", "Sistema de Usuarios")
    APP_VERSION = os.getenv("APP_VERSION", "1.0.0")
    ADMIN_USER = os.getenv("ADMIN_USER", "admin")
    DEBUG = os.getenv("DEBUG", "False").lower() == "true"

settings = Settings()
