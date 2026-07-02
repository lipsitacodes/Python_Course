'''Create a dictionary student = {"name": "John", "age": 20, "grade": "A"} and:
Print the value of "name".
Change "grade" to "A+".
Add a new key "city" with value "Delhi".'''

student = {"name": "John", "age": 20, "grade": "A"}
print(student["name"])
student["grade"] = "A+"
student["city"] = "Delhi"
print(student)

'''Create a dictionary of three friends and their phone numbers. Use:
keys() to get all names
values() to get all numbers
items() to loop over key-value pairs and print them'''
number = { "lipu" : 81443 , "laddu" : 78432 , "monu":45323}
print(number.keys())
print(number.values())
print(number.items())
for key,value in number.items():
    print(key,value)
