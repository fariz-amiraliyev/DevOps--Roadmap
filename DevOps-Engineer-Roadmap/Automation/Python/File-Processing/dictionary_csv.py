import csv

file_name = "employees.csv"

with open(file_name, 'r+', newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)

    writer = csv.DictWriter(f, fieldnames=reader.fieldnames)
    writer.writerows([
        {
            'id': 120,
            'first_name': 'Keith',
            'last_name': 'Thompson',
            'street': 'Berry St',
            'zip': '11000'
        },
        {
            'id': 121,
            'first_name': 'Larry',
            'last_name': 'Frittz',
            'street': 'Washington St',
            'zip': '00011'
        }
    ])


    
