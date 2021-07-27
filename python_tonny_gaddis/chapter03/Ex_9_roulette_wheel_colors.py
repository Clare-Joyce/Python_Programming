
#prompt for a pocket number
pocket_num = int(input("Enter pocket number: "))
if pocket_num==0:
	pocket_color = 'green'
for pocket_num in range(1, 10):
	if pocket_num%2 == 0:
		pocket_color = 'black'
	else:
		pocket_color='red.'
for pocket_num in range(11, 28):
	if pocket_num%2 == 0:
		pocket_color = 'red.'
	else:
		pocket_color = 'black'
for pocket_num in range(19, 28):
	if pocket_num%2 == 0:
		pocket_color = 'black'
	else:
		pocket_color = 'red'
for pocket_num in range(29, 36):
	if pocket_num%2==0:
		pocket_color = 'red'
	else:
		pocket_color = 'black'
if pocket_num <0 or pocket_num >36:
	print("Invalid Pocket number.")