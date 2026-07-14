# Class : Class is a blueprint or a template. Eg. From for an Exam that contains name , age , elcetives, father's name etc.
#Object : Object is a specific instance from the template (class.). Eg Form which contains the data for John Deo , 19 , Kai Deo
class Emp:
     company = "Microsoft"
     def get_sal(self): # self is important here because self is a way to reference the class which is being created
         print(self)
         return 50000
e = Emp() # An object of class employee created here
print(e.get_sal()) #Emp's get_sal method got called here
e2 = Emp()
print(e2.company)
print(e2.get_sal())
