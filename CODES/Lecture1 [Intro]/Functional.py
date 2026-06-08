# -*- coding: utf-8 -*-
"""
    @Created : Tue Jan 17 06:52:31 2023
    @author  : SWT
    @desc    : Simple Functional Programming
"""

# variable
species = "bird"

# method/functions
def bird_parrot(name, age):
    print("3. {0} is {1} years old".format(name, age))

def bird_sparrow(name, age):
    print("4. {0} is {1} years old".format(name, age))


# view variable parrot (burung beo) & sparrow (burung gereja)
print("1. parrot is a {}".format(species))
print("2. sparrow is also a {}".format(species))

# call functions
bird_parrot("parrot", 10)
bird_sparrow("sparrow", 15)