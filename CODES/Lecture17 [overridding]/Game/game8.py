# Parent #1
class Parent1():
    def skill(self):
        print("Parent skill One.");
        
# Parent #2
class Parent2():
    def skill(self):
        print("Parent skill Two.");
    
# Parent #3
class Parent3():
    def skill(self):
        print("Parent skill Three.");
    
# Child Class
class Child(Parent1, Parent2, Parent3):
    def skills(self):
        print("My skill is Programming.");
        
# create object from class
obj_child = Child();

# call method from object
obj_child.skill();

