# if you can not explain it on one sentence you have to break it more

print([x for x in range(1,15) if x%2 == 0])
tup = {1,4,1}
print(tup, type(tup), tup.union({1,5,6}), type('dgf'))

arr = [1, 2, 'hosam', 'menna']

arr.append('Spark Love')
#arr.extend(tup)

def isInt(integer):
    return isinstance(integer, int)

print([k**5 for k in arr if isInt(k)])

