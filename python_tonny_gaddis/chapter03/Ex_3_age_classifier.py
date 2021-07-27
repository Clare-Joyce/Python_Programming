#age classifier program.
#prompt user for an age
age = int(input("Enter an age: "))
if age <= 1: 
	print("she is an infant.")

elif age < 13:
	print(" he or she is a child.")

elif age < 20:
	print("he or she is a teenager.")
elif age >= 20:
	print("He or she is an adult.")
