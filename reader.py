import csv
with open("another-pakistan.csv", 'r') as file:
    csv_file = csv.DictReader(file)
    for row in csv_file:
        print(type(row['date']))
        break