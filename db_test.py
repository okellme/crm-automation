import sqlite3

def init_db():
    conn = sqlite3.connect("leads.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS leads (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT,
            status TEXT,
            date_added TEXT
        )
    """)
    conn.commit()
    conn.close()

init_db()
print("Database and table ready.")

def insert_lead(name, email, status, date_added):
    conn = sqlite3.connect("leads.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO leads (name, email, status, date_added) VALUES (?, ?, ?, ?)",
        (name, email, status, date_added)
    )
    conn.commit()
    conn.close()

def get_all_leads():
    conn = sqlite3.connect("leads.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM leads")
    rows = cursor.fetchall()
    conn.close()
    return rows

insert_lead("Test Lead", "test@email.com", "new", "2026-08-08")

leads = get_all_leads()
for lead in leads:
    print(lead)