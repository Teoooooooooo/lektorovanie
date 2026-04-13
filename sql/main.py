import sqlite3

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn

app = FastAPI()
DB_NAME = "database.db"


class PouzivatelCreate(BaseModel):
    meno: str
    vek: int


def get_connection():
    try:
        connection = sqlite3.connect(DB_NAME)
        connection.row_factory = sqlite3.Row
        return connection
    except sqlite3.Error as e:
        raise RuntimeError(f"Nepodarilo sa pripojiť k databáze: {e}") from e


def init_db():
    try:
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS pouzivatelia (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                meno TEXT NOT NULL,
                vek INTEGER NOT NULL
            )
            """
        )

        connection.commit()
        connection.close()
    except sqlite3.Error as e:
        raise RuntimeError(f"Nepodarilo sa vytvoriť tabuľku: {e}") from e


@app.on_event("startup")
def startup_event():
    init_db()


@app.get("/")
def root():
    return {"message": "FastAPI + SQLite funguje"}


@app.post("/pouzivatel")
def vytvor_pouzivatela(pouzivatel: PouzivatelCreate):
    try:
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
            "INSERT INTO pouzivatelia (meno, vek) VALUES (?, ?)",
            (pouzivatel.meno, pouzivatel.vek),
        )

        connection.commit()
        nove_id = int(cursor.lastrowid)
        connection.close()

        return {
            "message": "Používateľ bol pridaný",
            "id": nove_id,
            "meno": pouzivatel.meno,
            "vek": pouzivatel.vek,
        }
    except sqlite3.Error as e:
        raise HTTPException(status_code=500, detail=f"Chyba databázy: {e}") from e


@app.get("/pouzivatel/id/{user_id}")
def ziskaj_pouzivatela(user_id: int):
    try:
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
            "SELECT id, meno, vek FROM pouzivatelia WHERE id = ?",
            (user_id,),
        )
        row = cursor.fetchone()
        connection.close()

        if row is None:
            raise HTTPException(status_code=404, detail="Používateľ neexistuje")

        return {
            "id": row["id"],
            "meno": row["meno"],
            "vek": row["vek"],
        }
    except sqlite3.Error as e:
        raise HTTPException(status_code=500, detail=f"Chyba databázy: {e}") from e


@app.get("/pouzivatel/vek/{vek}")
def ziskaj_pouzivatelov_podla_veku(vek: int):
    try:
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
            "SELECT id, meno, vek FROM pouzivatelia WHERE vek = ?",
            (vek,),
        )
        rows = cursor.fetchall()
        connection.close()


        return {
            "data": rows
        }
    except sqlite3.Error as e:
        raise HTTPException(status_code=500, detail=f"Chyba databázy: {e}") from e


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
        reload=True,
    )