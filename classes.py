# Class: Blueprint for creating new objects
# Object: Instance of a class
# self is a reference to the current object

class Point:
    # default_color is a class level attribute
    default_color = "red"

    # This is a class or factory method
    @classmethod
    def zero(cls):
        return cls(0, 0)

    def draw(self):
        print(f"Point ({self.xattribute}, {self.yattribute})")

    # __init__ and __str__ are magic methods
    def __init__(self, x, y):
        self.xattribute = x
        self.yattribute = y

    def __str__(self):
        return f"({self.xattribute}, {self.yattribute})"

    def __eq__(self, other) -> bool:
        return self.xattribute == other.xattribute and self.yattribute == other.yattribute

    def __gt__(self, other):
        return self.xattribute > other.xattribute and self.yattribute > other.yattribute
    
    def __add__(self, other):
        return Point(self.xattribute + other.xattribute, self.yattribute + other.yattribute)
        

point1 = Point(10, 20)
print(type(point1))
print(isinstance(point1, Point))

print(point1.xattribute)
point1.draw()

#Instance attributs vs Class attributes
# Instance attributes are different for each instance
point1.zattribute = 30
another = Point(11, 22) 
another.draw()
yetanother = Point(100, 200)
yetanother.draw()

Point.default_color = "green"
# Using object reference to read class level attr
print(point1.default_color)
print(another.default_color)
# Using class reference to read class level attr
print(Point.default_color)

# Instance vs Class methods
# __init__ and draw are instance methods
# class methods can be used for initialization purpose and also known as factory method
point2 = Point.zero()
point2.draw()


# Magic methods
# __init__ and __str__ are magic methods
print(another)

# Comparing objects
point11 = Point(12, 14)
point12 = Point(2, 4)
# Result is false because the addresses are compared. So using magic method for comparison __eq__ . After implementing __eq__, result is true
print(point11 == point12)
# Using __gt__ magic method here
print(point11 > point12)

# Arithmetic operation between two objects using magic methods (Numeric magic methods) like __add__, __sub__, etc
print(point11 + point12)

# Making custom containers
class Tagcloud:

    def __init__(self) -> None:
        self.tags = {}
    
    def insert_item(self, item):
        self.tags[item.lower()] = self.tags.get(item.lower(), 0) + 1
    
    def __getitem__(self, item):
        return self.tags.get(item.lower(), 0)
    
    def __setitem__(self, item, value):
        self.tags[item.lower()] = value

    def __len__(self):
        return len(self.tags)
    
    # To make the object of this class iterable, a built in function named iter is used. It returns an iterator object which gives us one item at a time in for loop
    def __iter__(self):
        return iter(self.tags)



cloud = Tagcloud()

cloud.insert_item("Python")
cloud.insert_item("python")
cloud.insert_item("Java")
cloud.insert_item("Java")
print(cloud.tags)

cloud["Java"] = 12

print(cloud["Java"])
print(len(cloud))

# Private members
# By prefixing __ , the attributes can be made private. For example, to make tags dictionary private, tags needs to be replaced by __tags
# The concept here is not of security. Rather, it is to prevent accidental access of private members.
# However, even after making member private, it can be accessed using __dict__. 
# Every object has a property __dict__ 
# print(cloud.__dict__) which outputs __TagCloud__tags
# print(cloud.__TagCloud_tags)

print(cloud.__dict__)

# Properties
class Product:
    def __init__(self, price) -> None:
        self._price = price

    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self._price = value
 
product1 = Product(20)
print(product1.price)

# Inheritance
# object is the base class for all classes in Python.
o = object()
print(isinstance(product1, object))
print(issubclass(Product, object))

# Method overriding
class Animal:
    def __init__(self) -> None:
        self.age = 1
    
    def eat(self):
        print("eat")

class Mammal(Animal):
    # This constructor overrides the parent class constructor
    def __init__(self) -> None:
        super().__init__()
        self.weight = 2

    def walk(self):
        print("walk")


m = Mammal()
# print(m.age) This line gives an error --> Mammal object has no attribute age. 
# Still, if we need to call the parent class constructor, use super
print(m.age)
print(m.weight)

# Multi level inheritance
# One or two level of inheritance is okay but anything beyond that is bad, since it increases complexities in the code.

# Multiple inheritance
# Bad implementation
class Employee:
    def greet(self):
        print("Employee greet")

class Person:
    def greet(self):
        print("Person greet")

class Manager(Employee, Person):
    pass

manager1 = Manager()
manager1.greet()

# Good implementation of multiple inheritance is when both the parent classes have nothing in common. Note that both the classes Flyer and Swimmer have nothing in common. The class FlyingFish inherits both the classes which have nothing in common.
class Flyer:
    def fly(self):
        pass

class Swimmer:
    def swim(self):
        pass

class FlyingFish(Flyer, Swimmer):
    pass

# A good example of inheritance 
# Concept of abstract base class
# An abstract class cannot be initiated. It is like a half baked cookie. 
# By using the decorator @abstractmethod, we are enforcing all the child classes to implement this method. Otherwise, they also would be considered abstract.

from abc import ABC, abstractmethod

class InvalidOperationError(Exception):
    pass

class Stream(ABC):
    def __init__(self) -> None:
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOperationError("Stream already open")
        self.opened = True

    def close(self):
        if not self.opened:
            raise InvalidOperationError("Stream already closed")
        self.opened = False

    @abstractmethod
    def read(self):
        pass

class FileStream(Stream):
    def read(self):
        print("Reading data from a file")


class NetworkStream(Stream):
    def read(self):
        print("Reading data from a network")

class MemoryStream(Stream):
    pass

# stream1 = MemoryStream() 
# The above line gives an error. Since, the MemoryStream class has not implemented read method, it is also considered abstract.

# Polymorphism

class UIControl(ABC):
    @abstractmethod
    def draw(self):
        pass

class TextBox(UIControl):
    def draw(self):
        print("TextBox")

class DropDownList(UIControl):
    def draw(self):
        print("DropDownList")

# Here, the draw() method exhibits polymorphic behaviour. It does not know the control which is being passed to it. At runtime it renders the control. Thus, it takes many forms. Hence, the term Poly (many) morph (forms) Polymorphism.
def draw(controls):
    for control in controls:
        control.draw()

textbox1 = TextBox()
dropdownlist1 = DropDownList()
draw([textbox1, dropdownlist1])

# Duck Typing
# Even if we delete the UIControl class, the code will run as before i.e. the draw method will be polymorphic. Since, all it needs is a control object and it should have a draw method, irrespective of whether it is derived from a parent class called UIControl. 
# If it walks like a duck and quacks like a duck it is a duck!!!
# However, having abstract base class is a good thing, since it enforces a common behaviour among all it's descendants.

# Extending built in types
# Extending string class
class Text(str):
    def duplicate(self):
        return self + self

text1 = Text("Python")
print(text1.lower())
print(text1.duplicate())

# Extending lists
# Here, we have extended the functionality of append method of list class
class TrackableList(list):
    def append(self, object) -> None:
        print("Append called")
        super().append(object)

list1 = TrackableList()
list1.append("1")
print(list1)

# Data classes
# Classes where there are only attributes i.e. data and no methods are called Data classes

# class Point:
#     def __init__(self, x, y) -> None:
#         self.x = x
#         self.y = y

#     def __eq__(self, other) -> bool:
#         return self.x == other.x and self.y == other.y

# If we have classes that only have data and no methods, then we can use namedtuple instead of the above code. namedtuple are a concise way to represent such classes
# namedtuples are immutable
# No need of magic methods while using namedtuple

from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])

p1 = Point(x=1, y=2)
p2 = Point(x=1, y=2)
print(id(p1))
print(id(p2))
print(p1 == p2)


