#conversion from sqaure feets to acres
#1 acres = 43560 square feet
Square_feet_per_acre = 43560
#prompt user for number of square feets
square_feets = int(input("Enter the number of square_feetsin the land. "))
#calcculate the corresponding nummber of acres
acres = square_feets/Square_feet_per_acre
#display the value
print("Equivalent number of acres is ", acres)