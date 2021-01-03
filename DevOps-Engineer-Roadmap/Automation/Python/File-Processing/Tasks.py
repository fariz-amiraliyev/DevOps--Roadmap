1. Write a Python program to read an entire text file.
def file_read(fname):
        txt = open(fname)
        print(txt.read())

file_read('test.txt')

2. Write a Python program to read first n lines of a file.:
def file_read(file,nlines):
    from itertools import islice
    with open(file) as f:
        for line in islice(f,nlines):
            print(line)

3. Write a Python program to append text to a file and display the text.:
def file_read(fname):
        from itertools import islice
        with open(fname, "w") as myfile:
                myfile.write("Python Exercises\n")
                myfile.write("Java Exercises")
        txt = open(fname)
        print(txt.read())
file_read('abc.txt')

4. Write a Python program to read last n lines of a file.
# Python implementation to
# read last N lines of a file

# Function to read
# last N lines of the file
def LastNlines(fname, N):
    # opening file using with() method
    # so that file get closed
    # after completing work
    with open(fname) as file:

        # loop to read iterate
        # last n lines and print it
        for line in (file.readlines() [-N:]):
            print(line, end ='')


# Driver Code:
if __name__ == '__main__':
    fname = 'File1.txt'
    N = 3
    try:
        LastNlines(fname, N)
    except:
        print('File not found'
5. Write a Python program to read a file line by line and store it into a list:
def file_read(fname):
        with open(fname) as f:
                #Content_list is the list that contains the read lines.
                content_list = f.readlines()
                print(content_list)

file_read(\'test.txt\')

6. Write a python program to find the longest words:
def longest_word(filename):
    with open(filename, 'r') as infile:
              words = infile.read().split()
    max_len = len(max(words, key=len))
    return [word for word in words if len(word) == max_len]

print(longest_word('test.txt'))

7. Write a Python program to count the number of lines in a text file.
def count_lines(file):
    with open(file) as f:
        txt=f.readlines()
        print(len(txt))
8. Write a Python program to count the frequency of words in a file.
from collections import Counter
def word_count(fname):
        with open(fname) as f:
                return Counter(f.read().split())

11. Write a Python program to get the file size of a plain file.

import os
fs=os.stat("dumping.py").st_size

12. Write a Python program to write a list to a file:
color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
with open('abc.txt', "w") as myfile:
        for c in color:
                myfile.write("%s\n" % c)

content = open('abc.txt')
print(content.read())

13. Write a Python program to copy the contents of a file to another file:
from shutil import copyfile
copyfile('test.py', 'abc.py')

14. Write a Python program to combine each line from first file with the corresponding line in second file.

with open('abc.txt') as fh1, open('test.txt') as fh2:
    for line1, line2 in zip(fh1, fh2):
        # line1 from abc.txt, line2 from test.txtg
        print(line1+line2)



15. Write a Python program to read a random line from a file.
import random
def random_line(fname):
    op=open(fname).read().splitlines()
    return random.choice(op)

16. Write a Python program to assess if a file is closed or not.

 f = open('abc.txt','r')
print(f.closed)
f.close()
print(f.closed)


17. Write a Python program to remove newline characters from a file.

def remove_newlines(fname):
    flist = open(fname).readlines()
    return [s.rstrip('\n') for s in flist]

print(remove_newlines("test.txt"))

18. Write a Python program that takes a text file as input and returns the number of words of a given text file.

def find_words(fname):
    l=open(fname).read().split()
    print(len(l))

19. Write a Python program that takes a text file as input and returns the number of words of a given text file. Go to the editor
Note: Some words can be separated by a comma with no space.
def count_words(filepath):
   with open(filepath) as f:
       data = f.read()
       data.replace(",", " ")
       return len(data.split(" "))
print(count_words("words.txt"))

20. Write a Python program to extract characters from various text files and puts them into a list.
import glob
char_list = []
files_list = glob.glob("*.txt")
for file_elem in files_list:
   with open(file_elem, "r") as f:
       char_list.append(f.read())
print(char_list)

21. Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt.
import string, os
if not os.path.exists("letters"):
   os.makedirs("letters")
for letter in string.ascii_uppercase:
   with open(letter + ".txt", "w") as f:
       f.writelines(letter)

22. Write a Python program to create a file where all letters of English alphabet are listed by specified number of letters on each line.
import string
def letters_file_line(n):
   with open("words1.txt", "w") as f:
       alphabet = string.ascii_uppercase
       letters = [alphabet[i:i + n] + "\n" for i in range(0, len(alphabet), n)]
       f.writelines(letters)
letters_file_line(3)
