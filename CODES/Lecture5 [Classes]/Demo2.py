# create class
class Student:
    
    # Instance attribute in method constructor (default method)
    def __init__(self, name):
        self.name = name;
         
    # method #1 (create a function)
    def info(self):
        print("My name is {}.".format(self.name))

# main file
if __name__ == "__main__":    
    # create objects
    Rodger = Student("Rodger Patty")
    Tommy = Student("Tommy Modoaggo")
    Semmy = Student("Semmy Bambo")
    Julius = Student("Julius Meisi")
    Paksi = Student("Paksi Tegar")
    Putri = Student("Putri Mamarimbing")
    
    # Accessing class methods
    Julius.info()



