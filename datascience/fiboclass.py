class Fibonacci():
    def __init__(self, limit: int):
        self.initvalues()
        self.limit = limit or 0

    def initvalues(self):
        self.a = 0
        self.b = 1
        self._data = []

    @property
    def data(self):
        return self._data

    def series(self, printdata: bool = False):
        self.initvalues()
        while self.b < self.limit:
            self._data.append(self.b)
            self.a, self.b = self.b, self.a + self.b

        printdata and self.printData()

    printData = lambda self: print(self._data)

    @data.setter
    def setData(self, d):
        self._data = d

    @data.setter
    def setLimit(self, val):
        self.limit = val

    def getvalueat(self, val_index: int):
        if self.data.index(val_index):
            return f'number at position ({val_index}) -> {self.data[val_index]}'
        else:
            return ValueError('Fibonacci Number is not in range, try extending the range')


fibo = Fibonacci(10)  # create a new instance of custom Fibonacci numbers
fibo.series()         # create out full generated series
fibo.printData()      # print out full generated series
fibo.setData = []     # reset series data
fibo.printData()      # print out full generated series

fibo.setLimit = 100        # set a new limit for the fibonacci series
fibo.series(True)          # create and print the series
print(fibo.getvalueat(5))  # get specific value from the series
