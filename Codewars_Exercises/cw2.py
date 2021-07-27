def square_digits(num):
    sq_list = []
    for i in str(num):
        sq_list.append(str(int(i)**2))
    sq_nums = int(''.join(map(str, sq_list))) 
    return(sq_nums)
print(square_digits(2468))