def deposit(account,amount):
    account.balance += amount

def withdraw(account,amount):
    if amount > account.balance:
        print("Insufficient balance...")
    else:
        account.balance -= amount
