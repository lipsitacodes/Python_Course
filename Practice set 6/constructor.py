class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def get_info(self):
        print(f"Name: {self.name} , age : {self.age}")
p = Person("Lipsita", 19)
p.get_info()
