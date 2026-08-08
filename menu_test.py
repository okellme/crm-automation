while True:
    print("\n--- CRM Menu ---")
    print("1. View all leads")
    print("2. Add a new lead")
    print("3. Check overdue leads")
    print("4. Send follow-up emails")
    print("5. Quit")

    choice = input("Choose an option: ")

    if choice == "1":
        print("You picked View all leads")
    elif choice == "2":
        print("You picked Add a new lead")
    elif choice == "3":
        print("You picked Check overdue leads")
    elif choice == "4":
        print("You picked Send follow-up emails")
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice, try again.")