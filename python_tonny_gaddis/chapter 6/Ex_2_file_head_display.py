# programming execises
# exercise number 1
def main():
    #open the file to read the numbers

    #prompt user for filename
    filename=input("enter the name of the file; ")
    numbers = open(filename,'r')
    for i in range (1,6):
        num = int(numbers.readline())
        print(num)
    #close the file
    numbers.close()
#call the main function
main()