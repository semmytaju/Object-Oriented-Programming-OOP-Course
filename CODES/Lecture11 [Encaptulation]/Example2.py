# Creating a class
class Student:

    # Declaring public method
    def funny(self):
        print("Public method")
 
    # Declaring private method
    def __funny(self):
        print("Private method")
 
    # Declaring public method
    def Help(self):
        self.funny()   # public method
        self.__funny() # private method
 
# Create object
obj_semmy = Student()
obj_semmy.Help() # public method



