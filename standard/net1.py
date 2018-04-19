# urllib
import urllib.request as libreq

conn = libreq.urlopen('https://pluralsight.com')

data = ''.join([line.decode('utf-8') for line in conn.readlines()])

conn.close()

print(data)





