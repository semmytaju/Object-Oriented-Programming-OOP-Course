# Parent #1
class Parent1():
    def show(self):
        print("Parent One.");
        
# Parent #2
class Parent2():
    def show(self):
        print("Parent Two.");
        
# Child Class
class Child(Parent1, Parent2):
    def test(self):
        print("This is child class.");
        
# create object from class
obj_child = Child();

# call method from object
obj_child.show();

