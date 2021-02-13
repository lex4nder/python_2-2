import csv

with open('stage3_test.csv', encoding='utf-8') as csv_file, open('imgs.csv', 'w', encoding='utf-8') as filtered:
    reader = csv.DictReader(csv_file)
    field_names = ['Id', 'Images', 'Title', 'Description', 'Price']
    writer = csv.DictWriter(filtered, fieldnames=field_names)
    writer.writeheader()
    for row in reader:
        if len(row['Images'].split(',')) > 3:
            writer.writerow(row)
