class User:
    def __init__(self, username, income):
        self.username = username
        self.income = income
        self.expenses = []
    def add_expenses(self,category,amount):
        expense = Expense(category,amount)
        self.expenses.append(expense)
    def show_expenses(self):
        print("\n========== EXPENSES ==========")
        print(f"{'category': <15}{'amount'}")
        print("-" * 30)

        for expense in self.expenses:
            print(expense)
        print("-" * 30)
    def remaining_balance(self):
        total = 0
        for expense in self.expenses:
            total += expense.amount

        balance = self.income - total
        print(f"\nRemaining Balance : {balance}$")
class Expense:
    def __init__(self,category,amount):
        self.category = category
        self.amount = amount
    def __str__(self):
        return f"{self.category:<15}: {self.amount:>6}"
user = User("ksai9987", 7000)
user.add_expenses("food", 500)
user.add_expenses("fuel", 1200)
user.add_expenses("roadtrip", 200)
user.add_expenses("movie", 20)
user.add_expenses("savings", 1500)
user.add_expenses("investments", 500)
user.show_expenses()
user.remaining_balance()
