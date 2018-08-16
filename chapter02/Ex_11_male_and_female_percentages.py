# calculating the % of male and female students in a class

#prompt usr for the number of female students
females = int(input("Enter number of female students: "))

#prompt usr for the number of male students
males = int(input("Enter number of male students: "))

total_num_students = males + females
#calculate male percentage
male_percentage = males * 100/total_num_students
#calculate female percenatge
female_percentage = females * 100/total_num_students

#display the percentages
print("Percentage of males: ", male_percentage)
print("Percentage of females: ", female_percentage)