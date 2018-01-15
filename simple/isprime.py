def main():
    def isPrime(n):
        is_it = False
        if n == 1:
            is_it = True
        for x in range(2, n):
            if n % x == 0:
                is_it = False
                return '{} -> {} -- {} * {} =  {}'.format(n, 'Prime' if is_it else'Not Prime', n, x, n/x)
        else:
            is_it = True
            return '{} -> {}'.format(n, 'Prime' if is_it else'Not Prime')

    for i in range(1, 21):
        print(isPrime(i))

    d = dict(male='hosam', female='menna')
    print('there is two souls will join together at the end {male} <> {female}'.format(**d))



if __name__ == '__main__':
    main()