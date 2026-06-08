# create class
class Animal:
  
  # data members of class
  color = "black"                   # attribute 1
  species  = "Serangga"             # attribute 2
  name = "Kaki seribu (lipan)";     # attribute 3
  age = "6 Bulan";                  # attribute 4
  weight = "1 Kilo";                # attribute 5
  location = "Bitung";              # attribute 6
  gender = "Male";                  # attribute 7
  health_status = "Sick";           # attribute 8
   
  # constructor
  def __init__(self, name, age, species , color, gender): 
    self.species = species 
    self.color = color
    self.name = name
    self.age = age
    self.gender = gender

  def get_name(self): 
      return self.name;
  
  def get_age(self):
      return self.age;
  
  def get_weight(self):
      return self.weight;
  
  def get_location(self): 
      return self.location;
  
  def get_gender(self):
      return self.gender;
  
  def get_health(self):
      return self.health_status;
  
  def show_informations(self):
      print(self.get_name());
      print(self.get_age());
      print(self.get_weight());
      print(self.get_location());
      print(self.get_gender());
      print(self.get_health());
      

# objects are created and the parameterized constructor is called 
obj_cat = Animal('Cat', '20 Tahun', 'Mamalia', 'white', 'Female') # object 1
obj_dog = Animal('Dog', '25 Tahun', 'Mamalia', 'Black', 'Male') # object 2
obj_bird = Animal('Elang', '15 Tahun', 'Bird', 'white', 'Female') # object 3
obj_snake = Animal('Ular', '20 Tahun', 'Reptil', 'Green', 'Male') # object 3
obj_salmon = Animal('Salmon', '1 Tahun', 'Fish', 'Blue', 'Female') # object 3
obj_ant = Animal('Ant', '10 Tahun', 'Serangga', 'Red', 'Female') # object 3

# user-defined function is called from object 1 
obj_cat.show_informations();
print("");
obj_dog.show_informations();
print("");
obj_bird.show_informations();
print("");
obj_snake.show_informations();
print("");
obj_salmon.show_informations();
print("");
obj_ant.show_informations();





