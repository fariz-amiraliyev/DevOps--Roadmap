#!/bin/sh

str1="GeeksforGeeks";
str2="geeks";
if [ $str1 = $str2 ]
then
    echo "Both string are same";
else
    echo "Both string are not same";
fi


#!/bin/sh

str1="GeeksforGeeks";
str2="geeks";
if [ $str1 != $str2 ]
then
    echo "Both string are not same";
else
    echo "Both string are same";
fi


#!/bin/sh

str1="GeeksforGeeks";
str2="Geeks";
if [ $str1 \< $str2 ]
then
    echo "$str1 is less then $str2";
else
    echo "$str1 is not less then $str2";
fi


#!/bin/sh

str1="GeeksforGeeks";
str2="Geeks";
if [ $str1 \> $str2 ]
then
    echo "$str1 is greater then $str2";
else
    echo "$str1 is less then $str2";
fi
