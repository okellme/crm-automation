def add_lead(leads, name, email, status):
    new_lead = {"name": name, "email": email, "status": status}
    leads.append(new_lead)

leads = []

name = input("Enter lead name: ")
email = input("Enter lead email: ")
status = input("Enter lead status: ")

add_lead(leads, name, email, status)

for lead in leads:
    print(f"{lead['name']} - {lead['status']}")