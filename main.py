class ExpenseTracker:
    def __init__(self):
        self.expenses = {}

    def add_expense(self, category, amount):
        if category in self.expenses:
            self.expenses[category].append(amount)
        else:
            self.expenses[category] = [amount]

    def view_expenses(self):
        for category, amounts in self.expenses.items():
            total = sum(amounts)
            print(f"{category}: ${total}")

    def summary(self):
        total_expenses = sum(sum(amounts) for amounts in self.expenses.values())
        print(f"Total Expenses: ${total_expenses}")

    def info(self):
        print("Developed by")
        print("Mohamed Nashath")
        print("nashathmjm1@gmail.com")
        print("https://www.linkedin.com/in/mohamed-nashath-27a9142b6/")
        print("A mini project for CodeAlpha internship programme")

if __name__ == "__main__":
    tracker = ExpenseTracker()

    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Summary")
        print("4. Developer Info")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            category = input("Enter expense category: ")
            amount = float(input("Enter expense amount: "))
            tracker.add_expense(category, amount)
            print("Expense added successfully!")

        elif choice == "2":
            print("\nExpenses:")
            tracker.view_expenses()

        elif choice == "3":
            print("\nExpense Summary:")
            tracker.summary()

        elif choice == "4":
            print("\n:")
            tracker.info()

        elif choice == "5":
            print("Exiting...")
            break

        else:
            print("Invalid input. Please try again using 1 to 5 as inputs.")
