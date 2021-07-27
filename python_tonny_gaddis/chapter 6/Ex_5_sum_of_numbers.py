def main():
    total = 0
    numbers = open('numbers_txt','r')
    for line in numbers:
        num = int(line)
        total = total + num
    #close the file
    numbers.close()
    print(total)
#call the main function
main()