# class 1
class Employee:
    # constructor with parameters
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.companies = []
    
    def add_company(self, company):
        self.companies.append(company)
    
    def remove_company(self, company):
        self.companies.remove(company)

# class 2
class Company:
    # constructor with parameters
    def __init__(self, name):
        self.name = name
        self.employees = []
    
    def add_employee(self, employee):
        if employee not in self.employees:
            self.employees.append(employee)
            employee.add_company(self)
    
    def remove_employee(self, employee):
        if employee in self.employees:
            self.employees.remove(employee)
            employee.remove_company(self)
            

# membuat objek perusahaan
company = Company("PT Budi Mulya")

# membuat objek karyawan
employee1 = Employee("Semmy Taju", 25)
employee2 = Employee("Ferdy Mesakh", 30)

# menambahkan karyawan ke perusahaan
company.add_employee(employee1)
company.add_employee(employee2)

# mencetak nama karyawan dan nama perusahaan tempatnya bekerja
print("Karyawan 1: ", employee1.name)
for c in employee1.companies:
    print("Perusahaan 1: ", c.name)
print("Karyawan 2: ", employee2.name)
for c in employee2.companies:
    print("Perusahaan 2: ", c.name)

# mencetak nama perusahaan dan nama karyawan yang bekerja di dalamnya
print("Perusahaan: ", company.name)
for e in company.employees:
    print("Karyawan: ", e.name)

# menghapus karyawan dari perusahaan
company.remove_employee(employee1)

# mencetak nama karyawan dan nama perusahaan setelah dihapus
print("Karyawan 1: ", employee1.name)
for c in employee1.companies:
    print("Perusahaan 1: ", c.name)
print("Karyawan 2: ", employee2.name)
for c in employee2.companies:
    print("Perusahaan 2: ", c.name)
print("Perusahaan: ", company.name)
for e in company.employees:
    print("Karyawan: ", e.name)
