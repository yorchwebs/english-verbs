# app/db/database.py
import libsql
from decouple import config


class DatabaseSingleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DatabaseSingleton, cls).__new__(cls)
            cls._instance.init_conn()
        return cls._instance

    def init_conn(self):
        db_path = config("TURSO_DB_FILE", default="english-verbs.db")
        sync_url = config("TURSO_SYNC_URL")
        token = config("TURSO_AUTH_TOKEN")

        self.conn = libsql.connect(db_path, sync_url=sync_url, auth_token=token)
        self.conn.sync()  # Esto sincroniza con Turso

    def get_conn(self):
        return self.conn
