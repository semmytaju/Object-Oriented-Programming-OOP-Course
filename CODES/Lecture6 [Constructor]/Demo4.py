# create class
class Employee:
    # parameterized constructor
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    # display data employee
    def showInfo(self):
        print(self.name, self.age, self.salary)

# create object of the Employee class
semmy = Employee('Semmy Taju', 23, 7000000)
semmy.showInfo()

kelly = Employee('Kelly Tanos', 25, 8500000)
kelly.showInfo()

