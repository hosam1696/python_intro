even = (i for i in range(1,21) if i % 2 == 0)

print(even.__next__())
print(even.__next__())
even = (i for i in range(20) if i % 2 == 0)
print(sum(even))

# Febonacci Sequence
def fibonacci():
    f1, f2 = 0, 1
    while True:
        yield f2
        f1, f2 = f2, f1 + f2

f = fibonacci()

def getFibo(num):
    return [next(f) for num in range(num)]

print(getFibo(10))