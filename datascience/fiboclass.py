class Fibonacci():
    def __init__(self):
        self.a = 0
        self.b = 1
        self._data = []

    @property
    def data(self):
        return self._data

    def series(self):
        while self.b < 50:
            self._data.append(self.b)
            self.a, self.b = self.b, self.a + self.b

    printData = lambda self: print(self._data)

    @data.setter
    def setData(self, d):
        self._data = d

Fibo = Fibonacci()
Fibo.series()
Fibo.printData()
Fibo.setData = []
Fibo.printData()