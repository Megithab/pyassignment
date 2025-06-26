transactions = []
balance = 0

while True:
    print("\n1. Add Income")
    print("2. Add Expense")
    print("3. Show Balance")
    print("4. Show History")
    print("5. Exit")

    choice = input("Choose: ")

    if choice == "1":
        amount = float(input("Income amount: "))
        balance += amount
        transactions.append(f"Income: +${amount}")
    elif choice == "2":
        amount = float(input("Expense amount: "))
        balance -= amount
        transactions.append(f"Expense: -${amount}")
    elif choice == "3":
        print("Balance: $", balance)
    elif choice == "4":
        for t in transactions:
            print(t)
    elif choice == "5":
        break
    else:
        print("Invalid choice")
