#The primary colors because they cannot 
# be made by mixing other colors.
# When you mix red and blue, you get purple.
# When you mix red and yellow, you get orange.
# When you mix blue and yellow, you get green.


#color mixing program
#prompt user for first primary color
color1 = input("Enter a color: ")
#prompt user for second primary color
color2 = input("Enter another color: ")

#check if the colors are primary colors.
if color1 != 'red' and color1 != 'blue' and color1 != 'green':
	print("This is not a primary color.")
if color2 != 'red' and color2 != 'blue' and color2 != 'green':
	print("This is not a primary color.")

#mix the colours
if color1 == 'red' and color2 == 'yellow' or color1 =='yellow' and color2 =='red':
	print("This resulting of these two colors is purple")
elif color1 == 'red' and color2 == 'blue' or color1 =='blue' and color2 =='red':
	print("This resulting of these two colors is orange")
elif color1 == 'blue' and color2 == 'yellow' or color1 =='yellow' and color2 =='blue':
	print("This resulting of these two colors is purple")
elif color1==color2:
	print("Mixing", color2, "and", color1, "yeilds same colour")