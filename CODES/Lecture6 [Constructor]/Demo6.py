# create class
class Employee:
    # Parameterized constructor with default parameter values
    def __init__(self, name="Bryan Dadidu", age="25", salary=8000000):
        self.name = name
        self.age = age
        self.salary = salary

    # display data employee
    def showInfo(self):
        print("Name: {0}.".format(self.name));
        print("Age: {0} years old.".format(self.age));
        print("Salary: Rp. {0}.".format(self.salary));
        print("--------------------------------------");

# create multiple objects of the same class
test1 = Employee()
test1.showInfo()

test2 = Employee('Semmy Taju')
test2.showInfo()

test3 = Employee('Juan Walelang', 25)
test3.showInfo()

test4 = Employee('Patricia Mokodompit', 40, 6500000)
test4.showInfo()
