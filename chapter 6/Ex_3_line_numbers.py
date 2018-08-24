#programming execises
# exercise number 3
def main():
   count = 0
    filename = input('Enter filename: ')
    #open the file to read the numbers
    numbers = open(filename,'r')
    for line in numbers:
        num = int(line)
        count = count + 1
        print('#', count, ';', num)
    #close the file
    numbers.close()
#call the main function
main()