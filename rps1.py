#!/usr/bin/python3.6
import random


t=["stone","paper","scissors"]

comp=t[random.randint(0,2)]
my_ch=false
while my_ch==false:
	
	my_ch=input("rock ,paper, scissors")
	if comp==my_ch:
		print("tie")
	elif my_ch==stone
		if comp=="scissors":
			print("u win")
		if comp=="paper":
			print("u lose")
		
	elif my_ch==paper
		if comp=="scissors":
			print("u lose")
		if comp=="stone":
			print("u win")
		
	elif my_ch==scissors
		if comp=="stone":	
			print("u lose")
		if comp=="paper":
			print("u win")
		