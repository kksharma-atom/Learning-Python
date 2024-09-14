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
        self._tags = {}
    
    def insert_item(self, item):
        self._tags[item.lower()] = self._tags.get(item.lower(), 0) + 1
    
    def __getitem__(self, item):
        return self._tags.get(item.lower(), 0)
    
    def __setitem__(self, item, value):
        self._tags[item.lower()] = value

    def __len__(self):
        return len(self._tags)
    
    # To make the object of this class iterable, a built in function named iter is used. It returns an iterator object which gives us one item at a time in for loop
    def __iter__(self):
        return iter(self._tags)



cloud = Tagcloud()

cloud.insert_item("Python")
cloud.insert_item("python")
cloud.insert_item("Java")
cloud.insert_item("Java")
print(cloud._tags)

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
 

