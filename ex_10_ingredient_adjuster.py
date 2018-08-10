#ingredient adjuster
"""
recipe for 48 cookies
1.5 cups of sugar
1 cup of butter
2.75 cups of flour
"""
num_cookies = int(input("Enter the number of cookies you need: "))

amount_sugar = (1.5 * num_cookies)/48
amount_butter = num_cookies/48
amount_flour = (2.75 * num_cookies)/48

print("For ", num_cookies, "number of cookies, you require: ")

print(format(amount_sugar, '.2f'), "cups of sugar")
print(format(amount_butter, '.2f'), "cups of butter")
print(format(amount_flour, '.2f'), "cups of flour")