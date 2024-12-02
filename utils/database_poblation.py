import sqlite3
import json

# Conectar a la base de datos o crearla si no existe
conn = sqlite3.connect("app.db")

# Crear tabla si no existe
conn.execute(
    """
CREATE TABLE IF NOT EXISTS Verbs (
    NUM INTEGER PRIMARY KEY AUTOINCREMENT,
    TYPE TEXT,
    SIMPLE_FORM TEXT,
    THIRD_PERSON TEXT,
    SIMPLE_PAST TEXT,
    PAST_PARTICIPLE TEXT,
    GERUND TEXT,
    MEANING TEXT
);
"""
)

with open("Verbs.json", "r") as json_file:
    data = json.load(json_file)

for item in data:
    conn.execute(
        """
    INSERT INTO Verbs (NUM, TYPE, SIMPLE_FORM, THIRD_PERSON, SIMPLE_PAST, PAST_PARTICIPLE, GERUND, MEANING) 
    VALUES (?, ?, ?, ?, ?, ?, ?, ?);""",
        (
            item["ID"],
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
