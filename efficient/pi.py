acc = 0
for k in range(10000):
    acc += pow(-1, k) / (2 * k + 1)

print(acc * 4)

print(4 * sum(pow(-1, k) / (2 * k + 1) for k in range(10000)))
