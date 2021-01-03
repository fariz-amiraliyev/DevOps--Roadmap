import csv
import csv
with open("fru.csv", newline="") as ff:
    cvr=csv.reader(ff,delimiter=',')
    for x in cvr:
        print(x)
with open("fru.csv", newline="") as ff:
    cvr=csv.reader(ff,delimiter=',')
    for x in cvr:
        print(x)
['Apple', '30']
['Orange', '20']
['Grapes', '25']
['Mango', '40']
with open("fru.csv", newline="") as ff:
    cvv=csv.DictReader(ff,fieldnames=['Name','Quantity'])
    for x in cvv:
        print(x)
{'Name': 'Apple', 'Quantity': '30'}
{'Name': 'Orange', 'Quantity': '40'}
{'Name': 'Grapes', 'Quantity': '45'}
{'Name': 'Mango', 'Quantity': '60'}
6
with open('fru.csv', 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=',')
    data=[['Apple','30'], ['Orange', '40'],['Grapes', '45'], ['Mango', '60']]
    csv_writer.writerows(data)
"""Writing a dictionary to CSV file
You can write an ordered dictionary of key-value pairs to the csv file using the DictWriter function. Here is an example."""
​
import csv
​
with open('fruits_stock.csv', 'w', newline='') as csv_file:
    dict_writer = csv.DictWriter(csv_file, fieldnames = ['Name','Quantity'])
    dict_writer.writeheader()
    dict_writer.writerow({'Name': 'Apple', 'Quantity': '30'})
    dict_writer.writerow({'Name': 'Orange', 'Quantity': '20'}])
    dict_writer.writerow({'Name': 'Grapes', 'Quantity': '25'}])
    dict_writer.writerow({'Name': 'Mango', 'Quantity': '40'}])
  File "<ipython-input-53-ae04ee32e4f9>", line 10
    dict_writer.writerow({'Name': 'Orange', 'Quantity': '20'}])
                                                             ^
SyntaxError: closing parenthesis ']' does not match opening parenthesis '('
