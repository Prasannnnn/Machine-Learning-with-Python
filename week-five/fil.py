'''

file handling is an important part of any web application.

python has several functions for creating ,reading , updating and delete.


File Handling

key function for working with files in python is open() function

The open() function takes two parameters; filename, and mode.

four different methods (modes) for opening a file:

'r' - Read - Default value. Opens a file for reading, error if the file does not exist.

'a' - Append - Opens a file for appending, creates the file if it does not exist.

'w' - Write - Opens a file for writing, creates the file if it does not exist.

'x' - Create - Creates the specified file, returns an error if the file exists.

't' - Text - Default value. Text mode

'b' - Binary - Binary mode (e.g. images)

'''

#create a new file

'''
'w' - Write - will create a file 
if the specified file does not exist
'x' - Create - will create a file, 
returns an error if the file exist
'a' - Append - will create a file
'''
# a = open("router.txt","a")
# a.write(" Never Enough by Lorren Allred")
# a.close()

# '''

# '''
# b = open("rout.txt","r")
# print(b.read())

#read only parts of the file
a = open(r"C:\Users\sample\Desktop\Machine Learning\Machine-Learning-with-Python\week-five\route.txt","r")
#print(a.read(500))

#read lines
print(a.readline())
print(a.readline())

a.close()

import os
if os.path.exists("router.txt"):
    os.remove("router.txt")
else:
    print("the files doesnt exists")

import os
os.rmdir("klm")