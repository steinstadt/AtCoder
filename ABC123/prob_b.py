# Problem B - Five Dishes

from itertools import permutations
import math

# input
nums = [0]*5
for i in range(5):
    n = int(input())
    nums[i] = n

# initialization
pattern_moto = [i for i in range(5)]
patterns = permutations(pattern_moto)
min_time = 1000

# time count
for p in patterns:
    tmp = 0
    for i in range(4):
        tmp += nums[p[i]]
        tmp = math.ceil(tmp/10)*10
    tmp += nums[p[4]]
    min_time = min(min_time, tmp)

# output
print(min_time)
