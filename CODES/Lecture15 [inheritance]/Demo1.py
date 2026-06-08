# Parent class
class Hewan: 
    # method 1
    def bicara(self):  
        print("Hewan bisa bersuara.")  
         
    # method 2
    def lari(self):  
        print("Hewan bisa berlari.")  
    
    # method 3
    def makan(self):  
        print("Hewan bisa makan.")  
    
    
# Child class mewarisi dari parrent class
class Kucing(Hewan):
    # method 1 overriding
    def bicara(self):  
        print("Meaow meaow meaow!!!") 
 
    # method 2
    def bermain(self):  
        print("Kucing suka bermain !!!") 
        
# create object of class Kucing
obj_kucing = Kucing()

# call functions
obj_kucing.bicara()
obj_kucing.bermain()
obj_kucing.lari()
obj_kucing.makan()
