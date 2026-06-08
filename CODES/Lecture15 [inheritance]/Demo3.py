# parent class 1
class ParentSkillOne:
    # method 1
    def berlari(self):
        print("Skill parent pertama adalah berlari.")  
    
    # method 2
    def pidato(self):
        print("Skill parent pertama adalah berpidato.") 
        
    
# parent class 2
class ParentSkillTwo:
    # method 1
    def membaca(self):
        print("Skill parent kedua adalah membaca buku.")  
    
    # method 2
    def pidato(self):
        print("Skill parent kedua adalah berpidato.") 
        
    
# child class 
class Saya(ParentSkillOne, ParentSkillTwo):
    # method 1
    def pidato(self):
        print("Skill saya adalah berpidato.") 
 
# create object darri Class Saya
obj_me = Saya()
 
# call skills
obj_me.berlari()
obj_me.pidato()
obj_me.membaca()


