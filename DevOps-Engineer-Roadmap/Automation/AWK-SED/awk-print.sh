awk '{print NR,$1}' system.log
awk '{print $5,$1}' system.log
awk '{print $1,$NF}' employee.txt   # NF built-in variables (Display Last Field)
awk 'NR==3, NR==6 {print NR,$0}' employee.txt  #
awk '{print NR "- " $1 }' geeksforgeeks.txt   # To print the first item along with the row number(NR) separated with ” – “ from each line in geeksforgeeks.txt:



To find the length of the longest line present in the file:
awk '{ if (length($0) > max) max = length($0) } END { print max }' geeksforgeeks.txt

To count the lines in a file:
awk 'END { print NR }' geeksforgeeks.txt

Printing lines with more than 10 characters:
awk 'length($0) > 10' geeksforgeeks.txt

To find/check for any string in any column:
awk '{ if($3 == "B6") print $0;}' geeksforgeeks.txt


To print the squares of first numbers from 1 to n say 6:
awk 'BEGIN { for(i=1;i<=6;i++) print "square of", i, "is",i*i; }'
