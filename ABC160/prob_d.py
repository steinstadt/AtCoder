# Problem D - Line++

# input
N, X, Y = map(int, input().split())

# initialization
graph = [[0]*(N+1) for i in range(N+1)]
kyori_list = [0]*N

# dp count
for i in range(1, N+1):
    for j in range(i, N+1):
        if i==j:
            continue
        graph[i][j] = min(j-i, abs(X-i)+1+abs(Y-j))
for i in range(1, N+1):
    for j in range(1, N+1):
        if i==j:
            continue
        kyori_list[graph[i][j]] += 1

# output
for i in range(1, N):
    print(kyori_list[i])
