# Problem A - Takoyaki
import math

# input
n, x, t = map(int, input().split())

# initialization
ans = 0

# calc
ans = math.ceil(n / x) * t

# output
print(ans)
