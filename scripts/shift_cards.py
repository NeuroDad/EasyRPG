import sys
import re

fro = int(sys.argv[1])
too = int(sys.argv[2])
shift_by = int(sys.argv[3])

fh = open("DasSchicksalDesReiches.md", 'r')
text = fh.read()

for i in range(fro,too+1)[::-1]:
    ori = i
    new = i+shift_by
    text = re.sub('Karte ' + str(ori), 'Karte ' + str(new), text)

fh = open("DasSchicksalDesReiches.md", 'w')
fh.write(text)
