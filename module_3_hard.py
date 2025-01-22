
def calculate_structure_sum(*sbor):
    op = []
    summ = []
    op = list(*sbor)
    summa = 0
    print(op)
    def calculate_part(*detal):
        print(type(detal))
        for j in range(len(detal)):
            if isinstance(detal[j], (int, float)):
                summ.append(detal[j])
            elif isinstance(detal[j], str):
                summ.append(len(detal[j]))
            elif isinstance(detal[j], dict):
                total = sum(value for value in detal[j].values() if isinstance(value, (int, float)))
                total2 = sum(len(keys) for keys in detal[j].keys() if isinstance(keys, (str)))
                summ.append(total)
                summ.append(total2)
        print(summ)
        return  summ
    #print(summa)
    for i in range(len(op)):
        if isinstance(op[i], (tuple, set, list)):
            detal = op[i]
            summa += sum(calculate_part(detal))
        elif isinstance(op[i], (int, float)):
            summa += op[i]
            print(summa)
        elif isinstance(op[i], str):
            summa += len(op[i])
            print(summa)
    return summa


data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)
