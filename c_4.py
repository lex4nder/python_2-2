import csv
import collections as cs


with open('stage3_test.csv', encoding='utf-8') as csv_file, open('price_filter.csv', 'w', encoding='utf=8') as filtered:
    reader = csv.DictReader(csv_file)
    dct = {}
    for row in reader:
        dct[row['Title']] = row['Price']
    with open('c_4.txt', 'w', encoding='utf-8') as f:
        f.write(str(cs.OrderedDict(sorted(dct.items(), key=lambda t: float(t[1])))) + '\n\n')
        f.write(str(cs.OrderedDict(sorted(dct.items(), key=lambda t: float(t[1]), reverse=True))))
