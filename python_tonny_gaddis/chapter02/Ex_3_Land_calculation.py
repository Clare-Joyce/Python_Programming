# Conversion from sqaure feets to acres
# 1 acre = 43560 square feet
Square_feet_per_acre = 43560
# Prompt user for number of square feets
square_feets = int(input("Enter the number of square_feetsin the land: "))
# Calculate the corresponding nummber of acres
acres = square_feets/Square_feet_per_acre
# Display the value
print(f"Equivalent number of acres is {acres}")