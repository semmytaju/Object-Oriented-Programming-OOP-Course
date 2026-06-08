# create parent class
class Bird:
     def intro(self):
        print("There are several different types of bird species.")
  
     def fly(self):
        print("Almost all birds can fly, but there are some that cannot.")
         
# create child class 1  
class Eagle(Bird):
    
     def fly(self):
        print("Yes, an eagle can fly.")
     
# create child class 2  
class Weka(Bird):
    
     def fly(self):
        print("No, an Weka can't fly.")
  
# # object of parent class & child class created
obj_burung = Bird()
obj_elang = Eagle()
obj_weka = Weka()
  
# user-defined function is called from obj_burung (parent class) 
obj_burung.intro()
obj_burung.fly()
  
# user-defined function is called from obj_elang (child class) 
obj_elang.intro()
obj_elang.fly()
  
# user-defined function is called from obj_weka (child class) 
obj_weka.intro()
obj_weka.fly()