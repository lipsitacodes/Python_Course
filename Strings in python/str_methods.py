# text = "lipsita khadgarai" # Strings are immutable
# # text
# #[1] = "M" # You cannot do this
# a = len(text)
# print("Length of the a is :",a)
# print(text.upper(),text)
# print(text.upper())  # Output: "LIPSITA KHADGARAI"
# print(text.lower())  # Output: "LIPSITA KHADGARAI"
# print(text.title())  # Output: "Lipsita Khadgarai"
# print(text.capitalize())  # Output: "Lipsita khadgarai"

# text = "  hello world  "
# print(text.strip())  # Output: "hello world" it removes the newlines or spaces
# print(text.lstrip()) # Output: "hello world  " it removes the newlines or spaces towards left only
# print(text.rstrip()) # Output: "  hello world" it removes the newlines or spaces towards right only

# text = "Python is fun"
# print(text.find("is"))   # Output: 7
# print(text.replace("fun", "awesome"))  # Output: "Python is awesome"

# text = "Apples,Bananas,Pineapples"
# print(text.split(", "))  # Output: ['Apples', 'Bananas', 'Pineapples'] it will convert into list
# print(",".join(["Apples", "Bananas", "Pineapples"]))  # Output: "Apples,Bananas,Pineapples" it will convert into string


text = "Python123"
# text = "1245435"
# text = "jerry"
print(text.isalpha())  # Output: False is all the characters in string are alphabets or not
print(text.isdigit())  # Output: False is strings are in the form of numbers or not
print(text.isalnum())  # Output: True does it contains both charter or numbers or only char or only numbers
print(text.isspace())  # Output: False does it contains any spaces or not
