# Parent Class
class Human:
    # Declaring public method
    def funny(self):
        print("Public method")
 
    # Declaring private method
    def __funny(self):
        print("Private method")
 
# Child Class
class Teacher(Human):
    # Method #1
    def call_public(self):
        # Calling public method of parent class
        print("\nInside Teacher class")
        self.funny()
    
    # Method #2
    def call_private(self):
        # Calling private method of parent class
        self.__funny()
 
 
# Parent Class
obj1 = Human()
obj1.funny()     # Calling public method
obj1.__funny()   # raise an AttributeError

# Child Class
obj2 = Teacher()
obj2.call_public()   # Calling public method
obj2.call_private()  # raise an AttributeError

