# Problem B - 1%

import math

# input
X = int(input())

# initialization
ans = 0
tmp_count = 100

# count
while tmp_count<X:
    tmp_count = math.floor(tmp_count * 1.01)
    ans += 1

# output
print(ans)
