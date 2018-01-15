import collections

print(open('goldmedals.txt', 'r').readlines()[:10])

medal = collections.namedtuple('modal', ['year', 'athlete', 'team', 'event'])

m = medal('1996', 'Hosam', 'EG', '100 men')

print(m)