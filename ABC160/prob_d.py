# Problem D - Line++

# input
N, X, Y = map(int, input().split())

# initialization
INF = 10*18
graph = [[0]*N for i in range(N)]
kyori_graph = [[INF]*N for i in range(N)]
kosu_list = [0]*(N-1)
for i in range(N):
    for j in range(i, N):
        if i==j:
            continue
        if j==i+1:
            graph[i][j] = 1
            kyori_graph[i][j] = 1
        else:
            kyori_graph[i][j] = INF
graph[X-1][Y-1] = 1
kyori_graph[X-1][Y-1] = 1

# graph search
for i in range(N):
    for j in range(i, N):
        if i==j or j==i+1:
            continue
        # if j>X-1:
        #     kyori_graph[i][j] = min(kyori_graph[i][j-1]+1, kyori_graph[i][X-1]+abs(j-X-1), kyori_graph[i][X-1]+abs(j-(Y-1)+1))
        # else:
        #     kyori_graph[i][j] = min(kyori_graph[i][j], kyori_graph[i][j-1] + 1)
        # if j==Y-1 and i+1<=X:
        #     # 遷移先からの距離をもとめる
        #     kyori_graph[i][j] = min(kyori_graph[i][j] ,kyori_graph[i][X-1] + 1, kyori_graph[i][j-1]+1)
        # else:
        #     kyori_graph[i][j] = min(kyori_graph[i][j] , kyori_graph[i][j-1] + 1)

for g in kyori_graph:
    print(g)

for g in graph:
    print(g)

# 個数の数え上げ
for i in range(N):
    for j in range(i, N):
        if i==j:
            continue
        kyori = kyori_graph[i][j]
        kosu_list[kyori-1] += 1

# output
for k in kosu_list:
    print(k)
