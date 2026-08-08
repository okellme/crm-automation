try:
    number = int(input("Enter a number: "))
    print(f"You entered {number}")
except ValueError:
    print("That's not a valid number. Please try again.")