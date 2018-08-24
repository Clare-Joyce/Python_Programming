#DISPLAYING THE NUMBER IN A FILE

#a control variable 
#open the file
#execisse number 1\n,
def main():
	#open the file
	file = open('numbers.txt', 'r')
	for line in file:
		num = line.rstrip('\n')
		print(num)

	#close the file
	file.close()
#call the main function
main()