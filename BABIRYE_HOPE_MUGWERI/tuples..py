#creating a tuple
grades = ('A', 'B', 'C', 'D', 'E')


#accessing elements in a tuple
print(grades[0])  # Output: A
print(grades[-3])  # Output: C

#modifying elemets
#tuples cant be modified since they are immutable but they can be concantenated
another_grades = ('F', 'O')
new_grades = grades + another_grades
print(new_grades)  

#slicing a tuple
sliced_grades = new_grades[2:5]
print(sliced_grades)  

