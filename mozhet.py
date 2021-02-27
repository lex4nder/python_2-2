import xml.etree.ElementTree as etree

verb = 0
conj = 0

tree = etree.parse('corp.xml')
root = tree.getroot()
for token in root.iter('token'):
    if token.get('text') == 'может' or token.get('text') == 'Может':
        for g in token.iter('g'):
            if g.get('v') == 'VERB':
                verb += 1
            elif g.get('v') == 'CONJ':
                conj += 1
print(f'Слово \'может\' встречается как глагол {verb} раз(а), как союз - {conj}.')
