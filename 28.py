num = 7
while True :
    guess = int(input("Enter the number : "))
    if guess == num:
        print("Guessed successfully")
        break
    else:
        print("Wrong guess,try again")