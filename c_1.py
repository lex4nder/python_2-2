import csv
import collections as cs

with open('stage3_test.csv', encoding='utf-8') as csv_file:
    reader = csv.DictReader(csv_file)
    words = []
    for row in reader:
        for word in row['Title'].split():
            words.append(word.rstrip('.,!?').lower())
        for word in row['Description'].split():
            words.append(word.rstrip('.,!?').lower())

print(cs.Counter(words).most_common(20), cs.Counter(words).most_common()[:-21:-1], sep='\n')
