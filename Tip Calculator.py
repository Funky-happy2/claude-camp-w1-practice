meal_cost = float(input("Enter the meal cost: "))
tip_percentage = float(input("Enter the tip percentage: "))
tip_amount = meal_cost * (tip_percentage / 100)
total_cost = meal_cost + tip_amount
print(f"Tip amount: ${tip_amount:.2f}")
print(f"Total cost: ${total_cost:.2f}")