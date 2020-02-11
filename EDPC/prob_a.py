# Flog 1

N = int(input())
h_list = list(map(int, input().split()))

cost_list = [0 for i in range(N+1)]

# ステップiへたどり着くためのコスト最小値
for i in range(1,N):
    if i==1:
        cost_list[i+1] = abs(h_list[i] - h_list[i-1])
        continue

    step_1 = cost_list[i] + abs(h_list[i]-h_list[i-1])
    step_2 = cost_list[i-1] + abs(h_list[i]-h_list[i-2])
    min_cost = min(step_1, step_2)
    cost_list[i+1] = min_cost


print(cost_list[N])
