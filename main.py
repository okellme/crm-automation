import csv
import os
from datetime import datetime
import smtplib
from email.message import EmailMessage

from dotenv import load_dotenv
import os

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

def insert_lead_db(name, email, status, date_added):
    conn = sqlite3.connect("leads.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO leads (name, email, status, date_added) VALUES (?, ?, ?, ?)",
        (name, email, status, date_added)
    )
    conn.commit()
    conn.close()

def get_all_leads_db():
    conn = sqlite3.connect("leads.db")
    cursor = conn.cursor()
    cursor.execute("SELECT name, email, status, date_added FROM leads")
    rows = cursor.fetchall()
    conn.close()
    leads = []
    for row in rows:
        leads.append({"name": row[0], "email": row[1], "status": row[2], "date_added": row[3]})
    return leads



load_dotenv()

EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
init_db()
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

def add_lead(leads, name, email, status):
    date_added = datetime.now().strftime("%Y-%m-%d")
    new_lead = {"name": name, "email": email, "status": status, "date_added": date_added}
    leads.append(new_lead)

def save_leads(leads, filename):
    with open(filename, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["name", "email", "status", "date_added"])
        writer.writeheader()
        writer.writerows(leads)

def load_leads(filename):
    leads = []
    if os.path.exists(filename):
        with open(filename, "r", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                leads.append(row)
    return leads

leads = get_all_leads_db()

print("Currently saved leads:")
for lead in leads:
    print(f"{lead['name']} - {lead['status']} - {lead['date_added']}")

while True:
    name = input("Enter lead name: ")
    email = input("Enter lead email: ")
    status = input("Enter lead status: ")

    add_lead(leads, name, email, status)
    insert_lead_db(name, email, status, datetime.now().strftime("%Y-%m-%d"))

    again = input("Add another lead? (yes/no): ")
    if again != "yes":
        break



print("Leads saved to database")


def check_overdue(leads, days_threshold=7):
    today = datetime.now()
    overdue_leads = []

    for lead in leads:
        date_added = datetime.strptime(lead["date_added"], "%Y-%m-%d")
        days_since_added = (today - date_added).days

        if days_since_added >= days_threshold:
            overdue_leads.append(lead)

    return overdue_leads



overdue = check_overdue(leads, days_threshold=7)

print("\n--- Leads needing follow-up (7+ days old) ---")
if overdue:
    for lead in overdue:
        print(f"{lead['name']} ({lead['email']}) - added {lead['date_added']}")
else:
    print("No overdue leads. You're all caught up!")
    
def send_email(to_address, subject, body):
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = to_address
    msg.set_content(body)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)

    print(f"Email sent to {to_address}")

send_email("salcedojohnpaul503@gmail.com", "Follow up needed", "This lead hasn't been contacted in 7+ days.")
