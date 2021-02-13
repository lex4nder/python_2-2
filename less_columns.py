import csv

changed = open('less_columns.csv', 'w', encoding='utf=8')
field_names = ['Id', 'Title', 'Price']
writer = csv.DictWriter(changed, fieldnames=field_names)
writer.writeheader()
with open('stage3_test.csv', encoding='utf-8') as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        writer.writerow({'Id': row['Id'], 'Title': row['Title'], 'Price': row['Price']})
changed.close()
