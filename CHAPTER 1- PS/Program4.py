# Program to print the contents of a directory using the os module

# Importing the os module
import os

# Specify the directory path
path = "."   # "." means the current directory
# path = "/" 
# path = "/new folder"     

# Display all files and folders in the directory
contents = os.listdir(path)

print("Contents of the directory:")
for item in contents:
    print(item)