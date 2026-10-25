user_age = int(input("Enter your age"))
if user_age < 12:
    print("movie ticket price is ₹100")
elif user_age >=12 and user_age <= 59:
    print("movie ticket price is ₹200")
else:
    print("movie ticket price is ₹120")