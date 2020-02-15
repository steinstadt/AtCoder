# C - Vacation

N = int(input()) # days
happy_list = [] # action cost list
for i in range(N):
    happy_action = list(map(int, input().split()))
    happy_list.append(happy_action)

happy_cost_max = 0 # result prepare
happy_cost_list = [ [0]*3 for i in range(N+1)] # DP list

# DP loop
for i in range(N):
    happy_action = happy_list[i]
    for j in range(3):
        pre_cost = happy_cost_list[i][j]
        for k in range(3):
            if not j==k:
                new_cost = max(happy_cost_list[i+1][k], pre_cost+happy_action[j])
                happy_cost_list[i+1][k] = new_cost

happy_cost_max = max(happy_cost_list[N])
print(happy_cost_max)
