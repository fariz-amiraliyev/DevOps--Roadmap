#/bin/bash
​
Years=(2013 2014 2015 2016 2017 2018 2019 2020)
echo "year\tadded\tremoved"
for year in ${Years[*]}; do
    let nextYear=$year+1
    git log --after=$year-01-01 --before=$nextYear-01-01 --pretty=tformat: --numstat | grep -v '^-' | awk -v year=$year '{ add+=$1; remove+=$2 } END {printf("%s\t%s\t%s\n" , year, add, remove)}'
done
