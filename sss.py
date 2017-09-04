#1/usr/bin/python3
import random
i=0
def myroll():
while(i<=0):
    n=input("press r to roll the dice")
    if(n=='r'):
        r=myroll()
        i=i+r
        print("new position is",i)


def myroll():
	return random.randint(1,6)