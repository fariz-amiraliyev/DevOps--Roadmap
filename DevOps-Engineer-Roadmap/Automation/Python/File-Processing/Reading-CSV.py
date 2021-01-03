import csv

# opening the CSV file
with open('Giants.csv', mode ='r')as file:

  # reading the CSV file
  csvFile = csv.reader(file)

  # displaying the contents of the CSV file
  for lines in csvFile:
        print(lines)



import csv

# opening the CSV file
with open('Giants.csv', mode ='r') as file:

       # reading the CSV file
       csvFile = csv.DictReader(file)

       # displaying the contents of the CSV file
       for lines in csvFile:
            print(lines)

import pandas

# reading the CSV file
csvFile = pandas.read_csv('Giants.csv')

# displaying the contents of the CSV file
print(csvFile)
