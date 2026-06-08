# -*- coding: utf-8 -*-
"""
    @Created : Tue Jan 17 06:52:31 2023
    @author  : SWT
    @desc    : Simple OOP
"""

# create class
class animal:
    # variable
    species = "bird"
    # method/constructor
    def __init__(self, name, age):
        self.name = name;
        self.age = age;

# create object
parrot = animal("parrot", 10)
sparrow = animal("sparrow", 15)

# view attributes parrot (burung beo) & sparrow (burung gereja)
print("1. parrot is a {}".format(parrot.__class__.species))
print("2. sparrow is also a {}".format(sparrow.__class__.species))
print("3. {0} is {1} years old".format(parrot.name, parrot.age))
print("4. {0} is {1} years old".format(sparrow.name, sparrow.age))