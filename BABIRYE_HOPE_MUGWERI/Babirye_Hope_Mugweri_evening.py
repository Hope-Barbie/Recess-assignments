#lists
stu_names = ["Hope", "Peace", "Tracy", "Peter", "Trevor"]
print(stu_names[1])

stu_names[0] = "Gary"
print(stu_names)

#Write a python program to add a sixth item to the list
stu_names.append("Becky")
print(stu_names)

#Write a python program to add “Bathel” as the 3rd item in your list
stu_names.insert(2, "Bathel")
print(stu_names)

#Write a python program to remove the 4th item from the list
stu_names.remove("Tracy")
print(stu_names)

#Use negative indexing to print the last item in your list
print(stu_names[-1])

#Create a new list with 7 items and use a range of indexes to print the 3rd, 4th and 5th items.
scores = [1,3,5,7,9,11,13]
for i in range(2,5):
    print(scores[i])

# Write a list of countries and make a copy of it.
countries =["Kenya","Zambia", "South Africa", "Isreal"]
print(countries)
print("This is the copied list")
print(countries.copy())

# Write a python program to loop through the list of countries
for country in countries:
    print(country)

# Write a list of animal names and sort them in both descending and ascending order.
animal_names = ["Elephant", "Tiger", "Lion", "Giraffe", "Monkey", "Zebra"]

# Sorting the list in ascending order
ascending_order = sorted(animal_names)

# Sorting the list in descending order
descending_order = sorted(animal_names, reverse=True)

# Printing the sorted lists
print("Ascending order:", ascending_order)
print("Descending order:", descending_order)

# Using the list above, write a python program to output only animal names with the letter ‘a’ in them
animal_names = ["Elephant", "Tiger", "Lion", "Giraffe", "Monkey", "Zebra"]
a_animals = [animal for animal in animal_names if 'a' in animal.lower()]
print(a_animals)

# Write two lists, one containing your first names and the other your second names. Join the two lists.
first_names = ["Hope "]
last_names = ["Babirye Mugweri"]
full_names = []
for first, last in zip(first_names, last_names):
    full_names.append(f"{first} {last}")
print(full_names)




#tuples
x = ("samsung", "iphone", "tecno", "redmi")
favorite_phone_brand = x[1]
print(favorite_phone_brand)

#print the second last item in the tuple using negative indexing
second_last_item = x[-2]
print(second_last_item)

#update "iphone" to "itel" in the tuple
x = list(x)
x[x.index("iphone")] = "itel"
x = tuple(x)
print(x)

#add "Huawei" to the tuple
x = ("samsung", "iphone", "tecno", "redmi")
x = x + ("Huawei",)
print(x)

#loop through the tuple:
x = ("samsung", "iphone", "tecno", "redmi")
for phone in x:
    print(phone)

#remove the first item in the tuple
x = ("samsung", "iphone", "tecno", "redmi")
x = x[1:]
print(x)

#create a tuple of cities in Uganda using the tuple() constructor
cities = tuple(["Kampala", "Entebbe", "Jinja", "Mbarara"])
print(cities)

#unpack the tuple
x = ("samsung", "iphone", "tecno", "redmi")
brand1, brand2, brand3, brand4 = x
print(brand1)
print(brand2)
print(brand3)
print(brand4)

#print the 2nd, 3rd, and 4th cities from the tuple
cities = ("Kampala", "Entebbe", "Jinja", "Mbarara")
print(cities[1:4])

#join two tuples containing first names and second names
first_names = ("Hope ")
second_names = ("Babirye Mugweri")
full_names = first_names + second_names
print(full_names)

#create a tuple of colors and multiply it by 3
colors = ("red", "blue", "green")
multiplied_colors = colors * 3
print(multiplied_colors)

#return the number of times 8 appears in the tuple
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
count = thistuple.count(8)
print(count)



#sets
#Using the set() constructor to create a set of beverages
beverages = set(["coffee", "tea", "juice"])

#Using the add() method to add items to the above set
beverages.add("water")
beverages.add("soda")

#Checking if microwave is present in the set
mySet = {"oven", "kettle", "microwave", "refrigerator"}
if "microwave" in mySet:
    print("Microwave is present in the set")
else:
    print("Microwave is not present in the set")

#Removing kettle from the set
mySet.remove("kettle")
print(mySet)

#Looping through the set
for item in mySet:
    print(item)

#Adding elements from a list to a set
mySet = {1, 2, 3, 4}
myList = [5, 6]
mySet.update(myList)
print(mySet)

#Joining two sets
ages = {22}
names = {"Hope"}
joined_set = ages.union(names)
print(joined_set)



#strings
num = 10
text = "Hope"

# Concatenate variables
result = str(num) + text
print(result)

#remove spaces from the beginning, middle, and end of a string, you can use the strip() method

txt = " Hello, Uganda! "

# Remove spaces from the beginning and end
trimmed_txt = txt.strip()

# Remove spaces from the middle
trimmed_txt = trimmed_txt.replace(" ", "")

print(trimmed_txt)

#convert the value of the variable 'txt' to uppercase, you can use the upper() 
txt = "Hello, Uganda!"

# Convert to uppercase
txt_uppercase = txt.upper()
print(txt_uppercase)

#replace the character 'U' with 'V' in the given string, you can use the replace() method
txt = "Hello, Uganda!"

# Replace 'U' with 'V'
txt_replaced = txt.replace('U', 'V')
print(txt_replaced)

#return a range of characters in the 2nd, 3rd, and 4th positions of a string
y = "I am proudly Ugandan"

# Get characters in the 2nd, 3rd, and 4th positions
range_of_chars = y[1:4]

print(range_of_chars)

#rectifying an error 
x = "All \"Data Scientists\" are cool!"
print(x)
 


#dictionaries
Shoes = {
    "brand": "Nick",
    "color": "black",
    "size": 40
}

print(Shoes["size"])

#change the value "Nick" to "Adidas", you can modify the dictionary as follows:
Shoes["brand"] = "Adidas"
print(Shoes)

#add a key/value pair "type": "sneakers" to the dictionary
Shoes["type"] = "sneakers"
print(Shoes)

#return a list of all the keys in the dictionary, you can use the keys() method:
keys_list = list(Shoes.keys())
print(keys_list)

#return a list of all the values in the dictionary, you can use the values() method:
values_list = list(Shoes.values())
print(values_list)

#check if the key "size" exists in the dictionary, you can use the in operator:
if "size" in Shoes:
    print("Key 'size' exists in the dictionary.")
else:
    print("Key 'size' does not exist in the dictionary.")

#loop through the dictionary, you can use a for loop
for key, value in Shoes.items():
    print(key, ":", value)

#remove the key "color" from the dictionary, you can use the pop() method:
Shoes.pop("color")
print(Shoes)

#empty the dictionary, you can use the clear() method:
Shoes.clear()
print(Shoes)

#making a copy of it of a dictionary
original_dict = {"key1": "value1", "key2": "value2", "key3": "value3"}

# Method 1: Using the copy() method
copied_dict = original_dict.copy()

# Method 2: Using the dict() constructor
copied_dict = dict(original_dict)

print("Original Dictionary:", original_dict)
print("Copied Dictionary:", copied_dict)







