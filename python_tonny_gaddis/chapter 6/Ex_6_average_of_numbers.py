# exercise 6\n",
# average of numbers\n",
def main():
    count = 0
    total = 0
    numbers = open('number_list.txt','r')
    for line in numbers:
        num = int(line)
        total = total + num
        count = count + 1
    #close the file
    numbers.close()
    average = total / count
    print(total)
    print(count)
    print(average)
#call the main function
main()