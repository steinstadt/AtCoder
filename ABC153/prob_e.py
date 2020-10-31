# Problem E - Crested Ibis vs Monster

# input
h, n = map(int, input().split())
magic_list = []
for i in range(n):
    a, b = map(int, input().split())
    magic_list.append([a, b])

# initialization
dp = [float("inf")] * (h + 1)
dp[0] = 0

# dp
for i in range(1, h+1):
    for m in magic_list:
        past_pos = max(0, i - m[0])
        dp[i] = min(dp[i], dp[past_pos] + m[1])

# output
print(dp[h])
