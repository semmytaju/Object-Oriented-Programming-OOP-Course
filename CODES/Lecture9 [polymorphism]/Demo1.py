# create class 1
class Cat:
    # constructor (initialize instance variable)
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur
 
    def speak(self):
        print("Cat speaks Meow Meow Meow.")
 
# create class 2 
class Dog:
    # constructor (initialize instance variable)
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur
 
    def speak(self):
        print("Dog speaks Gukk Gukk Gukk.")
 
# object of Cat created
kucing1 = Cat("Catty", 5)

# object of Dog created
anjing1 = Dog("Doggy", 4)
 
# memanggil metode tanpa mengabaikan objek
kucing1.speak()
anjing1.speak()

# memanggil metode dengan mengabaikan objek
for hewan in (kucing1, anjing1):
    hewan.speak()
    
    