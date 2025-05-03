def calculate_structure_sum(*data_structure, summ = 0,):
    #print(len(data_structure))
    qua_ele = len(data_structure)
    print(type(data_structure))
    my_string = ''.join(map(str, data_structure))
    print(my_string)
    print(len(my_string))
    i = 0
    if isinstance(my_string[i], int):
        summ += [i]
    elif isinstance(data_structure[i], str):
        summ += len(data_structure[i])
    elif isinstance(data_structure[i], list | dict | set | tuple):
        while i <= len(data_structure[i]):



            i += 1






data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]
print(*data_structure)
result = calculate_structure_sum(data_structure)
print(result)

while j <= len(data_structure[i]):
    if isinstance(data_structure[j], int):
        summ += data_structure[j]
    elif isinstance(data_structure[j], str):
        summ += len(data_structure[j])
    elif isinstance(data_structure[j], list | dict | set | tuple):
        j = +1