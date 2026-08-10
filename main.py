from account import account
from transactions import deposit,withdraw

account = account("Vishnu",50000)

deposit(account,15000)
withdraw(account,12000)

print("Balance:", account.balance)
