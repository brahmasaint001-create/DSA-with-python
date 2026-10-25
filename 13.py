account_balance = int(input("Enter you account balance"))
withdrawl_amount = int(input("Enter your withdrawl amout"))
if withdrawl_amount <= account_balance:
    remaining_balance = account_balance - withdrawl_amount
    print(f"{withdrawl_amount} is deducted from the account and the remaining balance is {remaining_balance}")
elif withdrawl_amount > account_balance:
    print("Insufficient balance")
else:
    print("Invalid amount")