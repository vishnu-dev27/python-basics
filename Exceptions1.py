while True:
    try:
        amount = float(input("Enter an amount: "))
        if amount <= 0:
            raise ValueError("amount must be greater than zero")
            print(f"Valid amount:{amount:.2f}$")
            break
    except ValueError as error:
        print("Invalid Output:{error}")
