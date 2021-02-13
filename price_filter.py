import csv

filtered = open('price_filter.csv', 'w', encoding='utf=8')
field_names = ['Id', 'Images', 'Title', 'Description', 'Price']
writer = csv.DictWriter(filtered, fieldnames=field_names)
writer.writeheader()
with open('stage3_test.csv', encoding='utf-8') as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        if 10000 < float(row['Price']) < 50000:
            writer.writerow(row)
filtered.close()
