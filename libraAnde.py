import statistics
import math

print(i)
input_network = '''-,14,10,19,-,-,-,14,-,-,15,18,-,-,10,-,-,26,-,29,-,19,15,26,-,16,17,21,-,18,-,16,-,-,9,-,-,29,17,-,-,25,-,-,-,21,9,25,-'''
y = [m for m in input_network.split(',') if m != '-']
z = [x for x in input_network.split(',')]
r = 0
for k in y:
    r += int(k)
print(r)
print(z)
print(y)
ac = 10
ab = 14
bd = 15
df = 17
de = 16
eg = 9


