class Account:
    def __init__(self,name,customer_id,balance):
        self.name = name
        self.customer_id = customer_id
        self.balance = balance
        self.transactions = []
    def check_balance(self):
        print(f"{self.name} Bank Balance $ : {self.balance}")
    def deposit(self,amount):
        self.balance += amount
        self.transactions.append(f"Deposited{amount}$")
        print(f"{self.name} deposited $ {amount}")
    def withdraw(self,amount):
        if amount <= self.balance:
            self.balance -= amount
            self.transactions.append(f"Withdrew{amount}$")
            print(f"{self.name} Withdrew $ {amount}")
        else:
            print("Insufficient Funds...")
    def show_transactions(self):
        print(f"transaction history for {self.name}")
        for t in self.transactions:
            print("-",t)
    def add_interest(self):
        interest = self.balance * 0.08
        self.transactions.append(f"Interest added {interest}$")
        print(f"{self.name} received {interest} as interest")
class SavingsAccount(Account):
    def add_interest(self):
        interest = self.balance * 0.08
        print(f"{self.name} received {interest} as interest")
class CurrentAccount(Account):
    def business_Loan(self):
        print(f"Business Loan sanctioned for {self.name}")
    def Home_Loan(self):
        print(f"Home Loan sanctioned for {self.name}")
    def Personal_Loan(self):
        print(f"Personal Loan sanctioned for {self.name}")
c1 = CurrentAccount("Vishnu",1265,56890)
c2 = CurrentAccount("Nick",1266,46890)
c3 = CurrentAccount("Vishnu",1267,66890)
c1.check_balance()
c1.deposit(2190)
c1.withdraw(3247)
c1.add_interest()
c1.check_balance()
c1.Home_Loan()
c1.show_transactions()
print("--------------------")
c2.check_balance()
c2.deposit(2190)
c2.withdraw(3247)
c2.add_interest()
c2.check_balance()
c2.business_Loan()
c2.show_transactions()
print("--------------------")
c3.check_balance()
c3.deposit(2190)
c3.withdraw(3247)
c2.add_interest()
c3.check_balance()
c3.Personal_Loan()
c3.show_transactions()
