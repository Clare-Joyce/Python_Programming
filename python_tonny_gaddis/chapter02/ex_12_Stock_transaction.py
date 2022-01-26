"""Stock Transaction Program"""

num_share = num_sold = 2000
cost_per_share = 40.00
amount_paid = num_share * cost_per_share
stock_broker_commission = amount_paid * 3 / 100
selling_price_pershare = 42.75
amount_sold = num_sold * selling_price_pershare
stock_broker_commission2 = amount_sold * 3 / 100

print("\nAmount paid for stock $", amount_paid)
print("Amount received by stock broker before sale $", stock_broker_commission)
print("The stock was sold for $", amount_sold)
print("Amount received by stock broker after sales $", stock_broker_commission2)

stock_broker = stock_broker_commission2 + stock_broker_commission
amount_left = amount_sold  - stock_broker
print("Amount left: ", format(amount_left, ',.2f'))
if amount_left > amount_paid:
	print("profit made\n")
else:
	print("No profit\n")