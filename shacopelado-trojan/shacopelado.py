import os
import os.path
from pathlib import Path
i = 0
#writes the filename which gets larger
file = 'h'
while i < 40:
    #start creating .txt files which contains some arab random
    filetemp = file + '.txt'
    writing = open(filetemp, 'w')
    for i in range(0, 20):
         writing.write('الله الحمد لله ملكنا ومخلصن\n')
    writing.close()
    if file[-1] == 'a':
        file = file + 'h'
    else:
        file = file + 'a'
    i += 1
