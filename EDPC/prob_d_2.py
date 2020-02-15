# Knapsack 1

N, W = map(int, input().split())
knapsack_list = []
for i in range(N):
    knap =  list(map(int, input().split()))
    knapsack_list.append(knap)

cost_list = [0 for i in range(W+1)]

# DP loop
for knap in knapsack_list:
    weight = knap[0]
    value = knap[1]
    

for cost in cost_list:
    print(cost)
