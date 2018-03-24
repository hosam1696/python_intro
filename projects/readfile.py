
file = open('f.txt')

for line in file.readlines():
    print(line,end='')

with open('f.txt') as f:
    data = f.readlines()
    print("Here are all the current results:")
    print('\n')
    print(data)
    for line in file.readlines():
        print(line, end='')
    print(''.join(data))