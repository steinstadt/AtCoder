# Problem A - Painting

import math

# input
H = int(input())
W = int(input())
N = int(input())

# initialization
max_num = max(H, W)
ans = math.ceil(N / max_num)

# output
print(ans)
