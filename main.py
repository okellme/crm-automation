import csv
import os
from datetime import datetime

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

leads = load_leads("leads.csv")

print("Currently saved leads:")
for lead in leads:
    print(f"{lead['name']} - {lead['status']} - {lead['date_added']}")

while True:
    name = input("Enter lead name: ")
    email = input("Enter lead email: ")
    status = input("Enter lead status: ")

    add_lead(leads, name, email, status)

    again = input("Add another lead? (yes/no): ")
    if again != "yes":
        break

save_leads(leads, "leads.csv")

print("Leads saved to leads.csv")



from datetime import datetime

def check_overdue(leads, days_threshold=7):
    today = datetime.now()
    overdue_leads = []

    for lead in leads:
        date_added = datetime.strptime(lead["date_added"], "%Y-%m-%d")
        days_since_added = (today - date_added).days

        if days_since_added >= days_threshold:
            overdue_leads.append(lead)

    return overdue_leads

overdue = check_overdue(leads, days_threshold=0)
print("Overdue leads:")
for lead in overdue:
    print(f"{lead['name']} - {lead['date_added']}")