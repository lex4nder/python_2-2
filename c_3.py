import json
import collections as cs

with open('RomeoAndJuliet.json', 'r', encoding='utf-8') as f:
    m_dct = json.load(f)

c = cs.Counter()
for act in m_dct['acts']:
    for scene in act['scenes']:
        for line in scene['action']:
            c[line['character']] += len(line['says'])
print(c.most_common())
