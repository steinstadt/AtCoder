# Problem C - Five Transportations

import math

# input
N = int(input())
trans = [0]*5
for i in range(5):
    trans[i] = int(input())

# initialization
min_pos = 0
for i in range(5):
    if trans[min_pos]>trans[i]:
        min_pos = i

# calc
time_1 = min_pos
time_2 = math.ceil(N/trans[min_pos])
time_3 = 6 - (min_pos + 2)
ans = time_1 + time_2 + time_3

# output
print(ans)
