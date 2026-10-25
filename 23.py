numbers = []
print("Enter 5 numbers")
for i in range (5):
    num = int(input(f"Enter your numbers {i + 1} : "))
    numbers.append(num)
    smallest = min(numbers)
print(f"The smllest numbers is {smallest}")