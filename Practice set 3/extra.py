'''
Write a program that counts how many vowels are in a given string.

Take a user input string and check if it is a palindrome (same forwards and backwards).
'''
a = input("Enter a string of your choice : ")
rev = a[::-1]
if(a == rev):
    print("It's a palindrom string")
else: 
    print("It's not a palindrom string")

vowels = ['a','e','i','o','u','A','E','I','O','U']
sum = 0
sentence = "ACASDADRF"
for char in sentence:
    if(char in vowels):
        sum += 1
print("Numbers of vowels in the given string is:",sum)