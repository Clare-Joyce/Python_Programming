def format_name(first_name, last_name):
	# code goes here
	if first_name == "":
		full_name = last_name
	elif last_name == "":
		full_name = first_name
	elif last_name == first_name == "":
		full_name = ""
	else:
		full_name = last_name + ", " + first_name
	
	return "Name: " + full_name 

print(format_name("Ernest", "Hemingway"))
# Should return the string "Name: Hemingway, Ernest"

print(format_name("", "Madonna"))
# Should return the string "Name: Madonna"

print(format_name("Voltaire", ""))
# Should return the string "Name: Voltaire"

print(format_name("", ""))
# Should return an empty string