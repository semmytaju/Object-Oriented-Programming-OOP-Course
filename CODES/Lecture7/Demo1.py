# create class
class Animal:
  
  # data members of class
  color = "black"     # attribute 1
  species  = "Dog"    # attribute 2
   
  # constructor
  def __init__(self, species , color): 
    self.species = species 
    self.color = color
  
  # user defined function or method
  def func(self):
    print("After calling func() method.")
    print("Species type is", self.species)
    print("Its color is", self.color)


# objects are created and the parameterized constructor is called 
obj_cat = Animal('Cat', 'white') # object 1
obj_dog = Animal('Dog', 'Black') # object 2
obj_bird = Animal('Bird', 'Red') # object 3

# user-defined function is called from object 1 
obj_cat.func()

# access the attribute
print("\nDirect access of attributes using object.")
print(obj_cat.species)

