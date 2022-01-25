""" Calculate the tax and total cost of items purchased."""

tax_percent = 7 # in %
# Initialize an accumulator
total = 0.0
for i in range(5):
	print("Enter price for item #", i+1)
	try:
		price = float(input("Price = "))
	except  ValueError:
		print("Invalid input. Please enter a number.")
	# Calculate subtotal
	subtotal = price + (tax_percent * price / 100)
	print("total for item #", i + 1, "= ", subtotal)

	total =+ subtotal
print("\nYour total bill is $", total)


