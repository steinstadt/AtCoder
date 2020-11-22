# Problem C - Travel
from itertools import permutations

# input
N, K = map(int, input().split())
t_list = [[0] * N for i in range(N)]
for i in range(N):
    t_tmp = list(map(int, input().split()))
    for j in range(N):
        t_list[i][j] = t_tmp[j]
pattern = []
for i in range(1, N+1):
    if i==1:
        continue
    pattern.append(i)
pattern = permutations(pattern)
ans = 0

# pattern check
for p in pattern:
    tmp_p = [1] + list(p) + [1]
    tmp = 0
    for i in range(N):
        x_1 = tmp_p[i]
        x_2 = tmp_p[i+1]
        tmp += t_list[x_1-1][x_2-1]
    if tmp==K:
        ans += 1

# output
print(ans)
