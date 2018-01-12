x = [1,2,3,4,5,6,7,8,9]
print(x)

import random

y = []

while x:
    idx = random.randrange(0, len(x))
    val = x[idx]
    x[idx], x[len(x) - 1] = x[len(x) - 1], x[idx]
    y.append(val)
    x.pop()

print(y)