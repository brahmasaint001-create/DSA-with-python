your_balance = 10000
ATM_pin = 8080
for i in range (5):
    PIN = int(input(f"Enter your atm pin {i + 1} : "))
    if PIN == ATM_pin:
        print("Atm pin correct")
        while True:
            print("1.Check balance")
            print("2.Deposit")
            print("3.Withdraw")
            print("4.Exit")
            options = int(input("Enter your chossen option : "))
            if options == 1:
                print(f"Your balance is {your_balance}")
            elif options == 2:
                Deposit_amount = int(input("Enter your deposit amount"))
                if Deposit_amount <= 10000:
                    your_balance = Deposit_amount + your_balance
                    print(f"Your new balance is {your_balance}")
                else:
                    print("Your entered deposit amount is greater than one day deposit limit")
            elif options == 3:
                Withdrawl_amount = int(input("Enter the withdrawl amount : "))
                if Withdrawl_amount <= your_balance:
                    your_balance = your_balance - Withdrawl_amount
                    print(f"Your new balance is {your_balance}")
                else:
                    print("Not sufficient balance")
            elif options == 4:
                print("Exit!")
                print("THanku for coming")
                break
            else:
                print("Invalid option") 
        break 
    else:
        attempts_left = 4-i
        if attempts_left > 0:
            print(f"PIN is incorrect {attempts_left} attempts left . Try again!")
        else:
            print("Your account is banned")
            break       