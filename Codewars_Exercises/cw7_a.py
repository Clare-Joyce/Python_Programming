"""
Determining if three side lengths can make a triangle is easier than it looks. 
All you have to do is use the Triangle Inequality Theorem, which states that the sum 
of two side lengths of a triangle is always greater than the third side. 
If this is true for all three combinations of added side lengths, then you will have a triangle.
"""
def is_triangle(a, b, c):
	if a+b>c and b+c>a and a+c>b:
		return True 
	else:
		return False
print(is_triangle(2,2,2))