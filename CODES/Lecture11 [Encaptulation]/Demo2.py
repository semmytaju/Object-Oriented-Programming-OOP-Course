# create class
class Employee:
    
    # parameterized constructor
    def __init__(self, name, salary):
        
        # public data members
        self.name = name          # public variable
        
        # private member
        self.__salary = salary    # private variable

    # public instance methods
    def display(self):
        # accessing public data member
        print("Name: ", self.name, 'Salary:', self.__salary)


# creating object of a class
unklab_emp = Employee('Semmy Wellem Taju', 2000000)
yzu_emp = Employee('Semmy Wellem Taju', 3000000)
ntu_emp = Employee('Semmy Wellem Taju', 4000000)
ccu_emp = Employee('Semmy Wellem Taju', 5000000)

# calling public method of the class
unklab_emp.display()
yzu_emp.display()
ntu_emp.display()
ccu_emp.display()

# accessing public data members
print("Name: ", unklab_emp.name, 'Salary:', unklab_emp.__salary)
print("Name: ", yzu_emp.name, 'Salary:', yzu_emp.__salary)
print("Name: ", ntu_emp.name, 'Salary:', ntu_emp.__salary)
print("Name: ", ccu_emp.name, 'Salary:', ccu_emp.__salary)


