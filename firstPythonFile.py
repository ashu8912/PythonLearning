#restrictions with python variables
#variable in python can start with _ or letter no any other character 
#allowed at the front position of name
#variables are case sensitive varaible x is different than variable X
"""
this is a multiline comment
"""
"""
Naming Convention for variables
variables must be lowercase
variables must be named snake_case
constants are uppercase SNAKE_CASE
UpperCamelCase is used for classes
variables that start with two underscores(dunder) are supposed to be 
private or left alone
"""
#DATA TYPES
"""
1.Boolean True or False
2.integer
3.string can be declared with single as well as double quote
4.list
5.dictionary
type() method help us check data type for a variable passed as argument
python is a dynaimcally typed language
so a varaible can be reassigned to any type 
None is also a type,used to represent null or empty value
"""
"""
8+"hello" is an error
String Formatting

String Interpolation 
F-strings(python3.6+)
f"this is {x} times better"
for python3.5 and below
"this is {}".format(x)
"""
'''
"hello"[1] gives e
"hello"[-1] gives o so negative indexes are also allowed
"hello"[5] throws error saying string out of bound exception
'''
#converting data types
'''
int(someDecimalNumber) spits integer number
str(someNumber) will spit string
float(num) will spit float
'''
'''
input() is used to take input from user
it returns string;;;

round(number to round,how many decimal places)

#Conditionals
if condition:{
	doSomething
}
elif condition:{
	doSomething
}else:{
	doSomething
}

indentation matters for conditional blocks
if not using {}
'''
'''
#Truthiness and falsiness
falsiness include empty object,empty string,
None,zero
'''
'''
#Logical Operators
and,or,not
if a and b:
	condition
elif a or b:
     condition
if not a:
   condition       	
'''
'''
check for equality
== or is
a=1;
a==1;//true
a is 1;//true
== checks for value but is checks that 
they are stored on the same memory location
a=[1,2,3]
b=[1,2,3]
a==b;//true
a is b;//false
'''
'''
import random
random.randint(start,end)=>end is exclusive here
range(start,end,interval)=>used to create a particular set of
integers which we can loop over

'''
'''
lists is an array dataStructure but it can contain
different dataTypes in it 
len(array) is used to find the length of array
range(1,10) can be converted to list using list(range())
to check whether an element in list we use element in list 
it returns true or false
'''
'''
list's util methods are append,extend,insert
clear => deletes all elements in a list
pop(index) =>if index not passed it will remove from last
remove(num)=>deletes the first num found
index(num,startPoint) =>gives us the index of num 
count(num)=>counts the number of occurence of num in a list

reverse()=>reverses a list inplace
join()=>' '.join(list)=>joins all elements of list with a space
slice => array[start:end:step]
to make a complete copy of the array
use array[:] where array is the list you want to make copy of
'''
'''
dictionaries
similar to javascript objects
dict(key=value)
to check a key in dictionary 
use the in operator 
'property' in instructor
we can check for key using other way also 
that is dictionary.keys() and using in on this
we can also do dictionary.values() to check whether a value is 
there in dictionaryit returns a list like
data structure(not actual list) where we can do
property in dictionary.values()
#dictionary methods
clear=>empties the dictionary
dictionary.copy()=>creates a copy
fromKeys(key or keys list iterable,value)
get(key)=>returns None if not found and doesn't throws error 
'''
'''
tuple
alphabets=('a','b','c','d')
tuples are immutable meaning it can't be changed
than why use tuple??
coz tuples are lighter weight and faster than lists
use them when you know something is going to be same for an
entire execution of a program
we can access tuples by the square bracket syntax
tuple[0]
tuples can be used as key in dictionary
tuples.count(value) returns how many time the value occured in tuple
tuples.index(value) returns the index of value if not found than value error
we can use slices with tuples
'''
'''
Sets
sets do not have duplicate value
elements in set are not ordered 
we can't access element with index
syntax:
variable={1,2,3,4,5}
to check whether an element is in a set use
variable in set
set methods:
name_of_set.add(value)=>adds the value to set
name_of_set.remove(value)=>removes if not found throws error
name_of_set.discard(value)=>doesn't throws error when not found
name_of_set.copy(set)
name_of_sets.clear()
union in sets name_of_set | name_of_set
intersection in sets name_of_set & name_of_set
'''