import sqlite3

DB_PATH = "data/ifrs.db"

def get_connection():
    return sqlite3.connect(DB_PATH)

def get_standards():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT code, title FROM standards")
    rows = cursor.fetchall()

    conn.close()

    return rows


def get_description(code):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT description FROM standards WHERE code=?",
        (code,)
    )

    row = cursor.fetchone()

    conn.close()

    return row[0]
