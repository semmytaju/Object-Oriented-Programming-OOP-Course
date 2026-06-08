# class 1
class Zoo:
    # constructor with parameters
    def __init__(self, name):
        self.name = name
        self.animals = []
    
    def add_animal(self, animal):
        self.animals.append(animal)
        animal.set_zoo(self)
        
    def remove_animal(self, animal):
        self.animals.remove(animal)
        animal.set_zoo(None)
        print(f"Animal {animal.name} dikeluarkan/dihapus.");

# class 2
class Animal:
    # constructor with parameters
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.zoo = None
        
    def set_zoo(self, zoo):
        self.zoo = zoo
        
    def get_zoo(self):
        return self.zoo.name if self.zoo else None

# membuat objek zoo
zoo = Zoo("Taman Safari Jakarta")

# membuat objek animal
animal1 = Animal("Kuda", "Equus caballus")
animal2 = Animal("Jerapah", "Giraffa camelopardalis")
animal3 = Animal("Harimau", "Panthera tigris")

# menambahkan animal ke zoo
zoo.add_animal(animal1)
zoo.add_animal(animal2)
zoo.add_animal(animal3)

# mencetak daftar animal di zoo
print("Animal di", zoo.name, ":")
for animal in zoo.animals:
    print(animal.name, "(" + animal.species + ")")

# mencetak zoo tempat animal tinggal
print(animal1.name, "tinggal di", animal1.get_zoo())
print(animal2.name, "tinggal di", animal2.get_zoo())
print(animal3.name, "tinggal di", animal3.get_zoo())

# menghapus animal dari zoo
zoo.remove_animal(animal2)


