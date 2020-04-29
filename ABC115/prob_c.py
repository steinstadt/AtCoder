# Problem C - Christmas Eve

# input
N, K = map(int, input().split())
h = [0]*N
for i in range(N):
    h[i] = int(input())

# initialization
h = sorted(h)
min_ans = float('INF')
for i in range(N-K+1):
    tmp_max = h[i+K-1]
    tmp_min = h[i]
    min_ans = min(min_ans, tmp_max - tmp_min)

# output
print(min_ans)
