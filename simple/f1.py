str = 'Hosam'

justStr = str.ljust(15, '.')
print(justStr)
print('     Manana'.lstrip())


class NewOne:
    def __init__(self):
        print('why this is self')

    def __str__(self):
        return 'New One class'


newOne = NewOne()
print(newOne.__str__().center(25))
def printSep():
    print('|',' '*4,'|',' '*4, '|')
for i in range(2):
    print('+-----+'*2)
    for i in range(3):
        printSep()
print('+-----+' * 2)

newdict = {'x':'asdsdsd'}
print(newdict)

print('ssdkfjsdlf {}'.format(newdict['x']))

