# Weight of Package Rate per Pound
# 2 pounds or less $1.50
# Over 2 pounds but not more than 6 pounds $3.00
# Over 6 pounds but not more than 10 pounds $4.00
# Over 10 pounds $4.75

#prompt user of weight of package purchased
weight = float(input("Enter weight in pounds. "))

if weight <= 2:
	charge = 1.5
elif weight > 2 and weight <= 6:
	charge=3.0
elif weight > 6 and weight <= 10:
	charge=4.0
else:
	charge=4.75

	print(weight, charges)
