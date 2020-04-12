# Problem C - Prison

# input
N, M = map(int, input().split())

# initialization
max_left = 0
min_right = N

# update loop
for i in range(M):
    L, R = map(int, input().split())
    max_left = max(max_left, L)
    min_right = min(min_right, R)

# output
if max_left>min_right:
    print(0)
else:
    ans = min_right - max_left + 1
    print(ans)
