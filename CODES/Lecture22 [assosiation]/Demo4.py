# class 1
class Animal:
    # constructor with parameters
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.habitats = []
        
    def add_habitat(self, habitat):
        if habitat not in self.habitats:
            self.habitats.append(habitat)
            habitat.add_animal(self)
        
    def remove_habitat(self, habitat):
        if habitat in self.habitats:
            self.habitats.remove(habitat)
            habitat.remove_animal(self)
        
# class 2
class Habitat:
    # constructor with parameters
    def __init__(self, name):
        self.name = name
        self.animals = []
        
    def add_animal(self, animal):
        if animal not in self.animals:
            self.animals.append(animal)
            animal.add_habitat(self)
            
    def remove_animal(self, animal):
        if animal in self.animals:
            self.animals.remove(animal)
            animal.remove_habitat(self)

# create animal objects
lion = Animal("Simba", "Lion")
tiger = Animal("Rajah", "Tiger")
monkey = Animal("Abu", "Monkey")

# create habitat objects
savanna = Habitat("Savanna") # padang rumput
jungle = Habitat("Jungle") # hutan

# add habitats for animals
lion.add_habitat(savanna)
lion.add_habitat(jungle)
tiger.add_habitat(jungle)
monkey.add_habitat(jungle)

# print animals and their habitats
print(lion.name + " lives in: ")
for habitat in lion.habitats:
    print("- " + habitat.name)
    
print(tiger.name + " lives in: ")
for habitat in tiger.habitats:
    print("- " + habitat.name)
    
print(monkey.name + " lives in: ")
for habitat in monkey.habitats:
    print("- " + habitat.name)

# print habitats and their animals
print(savanna.name + " is home to: ")
for animal in savanna.animals:
    print("- " + animal.name + ", " + animal.species)
    
print(jungle.name + " is home to: ")
for animal in jungle.animals:
    print("- " + animal.name + ", " + animal.species)
    
    
    