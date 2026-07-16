class Animal:  # Parent class (superclass)
    location = "Africa"
    def __init__(self, name):
        self.name = name
    def speak(self):
        print("Speaking now...")
class Dog(Animal):
    def speak(self):
        super().speak()
        print("Woof")
# a = Animal('dog')
# a.speak()
d = Dog("Bruno")
d.speak()
print(d.location)
