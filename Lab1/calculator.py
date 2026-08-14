# calculator.py
# Menu driven calculator with 4 operations. Keeps asking for
# input until the user chooses to exit (option 5).

while True:
    print("\n---- MENU ----")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Choose an option (1-5): ")

    if choice == "5":
        print("Goodbye!")
        break  # exits the while loop

    if choice not in ("1", "2", "3", "4"):
        print("Invalid choice, try again.")
        continue  # skips the rest and re-shows the menu

    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    if choice == "1":
        print("Result:", a + b)
    elif choice == "2":
        print("Result:", a - b)
    elif choice == "3":
        print("Result:", a * b)
    elif choice == "4":
        # Guard against division by zero so the program doesn't crash
        if b == 0:
            print("Error: cannot divide by zero.")
        else:
            print("Result:", a / b)
