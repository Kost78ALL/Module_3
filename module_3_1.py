def count_calls():
	global calls
	calls += 1
	return calls
def string_info(string):
	str_U = string.upper()
	str_l = string.lower()
	str_len = len(string)
	string = (str_len,str_U,str_l,)
	#string = tuple(string)
	count_calls()
	return string
def if_contains(string, list_to_search):
	string = string.lower()
	for i in range(len(list_to_search)):
		list_to_search[i] = list_to_search[i].lower()
		cont = bool(list_to_search[i] == string)
		if cont:
			break
	#common_elements = [elem for elem in my_list if str(elem) in my_string]
	count_calls()
	return cont
	
calls = 0
print(string_info('Abrakadabra'))
print(string_info('Trahtibidoh'))
print(if_contains('Skorodom', ['rod','dom','skoRODOM']))
print(if_contains('Pochemuchka',['potom','zatem']))
print(string_info('right question includes answer'))
print((if_contains('Apocaliptica',['lips', 'local','aPOCaLIPtica'] )))
print(calls)

