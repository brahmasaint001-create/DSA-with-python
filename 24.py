real_username = "Brahama152008"
real_password = 152008
for i in range (3):
    username = input(f"Enter username {i + 1} : ")
    password = input(f"Enter password {i + 1} : ")
    if username == real_username and password == real_password:
        print("Login successful")
        break
    else:
        attempts_left = 2 - i
        if attempts_left > 0:
            print(f"Invalid details. you have {attempts_left} attempts left.\n")
else:
    print("Accoun locked, Too many failed login attempts.")    
