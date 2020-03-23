# Problem B - Two Colors Card Game

# input
N = int(input())
s_list = {}
for i in range(N):
    s = input()
    if s in s_list:
        s_list[s] += 1
    else:
        s_list[s] = 1
M = int(input())
t_list = {}
for i in range(M):
    t = input()
    if t in t_list:
        t_list[t] += 1
    else:
        t_list[t] = 1

# initialization
max_cost = 0

# count step
for s in s_list:
    s_cost = s_list[s]
    if s in t_list:
        max_cost = max(max_cost, s_cost - t_list[s])
    else:
        max_cost = max(max_cost, s_cost)

# output
print(max_cost)
