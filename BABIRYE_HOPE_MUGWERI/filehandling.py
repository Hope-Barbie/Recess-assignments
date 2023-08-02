# Creating a new file and writing to it
file_path = 'example.txt'

# Opening the file in 'w' mode (write mode)
file = open(file_path, 'w')

# Writing content to the file
file.write('Hello, world!\n')
file.write('This is an example file.')

# Closing the file
file.close()

# Reading from an existing file
# Opening the file in 'r' mode (read mode)
file = open(file_path, 'r')

# Reading the entire file content
content = file.read()
print(content)

# Closing the file
file.close()







# Open the file in write mode ('w')
file_path = 'example.txt'
file = open(file_path, 'w')

# Writing content to the file
file.write('Hello, world!\n')
file.write('This is an example file.')

# Closing the file
file.close()




import os

# Specify the file path to be deleted
file_path = 'example.txt'

# Delete the file
os.remove(file_path)

# Open the file in 'r+' mode (read and write mode)
file_path = 'example.txt'
file = open(file_path, 'r+')

# Read the existing content
content = file.read()
print("Existing content:")
print(content)

# Move the file pointer to the beginning of the file
file.seek(0)

# Write the updated content
file.write('Updated content.\n')

# Move the file pointer to the end of the file
file.seek(0, 2)

# Write additional content
file.write('Additional content.')

# Move the file pointer to the beginning of the file
file.seek(0)

# Read the updated content
updated_content = file.read()
print("\nUpdated content:")
print(updated_content)

# Closing the file
file.close()