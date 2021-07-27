#import math module to make use of the sqrt function
import math
def find_next_square(sq):
#get square root of sq
	a = math.sqrt(sq)
    #convert the sqaure root to int
	b = int(math.sqrt(sq))
    #check for diff between that actual square root and 
    #its integer form
	if a-b==0:
    #if sq is a perfect square
    #get next integer after the square of sp
		c = b+1
        #return the square of the next integer
		return(c**2)
    #is sq is not a perfect square, return -1
	else:
		return -1
print(find_next_square(10))