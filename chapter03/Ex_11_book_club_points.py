# Serendipity Booksellers has a book club that awards points to its customers based on the 
# number of books purchased each month. The points are awarded as follows:
# •	 If	a	customer	purchases	0	books,	he	or	she	earns	0	points.
# •	 If	a	customer	purchases	2	books,	he	or	she	earns	5	points.

# •	 If	a	customer	purchases	4	books,	he	or	she	earns	15	points.
# •	 If	a	customer	purchases	6	books,	he	or	she	earns	30	points.
# •	 If	a	customer	purchases	8	or	more	books,	he	or	she	earns	60	points.


#prompt user for number of book purchased

books = int(input("Enter numbr of books: "))



if books == 0:
	points = 0
elif books == 2:
	points = 5
elif books==4: 
	points = 15
elif books==6:
	points = 30
else:
	points=60	

print("you have earned", points, "points this month")