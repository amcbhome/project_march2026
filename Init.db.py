import sqlite3

conn = sqlite3.connect("data/ifrs.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS standards (
    id INTEGER PRIMARY KEY,
    code TEXT,
    title TEXT,
    description TEXT
)
""")

standards = [

("IFRS 1",
"First-time Adoption of IFRS",
"IFRS 1 establishes procedures for entities adopting IFRS for the first time and ensures comparability of financial statements."),

("IFRS 2",
"Share-based Payment",
"IFRS 2 requires entities to recognise share-based payment transactions, including equity-settled and cash-settled awards."),

("IFRS 3",
"Business Combinations",
"IFRS 3 prescribes the acquisition method for accounting for business combinations and recognition of goodwill."),

("IFRS 9",
"Financial Instruments",
"IFRS 9 addresses classification, measurement, hedge accounting and the expected credit loss model."),

("IFRS 15",
"Revenue from Contracts with Customers",
"IFRS 15 introduces the five-step revenue recognition model based on transfer of control."),

("IFRS 16",
"Leases",
"IFRS 16 requires lessees to recognise right-of-use assets and lease liabilities for most leases.")
]

cursor.executemany(
"INSERT INTO standards (code,title,description) VALUES (?,?,?)",
standards
)

conn.commit()
conn.close()

print("Database created.")
