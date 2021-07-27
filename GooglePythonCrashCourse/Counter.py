def counter(start, stop):
    
    """
    The counter function counts down from start to 
    stop when start is bigger than stop, and counts 
    up from start to stop otherwise
    """
    x = start
    if x > stop:
        return_string = "Counting down: "
        while x >= stop:
            return_string += str(x)
            if x>stop:
                return_string += ","
            x = x -1         
    else:
        return_string = "Counting up: "
        while x <= stop:
            return_string += str(x)
            if x < stop:
                return_string += ","
            x = x + 1
    return return_string
print(counter(5, 1))
print(counter(1, 11))
print(counter(5, 5))