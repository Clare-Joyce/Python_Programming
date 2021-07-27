"""
Description:
Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence, which is the number of times you must multiply the digits in num until you reach a single digit.

For example:

 persistence(39) => 3  # Because 3*9 = 27, 2*7 = 14, 1*4=4
                       # and 4 has only one digit.

 persistence(999) => 4 # Because 9*9*9 = 729, 7*2*9 = 126,
                       # 1*2*6 = 12, and finally 1*2 = 2.

 persistence(4) => 0   # Because 4 is already a one-digit number.
 persistence(39) # returns 3, because 3*9=27, 2*7=14, 1*4=4
                 # and 4 has only one digit

 persistence(999) # returns 4, because 9*9*9=729, 7*2*9=126,
                  # 1*2*6=12, and finally 1*2=2

 persistence(4) # returns 0, because 4 is already a one-digit number
"""

from itertools import accumulate # import accumulate function to store results when doingn multiplication.
from operator import mul #mul is a function for multiplication
def persistence(n):
    #define a control variable
	x = 10
    #initialize count
	cnt = 0
    #check for n less than 10
	if n <=9:
    #if n<10
    #set count to 0
		cnt = 0
    #if n>10 
    #perform the following operations
	else:
		while x >= 9:
        #initiaize an empty list
			c = []
            #convert n to a string
            #for each item in the string
            #convert it to an integer and
            # and append it to c
			for i in str(n):
				c.append(int(i))
            #for all integers in list c,
            #calculate the product
			for n in accumulate(c, mul):
				pass
            #set x to the product
			x = n
            #increment count by 1
			cnt = cnt + 1
	return cnt

print(persistence(10))