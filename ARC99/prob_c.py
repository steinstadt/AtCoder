# Problem C - Minimization

import math

# input
N, K = map(int, input().split())

# output
ans = math.ceil((N - 1) / (K - 1))
print("%d"%(ans))
