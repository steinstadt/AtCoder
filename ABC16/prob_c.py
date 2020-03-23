# Problem C - 友達の友達

# input
N, M = map(int, input().split())

# initialization
friends_graph = [[0]*N for i in range(N)]
for i in range(N):
    friends_graph[i-1][i-1] = 1

# graph search
for i in range(M):
    A, B = map(int, input().split())
    friends_graph[A-1][B-1] = 1
    friends_graph[B-1][A-1] = 1

# output
for i in range(N):
    zero_count = 0
    for j in range(N):
        if friends_graph[i][j]==0:
            zero_count += 1
    print(zero_count)
