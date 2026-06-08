# create class
class Calculator:
    def __init__(self):
        print("Simple Calculator !!!");
        
    #  method argument default
    def compute(self, x = 0, y = 0, operation="sum"):
        if operation == "sum": # equality ( == )
            return x + y;
        
        elif operation == "multiply":
            return x * y;
        
        elif operation == "divide":
            return x / y;
        
        elif operation == "subtract":
            return x - y;
        
        else:
            return 0;

    #  method argument opsional
    def info(self, name = None, age = None):
        if name != None and age != None:
            return "My name is {0} and I'm {1} years old.".format(name, age);
        
        elif name != None:
            return "My name is {0}.".format(name);
        
        elif age != None:
            return "I'm {0} years old.".format(age);
        
        else:
            return 0;

# create object
obj = Calculator()
print("Output:", obj.compute(12, 13))
print("Output:", obj.compute(operation="sum"))
print("Output:", obj.compute(20, 4, "sum"))
print("Output:", obj.compute(20, 4, "multiply"))
print("Output:", obj.compute(20, 4, "divide"))
print("Output:", obj.compute(20, 4, "subtract"))
print("Information:", obj.info(name="Semmy Wellem Taju"))

