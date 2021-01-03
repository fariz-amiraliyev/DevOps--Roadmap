1.  awk '{ printf  "%10s\n", $1 }' employee.txt  #Here, “%10s\n” means that the output will be 10 characters long.
2.  # awk to split on white space
    echo 'I like programming' | awk '{ print $3 }'

3.  awk to change the delimiter: FS is input field separator and OFS is output field separator variables.
    awk '$1=$1' FS=":" OFS="-" phone.txt

4.  Using FS variable with tab:
    awk '{ print $1 }' FS='\t' input.txt

5. The following awk command will print the 9th and 5th fields of ‘ls -l’ command output with tab
   separator after printing the column title “Name” and “Size”:
   ls -l | awk -v OFS='\t' 'BEGIN { printf "%s\t%s\n", "Name", "Size"} {print $1,$2}'

6. awk regex:
   printf "Fool\nCool\nDoll\nbool" | awk '/[FbC]ool/'
