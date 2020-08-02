# Problem B - Distance

import math

# input
N, D = map(int, input().split())

# initialization
count = 0

# count
for i in range(N):
    x, y = map(int, input().split())
    tmp = math.sqrt(x**2 + y**2)
    if tmp<=D:
        count += 1

# output
print(count)
