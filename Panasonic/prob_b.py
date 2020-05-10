# Problem B - Bishop

import math

# input
H, W = map(int, input().split())

# check
if H==1 or W==1:
    print(1)
else:
    ans = math.ceil(H * W / 2)
    print(ans)
