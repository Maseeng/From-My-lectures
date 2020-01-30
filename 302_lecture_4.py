# -*- coding: utf-8 -*-
"""302 Lecture 4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/github/Maseeng/302_test_repo/blob/master/302_Lecture_4.ipynb

# **Type Conversion**

What's the difference between '15' and 15 without the quotes?
"""

Rapinoe = 15 #Pronounced Rah-PEE-no.
type(Rapinoe)

float(32) # converts an integer into a float what's the result?



"""How might we convert the integer, 42, to a string?"""

a = str(42) # code here
type(a)

"""How about converting 3.14149 to a string?"""

str(3.14)

"""Type conversion with expressions:"""

59/60

number = 59
number / 60.0

float(number) / 60 #converts to float for Python 2



"""# **Modules**"""

import math

math.pi #what does this do?

help(math.log) #handy way to find out more about things you may not understand. Documentation is cool.

"""# **Defining New Functions**"""

#This function prints a string
def print_strings():
  print ("Python Programming") #Indent is important
  print ("Super Cool")

# Run - or "call" - the function
print_strings()



"""**Execution Flow**"""

def WorkdayHours():
  print("Mon-Fri: 9-9")
def WeekendHours():
  print("Weekends: 11-5")

# Call two previously defined functions
def ShopHours():
  WorkdayHours()
  WeekendHours()

# Call the function
ShopHours()

"""**Function Arguments**"""

def print_twice(bruce): # the name 'bruce' is only here as a placeholder to tell 
  print(bruce)
  print(bruce)

bruce #try running "bruce"

"""A *parameter* is a variable. Arguments are the *data* you pass into the parameter. These can be the same, or different. Think of an argument as a placeholder for the actual input of the argument."""

print_twice(42)

"""The code above (lines 21 & 23) prints whatever argument you pass, twice. Create a function, that calls this function to print the passed argument 4 times."""

# Create a new function with a good name. 
# Perhaps call the previous function...
# Call the new function with a new argument.

"""# **Returned Values**
What's the output and order of the following code?
"""

def square(x):
  y = x * x
  return y
  # Generally you want a hard return/space in your code before you call the function
square(7)

"""Can we simplify this code by one line: make it "cleaner"?"""



"""What's the output and order of this code? (Hint, it uses the code above in line 26)"""

toSquare = 10
result = square(toSquare)
print("The result of", toSquare, "squared is", result)

"""# Exercise 1

Create and run a .py program to calculate the area of a circle. Formula for this is A = pi * r squared. So the function should take the radius as an input parameter and return area. Print the calculated area by calling the function.
"""

# Comment about what the code is for.
# Define a new function and give it a good name. It will take the radius for an argument. 
# Calculation for area (you can use math.pi instead of typing out the integer value of pi)
# return a value

#print statement contains the function call with an argument.

"""# Exercise 1 Answer"""

import math
def circle_area(r):
  # This function defines the area of a circle. Takes radius as the input. 
  a = r**2 * math.pi
  return a

print(circle_area(5))

"""# Exercise 2

Make your .py program interactive by using the `input` function. The syntax is `input()`.
Using the previous code, create a line that makes the argument passed for "r" equal to input from the user.
Exmple `r = input()`
Use type conversion to make sure integers are converted to floats in case the user enters a whole number.
"""

# import math
# user input for r here.

#define the function:
  # formula goes here. 
  # return formula result

# print function name with paramter.

"""# Exercise 2 Answer

This is one, possible, answer.
"""

import math
r = float(input("Input the radius of the circle: "))

def circle_area_input (r):
  # Function defines the area of a circle. 
  a = r**2 * math.pi
  return a

print(circle_area_input(r))