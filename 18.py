total_amount = float(input("Enter your amount = "))
if total_amount >= 5000:
    Discount_percentage = 20
elif total_amount >= 3000:
    Discount_percentage = 10
elif total_amount >= 1000:
    Discount_percentage = 5
else:
    print("No discount")

Discount_value = (Discount_percentage / 100) * total_amount
final_amount = total_amount - Discount_value
print(f"Final amount is {final_amount}")