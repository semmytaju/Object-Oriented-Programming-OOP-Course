# create class
class Teacher:
    # instance creator (new empty object)
    def __new__(cls, *args, **kwargs):
        print("1. Create a new instance of class Teacher.")
        return super().__new__(cls)

    # constructor (instance initializer)
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("2. Initialize the new instance of class Teacher.")
        print('My name is {0} ({1} years old).'.format(self.name, self.age));

    # string representator
    def __repr__(self) -> str:
        return f"{type(self).__name__}(name={self.name}, age={self.age})"
    
    # destructor (object is deleted or destroyed)
    def __del__(self):
        print('3. Object destroyed.')
        
# create object using constructor
t1 = Teacher('Semmy Taju', 30)
t2 = Teacher('Eugenie Lamansiang', 17)

# delete object
del t1
