# Calculate the car’s MPG and display the result

# Prompt user for number of gas gallons
gallons = float(input("Enter number of gas gallons used: "))
# Prompt user the miles traveled
miles = float(input("Enter number of miles driven: "))

# Calculate the miles per gallon
MPG = miles/gallons

print (f"{MPG} miles per gallons")