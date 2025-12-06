# coding: utf-8
print('PyDev console: using IPython 8.6.0\n')

import sys; print('Python %s on %s' % (sys.version, sys.platform))
sys.path.extend(['C:\\Users\\pc\\PycharmProjects\\pythonProject', 'C:/Users/pc/PycharmProjects/pythonProject'])
""" * VS. +"""
### When you use the '*' sign it means 0 or more...But the '+' sign means at least one ###  
import re
'Valid' if re.fullmatch('[A-Z][a-z]+', 'Wally') else 'Invalid'
'valid' if re.fullmatch('[A-Z][a-z]+', 'Ea') else 'Invalid'
'valid' if re.fullmatch('[A-Z][a-z]+', 'E') else 'Invalid'
'Match' if re.fullmatch('Labell?ed', 'Labelled') else 'No Match'
'Match' if re.fullmatch('Labell?ed', 'Labeled') else 'No Match'
'Match' if re.fullmatch('Labell?ed', 'Labellled') else 'No Match'
'Match' if re.fullmatch('Labe{n,3}ed', 'Labellled') else 'No Match'
'Match' if re.fullmatch('Labe{n,3}ed', 'Labelled') else 'No Match'
'Match' if re.fullmatch('Labe{n,}ed', 'Labellled') else 'No Match'
### The three direct snippets above are unwanted...Just trials of my own...nothing serious ###
'Valid' if re.fullmatch('\d{3,}', '123') else 'Invalid'
'Valid' if re.fullmatch('\d{3,}','123456789') else 'Invalid'
'Valid' if re.fullmatch('\d{3,}', '12') else 'Invalid'
'Valid' if re.fullmatch('\d{3,6}', '123') else 'Invalid'
'Valid' if re.fullmatch('\d{3,6}', '123456') else 'Invalid'
'Valid' if re.fullmatch('\d{3,6}', '1234567') else 'Invalid'
'Valid' if re.fullmatch('\d{3,6}', '12') else 'Invalid'
### The first three snippets from the top is used to specify three or more characters whiles the other four below them are used to 
### specify length of digits between three and Six ###
### Or let me say from three to six digits ###
re.sub(r'\t', ',', '1\t2\t3\t4')
###The 'sub()' function used above is used to substitute or replace characters in a string### 
###Its first argument takes the character to replace in single quotes###
###The second argument takes the replacement character...also in single quotes###
###The final argument takes the string in which these changes are to be made###
###It has a keyword argument 'count' which could be used to specify the number of the targeted character to be replace###
re.sub(r'\t', ',', '1\t2\t3\t4', count=2)
re.split(r'\s*', '1, 2, 3,4,  5,6,7,8,9')
re.split(r',\s*', '1, 2, 3,4,  5,6,7,8,9')
re.split(r',\s*', '1, 2, 3,4,  5,6,7,8,9', maxsplit=3)
###The  re 'split()' function splits the string into individual parts and fixes in the specified character condition###
###The first argument takes the character condition###
###The second argument takes the string to split###
###The third argument is optional and takes the optional argument 'maxsplit=' which specifies the no. of splits to be adminstered###
