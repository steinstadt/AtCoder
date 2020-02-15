# Knapsack 1

N, W = map(int, input().split())
knapsack_list = []
for i in range(N):
    knap =  list(map(int, input().split()))
    knapsack_list.append(knap)

cost_list = [0 for i in range(W+1)]

# DP loop
for i in range(1,W+1):
    for knap in knapsack_list:
        pre_w = i - knap[0]
        if pre_w < 0:
            continue
        new_cost = cost_list[pre_w] + knap[1]
        new_cost = max(cost_list[i], new_cost)
        cost_list[i] = new_cost

for cost in cost_list:
    print(cost)
