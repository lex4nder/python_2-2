import json

new_dct = {}

with open('wikidata_1000.json', 'r', encoding='utf-8') as f1:
    for el in f1:
        dct = json.loads(el)
        if 'description' in dct.keys():
            new_dct[dct['label']['value']] = dct['description']['value']
        else:
            new_dct[dct['label']['value']] = None

with open('wikidata_defs.json', 'w', encoding='utf-8') as f2:
    json.dump(new_dct, f2, indent=4, ensure_ascii=False)
