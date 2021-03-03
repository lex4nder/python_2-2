import xml.etree.ElementTree as etree

tree = etree.parse('corp.xml')
root = tree.getroot()
with open('plural_nouns.txt', 'w', encoding='utf-8') as f:
    for token in root.iter('token'):
        plur = False
        noun = False
        for g in token.iter('g'):
            if g.get('v') == 'NOUN':
                noun = True
            elif g.get('v') == 'plur':
                plur = True
        if plur and noun:
            f.write(token.get('text') + '\n')
