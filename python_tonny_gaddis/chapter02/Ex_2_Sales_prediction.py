#predicting profit from a projected amount of total sales


#annual profit percentage
annual_profit = 23

#prompt user for projected sales
sales = float(input("Enter projected sales: "))

#calculate the projected profit
projected_profit = sales*annual_profit/100

#display the projected profit
print("Projected Profit = $", projected_profit)