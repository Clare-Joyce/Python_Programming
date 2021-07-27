# Assume that hot dogs come in packages of 10, and 
# hot dog buns come in packages of 8.

num_hot_dogs_pack = 10
num_hot_buns_pack = 8


#prompt user for number of invitees
number = int(input("Enter the number of invitees. "))
dogs_per_person = int(input("Enter number of dogs each person will be given;"))

#Calculate number og dogs required
total = number * dogs_per_person