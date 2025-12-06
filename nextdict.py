import random
import numpy as np
from collections import Counter
text = ('This is sample text with several words ' 
        'This is more sample text with some different words')

mydict = {}
for word in text.split():
    if word in mydict:
        mydict[word] += 1
    else:
        mydict[word] = 1
print(f'Word{"Word":<13}Count')
for block, counting in mydict.items():
    print(f'{block:<19}{counting}')
print(f'Number of distinct words = {len(mydict)}')

mydict.update(come='7')
mydict.update(go=8, yo=2, man=9)
print(mydict)

roll = [random.randrange(1, 7) for i in range(600)]
mydict.update(Counter(roll))
print(mydict)
