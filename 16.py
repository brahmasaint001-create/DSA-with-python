real_password = "admin123"
password = str(input("Enter the password"))
if password == real_password:
    print("Login successful")
else:
    print("Invalid password")