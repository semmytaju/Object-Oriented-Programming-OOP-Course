# create class
class Employee:
    # constructor #1
    def __init__(self, name):
        self.name = name
      
    # constructor #2
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    # constructor #3    
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    # display data employee
    def showInfo(self):
        print(self.name)

# create object of the Employee class
test1 = Employee('Semmy Taju')
test1.showInfo()

test2 = Employee('Juan Walelang', 25, 8500000)
test2.showInfo()

test3 = Employee('Patricia Mokodompit', 25, 8500000)
test3.showInfo()
