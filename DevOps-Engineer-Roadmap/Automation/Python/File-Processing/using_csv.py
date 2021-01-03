import csv

file_name = "employees.csv"
sniffer = csv.Sniffer()

with open(file_name, 'r+', newline='') as f:
    snippet = f.read(2048)
    f.seek(0)

    dialect = sniffer.sniff(snippet)
    print(f"Dialect: {dialect.__dict__}")

    reader = csv.reader(f, dialect)

    if sniffer.has_header(snippet):
        header_row = next(reader)

    for row in reader:
        last_id = int(row[0])
        print(row)

    writer = csv.writer(f, dialect)

    # writer.writerow(
    #     [last_id + 1, 'Kevin', 'Bacon', 61, 'Mulberry St', 90210]
    # )

    writer.writerows([
        [last_id + 1, 'Kevin', 'Bacon', 61, 'Mulberry St', 90210],
        [last_id + 2, 'Kevin', 'Bacon', 61, 'Mulberry St', 90210],
        [last_id + 3, 'Kevin', 'Bacon', 61, 'Mulberry St', 90210],
    ])


    
