# Problem D - Floor Function

import math

# input
A, B, N = map(int, input().split())

# initialization
ans = 0
if N<B:
    ans = math.floor(A*N/B) - A * math.floor(N/B)
else:
    ans = math.floor(A*(B-1)/B) - A * math.floor((B-1)/B)

# output
print(ans)
