# Defining parent class
class Parent(): 
        
    # Parent's show method
    def display(self):
        print("Inside Parent")
    
    
# Inherited or Sub class 
class Child(Parent): 
        
    # Child's show method
    def show(self):
        print("Inside Child")
    
# Inherited or Sub class
class GrandChild(Child): 
          
    # Child's show method
    def show(self):
        print("Inside GrandChild")         
    
# Create objects of the class
g = GrandChild()   
g.show()
g.display()

