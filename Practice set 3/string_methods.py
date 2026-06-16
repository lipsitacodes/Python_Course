'''
Take the string "  i love python programming  " and:

Remove extra spaces from both ends
Convert it to title case
Count how many times "o" appears

4. String Formatting and f-Strings
Using format(), create a sentence:
"My name is John and I am 25 years old."
by passing "John" and 25 as variables.

Do the same using f-strings.

5. String Manipulation Challenges
Given sentence = "Coding in Python is fun", replace "fun" with "awesome" and print it.
Find the index of the word "Python" in sentence.
Convert the entire sentence to uppercase and print it.
'''
str = "  i love python programming  "
print(str.strip())
print(str.title())
print(str.count("o"))

a = "123abc"
print(a.isalnum())
temp = "My name is {} and I am {} years old."
name = "John"
age = 20
print(temp.format(name,age))
print(f"My name is {name} and I am {age} years old.")

sentence = "Coding in Python is fun"
print(sentence.replace("fun","awesome"))
print(sentence.find("Python"))
print(sentence.upper())
