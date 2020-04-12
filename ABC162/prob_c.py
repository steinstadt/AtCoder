
import math

# input
K = int(input())

# initialization
ans = 0

# count
for a in range(1, K+1):
    for b in range(1, K+1):
        tmp = math.gcd(a, b)
        for c in range(1, K+1):
            tmp_1 = math.gcd(tmp, c)
            ans += tmp_1

# output
print(ans)
