# parent class (level 1)
class GrandFather:
    # public variables
    nama = "Robert Toda"
    __max_umur = "60"
    
    # parameterized constructor
    def __init__(self, input_nama, input_umur):
        # public data members
        self.nama = input_nama        # public variable
        self.__max_umur = input_umur  # private variable
        self.__info()
        
    # method 1
    def menulis(self):
        print("Skill grand father adalah menulis.")  
    
    # method 2
    def __info(self):
        print("Grand Father:",self.nama," dan umur:",self.__max_umur,".") 
        
    
# parent class (level 2)
class Father(GrandFather):
    # method 1
    def membaca(self):
        print("Skill father adalah membaca buku.")  
    
    # method 1
    def menulis(self):
        print("Skill father adalah menulis jurnal international.")  
    
    # method 2
    def programmer(self):
        print("Skill father adalah membuat program computer.") 
        
    
# child class 1 
class Semmy(Father):
    # method 1
    def berenang(self):
        print("Skill Semmy adalah berenang.") 

    # method 2
    def programmer(self):
        print("Skill Semmy adalah programmer Java.") 

# child class 2
class Buddy(Father):
    # method 1
    def pidato(self):
        print("Skill Buddy adalah pidato.") 

    # method 2
    def menulis(self):
        print("Skill Buddy adalah menulis buku.") 

# create object #1
obj_sem = Semmy("Hendra Bayu", "58")
#obj_sem.__info() # can't access private method
obj_sem.menulis()
obj_sem.membaca()
obj_sem.berenang()
obj_sem.programmer()

print();

# create object #2
obj_bud = Buddy("John Tambayun", "89")
#obj_bud.__info() # can't access private method
obj_bud.membaca()
obj_bud.programmer()
obj_bud.pidato()
obj_bud.menulis()
