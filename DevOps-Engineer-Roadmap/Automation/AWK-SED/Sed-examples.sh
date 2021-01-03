1. Replacing or substituting string:
   sed 's/unix/linux/' geekfile.txt

2. Replacing the nth occurrence of a pattern in a line:
   sed 's/unix/linux/2' geekfile.txt

3. Replacing all the occurrence of the pattern in a line:
   sed 's/unix/linux/g' geekfile.txt

4. Replacing from nth occurrence to all occurrences in a line:
   sed 's/unix/linux/3g' geekfile.txt

5. Parenthesize first character of each word:
  echo "Welcome To The Geek Stuff" | sed 's/\(\b[A-Z]\)/\(\1\)/g'

6. Replacing string on a specific line number:
   sed '3 s/unix/linux/' geekfile.txt

7. Duplicating the replaced line with /p flag
  sed 's/unix/linux/p' geekfile.txt

8. Printing only the replaced lines:
  sed -n 's/unix/linux/p' geekfile.txt

10. Replacing string on a range of lines
   sed '1,3 s/unix/linux/' geekfile.txt

11. Deleting lines from a particular file:
    sed '5d' filename.txt

12. Delete line from range x to y:
Syntax:
$ sed 'x,yd' filename.txt
Example:
$ sed '3,6d' filename.txt

13. To Delete from nth to last line:
Syntax:
$ sed 'nth,$d' filename.txt
Example:
$ sed '12,$d' filename.txt

13. To Delete pattern matching line:
Syntax:
$ sed '/pattern/d' filename.txt
Example:
$ sed '/abc/d' filename.txt
