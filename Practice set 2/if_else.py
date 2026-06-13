# 1.Write a program that asks the user for a number and prints whether it is positive, negative, or zero.
number = int(input("Enter a number: "))
if number > 0:
    print("The number is positive.")
elif number < 0 :
    print("The number is negative.")
else: 
    print("The number is zero.")

age =  int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

if number % 2 == 0:
    print(number," is even.")
else:
    print( number,"is odd.")