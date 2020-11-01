# Problem A - Don't be late

import math

# input
D, T, S = map(int, input().split())

# initialization
take_time = math.ceil(D / S)

# output
if take_time<=T:
    print("Yes")
else:
    print("No")
