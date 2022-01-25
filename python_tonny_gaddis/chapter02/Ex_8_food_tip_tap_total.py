""" Calculating the tip, tax and total in a restaurant."""

# Prompt user for cost of food
food_cost = float(input("Enter the cost of the food: "))

# Percentage tip
tip_percentage = 18
# Sales tax percentage
sales_tax_percentage = 7
# Calculate the tip amount
tip = tip_percentage * food_cost / 100
# Calculate the amount of sales tax
sales_tax = sales_tax_percentage * food_cost / 100
# Calculate the total
total = sum([food_cost, tip, sales_tax])

# Display these values
print("Tip: ", tip)
print("Sales Tax:", sales_tax)
print("Total Cost:", format(total, '.2f'))