def printargs(**kwargs):
    print(kwargs)

printargs(n='hosam', age=1996)

def sumall(*args, multiplier=1):
    print(sum(args*multiplier))

sumall(*list(range(1,5)))