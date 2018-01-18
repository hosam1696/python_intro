import os
try:
    youent = str(input('type file name..\n'))
    if isinstance(youent, str):
        try:
            file = open(youent, 'r')
        except FileNotFoundError:
            print('File Not Found: {}'.format(youent))
            exit()
        print('-'*40)
        print(file.read())
        print('-'*40)

    else:
        print('you have to write correct file name')

except ValueError:
    print('input err',ValueError)
    exit(0)
