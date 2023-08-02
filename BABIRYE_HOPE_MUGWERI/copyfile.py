#copying content to another file

def copy_file(orignal_file, new_file):
  original = open(original_file, "r")
  new = open(new_file, "w")  
  new.write(original.read())
  original.close()
  new.close()
  print("content copied")

original_file = "exp.txt"
new_file = "hope.txt"
copy_file("exp.txt", "hope.txt")

new_file= open("hope.txt", "r")
print(new_file.read())
new_file.close()
