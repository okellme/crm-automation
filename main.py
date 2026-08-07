def add_lead(leads, name, email, status):
    new_lead = {"name": name, "email": email, "status": status}
    leads.append(new_lead)

leads = []

while True:
    name = input("Enter lead name: ")
    email = input("Enter lead email: ")
    status = input("Enter lead status: ")

    add_lead(leads, name, email, status)

    again = input("Add another lead? (yes/no): ")
    if again != "yes":
        break

for lead in leads:
    print(f"{lead['name']} - {lead['status']}")