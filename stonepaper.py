#!/usr/bin/python3.6
import random
choice=["stone","paper","scissors"]

comp=choice[random.randint(0,2)]
my_ch=input("enter ur choice:")
if comp==my_ch:
	print("tie")
elif comp==stone and my_ch==paper:
	print("u win")
if comp==paper and my_ch==scissors:
	print("u win")
else:
	print("u lose")