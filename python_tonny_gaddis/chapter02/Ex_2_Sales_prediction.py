"""Predicting profit from a projected
amount of total sales."""

# Annual profit percentage
annual_profit = 23

# Prompt user for projected sales
sales = float(input("Enter projected sales: "))

# Calculate and display the projected profit
print("Projected Profit = $", sales*annual_profit/100)