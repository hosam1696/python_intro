import bs4
import requests


pageurl = 'http://mars.nasa.gov/msl/multimedia/raw/?s=1537&camera=FHAZ_'

webpage = requests.get(pageurl)
print('webpage response',webpage)
soup = bs4.BeautifulSoup(webpage, 'lxml')

print(soup)