#!/user/bin/python
# -*- coding: utf-8 -*-
# Author : Kaushal Prajapati

def remove_duplicate_element(list_of_int):
	if type(list_of_int) != list:
		return False
	unique_list = []
	for num in list_of_int:
		if num not in unique_list:
			unique_list.append(num)	
	return unique_list

if __name__ == '__main__':
	res = remove_duplicate_element([1,2,55,1,3,2,34,55])
	if not res:
		print("Method accespt list type argument")
	else:
		print(res)
