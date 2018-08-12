#calculating the tip, tax and total in a restau

#prompt user for cost of food
food_cost = float(input("Enter the cost of the food: "))

#percentage tip
tip_percentage = 18
#sales tax percentage
sales_tax_percentage = 7
#calculate the tip amount
tip = tip_percentage*food_cost/100
#calculate the amount of sales tax
sales_tax = sales_tax_percentage*food_cost/100
#calculate the total
Total = food_cost+tip+sales_tax

#display these values

print("Tip: ", tip)
print("Sales Tax:", sales_tax)
print("Total Cost:", Total)

