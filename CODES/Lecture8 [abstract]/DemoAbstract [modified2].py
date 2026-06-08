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
  
    @abstractmethod
    def get_name(self, nama): 
        pass
  
    @abstractmethod
    def get_age(self, umur):
        pass
  
    def get_gender(self):
        return self.gender;
  
    def show_informations(self):
        print(self.name);
        print(self.age);
        print(self.get_weight());
        print(self.get_location());
        print(self.get_gender());
        print(self.get_health());

class Mamalia(Animal):
    def get_name(self, nama):
        self.name = nama;
        
    def get_age(self, umur):
        self.age = umur;
        
    def get_weight(self):
        return "1 Kilo"

    def get_location(self): 
        return "Bitung"

    def get_health(self):
        return "Sick"

class Bird(Animal):
    def get_name(self, nama):
        self.name = nama;
        
    def get_age(self, umur):
        self.age = umur;
    
    def get_weight(self):
        return "0.5 Kilo"

    def get_location(self): 
        return "Tropical forest"

    def get_health(self):
        return "Healthy"

class Fish(Animal):
    def get_name(self, nama):
        self.name = nama;
        
    def get_age(self, umur):
        self.age = umur;
    
    def get_weight(self):
        return "2 Kilos"

    def get_location(self): 
        return "Ocean"

    def get_health(self):
        return "Moderate"

class Amfibi(Animal):
    def get_name(self, nama):
        self.name = nama;
        
    def get_age(self, umur):
        self.age = umur;
    
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
obj_buaya = Amfibi('Buaya', '20 Tahun', 'Amfibi', 'Putih', 'Male') # object 3


# panggil method get_name and method get_age

# class mamalia
obj_cat.get_name("Kucing Putih");
obj_cat.get_age("50 Tahun");

# class Bird
obj_bird.get_name("Elang Putih");
obj_bird.get_age("75 Tahun");

# class Fish
obj_salmon.get_name("Tude Putih");
obj_salmon.get_age("2 Tahun");

obj_buaya.get_name("Buaya Darat");
obj_buaya.get_age("100 Tahun");

# user-defined function is called from object 1 
obj_cat.show_informations();
print("");
obj_bird.show_informations();
print("");
obj_salmon.show_informations();
print("");
obj_buaya.show_informations();

