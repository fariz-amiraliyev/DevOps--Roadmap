1. Write a Python program to get the name of the operating system
(Platform independent), information of current operating system,
current working directory, print files and directories in the current directory
and raises error in the case of invalid or inaccessible file names and paths.

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


2.Write a Python program to list only directories, files and all directories, files in a specified path.

import os
path = 'g:\\testpath\\'
print("Only directories:")
print([ name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name)) ])
print("\nOnly files:")
print([ name for name in os.listdir(path) if not os.path.isdir(os.path.join(path, name)) ])
print("\nAll directories and files :")
print([ name for name in os.listdir(path)])


3. Write a Python program to scan a specified directory and identify the sub directories and files.

import os
root = 'g:\\testpath\\'
for entry in os.scandir(root):
   if entry.is_dir():
       typ = 'dir'
   elif entry.is_file():
       typ = 'file'
   elif entry.is_symlink():
       typ = 'link'
   else:
       typ = 'unknown'
   print('{name} {typ}'.format(
       name=entry.name,
       typ=typ,
   ))
4. Write a Python program to check for access to a specified path.
Test the existence, readability, writability and executability of the specified path.

import os
print(os.access('EngineerBP',os.F_OK))
print('Exist:', os.access('c:\\Users\\Public\\C programming library.docx', os.F_OK))
print('Readable:', os.access('c:\\Users\\Public\\C programming library.docx', os.R_OK))
print('Writable:', os.access('c:\\Users\\Public\\C programming library.docx', os.W_OK))
print('Executable:', os.access('c:\\Users\\Public\\C programming library.docx', os.X_OK))

5. Write a Python program to get the size, permissions, owner, device, created,
last modified and last accessed date time of a specified path.

import os
import sys
import time
path = 'g:\\testpath\\'
print('Path Name ({}):'.format(path))
print('Size:', stat_info.st_size)
print('Permissions:', oct(stat_info.st_mode))
print('Owner:', stat_info.st_uid)
print('Device:', stat_info.st_dev)
print('Created     :', time.ctime(stat_info.st_ctime))
print('Last modified:', time.ctime(stat_info.st_mtime))
print('Last accessed:', time.ctime(stat_info.st_atime))

6.
