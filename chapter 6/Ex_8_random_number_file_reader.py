#execise 8
#random number reader,
def main():
    #initialize the accumulator
    total = 0
    count = 0
    #open the file
    rand_num_file = open('random_numbers.txt', 'r')
    for line in rand_num_file:
        num = int(line)
        count = count + 1
        total = total + num
    #close the file
    rand_num_file.close()
    #display total numbe =r of random numbers
    print('number of random numbers = ', count)
    #display the sum of all numbers read
    print('sum of numbers read = ',total)
#call the main function
main()