# Problem Line++

# input
N, X, Y = map(int, input().split())

# initialization
kyori_graph = [[N]*N for i in range(N)]
kosu_list = [0]*(N-1)

# dp
for i in range(N):
    for j in range(i+1, N):
        kyori_graph[i][j] = min(abs(j-i), abs((X-1)-i)+1+abs(j-(Y-1)))

# output
for i in range(N):
    for j in range(i+1, N):
        kyori = kyori_graph[i][j]
        kosu_list[kyori-1] += 1
for k in kosu_list:
    print(k)
