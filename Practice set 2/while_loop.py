# Print numbers from 1 to 10 using a while loop.
i = 0
while(i<=10):
    print(i)
    i += 1

# Write a program that keeps asking the user to enter a password until they enter the correct one.
pas = "hellodidi kaise ho"
l = input("Enter your passoword ")
while(pas != l ):
    l = input("Kindly enter correct password")

# Use a while loop to reverse a given number (e.g., 123 → 321).
n = 123
rem = 0
rev = 0
while(n!= 0):
    rem = n%10
    rev = rev*10+rem
    n = int(n/10)

print(rev)