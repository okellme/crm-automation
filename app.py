from flask import Flask, request
import sqlite3
from datetime import datetime

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
    return html

@app.route("/add", methods=["POST"])
def add_lead_route():
    name = request.form["name"]
    email = request.form["email"]
    status = request.form["status"]
    date_added = datetime.now().strftime("%Y-%m-%d")
    insert_lead_db(name, email, status, date_added)
    return f"<p>Lead '{name}' added! <a href='/'>Go back</a></p>"

if __name__ == "__main__":
    app.run(debug=True)