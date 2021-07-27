#mass and weigh t relations

#promt user for mass of an object
mass = float(input("enter mass of an object:"))

#calculate the weight of th object
weight = mass * 9.8

if weight > 500:
	print("Object is too heavy.")
if weight < 100:
	print("Objectis too light.")