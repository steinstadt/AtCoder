# Problem C - Colon

import math

# input
A, B, H, M = map(int, input().split())

# initialization
tmp_1 = H * 30 + 0.5 * M
tmp_2 = 6 * M
tmp_3 = min(abs(tmp_1-tmp_2), 360-abs(tmp_1-tmp_2))
radian = math.radians(tmp_3)
tmp_4 = math.sqrt(A**2 + B**2 - 2*A*B*math.cos(radian))

# output
print(tmp_4)
