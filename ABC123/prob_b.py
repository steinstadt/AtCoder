# Problem B - Five Dishes

import itertools
import math

# input process
cost_list = []
for i in range(5):
    cost_list.append(int(input()))

# initialization
min_ans = 1000

# count process
perm_list = list(itertools.permutations(cost_list))
for p in perm_list:
    p = list(p)
    # cost calc
    tmp = 0
    for i in range(len(p)):
        if i==4:
            tmp += p[i]
            break
        tmp += p[i]
        tmp = math.ceil((tmp/10))*10

    min_ans = min(min_ans, tmp)

# output process
print(min_ans)
