# Defining parent class
class Parent():
      
    # Constructor
    def __init__(self):
        self.value = "Inside Parent"
          
    # Parent's show method
    def show(self):
        print(self.value)
          
# Defining child class
class Child(Parent):
      
    # Constructor
    def __init__(self):
        self.value = "Inside Child"
          
    # Child's show method
    def show(self):
        print(self.value)
          
          
# create objects of the class
obj1 = Parent()
obj2 = Child()
  
obj1.show()
obj2.show()

