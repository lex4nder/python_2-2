import json
import collections as cs

with open('RomeoAndJuliet.json', 'r', encoding='utf-8') as f:
    m_dct = json.load(f)

dd = cs.defaultdict(list)
for act in m_dct['acts']:
    for scene in act['scenes']:
        for line in scene['action']:
            dd[line['character']].append(line['says'])

with open('c_2.txt', 'w', encoding='utf-8') as f:
    for c in dd:
        f.write(c + ': ' + str(dd[c]) + '\n\n')
