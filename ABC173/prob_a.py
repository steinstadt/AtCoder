# Problem A - Payment
import math

# input
N = int(input())

# initialization
tmp = math.ceil(N / 1000)
ans = 1000*tmp - N

# output
print(ans)
