# app/__init__.py

from flask import Flask

from app.db.database import DatabaseSingleton
from app.index.views import index_bp

db_singleton = DatabaseSingleton()


def create_app(config_class):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Blueprints
    app.register_blueprint(index_bp)

    # Sincronizar la base con Turso (solo la primera vez que se conecte)
    with app.app_context():
        conn = db_singleton.get_conn()
        conn.sync()  # Puedes omitir si ya se hace en el Singleton

    return app
