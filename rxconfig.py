import reflex as rx
import os

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///sqlite.db")

config = rx.Config(
    app_name="todo_app",
    # 1. Redirige el tráfico al puerto que tienes libre
    api_url="http://localhost:8080",
    # 2. Permite que el puerto 3000 hable con el 8080
    cors_allowed_origins=["http://localhost:3000"],
    db_url=DATABASE_URL,
)