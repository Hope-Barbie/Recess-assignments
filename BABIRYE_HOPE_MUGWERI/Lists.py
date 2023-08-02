#creating a list
marks = [80, 67,90, 45, 98]
print(marks)

#Accessing List elements
print(marks[0]) #returns element at positin 1
print(marks[-2]) # returns element at posotion 4 

#Modifying a list
marks[2] = 91
print(marks)

#adding an element to a list at the end
marks.append(100)
print(marks)

#Adding an element at a given position
fruits = ["oranges" "mangoes" "melon "]
fruits.insert(2, "jackfruit") # 2 is the index where you want to insert the new element
print(fruits)

#removing an element from the list 
fruits.remove("jackfruit")
print(fruits)

#Length of a list
cars = ["toyota"]
print(len(marks))
print(len(cars))
print(len(fruits))
