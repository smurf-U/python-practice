#!/user/bin/python
# -*- coding: utf-8 -*-
# Author : Kaushal Prajapati

list_of_statment = []
while True:
	st = input("Enter Statement:")
	if st == 'exit':
		break
	list_of_statment.append(st.upper())
print('\n'.join(list_of_statment))
