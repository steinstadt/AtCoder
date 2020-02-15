# Knapsack 1

N, W = map(int, input().split())
knapsack_list = []
for i in range(N):
    knap =  list(map(int, input().split()))
    knapsack_list.append(knap)

cost_list = [0 for i in range(W+1)]
max_cost = 0

# DP loop
for knap in knapsack_list:
    weight = knap[0]
    value = knap[1]
    for i in reversed(range(0, W+1)): # cost update
        loc = i - weight
        if loc<0:
            break
        new_cost = cost_list[loc] + value
        new_cost = max(cost_list[i], new_cost)
        cost_list[i] = new_cost

# max cost process
for cost in cost_list:
    if cost > max_cost:
        max_cost = cost

# print max cost
print(max_cost)
