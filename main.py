import csv

def add_lead(leads, name, email, status):
    new_lead = {"name": name, "email": email, "status": status}
    leads.append(new_lead)

def save_leads(leads, filename):
    with open(filename, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["name", "email", "status"])
        writer.writeheader()
        writer.writerows(leads)

leads = []

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