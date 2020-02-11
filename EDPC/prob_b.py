# Flog 2

N, K = map(int, input().split())
h_list = list(map(int, input().split()))

cost_list = [10**9 for i in range(N+1)] # iまでのコスト最小値

# コスト最小値の生成
cost_list[1] = 0 # 初期化
for i in range(1,N):
    # ステップごとのコスト更新
    for step in range(1,K+1):
        p = i + step
        if p>N:
            continue
        cost = cost_list[i] + abs(h_list[p-1]-h_list[i-1])
        if cost<cost_list[p]: # 小さければコスト更新
            cost_list[p] = cost

print(cost_list[N])
