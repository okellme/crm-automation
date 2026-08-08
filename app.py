from flask import Flask
import sqlite3

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

@app.route("/")
def home():
    leads = get_all_leads_db()
    html = "<h1>My CRM</h1><ul>"
    for lead in leads:
        html += f"<li>{lead['name']} - {lead['status']} - {lead['date_added']}</li>"
    html += "</ul>"
    return html

if __name__ == "__main__":
    app.run(debug=True)

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>My CRM is working!</h1>"

if __name__ == "__main__":
    app.run(debug=True)