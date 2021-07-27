#calculate the tax and total cost of items purchased


tax_percent = 7 #in %
#initialize an accumulator
total = 0.0
for i in range(5):
	print("Enter price for item #", i+1)
	price = float(input("Price = "))
	#calculate subtotal
	subtotal=price+(tax_percent*price/100)
	print("total for item #", i+1, "= ", subtotal)

	total= total+subtotal
print("Your total bill is $", total)


