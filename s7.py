Python 3.6.2 (default, Jul 20 2017, 08:43:29) 
[GCC 6.3.0 20170406] on linux
Type "copyright", "credits" or "license()" for more information.
>>> for i in range(o,20:
	       
SyntaxError: invalid syntax
>>> for i in range(0,20):
          if(i%2==0):
		  print(i<"is an even num")
		  
SyntaxError: inconsistent use of tabs and spaces in indentation
>>> print(i,"is an even num")
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    print(i,"is an even num")
NameError: name 'i' is not defined
>>> for i in range(0,20):
	if(i%2==0):
		print(i,"is an even num")

		
0 is an even num
2 is an even num
4 is an even num
6 is an even num
8 is an even num
10 is an even num
12 is an even num
14 is an even num
16 is an even num
18 is an even num
>>> 
