# exercise 9\n",
# modification of exercise 6\n",
# exception handling\n",
def main():
    count = 0
    total = 0
    #ask user to enter file name
    filename = input('Enter the name of the file')
    try:
        numbers = open(filename,'r')
        for line in numbers:
            num = int(line)
            total = total + num
            count = count + 1
    #close the file\n",
        numbers.close()
        average = total / count
        print(total)
        print(count)
        print(average)
    except IOError:
        print('file does not exist')
    except ValueError:
        print('invalid integer conversion')
#call the main function\n",
main()