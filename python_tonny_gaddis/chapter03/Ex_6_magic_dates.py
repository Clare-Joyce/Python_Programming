#june 10 1960 is special coz 6(month)*10(day)
#gives the last two digits of the year 1960

#prompt a user for a month(numeeric value)
month = int(input("enter the month"))
day = int(input("enter the day"))
year = int(input("enter the last two digits of the year"))

if (month * day)==year:
	print("This is a magic year")
else:
	print("This is not a magic year")
