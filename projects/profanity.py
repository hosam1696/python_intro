from urllib import request

try:
    file = open('C:\\Users\\hosam\\PycharmProjects\\first\\projects\\simple.py')
    print(file, file.read())
    pythonurl = "http://www.python.org"
    profalityurl = 'http://www.wdyl.com/profanity?q='+file.read()

    urlconnect = request.urlopen(pythonurl)
    output = urlconnect.read()
    print('> Output: ',output)
except ValueError as err:
    print('Error happened', err)
finally:
    print('file loaded!')
