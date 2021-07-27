#software sales and discounts
#prompt user for number od items purchased
#discount in %
num = int(input("Enter number of items purchased: "))
price_per_package = 99
if num >= 10 and num <= 19:
	discount = 10
elif num >= 20 and num <= 49:
	discount = 20
elif num >= 50 and num <= 99:
	discount = 30
elif num >= 100:
	discount = 40
#calculate the discount
amt_discount = (discount/100)*num*price_per_package
#calculate the amount paid
amt_paid = (num*price_per_package) - amt_discount

#display the number of books
print(num)
#display the discount w.r.t numbers of books
print(discount)
#display the amount of the discount for the books
print(amt_discount)
print(amt_paid)