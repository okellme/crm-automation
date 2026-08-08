try:
    name = input("Enter lead name: ")
    while name.strip() == "":
        print("Name cannot be empty.")
        name = input("Enter lead name: ")
    print(f"You entered {number}")
except ValueError:
    print("That's not a valid number. Please try again.")