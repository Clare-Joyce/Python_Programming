def square_digits(num):
    a = str(num)
    sq_list = []
    for i in a:
        b = int(i)
        c = str(b**2)
        sq_list.append(c)
    sq_str = ''.join(map(str, sq_list))
    sq_nums = int(sq_str)
    return(sq_nums)
print(square_digits(2468))