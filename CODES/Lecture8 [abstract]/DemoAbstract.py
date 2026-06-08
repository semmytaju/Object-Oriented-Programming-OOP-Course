from abc import ABC, abstractmethod

# class abstract
class Animal(ABC):
    def __init__(self, name, age, species , color, gender): 
        self.species = species 
        self.color = color
        self.name = name
        self.age = age
        self.gender = gender

    @abstractmethod
    def get_weight(self):
        pass
  
    @abstractmethod
    def get_location(self):
        pass
  
    @abstractmethod
    def get_health(self):
        pass
  
    def get_name(self): 
        return self.name;
  
    def get_age(self):
        return self.age;
  
    def get_gender(self):
        return self.gender;
  
    def show_informations(self):
        print(self.get_name());
        print(self.get_age());
        print(self.get_weight());
        print(self.get_location());
        print(self.get_gender());
        print(self.get_health());

class Mamalia(Animal):
    def get_weight(self):
        return "1 Kilo"

    def get_location(self): 
        return "Bitung"

    def get_health(self):
        return "Sick"

class Bird(Animal):
    def get_weight(self):
        return "0.5 Kilo"

    def get_location(self): 
        return "Tropical forest"

    def get_health(self):
        return "Healthy"

class Fish(Animal):
    def get_weight(self):
        return "2 Kilos"

    def get_location(self): 
        return "Ocean"

    def get_health(self):
        return "Moderate"

# objects are created and the parameterized constructor is called 
obj_cat = Mamalia('Kucing', '20 Tahun', 'Mamalia', 'white', 'Female') # object 1
obj_bird = Bird('Elang', '15 Tahun', 'Bird', 'white', 'Female') # object 2
obj_salmon = Fish('Salmon', '1 Tahun', 'Fish', 'Blue', 'Female') # object 3

# user-defined function is called from object 1 
obj_cat.show_informations();
print("");
obj_bird.show_informations();
print("");
obj_salmon.show_informations();


