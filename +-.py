a=[0,1,2,3,4,5,6,7,8,9,-1,-2,-3]
print(a)
for i in a:
    if(i<0):
        print(i)
        print("negative")
    if(i>0):
        print(i)
        print("positive")
    if(i==0):
        print(i)
        print("zero")
