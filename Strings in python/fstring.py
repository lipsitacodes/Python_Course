template = "Dear {}, you are awesome.Take this ${} bag"
a = "jack"
b = "John"
a1 = 1000
c = "Marie"
b1 = 2000
c1 = 30000
s1 = template.format(a, a1)
s2 = template.format(b, b1) 
s3 = template.format(c, c1) 
# print(s1)   
# print(s2)
# print(s3)

print(f"Dear {a}, you are awesome.Take this ${b1} bag")