# Problem D - Line++

# input
N, X, Y = map(int, input().split())

# initialization
INF = N
kyori_graph = [[INF]*N for i in range(N)]
kosu_list = [0]*(N-1)

# graph search
for i in range(N):
    for j in range(i+1, N):
        # グラフの更新
        kyori_graph[i][j] = min(abs(j-i), abs(X-1-i)+1+abs(j-(Y-1)))

# 個数の数え上げ
for i in range(N):
    for j in range(i+1, N):
        kyori = kyori_graph[i][j]
        kosu_list[kyori-1] += 1

# output
for k in kosu_list:
    print(k)
