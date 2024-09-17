#  List, Tuple, Set, and Dictionary are the examples of data structures in Python.

# To create a list with hundred zeroes

zeros = [0] * 100
print(zeros)

# Use + to combine lists

# The objects can be of different type like numbers, strings, boolean, or even lists

# The list function takes an iterable object as an argument. The range object returns an iterable object.

print(list(range(20)))

# The above line creates a list of 20 numbers starting from 0.

chars = list("Hello")

# To get the length of a list
print(len(chars))

# Accessing items in the list
# To access last item in the list
print(chars[-1])

# To slice a list
# The below line of code returns the first two items from the list starting from index 0
print(chars[0:2])

# If the first index is not specified, it is assumed by default.
print(chars[:2])

# If the end index is not specified, the length of the list is used
print(chars[0:])

# If both the index are not specified, the copy of the list is returned
print(chars[:])

# To get stepwise items from the list
print(chars[::2])

# To get even numbers, step of 2
numbers1 = list(range(20))
print(numbers1[::2])

# To get reverse of list. Step of -1
print(chars[::-1])

# UNPACKING LISTS

numbers2 = [1, 2, 3]
first, second, third, *other = numbers2
print(first)

# Unpacking and packing simultaneously
# Remember, number1 contains numbers from 0 to 19
first, second, third, *other = numbers1
print(other)


# To get the first and last item in the list
first, *other, last = numbers1
print(first, last)

# LOOPING OVER LISTS

# The enumerate() function returns an iterable object. In each iteration, this object gives a tuple which contains the index and the item at that index.

for index, letter in enumerate(chars):
    print(index, letter)

# In the above code, we are unpacking the tuple returned by enumerate() in each iteration.

# ADDING OR REMOVING ITEMS IN THE LIST

# append, insert, pop, remove (first occurence), del statement (remove range of items), and clear (remove all objects in the list)

# FINDING ITEMS

# Using the in operator for determining if an object exists in the list

print(numbers2)
print(numbers2.count(2))
if 2 in numbers2:
    print(numbers2.index(2))

# SORTING LISTS

# There are two options to sort lists. First is the sort method, which modifies the original list

numbers3 = [51, 3, 1, 10, 19]
numbers3.sort(reverse = True)
print(numbers3)

# Second option is to use the sorted function. It does not modify the original list i.e. numbers3 in this case.
print(sorted(numbers3, reverse = True))
print(numbers3)

# What if the items in the list are tuples? How can they be sorted?

items = [
    ("Toy", 30),
    ("T-Shirt", 5),
    ("Bag", 40)
]
# The below two lines of code won't work.
# items.sort()
# print(items)
def sort_item(item):
    return item[1]
# The above function takes a tuple and returns the price which is the second item in each tuple.

items.sort(key=sort_item)
print(items)
# In the sort method, the sort_item function is referenced and not called. 

# LAMBDA FUNCTIONS

# The above code can be implemented using lambda function, which is an anonymous function. The syntax is lambda arguments: expression

listoftuples = [
    ("a", 5),
    ("b", 11),
    ("c", 1)
]

listoftuples.sort(key = lambda item: item[1], reverse=True)
print(listoftuples)

# MAP FUNCTION
# Here, we are applying map function to the numbers3 list.
print(list(map(lambda item: item[1] + 1, listoftuples)))

# FILTER FUNCTION
# Here, we are applying filter function to the items list which contains tuples of product name and price

print(items)
print(list(filter(lambda item: item[1] > 25, items)))
# The above code filters the items list and returns items which have a price greater than 25.

# LIST COMPREHENSION
# map and filter function can be replaced by a concept called list comprehension in Python. 
# The syntax is expression for item in itertable if condition.

# This line of code is equivalent to map function
price = [item[1] for item in items]
print(price)

# This line of code is equivalent to filter function
price_morethan_25 = [item[0] for item in items if item[1] >25]
print(price_morethan_25)

# ZIP FUNCTION

# It is used to combine two lists into tuples
# Cannot use map or filter since they work with single lists

list11 = [1, 2, 3]
list12 = [11, 22, 33]
print(list(zip("abc",list11, list12)))

# STACK

# LIFO behaviour

browsing_session = []
browsing_session.append(1)
browsing_session.append(2)
browsing_session.append(3)
print(browsing_session)

browsing_session.pop()
print(browsing_session)

if not browsing_session:
    print("redirect",browsing_session[-1])

# QUEUES

# FIFO behaviour

# use deque object

from collections import deque

queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)
print(queue)

queue.popleft()
print(queue)

if not queue:
    print("empty")


# TUPLES
# Cannot modify
# parantheseis instead of square brackets. Can even exlude paranthesis

point1 = 1, 2
print(type(point1))

# Empty tuple
point11 = ()

# This is a tuple since it has trailing comma. If the trailing comma is removed, it becomes an integer
point22 = 1,

# Concatenate tuple
point33 = (11, 22) + (44, 55)

# Repeat tuple
point44 = (1, 2) * 3

# Use tuple function to convert list to tuple
point55 = tuple([1, 2])
point66 = tuple("Hello")

# SWAPPING VARIABLES WITHOUT A THIRD ONE

x = 11
y = 22

# Here, tuple is defined on the right side and then unpacked
x, y = y, x

print("x", x)
print("y", y)

# ARRAYS
# To be used only when dealing with large set of numbers and encountering performance problems with lists

from array import array

numbers55 = array("i", [1, 2, 3])

# SETS
# Collection with no duplicates
# Curly braces are used to define set
# Cannot access items by index in set since they are unordered

# The set function removes all duplicates from the list and converts it to a set
list66 = [1, 1, 2, 2, 3, 3, 3, 5, 5]
uniques1 = set(list66)
uniques2 = {5, 6, 7}
print(uniques1)

# Union
print(uniques1 | uniques2)

# Intersection
print(uniques1 & uniques2)

# Difference
print(uniques1 - uniques2)

# Symmetric Difference
print(uniques1 ^ uniques2)

# DICTIONARY
# Collection of key value pair
# Real world example is a phonebook
# Access items using keys

point77 = {"x": 1, "y": 2}
point88 = dict(x=2, y=9)

print(point88.get("x"))

# Looping over dictionary
# Option 1
for key in point88:
    print(key, point88[key])

# Option 2
for key, value in point88.items():
    print(key, value)

# In option 2, the items method returns a tuple like this (key, value). Then we unpack the tuple and print both.
# Just like items method, there is a values method which returns only the values and a keys method which returns only the keys.

# Dictionary Comprehensions
# values = {}
# for x in range(5):
#     values[x] = x * 2

# The above code can be written ina concise way using comprehension
# The syntax is 
# expression for item in iterable

values1 = {x: x * 2 for x in range(5)}
print(values1)

# Comprehension can be used in list, set, dictionary
# Let's see what happens if comprehension is used in tuple
values22 = (x + 2 for x in range(5))
print(values22)

# When the above code is run, we get a generator object instead of a tuple.

# GENERATOR OBJECT
# When working with a humumgous amount of data, the generator object is used. 
# It doesn't store all the values in memory. Instead, it generates or spits out data when we iterate over it.
# So, for the above code, we iterate over values22

for x in values22:
    print(x)

# Size of generator object
from sys import getsizeof

values88 = (x + 2 for x in range(100000))
print(getsizeof(values88))
# The above two lines of code, when run, give an output of 200. So the size of generator object is 200.

values88 = [x + 2 for x in range(100000)]
print(getsizeof(values88))
# The above two lines of code, when run, give an output of 800984. So the size of list object is 800984. 
# This goes on to show that the generator object occupies very less space im memory comparatively.
# So, when dealing with large dataset, generator object needs to be used.
# Cannot get the length of the generator object since the items can only be accessed when the generator object is iterated upon. So, cannot know ahead of time.

# UNPACKING OPERATOR
# * is the unpacking operator 
print([*range(5), *"World"])

# Unpacking dictionary
dict11 = dict(x=11, y=22, z= 33)
dict22 = dict(m=88)

combined = {**dict11, **dict22}
print(combined)

# EXERCISE
# sentence = "This is a common interview question"
# Find out the most repeated character in the above sentence
sentence = "This is a common interview question"
letters = [*sentence]
print(letters)

dict33 = {}
for letter in letters:
    dict33[letter] = dict33.get(letter, 0) + 1

# list99 = []
# for everyentry in dict33.items():
#     list99.append(everyentry)

# list99.sort(key = lambda x: x[1], reverse=True)

# print(list99[0])
# The above code is also correct. But the below code is the concise way of doing the same thing.
char_frequency_sorted = sorted(dict33.items(),key=lambda x:x[1], reverse=True)

print(char_frequency_sorted[0])


 





