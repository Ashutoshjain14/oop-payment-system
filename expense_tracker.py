
import os

while True:
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Show Summary")
    print("4. Exit")

    choice = int(input("Choose from 1-4 : "))
    if choice == 1:
        print("You chose to add an expense")
        date = input("Enter the date (YYYY-MM-DD): ")
        category = input("Enter the category: ")
        amount = input("Enter the amount: ")
        description = input("Description of your expense: ")

        file_exists = os.path.exists("expenses.csv")
        is_empty = not file_exists or os.stat("expenses.csv").st_size == 0


        with open("expenses.csv", "a") as file:
            if is_empty:
                file.write("date, category, amount, description\n")
            file.write(f"{date}, {category}, {amount}, {description}\n")
        print("Your expense is added successfully")
    elif choice == 2:
        print("You chose to view all expenses")
        print("\nDate | Category | Amount | Description")
        print("-"*50)
        try:
            with open("expenses.csv", "r") as file:
                next(file)
                for line in file:
                    line = line.strip()
                    if line == "":
                        continue
                    date, category, amount, description = line.split(",", 3)
                    print(f"{date:<12} | {category:<10} | {amount:<8} | {description}")
        except fileNotFoundError:
            print("No expenses recorded yet.")

    elif choice == 3:
        print("You chose to show summary of your expenses")
        with open("expenses.csv", "r") as file:
            next(file)
            total_amount = 0
            total_entries = 0
            for line in file:
                line = line.strip()
                if line == "":
                    continue
                date, category, amount, description = line.split(",", 3)
                amount = float(amount)
                total_amount += amount
                total_entries+=1
            print(f"Total amount : {total_amount}")
            print(f"Total entries: {total_entries}")
            if total_entries > 0:
                print(f"Average amount : {total_amount/total_entries}")

    elif choice == 4:
        print("You chose to exit: goodbye!")
        break
    else:
        print("Invalid choice, please try again.")