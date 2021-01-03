Python Operating System Services - Exercises, Practice, Solution

1. Write a Python program to get the name of the operating system (Platform independent),
information of current operating system, current working directory, print files and directories
in the current directory and raises error in the case of invalid or inaccessible file names and paths

import os
print("Operating System:",os.name)
print("\nInformation of current operating system: ",os.uname())
print("\nCurrent Working Directory: ",os.getcwd())
print("\nList of files and directories in the current directory:")
print(os.listdir('.'))
print("\nTest if a specified file exis or not:")
try:
   filename = 'abc.txt'
   f = open(filename, 'r')
   text = f.read()
   f.close()
except IOError:
   print('Not accessed or problem in reading: ' + filename)


2. Write a Python program to list only directories, files and all directories, files in a specified path.:
import os
path = 'g:\\testpath\\'
print("Only directories:")
print([ name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name)) ])
print("\nOnly files:")
print([ name for name in os.listdir(path) if not os.path.isdir(os.path.join(path, name)) ])
print("\nAll directories and files :")
print([ name for name in os.listdir(path)])

3.  write a python script that will find a specific string in a .txt file,
select the rest of string surrounding it, and paste in another .txt?
stringToMatch = 'specific'
matchedLine = ''
#get line
with open('path/to/file.txt', 'r') as file:
	for line in file:
		if stringToMatch in line:
			matchedLine = line
            			break
#and write it to the file
with opne('path/to/new/file.txt', 'w') as file:
	file.write(matchedLine)
4. write text in the first line of an existing file using Python?
#We read the existing text from file in READ mode
src=open("text.txt","r")
fline="newly added FIRST LINE\n"    #Prepending string
oline=src.readlines()
#Here, we prepend the string we want to on first line
oline.insert(0,fline)
src.close()

#We again open the file in WRITE mode
src=open("text.txt","w")
src.writelines(oline)
src.close()

5. How can I read a text file in Python and convert text within that file into
variables (i.e. if my text file contained 1324, how do I convert 1324 into a variable I can use in my code)?
with open("file name.txt") as f:
  lines = f.readlines()

for line in lines:
  words = line.strip("\n").split()
  print(words)

 6.
