import sys
import re

ori = sys.argv[1]
new = sys.argv[2]

fh = open("DasSchicksalDesReiches.md", 'r')
text = fh.read()

text = re.sub('Karte ' + str(ori), 'Karte ' + str(new), text)

fh = open("DasSchicksalDesReiches.md", 'w')
fh.write(text)
