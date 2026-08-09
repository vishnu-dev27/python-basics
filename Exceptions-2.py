balance = 10000
try:
    withdrawal = float(input("Enter an amount: "))
    if withdrawal <= 0:
        raise ValueError("Withdrawal must be greater than zero.")
    if withdrawal > balance:
        raise ValueError ("Insufficient Funds...")
    balance -= withdrawal
except ValueError as error:
    print("Transaction failed:{error}")
else:
    print("Withdrawal sucsessful")
    print(f"Remaining balance:{balance:.2f}$")
