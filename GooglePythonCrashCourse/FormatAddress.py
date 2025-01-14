def format_address(address_string):
    # Declare variables
    house_number = ""
    street_name = ""

    # Separate the address string into parts
    address_content = address_string.split()
    # Traverse through the address parts
    for string in address_content:
    # Determine if the address part is the
    # house number or part of the street name
        if string.isnumeric():
            house_number = string
        else:
            street_name = street_name + " " + string

    # Does anything else need to be done 
    # before returning the result?

    # Return the formatted string  
    return "house number {} on street named {}".format(house_number, street_name.strip())

print(format_address("123 Main Street"))
# Should print: "house number 123 on street named Main Street"

print(format_address("1001 1st Ave"))
# Should print: "house number 1001 on street named 1st Ave"

print(format_address("55 North Center Drive"))
# Should print "house number 55 on street named North Center Drive"
