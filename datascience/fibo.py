a,b = 0, 1
while b<40:
    print(b)
    a,b = b, a+b
print('Done'.center(15))

fh = open('f1.py','r')

print(['This line contains class {}'.format(l) for l in fh.readlines() if l.startswith(r'class')])