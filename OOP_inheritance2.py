#1. A Knight's Apprentice inherits his master's skill:

class Warrior:
    def __init__(self,name):
        self.name = name
        self.health = 100
    def Attack(self):
        print(f"{self.name} swings the sword.")
    def Defend(self):
        print(f"{self.name} blocks the Attack.")
    def Rest(self):
        print(f"{self.name} rests and recovers.")
class Apprentice(Warrior):
    def fire_slash(self):
        print(f"{self.name} uses the Fire Slash!")
master = Warrior("Arin")
student = Apprentice("Kai")
master.Attack()
master.Defend()
master.Rest()
print("---------------")
student.Attack()
student.Defend()
student.Rest()
student.fire_slash()


#2. Banking System:
class Account:
    def __init__(self,name,customer_id,balance):
        self.name = name
        self.customer_id = customer_id
        self.balance = balance
    def check_balance(self):
        print(f"{self.name} bank balance: ${self.balance}")
    def deposit(self,amount):
        self.balance += amount
        print(f"{self.name} deposited ${amount}")
    def withdraw(self,amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{self.name} withdrew ${amount}")
        else:
            print("Insufficient Funds...")
class SavingsAccount(Account):
    def add_interest(self):
        interest = self.balance * 0.05
        self.balance += interest
        print(f"{self.name} received ${interest} as interest")
class CurrentAccount(Account):
    def business_loan(self):
        print(f"Business Loan Approved for {self.name}")
customer1 = SavingsAccount("Vishnu",12340986,50000)
customer2 = SavingsAccount("Leon",12340987,60000)
customer3 = SavingsAccount("Chris",12340988,70000)
customer4 = SavingsAccount("Ada",12340989,80000)
   
customer1.check_balance()
customer1.deposit(5400)
customer1.withdraw(12000)
customer1.add_interest()
customer1.check_balance()
print("---------------")
customer2.check_balance()
customer2.deposit(6400)
customer2.withdraw(17000)
customer2.add_interest()
customer2.check_balance()
print("---------------")
customer3.check_balance()
customer3.deposit(7400)
customer3.withdraw(19000)
customer3.add_interest()
customer3.check_balance()
print("---------------")
customer4.check_balance()
customer4.deposit(9400)
customer4.withdraw(23000)
customer4.add_interest()
customer4.check_balance()

