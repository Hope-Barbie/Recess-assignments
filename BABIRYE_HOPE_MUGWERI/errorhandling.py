#Exception handling in Python allows you to handle and manage errors 

#Here we use the try-except block for exception handling.
#The code that may raise an exception is placed inside a try block.
#The code to handle the exception is written inside an except block. 

#for example
#ZeroDivisionError exception is raised when we divide a number by zero. 
#The `except ZeroDivisionError` block catches the exception,
#The code inside it is executed to handle the situation.
try:
    # code that may raise an exception
    x = 10 / 0  # Division by zero will raise an exception
except ZeroDivisionError:
    # code to handle the specific exception
    print("we cant get a solution for this, its a zero division error")


# ValueError exception
try:
    x = int("abc")  
except ValueError:
    # code to handle ValueError exception
    print("invalid Integer")


#In the above example, if the `int("abc")` statement raises a `ValueError` exception
#the code inside the second `except` block will be executed.
#We can use the `else` block, which is executed if no exception occurs, and the `finally` block, which is always executed, whether an exception occurred or not:

try:
    x = 10 / 0
except ZeroDivisionError:
    print("Division by zero is not allowed!")
else:
    # code to execute if no exception occurs
    print("Division successful!")
finally:
    # code that always executes, regardless of exceptions
    print("Divide with another number")
