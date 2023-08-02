#my first python code
print("Welcome to coding")

#Strings
#stirngs are used to represent text

#determining the datatype of a string
name = "Hope"
print(type(name))  # output is <class 'str'>

#Strings have three important properties:
#1. Strings contain individual letters or symbols called characters.
#2. Strings have a length, defined as the number of characters the string contains.
#3. Characters in a string appear in a sequence, which means that each character has a numbered position in the string.

#length of a string
# we use the len() to determine the length of a string, length includes space
print(len(name))
print(len("how are you my mum"))

#Concatenation, Indexing, and Slicing
#1. Concatenation, which joins two strings together 
#2. Indexing, which gets a single character from a string 
#3. Slicing, which gets several characters from a string at once

#String Concatenation
#You can combine, or concatenate, two strings using the + operator:

stu_name1 = "Nakato"
stu_name2 = "Peace"
my_name = stu_name1 + " " + stu_name2
print(my_name)

#String Indexing
#Each character in a string has a numbered position called an index.
#You can access the character at the nth position by putting the number between two square brackets ([]) immediately after the string:
animal = "elephant"
print(animal[3]) # output is p
print(animal[0]) # output is e
print(animal[-1]) # output is t
#  print(animal[8]) # error as index is out of range

#String Slicing
#Suppose you need a string containing just the first three letters of the string "mummy". 
# You could access each character by index and concatenate them like this

parent = "mummy"
new_term = parent[0] + parent[1] + parent[2]
print(new_term)
print(parent[0:3])

#Converting String Case
#To convert a string to all lowercase letters, you use the string’s .lower()method. 
#This is done by tacking .lower() onto the end of the string itself:
greeting = "Welcome".lower()
print(greeting)
fruit = "APPLE".lower()
print(fruit)

#The dot (.) tells Python that what follows is the name of a method— the lower() method in this case

#To convert a string to all uppercase letters, you use the string’s .upper()method. 
car = "jeep".upper()
print(car)