'''
Create a list fruits = ["apple", "banana", "cherry"].
Print the first fruit.
Replace "banana" with "orange".
Print the length of the list.
'''
fruits = ["apple", "banana", "cherry"]
print(fruits[0])
fruits[1] = "orange"
print(fruits)
print(len(fruits))

'''
Create a list of numbers from 1 to 10.
Print the first three numbers using slicing.
Print the last three numbers using slicing
'''
num = [1,2,3,4,5,6,7,8,9,10]
print(num[0:3])
print(num[-3:])

'''Start with numbers = [5, 2, 9, 1, 7] and do the following:
Sort the list in ascending order.
Append the number 10 to the list.
Remove the number 2 from the list.'''
numbers = [5, 2, 9, 1, 7]
print(numbers.sort())
numbers.append(10)
print(numbers)
numbers.remove(2)
print(numbers)
'''Create a list names = ["Alice", "Bob", "Charlie"] and use the insert() method to add "David" at index 1.'''
names = ["Alice", "Bob", "Charlie"]
names.insert(1,"David")
print(names)
