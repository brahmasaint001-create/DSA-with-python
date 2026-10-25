n = int(input("Enter the number = "))
is_prime = True
if n <= 1:
    is_prime = False

else:
    for i in range(2, n):
        if n % i == 0:
            is_prime = False
            break
if is_prime:
    print("It is prime number")
else:
    print("It is not a prime number")
