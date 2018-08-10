# The program should then compute the state and county sales tax. 
# state sales tax is 5 percent 
# county sales tax is 2.5 percent.
# display the amount of the pur-chase, 
# the state sales tax, 
# the county sales tax;
# the total sales tax, 
# the total of the sale 

#initalize variables
state_sales_tax_percent = 5
county_sales_tax_percent - 2.5


#prmpt user for amount of purchase
amount_purchase = float(input("enter amount of purchase: "))
#calculate state sales tax
state_sales_tax = amount_purchase * state_sales_tax_percent / 100
#calculate the county sales tax
county_sales_tax = amount_purchase * county_sales_tax_percent / 100 
#calculate the total sales tax
total_sales_tax = state_sales_tax + county_sales_tax
#calculate  total sale
total_sales = amount_purchase + total_sales_tax

#display these values
print("Amount purchase: ", amount_purchase)
print("State sales tax: ", state_sales_tax)
print("County sales tax: ", county_sales_tax)
print("Total sales tax: ", total_sales_tax)
print("Total of sales: ", total_sales) 