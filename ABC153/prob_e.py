# Problem E - Crested Ibis vs Monster

# input
H, N = map(int, input().split())
ab_pattern = []
for i in range(N):
    a, b = map(int, input().split())
    ab_pattern.append([a, b])

# initialization
mp_list = [float('INF')] * (H+1)
mp_list[0] = 0

# dp
for i in range(1, H+1):
    for ab in ab_pattern:
        a = ab[0]
        b = ab[1]
        if i-a>=0:
            mp_list[i] = min(mp_list[i], mp_list[i-a] + b)
        else:
            mp_list[i] = min(mp_list[i], mp_list[0] + b)

# output
print(mp_list[H])
