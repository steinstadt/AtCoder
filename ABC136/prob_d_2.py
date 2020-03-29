# Problem D - Gathering Children

import re

# input
S = input()

# initialization
rl_list = re.findall(r'R+L+', S)
ans_list = []

# count
for rl in rl_list:
    right_count = 0
    left_count = 0

    right = re.findall(r'R+', rl)[0]
    left = re.findall(r'L+', rl)[0]

    # right count
    for i in range(1, len(right)+1):
        if i%2==0:
            left_count += 1
        else:
            right_count += 1

    # left count
    for i in range(1, len(left)+1):
        if i%2==0:
            right_count += 1
        else:
            left_count += 1

    # answer decision
    for i in range(len(right)-1):
        ans_list.append(0)
    ans_list.append(right_count)
    ans_list.append(left_count)
    for i in range(len(left)-1):
        ans_list.append(0)

# output
ans_list = list(map(str, ans_list))
print(" ".join(ans_list))
