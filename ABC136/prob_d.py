# Porblem D - Gathering Children
import re

# input process
S = input()

# initialization
ans_list = []
in_list = re.findall(r"R+L+", S)

# ["RRL", "RL"]
# part of list process
for p in in_list:
    p_r = re.findall(r"R+", p)[0]
    p_l = re.findall(r"L+", p)[0]
    l_count = 0
    r_count = 0

    # R to L process
    for i in range(1, len(p_r)+1):
        if i%2==0:
            l_count = l_count + 1
        else:
            r_count = r_count + 1

    # L to R process
    for i in range(1, len(p_l)+1):
        if i%2==0:
            r_count = r_count + 1
        else:
            l_count = l_count + 1

    # output prcess R
    for i in range(len(p_r)-1):
        ans_list.append(0)
    ans_list.append(r_count)

    # output process L
    ans_list.append(l_count)
    for i in range(len(p_l)-1):
        ans_list.append(0)

# output process
for a in ans_list:
    print(a, end=" ")
