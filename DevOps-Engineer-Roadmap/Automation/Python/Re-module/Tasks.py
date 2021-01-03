1. Write a Python program to check that a string contains only a certain
 set of characters (in this case a-z, A-Z and 0-9):

 def check(string):
    pat=re.compile(r"[a-zA-Z0-9.]")
    dot= pat.search(string)
    print(dot)
    return bool(string)


2.  Write a Python program that matches a string that has an a followed by zero or more b's.:
import re
pattern="ab*?"
i
def check_b(string):
if re.search(pattern,string):
    print("string is found")
else:
    print("string is not found")
check_b("abook")
string is found


3.  Write a Python program that matches a string that has an a followed by one or more b's.

import re
+?
def check_text(string):
    pat="ab+?"
    return bool(re.search(pat,string))
c
check_text("ac")
False

4. Write a Python program to remove lowercase substrings from a given string.
import re
str1 = 'KDeoALOklOOHserfLoAJSIskdsf'
print("Original string:")
print(str1)
print("After removing lowercase letters, above string becomes:")
remove_lower = lambda text: re.sub('[a-z]', '', text)
result =  remove_lower(str1)
print(result)

5.Write a Python program that reads a given expression and evaluates it. Go to the editor
Terms and conditions:
The expression consists of numerical values, operators and parentheses, and the ends with '='.
The operators includes +, -, *, / where, represents, addition, subtraction, multiplication and division.
When two operators have the same precedence, they are applied to left to right.
You may assume that there is no division by zero.
All calculation is performed as integers, and after the decimal point should be truncated Length of the expression will not exceed 100.

import re
print("Input number of data sets:")
class c(int):
    def __add__(self,n):
        return c(int(self)+int(n))
    def __sub__(self,n):
        return c(int(self)-int(n))
    def __mul__(self,n):
        return c(int(self)*int(n))
    def __truediv__(self,n):
        return c(int(int(self)/int(n)))

for _ in range(int(input())):
  print("Input an expression:")
  print(eval(re.sub(r'(\d+)',r'c(\1)',input()[:-1])))


6. Write a Python program that matches a string that has an a followed by two to three 'b':
  import re
def text_match(text):
        patterns = 'ab{2,3}?'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

print(text_match("ab"))
print(text_match("aabbbbbc"))

7. Write a Python program to find sequences of lowercase letters joined with a underscore.:
  import re
def text_match(text):
        patterns = '^[a-z]+_[a-z]+$'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

8. Write a Python program to find the sequences of one upper case letter followed by lower case letters.
 import re
def text_match(text):
        patterns = '^[a-z]+_[a-z]+$'
        if not re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

9. Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.
import re
def text_match(text):
        patterns = 'a.*?b$'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

10. Write a Python program that matches a word at the beginning of a string.
import re
def text_match(text):
        patterns = '^\w+'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')
11. Write a Python program that matches a word at the end of a string, with optional punctuation.
import re
def text_match(text):
        patterns = '\w+\S*$'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

12. Write a Python program that matches a word containing 'z'.

import re
def text_match(text):
        patterns = '\w*z.\w*'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

13. Write a Python program that matches a word containing 'z', not at the start or end of the word.
import re
def text_match(text):
        patterns = '\Bz\B'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

14. Write a Python program to match a string that contains only upper and lowercase letters, numbers, and underscores.
import re
def text_match(text):
        patterns = '^[a-zA-Z0-9_]*$'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')
15. Write a Python program where a string will start with a specific number.
import re
def match_num(string):
    text = re.compile(r"^5")
    if text.match(string):
        return True
    else:
        return False
print(match_num('5-2345861'))
print(match_num('6-2345861'))

16. Write a Python program to remove leading zeros from an IP address:
import re
ip = "216.08.094.196"
string = re.sub('\.[0]*', '.', ip)
print(string)

17.  Write a Python program to check for a number at the end of a string.
import re
def end_num(string):
    text = re.compile(r".*[0-9]$")
    if text.match(string):
        return True
    else:
        return False

18. Write a Python program to search the numbers (0-9) of length between 1 to 3 in a given string.
"Exercises number 1, 12, 13, and 345 are important"

import re
results = re.finditer(r"([0-9]{1,3})", "Exercises number 1, 12, 13, and 345 are important")
print("Number of length 1 to 3")
for n in results:
     print(n.group(0))


19.Write a Python program to search some literals strings in a string. Go to the editor
Sample text : 'The quick brown fox jumps over the lazy dog.'
Searched words : 'fox', 'dog', 'horse'

import re
patterns = [ 'fox', 'dog', 'horse' ]
text = 'The quick brown fox jumps over the lazy dog.'
for pattern in patterns:
    print('Searching for "%s" in "%s" ->' % (pattern, text),)
    if re.search(pattern,  text):
        print('Matched!')
    else:
        print('Not Matched!')

20.
