#!/user/bin/python
# -*- coding: utf-8 -*-
# Author : Kaushal Prajapati

heads = input("Enter Number of Heads:")
legs = input("Enter Number of Legs:")
if int(legs) % 2 !=0 or int(heads)==0:
	print("No solution!")
else:
	rabbits=int(heads)
	chicks=0
	while((rabbits + chicks) != heads and ((rabbits*4) + (chicks*2)) != int(legs)):
		rabbits = rabbits-1;
		chicks = chicks+1;
print("Chickens--------> %s \nRabbits--------> %s" %(chicks,rabbits))


