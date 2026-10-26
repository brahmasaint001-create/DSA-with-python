num = int(input("Enter the number : "))
if num == 0:
    count = 0
else:
    temp = abs(num)
    count = 1

    while temp > 0:
        count += 1
        temp //= 10
print(f"The numbers of digits is {count}")