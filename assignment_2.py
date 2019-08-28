#!/user/bin/python
# -*- coding: utf-8 -*-
# Author : Kaushal Prajapati

st = input("Enter Statement:")
list_st = list(set(st.split(' ')))
list_st.sort()
print(' '.join(list_st))

