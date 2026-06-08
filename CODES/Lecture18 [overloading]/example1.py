# create class
class Calculator:
    def __init__(self):
        print("Simple Calculator !!!");
        
    # method 1
    def add(self, x, y):
       return x + y;
    
    # method 2
    def add(self, x, y, z):
       return x + y + z;
    
    # method 3
    def add(self, *args):
       return sum(args);
   
    # method 4
    def sub(self, x, y):
        return x - y;
    
# create object
obj = Calculator()
print(obj.sub(6, 4)) #akan memanggil fungsi pertama dengan 2 parameter
print(obj.add(2, 3)) #akan memanggil fungsi kedua dengan 2 parameter
print(obj.add(2, 3, 4)) #akan memanggil fungsi ketiga dengan 3 parameter
print(obj.add(2, 3, 4, 5)) #akan memanggil fungsi dengan 4 parameter
print(obj.add(2, 3, 4, 5, 6)) #akan memanggil fungsi dengan 5 parameter
print(obj.add(2, 3, 4, 5, 6, 7)) #akan memanggil fungsi dengan 6 parameter
print(obj.add(2, 3, 4, 5, 6, 7, 8)) #akan memanggil fungsi dengan 7 parameter

