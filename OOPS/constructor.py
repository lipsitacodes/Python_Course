from os import name


class Emp:

     def __init__(self,sal,name,bond) :
        self.sal = sal
        self.name = name
        self.bond = bond

     def get_sal(self): # self is important here because self
         return self.sal
     def get_info(self):
        print(f"The name of the empoloyee is {self.name}, Salary is {self.sal}, the bond is : {self.bond} years")
e1 = Emp(34000,"Lipsita",6)
print(e1.get_sal())
e1.get_info()

class Dog:
    def __init__(self, name="Unknown", breed="Mixed"):
        self.name = name
        self.breed = breed
    def get_info(self):
        print(f"{self.name} , {self.breed}")
dog1 = Dog()
# name will be "Unknown", breed will be "Mixed"
dog2 = Dog("Rex")
# name will be "Rex", breed will be "Mixed"
dog3 = Dog("Bella", "Labrador")
# name will be "Bella", breed will be "Labrador"
print(dog1.get_info(),dog2.get_info(),dog3.get_info())
