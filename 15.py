num = int(input("Enter your number"))
if num >= 1 and num <= 20:
    print(f"{num} is between 1 and 20 ")
elif num >= 11 and num < 20:
    print(f"{num} is between 11 and 20")
elif num > 20:
    print(f"{num} is greater than 20")
else:
    print(f"{num} is less than 1")
