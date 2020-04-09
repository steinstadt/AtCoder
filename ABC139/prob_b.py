# Problem B - Power Socket

import math

# input
A, B = map(int, input().split())

# initialization
ans = math.ceil((B-1) / (A-1))

# output
print(ans)
