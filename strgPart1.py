# coding: utf-8
print('PyDev console: using IPython 8.6.0\n')

import sys; print('Python %s on %s' % (sys.version, sys.platform))
sys.path.extend(['C:\\Users\\pc\\PycharmProjects\\pythonProject', 'C:/Users/pc/PycharmProjects/pythonProject'])
sentence = '\t\n This is a test string \t\t \n'
sentence.strip()
sentence.lstrip()
sentence.rstrip()
s1 = 'happy birthday'
s1.capitalize()
s1.title()
sentence.title()
print(f'A: {ord("A")} ; a: {ord("a")}')
'Orange' == 'orange'
'Orange' != 'orange'
'Orange' >= 'orange'
'Orange' <= 'orange'
'Orange' > 'orange'
'Orange' < 'orange'
sentence1 = 'to be or not to be that is the question'
sentence1.count('to')
sentence1.count('not')
sentence1.count('to', 12)
sentence1.count('that', 12, 25)
sentence1.count('t')
sentence1.index('be')
sentence1.rindex('be')
sentence1.find('not')
sentence1.rfind('not')
sentence1.rfind('be')
sentence1.find('be')
'that' in sentence
'that' in sentence1
'THAT' in sentence1
'THAT' not in sentence1
sentence1.startswith('to')
sentence1.startswith('be')
sentence1.endswith('question')
sentence1.endswith('quest')
values = '1\t2\t3\t4\t5'
values.replace('\t', ',')
