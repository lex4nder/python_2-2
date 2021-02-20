import json

with open('RomeoAndJuliet.json', 'r', encoding='utf-8') as f:
    m_dct = json.load(f)

with open('RaJ_cs.json', 'w', encoding='utf-8') as f1:
    for act in m_dct['acts']:
        for scene in act['scenes']:
            characters = set()
            for line in scene['action']:
                characters.add(line['character'])
            characters = list(characters)
            characters.sort()
            json.dump(characters, f1)
            f1.write('\n')

lines = {}
for act in m_dct['acts']:
    for scene in act['scenes']:
        for line in scene['action']:
            if line['character'] in lines.keys():
                lines[line['character']].append(line['says'])
            else:
                lines[line['character']] = [line['says']]
for char in lines:
    lines[char] = len(lines[char])
amounts = dict(zip(lines.values(), lines.keys()))
print(f'{amounts[max(amounts.keys())]} ({max(amounts.keys())} lines)')
