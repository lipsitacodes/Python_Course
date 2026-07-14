class Employee:
    company = "Asus" #This is class Atrributes
    def __init__(self,sal,name,bond,company):
        self.sal = sal
        self.name = name
        self.bond = bond
        self.company =company
    def ger_sal(self):
        return self.sal
    def get_info(self):
        print(f"The name of the empoloyee is {self.name}, Salary is {self.sal}, the bond is : {self.bond} years")

e1 = Employee(23000,'John',3,"Acer")
print(e1.company) #It will always prints if instance attribute is present
#Object Introspection
print(dir(e1))
print(Employee.company) #This will always print the class attribute
