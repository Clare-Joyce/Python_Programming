# Calculating the % of male and female students in a class

# Prompt the user for the number of female students
females = int(input("Enter number of female students: "))

# Prompt user for the number of male students
males = int(input("Enter number of male students: "))

total_num_students = males + females
# Calculate male percentage
male_percentage = males/total_num_students
# Calculate female percenatge
female_percentage = females/total_num_students

# Display the percentages
print("Percentage of males: ", format(male_percentage, '.1%'))
print("Percentage of females: ", format(female_percentage, '.1%'))