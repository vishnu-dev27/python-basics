# a person has an investment account:

class Investment:
    def invest(self,amount):
        print(f"{amount} Invested Successfuly.")
class person:
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance
        self.investment = Investment()
    def transfer_to_investment(self,amount):
        if amount <= self.balance:
            self.balance -= amount
            self.investment.invest(amount)
            print(f"remaining balance: ${self.balance}")
        else:
            print("Insufficient Balance!")
vishnu= person("vishnu",10000)
vishnu.transfer_to_investment(1750)

