# Parent #1
class Parent1():
    def show(self):
        print("Parent One.");
        
# Parent #2
class Parent2():
    def shows(self):
        print("Parent Two.");
    
# Parent #3
class Parent3():
    def shows(self):
        print("Parent Three.");
    
# Child Class
class Child(Parent3, Parent2, Parent1):
    def shows(self):
        print("This is child class.");
        
# create object from class
obj_child = Child();

# call method from object
obj_child.show();

