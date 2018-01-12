
import urllib.request as req
import random
import datetime


def main():
    page = req.urlopen('http://bw.org')
    print(page)
    x = list(range(1, 25))
    print(random.shuffle(x))
    print(datetime.date)

if __name__ == '__main__':
    main()