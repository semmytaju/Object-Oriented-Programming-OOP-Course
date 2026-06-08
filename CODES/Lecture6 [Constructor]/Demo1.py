# create class 
class Student:

    # constructor (initialize instance variable)
    def __init__(self, name):
        print('Inside Constructor')
        self.name = name
        print('All variables initialized')

    # destructor
    def __del__(self):
        print('Inside destructor')
        print('Object destroyed')
        
    # instance Method
    def show(self):
        print('Hello, my name is', self.name)


# create object using constructor
s1 = Student('Semmy Wellem Taju')
s2 = Student('Eugenie Patricia Lamansiang')
s3 = Student('Putra Budy Harwaiyan')

# call method
s1.show()

# delete object
del s1

# call method
s1.show()

