# exercise 7\n",
# random number file writer\n",

#import random moduke to use and generate random numbers
import random
def main():
    # specify how many random numbers u want.
    num_rand_number = int(input('how many random numbes do u want to generate:'))
    #create a file to store the random numbers in
    rand_num_file = open('random_numbers.txt', 'w')
    for count in range(num_rand_number):
        #genarate a random number between 1 and 500
        num = random.randint (1,500)
        #write this numbe to a file.
        rand_num_file.write(str(num) + '\n')

    #close the file
    rand_num_file.close()
main()