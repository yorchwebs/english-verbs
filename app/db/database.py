"""This is my Singleton Class to connect MySQL and Flask with:
peewee, pymysql and python-decouple.
"""

import peewee

from decouple import config


class DatabaseSingleton:
    """Singleton class to connect SQLite and Flask with peewee."""

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.init_db()
        return cls._instance

    def init_db(self):
        """Initialize the database."""
        db_path = "/Users/yorchwebs/Documents/flask/english-verbs/app.db"  # Ruta por defecto
        self.database = peewee.SqliteDatabase(db_path)

    def get_database(self):
        """Return the database instance."""
        return self.database