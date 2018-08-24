#comparing the area of two rectangles

#prompt user for dimensions of rectangle one
length1 = float(input("Enter the length of rectangle 1: "))
width1 = float(input("Enter the width of rectangle 1: "))

#calculate area of rectangle 1
area1 = length1 * width1

#prompt user for dimensions of rectangle two
length2 = float(input("Enter the length of rectangle 2: "))
width2 = float(input("Enter the width of rectangle 2: "))

#calculate area of rectangle 2
area2 = length2 * width2

#compare the values
if area1 < area2:
	print("rectangle 1 has a smaller area.")
elif area1 > area2:
	print("rectangle 1 has a larger area.")
else:
	print("the rectangles have the same area.")