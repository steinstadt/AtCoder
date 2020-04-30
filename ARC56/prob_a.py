# Problem A - みんなでワイワイミカン

import math

# input
A, B, K, L = map(int, input().split())

# initialization
ans = 0

# check
ans += B * math.floor(K / L)
amari = K % L
if A * amari < B:
    ans += A * amari
else:
    ans += B

# output
print(ans)
