# Problem C - Colon

import math

# input
A, B, H, M = map(int, input().split())

# initialization
hour_kakudo = 360*(H/12) + 30*(M/60)
minute_kakudo = 360*(M/60)
kakudo = min(abs(hour_kakudo-minute_kakudo), 360-abs(hour_kakudo-minute_kakudo))
radian = math.radians(kakudo)

# calc
ans = math.sqrt(A**2 + B**2 - 2*A*B*math.cos(radian))

# output
print(ans)
