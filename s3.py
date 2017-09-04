#!/usr/bin/python3
# guss what this program does????
import random
r=random.randint(23,49) # gives random num
print(r)
if r<35:
	print(r)
	print(": is less than 35")
elif r==30:
	print("30 ismultiple of 10 and 3 ,both")
elif r>=35:
    print(r,"is greater than 35")
else:
	print("your number is:",r)