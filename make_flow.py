import sys
import re

filename = sys.argv[1]

fh = open(filename, 'r')
text = fh.read()

m_all = re.findall('VAR_DESC: ([\s\S]+?)\nVAR_CARD: Karte ([0-9]+)([\s\S]+?)END', text)

for i, v in enumerate(m_all):
    print v[1], v[0], " "*(45-len(v[0])),

    m = re.findall('Karte ([0-9]+)', v[2])	
    print m