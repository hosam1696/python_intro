class X:
    def __init__(self):
        print('X Init')
        self.staticmethod('inline static method res')

    @staticmethod
    def staticmethod(x):
        print('static method result: {} '.format(x))

    def __get__(self, instance, owner):
        return instance



X.staticmethod('hosam')

X()
