# Parent #1
class Parent1():
    def skill(self, name):
        print("Parent skill One.");
        
# Parent #2
class Parent2():
    def skill(self, name, age):
        print("Parent skill Two.");
    
# Parent #3
class Parent3():
    def skill(self, name, age, gender):
        print("Parent skill Three.");
    
# Parent #4
class Parent4():
    def skill(self, name, age, gender, job):
        print("Parent skill Four.");
    
# Child Class
class Child(Parent1, Parent2, Parent3, Parent4):
    def skill(self):
        print("My skill is Programming.");
        
# create object from class
obj_child = Child();

# call method from object
obj_child.skill("Juan Taju", "27", "Male");

