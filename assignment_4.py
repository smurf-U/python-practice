#!/user/bin/python
# -*- coding: utf-8 -*-
# Author : Kaushal Prajapati

def count_word_len(list_of_str):
	if type(list_of_str) != list:
		return False
	str_len_dict = dict()
	for word in list_of_str:
		str_len_dict.update({word:list_of_str.count(word)})
	return str_len_dict

if __name__ == '__main__':
	res = count_word_len(['python', 'pyhton3', 'user1', 'assignment', 'user', 'user1', 'python', 'User1'])
	if not res:
		print("Method accespt list type argument")
	else:
		print(res)
