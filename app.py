import streamlit as st
import sqlite3
import os

DB = "ifrs.db"

def init_db():

    conn = sqlite3.connect(DB)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS standards (
        code TEXT,
        title TEXT,
        description TEXT
    )
    """)

    cursor.execute("SELECT COUNT(*) FROM standards")
    count = cursor.fetchone()[0]

    if count == 0:

        standards = [

        ("IFRS 1","First-time Adoption of IFRS",
        "Procedures for entities adopting IFRS for the first time."),

        ("IFRS 2","Share-based Payment",
        "Recognition of transactions involving share-based compensation."),

        ("IFRS 3","Business Combinations",
        "Accounting treatment for acquisitions and goodwill."),

        ("IFRS 9","Financial Instruments",
        "Classification, measurement and impairment of financial assets."),

        ("IFRS 15","Revenue from Contracts with Customers",
        "Five-step model for revenue recognition."),

        ("IFRS 16","Leases",
        "Recognition of right-of-use assets and lease liabilities.")
        ]

        cursor.executemany(
            "INSERT INTO standards VALUES (?,?,?)",
            standards
        )

    conn.commit()
    conn.close()


def get_standards():

    conn = sqlite3.connect(DB)
    cursor = conn.cursor()

    cursor.execute("SELECT code,title FROM standards")

    rows = cursor.fetchall()

    conn.close()

    return rows


def get_description(code):

    conn = sqlite3.connect(DB)
    cursor = conn.cursor()

    cursor.execute(
        "SELECT description FROM standards WHERE code=?",
        (code,)
    )

    row = cursor.fetchone()

    conn.close()

    return row[0]


# Create DB automatically
init_db()

st.title("IFRS Explorer")
st.write("Select a standard to view its description.")

standards = get_standards()

options = [
    f"{code} – {title}"
    for code,title in standards
]

selection = st.selectbox(
    "Choose IFRS Standard",
    options
)

code = selection.split(" – ")[0]

description = get_description(code)

st.subheader(selection)
st.write(description)
