# Parent #1
class Parent1():
    def show(self):
        print("Parent One !!!");
        
# Child Class
class Child(Parent1):
    def show(self):
        print("This is child class.");
        
# create object from class
obj_child = Child();
obj_child.show();

