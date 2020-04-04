# Problem C - Together

import collections

# input
N = int(input())
a_list = list(map(int, input().split()))

# initialization
num_counter = collections.Counter(a_list)
max_count = 0

# count
for k in num_counter.keys():
    nc = num_counter[k]
    tmp_mae = num_counter[k-1]
    tmp_ushiro = num_counter[k+1]
    max_count = max(max_count, nc + tmp_mae + tmp_ushiro)

# output
print(max_count)
