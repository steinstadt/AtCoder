# Problem D - Line++

# input
N, X, Y = map(int, input().split())

# initialization
graph = [[float('INF')]*(N+1) for i in range(N+1)]
for i in range(1, N):
    graph[i][i+1] = 1
graph[X][Y] = 1
kyori = [0]*N

# dp
for i in range(1, N):
    for j in range(i+1, N+1):
        if j<=X:
            graph[i][j] = min(graph[i][j], abs(j - i))
        else:
            graph[i][j] = min(graph[i][j], abs(j - i), abs(X - i)+1+abs(j - Y))

# kyori count
for i in range(1, N+1):
    for j in range(i+1, N+1):
        if not graph[i][j]==float('INF'):
            kyori[graph[i][j]] += 1

# output
for i in range(1, N):
    print(kyori[i])
