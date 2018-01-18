from projects import bits


def main():
    class Hosam:
        fullname = 'Hosam Elnabawy Ahmed'
        age = 21
        nationality = 'Egyptian'

        def say(self):
            return 'Hello {}.'.format(self.fullname)

    x = (Hosam(), 'Menna')

    print(x, Hosam().say(), sep='\n')

    print(bits.AND(2, 4))


if __name__ == '__main__':
    main()
