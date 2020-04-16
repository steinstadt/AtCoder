# Problem E - Crested Ibis vs Monster

# input
H, N = map(int, input().split())
magic_list = []
for i in range(N):
    A, B = map(int, input().split())
    magic_list.append([A, B])

# initialization
dp = [float('INF')]*(H+1)
dp[0] = 0
mg_len = len(magic_list)

# dp
for i in range(1, H+1):
    for j in range(mg_len):
        a = magic_list[j][0]
        b = magic_list[j][1]
        last_p = i - a
        if last_p<0:
            last_p = 0
        tmp = dp[last_p] + b
        dp[i] = min(dp[i], tmp)

# output
print(dp[H])
