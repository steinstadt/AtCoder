# E - Knapsack 2

N, W = map(int, input().split())
knapsack_list = []
value_max = 0
max_cost = 0
for i in range(N):
    knap =  list(map(int, input().split()))
    knapsack_list.append(knap)
    value_max = value_max + knap[1]

cost_list = [[10**12]*(value_max+1) for _ in range(N+1)]

cost_list[0][0] = 0
for i in range(N):
    cost_list[i+1][0] = 0
    weight = knapsack_list[i][0]
    value = knapsack_list[i][1]
    for j in range(value_max+1):
        if j<value:
            cost_list[i+1][j] = cost_list[i][j] # そのまま遷移させる
            continue
        new_cost = cost_list[i][j-value] + weight
        new_cost = min(cost_list[i][j], new_cost)
        cost_list[i+1][j] = new_cost # 次の遷移状態へコストを渡す

for i in range(value_max+1):
    weight = cost_list[N][i]
    if weight<=W:
        max_cost = i

print(max_cost)
