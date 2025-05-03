# test_list = ['gfg', 1, 2, 'is', 'best']
#
# # printing original list
# print("The original list : " + str(test_list))
#
# # Split heterogeneous type list
# # using list comprehension + isinstance
# res_str = [ele for ele in test_list if isinstance(ele, str)]
# res_int = [ele for ele in test_list if isinstance(ele, int)]
#
# # printing result
# print("Integer list : " + str(res_int))
# # print("String list : " + str(res_str))
#
# test_tup = ('gfg', 1, ['is', 'best'])
# print("Исходный кортеж равен: " + str(test_tup))
#
# # Получаем типы данных элементов кортежа
# res = list(map(type, test_tup))
# print("Типы данных кортежа по порядку следующие: " + str(res))
#
# a=('!',',','?')
# s='dasd,sadarg!ada'
# ''.join(filter(lambda x: x not in a, s))
# 'dasdsadargada'
#
# punct = ('[', ']', '{', '}', ':', '(', ')')
# # no_punct = ''.join([c for c in op if c not in punct])
# # print(punct)
#
# import collections
#
# test_tup = ('gfg', 1, ['is', 'best'])
#
# print("The original tuple is : " + str(test_tup))
#
# # Get tuple element data types
# # Using collections.Sequence + isinstance() + type()
# res = [(type(ele), len(ele) if isinstance(ele, collections.test_tup) else None) for ele in test_tup]
#
# data = (4.5, 8.7, True, "книга", 8, 10, -11, [True, False])
# s = 0
# for x in data:
#     if isinstance(x, (str)):
#         s += len(x)
#
# print(s)
sbor = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]
op = list(sbor)
summa = 0
print(1+2+3+1+4+1+5+6+4+7+4+8+5+2+5+6+35)
for i in range(len(op)):
    if isinstance(op[i],(tuple,set,list)):
        opt = op[i]
        for j in range(len(opt)):
            if isinstance(opt[j],(int,float)):
                summa += opt[j]
            elif isinstance(opt[j],str):
                summa += len(opt[j])
            elif isinstance(opt[j],dict):
                total = sum(value for value in opt[j].values() if isinstance(value, (int, float)))
                total2 = sum(len(keys) for keys in opt[j].keys() if isinstance(keys, (str)))
                summa += total + total2
        print(summa)
    elif isinstance(op[i],(int,float)):
        summa += op[i]
        print(summa)
    elif isinstance(op[i],str):
        summa += len(op[i])
        print(summa)
print(summa)




