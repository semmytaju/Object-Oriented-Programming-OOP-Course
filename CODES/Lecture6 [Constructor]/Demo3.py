# create class
class Employee:

    # no-argument constructor
    def __init__(self):
        self.name = "Semmy" # static value
        self.address = "Bitung City" # static value

    # method print data
    def showInfo(self):
        print('Name:', self.name, 'Address:', self.address)

# create object of the class
semmy = Employee()

# call instance method using the object
semmy.showInfo()



