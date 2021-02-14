import csv

with open('stage3_test.csv', encoding='utf-8') as csv_file, open('price_filter.csv', 'w', encoding='utf=8') as filtered:
    reader = csv.DictReader(csv_file)
    writer = csv.DictWriter(filtered, fieldnames=reader.fieldnames)
    writer.writeheader()
    for row in reader:
        if 10000 < float(row['Price']) < 50000:
            writer.writerow(row)
