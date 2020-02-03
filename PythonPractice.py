Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:44:40) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 5
5
>>> X=5
>>> X+1
6
>>> print (x+1)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    print (x+1)
NameError: name 'x' is not defined
>>> print (X+)
SyntaxError: invalid syntax
>>> print (X+1)
6
>>> print (X)
5
>>> print 5
SyntaxError: Missing parentheses in call to 'print'
>>> print (5)
5
>>> int(32)
32
>>> int("32")
32
>>> int(hello)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    int(hello)
NameError: name 'hello' is not defined
>>> int ("hello")
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    int ("hello")
ValueError: invalid literal for int() with base 10: 'hello'
>>> int("hello")
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    int("hello")
ValueError: invalid literal for int() with base 10: 'hello'
>>> int('hello)
    
SyntaxError: EOL while scanning string literal
>>> int('hello')
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    int('hello')
ValueError: invalid literal for int() with base 10: 'hello'
>>> import math
>>> math
<module 'math' (built-in)>
>>> ratio = signal_power/noise_power
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    ratio = signal_power/noise_power
NameError: name 'signal_power' is not defined
>>> ratio = signal_power / noise_power
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    ratio = signal_power / noise_power
NameError: name 'signal_power' is not defined
>>> ratio = signal_power / noise_power
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    ratio = signal_power / noise_power
NameError: name 'signal_power' is not defined
>>> decibels = 10 * math.log(ratio)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    decibels = 10 * math.log(ratio)
NameError: name 'ratio' is not defined
>>> n=454
>>> 
>>> n=45
>>> radians=(n/180)*math.pi
>>> math.sin(radians)
0.7071067811865475
>>> math.sqrt1
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    math.sqrt1
AttributeError: 'module' object has no attribute 'sqrt1'
>>> math.sqrt(1)
1.0
>>> math.sqrt(2)/2.0
0.7071067811865476
>>> math.sqrt(2)/(2)
0.7071067811865476
>>> math.sqrt(1)/1
1.0
>>> x=math.sin(n/360*math.pi)
>>> x=math.exp(math.log(x+1))
>>> x=math.sin(n/360*math.pi)
>>> math.sin(n/360.0*2*math.pi)
0.7071067811865475
>>> math.exp(math.log(x+1))
1.3826834323650898
>>> def print_lyrics
SyntaxError: invalid syntax
>>> def print_lyrics():
	print("I'm a lumberjack, and I'm okay.")
	print("I sleep all night and I work all day.")

	
>>> def repeat_lyrics():
	print_lyrics()
	print_lyrics()

	
>>> repeat_lyrics()
I'm a lumberjack, and I'm okay.
I sleep all night and I work all day.
I'm a lumberjack, and I'm okay.
I sleep all night and I work all day.
>>> 
>>> def print_twice(bruce):
	print(bruce)
	print(bruce)

	
>>> print_twice('Spam')
Spam
Spam
>>> print_twice(42)
42
42
>>> print_twice(math.pi)
3.141592653589793
3.141592653589793
>>> def print_twice(bruce):
	print(bruce)
	print(bruce)

	
>>> #Python code to demonstrate pow()
>>> #version 1
>>> print("The value of 3**4 is : ",end="")
The value of 3**4 is : 
>>> #Returns 81
>>> print (pow(3,4))
81
>>> 3**4
81
>>> pow(3,4)
81
>>> def cat_twice(part1,part2):
	cat = part1 + part2
	print_twice(cat)

	
>>> line1 = 'Bing tiddle'
>>> line2 = 'tiddle bang.'
>>> cat_twice(line1,line2)
Bing tiddletiddle bang.
Bing tiddletiddle bang.
>>> 
