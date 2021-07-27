#weight is measured in pounds and heightis measured in inches

weight = float(input("Enter your weight in pounds: "))
height = float(input("Enter your height in inches: "))

BMI = (weight*703)/height**2
if BMI < 18.5:
	print("Underweight") 
elif BMI >18.5 and BMI < 25:
	print("Optimal weight")
else:
	print("Overwight.")