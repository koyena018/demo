import datetime

class FinanceBuddy:
    def __init__(self):
        self.expenses = []
        self.budget = {}
        self.goals = {}

    def add_expense(self, amount, category, description=""):
        timestamp = datetime.datetime.now()
        self.expenses.append({"timestamp": timestamp, "amount": amount, "category": category, "description": description})
        print(f"Expense of ₹{amount:.2f} in '{category}' added.")

    def view_expenses(self, category=None, month=None, year=None):
        if not self.expenses:
            print("No expenses recorded yet.")
            return

        print("\n--- Expenses ---")
        filtered_expenses = self.expenses
        if category:
            filtered_expenses = [exp for exp in filtered_expenses if exp["category"] == category]
        if month:
            filtered_expenses = [exp for exp in filtered_expenses if exp["timestamp"].month == month]
        if year:
            filtered_expenses = [exp for exp in filtered_expenses if exp["timestamp"].year == year]

        if not filtered_expenses:
            print("No expenses found based on the filter criteria.")
            return

        for exp in filtered_expenses:
            print(f"{exp['timestamp'].strftime('%Y-%m-%d %H:%M')}: ₹{exp['amount']:.2f} - {exp['category']} - {exp['description']}")
        print("------------------\n")

    def set_budget(self, category, amount):
        self.budget[category] = amount
        print(f"Budget for '{category}' set to ₹{amount:.2f}.")

    def view_budget(self):
        if not self.budget:
            print("No budget set yet.")
            return

        print("\n--- Budget ---")
        for category, amount in self.budget.items():
            spent = sum(exp["amount"] for exp in self.expenses if exp["category"] == category)
            remaining = amount - spent
            print(f"{category}: Budgeted ₹{amount:.2f}, Spent ₹{spent:.2f}, Remaining ₹{remaining:.2f}")
        print("---------------\n")

    def set_goal(self, name, target_amount):
        self.goals[name] = {"target": target_amount, "saved": 0}
        print(f"Goal '{name}' set with a target of ₹{target_amount:.2f}.")

    def view_goals(self):
        if not self.goals:
            print("No goals set yet.")
            return

        print("\n--- Goals ---")
        for name, goal_data in self.goals.items():
            progress = (goal_data["saved"] / goal_data["target"]) * 100 if goal_data["target"] > 0 else 0
            print(f"{name}: Target ₹{goal_data['target']:.2f}, Saved ₹{goal_data['saved']:.2f} ({progress:.2f}%)")
        print("---------------\n")

    def add_savings(self, goal_name, amount):
        if goal_name in self.goals:
            self.goals[goal_name]["saved"] += amount
            print(f"₹{amount:.2f} added to '{goal_name}'.")
        else:
            print(f"Goal '{goal_name}' not found.")

    def analyze_spending(self):
        if not self.expenses:
            print("No spending data to analyze.")
            return

        category_spending = {}
        for exp in self.expenses:
            category = exp["category"]
            amount = exp["amount"]
            category_spending[category] = category_spending.get(category, 0) + amount

        print("\n--- Spending Analysis ---")
        for category, total_spent in sorted(category_spending.items(), key=lambda item: item[1], reverse=True):
            print(f"{category}: ₹{total_spent:.2f}")
        print("-------------------------\n")

        # Simple money-saving tips based on spending
        if "Food" in category_spending and category_spending["Food"] > 500:
            print("💡 Tip: Consider cooking more meals at home to save on food expenses.")
        if "Entertainment" in category_spending and category_spending["Entertainment"] > 300:
            print("💡 Tip: Look for free or discounted entertainment options.")

    def generate_alerts(self):
        if not self.budget:
            print("Set a budget to receive spending alerts.")
            return

        print("\n--- Spending Alerts ---")
        for category, budgeted_amount in self.budget.items():
            spent = sum(exp["amount"] for exp in self.expenses if exp["category"] == category)
            if spent > budgeted_amount:
                overspent_by = spent - budgeted_amount
                print(f"⚠️ Alert! You've exceeded your '{category}' budget by ₹{overspent_by:.2f}.")
            elif budgeted_amount > 0 and spent / budgeted_amount > 0.8:
                print(f"⚠️ Alert! You're approaching your '{category}' budget. You've spent ₹{spent:.2f} out of ₹{budgeted_amount:.2f}.")
        print("-----------------------\n")

def main():
    buddy = FinanceBuddy()

    while True:
        print("\n--- Personal Finance Buddy ---")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Set Budget")
        print("4. View Budget")
        print("5. Set Goal")
        print("6. View Goals")
        print("7. Add Savings to Goal")
        print("8. Analyze Spending")
        print("9. Generate Alerts")
        print("10. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            try:
                amount = float(input("Enter expense amount: "))
                category = input("Enter expense category (e.g., Food, Transport, Entertainment): ")
                description = input("Enter description (optional): ")
                buddy.add_expense(amount, category, description)
            except ValueError:
                print("Invalid amount. Please enter a number.")
        elif choice == '2':
            print("Filter options:")
            print("a. All")
            print("b. By Category")
            print("c. By Month")
            print("d. By Year")
            filter_choice = input("Enter filter option: ").lower()
            category_filter = None
            month_filter = None
            year_filter = None
            if filter_choice == 'b':
                category_filter = input("Enter category to filter by: ")
            elif filter_choice == 'c':
                try:
                    month_filter = int(input("Enter month (1-12): "))
                    if not 1 <= month_filter <= 12:
                        print("Invalid month.")
                        continue
                except ValueError:
                    print("Invalid month.")
                    continue
            elif filter_choice == 'd':
                try:
                    year_filter = int(input("Enter year: "))
                except ValueError:
                    print("Invalid year.")
                    continue
            buddy.view_expenses(category=category_filter, month=month_filter, year=year_filter)
        elif choice == '3':
            category = input("Enter budget category: ")
            try:
                amount = float(input(f"Enter budget amount for '{category}': "))
                buddy.set_budget(category, amount)
            except ValueError:
                print("Invalid amount. Please enter a number.")
        elif choice == '4':
            buddy.view_budget()
        elif choice == '5':
            name = input("Enter goal name (e.g., Concert Ticket, New Book): ")
            try:
                target_amount = float(input(f"Enter target amount for '{name}': "))
                buddy.set_goal(name, target_amount)
            except ValueError:
                print("Invalid amount. Please enter a number.")
        elif choice == '6':
            buddy.view_goals()
        elif choice == '7':
            goal_name = input("Enter the name of the goal to add savings to: ")
            try:
                amount = float(input("Enter the amount to add: "))
                buddy.add_savings(goal_name, amount)
            except ValueError:
                print("Invalid amount. Please enter a number.")
        elif choice == '8':
            buddy.analyze_spending()
        elif choice == '9':
            buddy.generate_alerts()
        elif choice == '10':
            print("Exiting Personal Finance Buddy. Take care!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()