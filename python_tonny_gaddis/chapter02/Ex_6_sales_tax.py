"""The program should then compute the state and county sales tax. 
- state sales tax is 5 percent 
- county sales tax is 2.5 percent.
- display the amount of the pur-chase, 
- the state sales tax, 
- the county sales tax;
- the total sales tax, 
- the total of the sale """

# Initalize variables
state_sales_tax_percent = 5
county_sales_tax_percent = 2.5

# Prompt user for amount of purchase
purchase_amount = float(input("enter amount of purchase: "))
# Calculate state sales tax
state_sales_tax = purchase_amount * state_sales_tax_percent / 100
# Calculate the county sales tax
county_sales_tax = purchase_amount * county_sales_tax_percent / 100 
# Calculate the total sales tax
total_sales_tax = state_sales_tax + county_sales_tax
# Calculate  total sale
total_sales = purchase_amount + total_sales_tax

# Display these values
print("Amount purchase: ", purchase_amount)
print("State sales tax: ", state_sales_tax)
print("County sales tax: ", county_sales_tax)
print("Total sales tax: ", total_sales_tax)
print("Total of sales: ", total_sales) 