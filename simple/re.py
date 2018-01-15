"""import re

cf = open('fiboclass.py')
for line in cf.readlines():
    print(line)
    matched = re.findall('def', line)
    if (matched):
        print(line, matched, sep='\n')


"""
import os

string = 'hosam elnabawy ahmed'

print(string.startswith('menna'))

print('path one', os.path.dirname(__file__), __file__)
print('path two', os.path.dirname(os.path.dirname(os.path.abspath(__file__))))