a = float(input("Enter your first number"))
b = float(input("Enter your second number"))
operator = input("Emter your operator('+', '-', '*', '/')= ")
if operator == '+':
    result = a + b
    print(f"Result = {a} + {b} = {result}")
elif operator == '-':
    result = a - b
    print(f"Result = {a} - {b} = {result}")
elif operator == '*':
    result = a * b
    print(f"Result = {a} * {b} = {result}")
elif operator == '/':
    result = a / b
    print(f"Result = {a} / {b} = {result}")
else:
    print("Invalid operator")