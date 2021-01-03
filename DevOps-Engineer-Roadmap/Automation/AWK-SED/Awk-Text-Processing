awk '{print "Welcome to awk command tutorial"}'


Sometimes the separator in some files is not space nor tab but something else.

You can specify it using –F option:
awk -F: '{print $1}' /etc/passwd

echo "Hello Tom" | awk '{$2="Adam"; print $0}'

Reading The Script From a File:
awk -F: -f testfile /etc/passwd


If you need to create a title or a header for your result or so. You can use the
BEGIN keyword to achieve this.
It runs before processing the data:

awk 'BEGIN {print "Report Title"}'



To run a script after processing the data, use the END keyword:

awk 'BEGIN {print "The File Contents:"}

{print $0}

END {print "File footer"}' myfile


FIELDWIDTHS     Specifies the field width.

RS     Specifies the record separator.

FS     Specifies the field separator.

OFS  Specifies the Output separator.

ORS  Specifies the Output separator.


To change separators to - and print full file.
awk 'BEGIN{FS=":"; OFS="-"} {print $1,$6,$7}' /etc/passwd


Sometimes, the fields are distributed without a fixed separator. In these cases,
FIELDWIDTHS variable solves the problem.
awk 'BEGIN{FIELDWIDTHS="3 4 3"}{print $1,$2,$3}' testfile


awk 'BEGIN {print ENVIRON["PATH"] }'
