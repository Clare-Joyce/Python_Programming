"""Description:
A square of squares
You like building blocks. You especially like building blocks that are squares. 
And what you even like more, is to arrange them into a square of square building blocks!

However, sometimes, you can't arrange them into a square. 
Instead, you end up with an ordinary rectangle! Those blasted things! 
If you just had a way to know, whether you're currently working in vain… Wait! 
That's it! You just have to check if your number of building blocks is a perfect square.

Task
Given an integral number, determine if it's a square number:

In mathematics, a square number or perfect square is an integer that is the square of an integer; 
in other words, it is the product of some integer with itself.

The tests will always use some integral number, so don't worry about that in dynamic typed languages.

Examples
isSquare(-1) returns  false
isSquare(0) returns   true
isSquare(3) returns   false
isSquare(4) returns   true
isSquare(25) returns  true  
isSquare(26) returns  false
"""


#import the math module to make use of the sqrt function
import math
#define a function is_square with n as argument(integer)
def is_square(n):
    #check if n is less than 0
    #if it is return false
	if n<0:
		return False
    #what happens when n is greter than or equal to zero
	else:
    #check if the difference between the square root of 
    #and the int value of the square root of n is different
    #from zero
		if math.sqrt(n)-int(math.sqrt(n)) == 0:
        #if the different is zero return true
			return True
		else:
        #if the difference is not zero return false
			return False