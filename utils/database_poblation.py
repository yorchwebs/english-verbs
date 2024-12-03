from decouple import config

import psycopg2
import json

# Conectar a la base de datos o crearla si no existe
conn = psycopg2.connect(
    database=config("DB_NAME"),
    user=config("DB_USER"),
    password=config("DB_PASSWORD"),
    host=config("DB_HOST"),
)

cur = conn.cursor()

# Crear tabla si no existe
cur.execute(
    """
CREATE TABLE IF NOT EXISTS verbs (
    NUM_ID SERIAL PRIMARY KEY,
    TYPE VARCHAR,
    SIMPLE_FORM VARCHAR,
    THIRD_PERSON VARCHAR,
    SIMPLE_PAST VARCHAR,
    PAST_PARTICIPLE VARCHAR,
    GERUND VARCHAR,
    MEANING VARCHAR
);
"""
)

with open("Verbs.json", "r") as json_file:
    data = json.load(json_file)

for item in data:
    cur.execute(
        """
    INSERT INTO verbs ("TYPE", "SIMPLE_FORM", "THIRD_PERSON", "SIMPLE_PAST", "PAST_PARTICIPLE", "GERUND", "MEANING")
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """,
        (
            item["TYPE"],
            item["SIMPLE_FORM"],
            item["THIRD_PERSON"],
            item["SIMPLE_PAST"],
            item["PAST_PARTICIPLE"],
            item["GERUND"],
            item["MEANING"],
        ),
    )

conn.commit()
conn.close()