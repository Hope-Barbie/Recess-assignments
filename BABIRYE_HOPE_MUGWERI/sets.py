
# Creating a set
fruits = {'apple', 'banana', 'orange'}
print(fruits)  

# creating a set using set() constructor
colors = set(['red', 'green', 'blue'])
print(colors)  
#Sets only store unique elements. If you try to add a duplicate element to a set, it will be ignored.
fruits = {'apple', 'banana', 'orange', 'apple'}
print(fruits)  # {'banana', 'orange', 'apple'}

#Modifying Sets
# Adding a single element
fruits.add('kiwi')  

 # Adding multiple elements
fruits.update(['grape', 'mango']) 
print(fruits)  

# Removing an element
fruits.remove('banana')   
fruits.discard('kiwi')    
print(fruits) 


#Set Operations
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

union = set1 | set2            # Union
intersection = set1 & set2     # Intersection
difference = set1 - set2       # Difference, elements in set1 but not in set2
symmetric_difference = set1 ^ set2  # Symmetric difference, elements in either set1 or set2, but not in both
print(union)                  
print(intersection)           
print(difference)            
print(symmetric_difference) 


#Iterating over Sets, You can iterate over the elements of a set using a loop.
fruits = {'apple', 'banana', 'orange'}
for fruit in fruits:
    print(fruit)

