def get_multiplied_digits(number):
    str_number = str(number)
    #print(len(str_number))
    first = int(str_number[0])
    if len(str_number) <= 1:
        return first
    second = int(str_number[1:])
    return first * get_multiplied_digits(int(str_number[1:]))






result = get_multiplied_digits(40203)
print(result)
result2 = get_multiplied_digits(402030)
print(result2)
result3 = get_multiplied_digits(402031)
print(result3)