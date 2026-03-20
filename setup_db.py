import sqlite3
from pathlib import Path

from app import create_app

app = create_app()
db_path = app.config["DATABASE"]
schema_path = Path(__file__).resolve().parent / "app" / "schema.sql"

connection = sqlite3.connect(db_path)
with open(schema_path) as f:
    connection.executescript(f.read())
connection.close()

print("Database creato con successo in:", db_path)


#sto impazzendo ora mi dice che non ho installato flask e non mi riconosce pip (che ho sempre usato), non riesco a runnare sto file quindi non posso creare istance 
#ne controllare l'app effettiva, per il codice sono abbastanza confident però