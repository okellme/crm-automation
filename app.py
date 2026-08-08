from flask import Flask, request
import sqlite3
from datetime import datetime
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
import os

load_dotenv()
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

def send_email(to_address, subject, body):
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = to_address
    msg.set_content(body)

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)
        print(f"Email sent to {to_address}")
    except Exception as e:
        print(f"Failed to send email to {to_address}: {e}")



app = Flask(__name__)

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

def insert_lead_db(name, email, status, date_added):
    conn = sqlite3.connect("leads.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO leads (name, email, status, date_added) VALUES (?, ?, ?, ?)",
        (name, email, status, date_added)
    )
    conn.commit()
    conn.close()

def check_overdue(leads, days_threshold=7):
    today = datetime.now()
    overdue_leads = []
    for lead in leads:
        date_added = datetime.strptime(lead["date_added"], "%Y-%m-%d")
        days_since_added = (today - date_added).days
        if days_since_added >= days_threshold:
            overdue_leads.append(lead)
    return overdue_leads

@app.route("/")
def home():
    leads = get_all_leads_db()
    html = "<h1>My CRM</h1><ul>"
    for lead in leads:
        html += f"<li>{lead['name']} - {lead['status']} - {lead['date_added']}</li>"
    html += "</ul>"

    html += """
    <h2>Add a Lead</h2>
    <form action="/add" method="POST">
        Name: <input type="text" name="name"><br>
        Email: <input type="text" name="email"><br>
        Status: <input type="text" name="status"><br>
        <input type="submit" value="Add Lead">
    </form>
    """
    html += "<br><a href='/overdue'>View Overdue Leads</a>"
    return html

@app.route("/add", methods=["POST"])
def add_lead_route():
    name = request.form["name"]
    email = request.form["email"]
    status = request.form["status"]
    date_added = datetime.now().strftime("%Y-%m-%d")
    insert_lead_db(name, email, status, date_added)
    return f"<p>Lead '{name}' added! <a href='/'>Go back</a></p>"

@app.route("/overdue")
def overdue_route():
    leads = get_all_leads_db()
    overdue = check_overdue(leads, days_threshold=7)
    html = "<h1>Overdue Leads (7+ days)</h1><ul>"
    if overdue:
        for lead in overdue:
            html += f"<li>{lead['name']} ({lead['email']}) - added {lead['date_added']}</li>"
    else:
        html += "<li>No overdue leads. You're all caught up!</li>"
    html += "</ul>"
    html += "<a href='/'>Back to home</a> | <a href='/send-emails'>Send Follow-up Emails</a>"
    return html

@app.route("/send-emails")
def send_emails_route():
    leads = get_all_leads_db()
    overdue = check_overdue(leads, days_threshold=7)
    count = 0
    if overdue:
        for lead in overdue:
            send_email(
                lead["email"],
                "Follow up needed",
                f"Hi {lead['name']}, this lead hasn't been contacted in 7+ days."
            )
            count += 1
        message = f"Sent {count} follow-up email(s)."
    else:
        message = "No overdue leads to email."
    return f"<p>{message}</p><a href='/'>Back to home</a>"


if __name__ == "__main__":
    app.run(debug=True)