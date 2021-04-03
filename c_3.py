import json
import collections as cs

with open('RomeoAndJuliet.json', 'r', encoding='utf-8') as f:
    m_dct = json.load(f)

dct = {}
for act in m_dct['acts']:
    for scene in act['scenes']:
        for line in scene['action']:
            try:
                dct[line['character']] += len(line['says'])
            except KeyError:
                dct[line['character']] = len(line['says'])
print(cs.Counter(dct).most_common())
