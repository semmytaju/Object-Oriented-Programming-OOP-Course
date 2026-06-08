# import module
from abc import ABC, abstractmethod

# abstract class
class Absclass(ABC):
    # normal method
    def print(self, x):
        print("Passed value: ", x)
        
    @abstractmethod
    def task(self):
        print("Ada di dalam struktur Absclass.")
 
class test_class(Absclass): # normal class
    def task(self):
        print("Ada di dalam struktur test_class.")
 
class example_class(Absclass): # normal class
    def task(self):
        print("Ada di dalam struktur example_class.")
 
# object of test_class created
test_obj = test_class()
test_obj.task()                 # abstract method
test_obj.print(100)             # normal method
 
# object of example_class created
example_obj = example_class()
example_obj.task()              # abstract method
example_obj.print(200)          # normal method
 
print("test_obj is instance of Absclass? ", isinstance(test_obj, Absclass))
print("example_obj is instance of Absclass? ", isinstance(example_obj, Absclass))