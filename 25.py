s = None

for i in range(5):
    a = int(input("Enter the number : "))
    if s is None or a > s:
        s = a
print(s)