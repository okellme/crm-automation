def add_lead(leads, name, email, status):
    new_lead = {"name": name, "email": email, "status": status}
    leads.append(new_lead)

leads = []

add_lead(leads, "Paul", "paul@email.com", "New")
add_lead(leads, "Maria", "maria@email.com", "Contacted")

for lead in leads:
    print(f"{lead['name']} - {lead['status']}")