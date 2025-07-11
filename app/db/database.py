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
        sync_url = config("TURSO_SYNC_URL")
        token = config("TURSO_AUTH_TOKEN")
        db_path = config("TURSO_DB_FILE")  # Este puede dejarse como nombre simbólico
        self.conn = libsql.connect(db_path, sync_url=sync_url, auth_token=token)
        self.conn.sync()

    def get_conn(self):
        return self.conn
