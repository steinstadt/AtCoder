# Problem C - Strange Bank

# input
N = int(input())

# initialization
INF = 10**15
dp = [INF] * (N+1)

# dynamic programming
dp[0] = 0
for i in range(1, N+1):

    # 9 yen
    if i>=9:
        nine_count = 0
        tmp = 1
        while tmp*9<=i:
            nine_count += 1
            tmp *= 9
        dp[i] = min(dp[i], dp[i-9**nine_count]+1)

    # 6 yen
    if i>=6:
        six_count = 0
        tmp = 1
        while tmp*6<=i:
            six_count += 1
            tmp *= 6
        dp[i] = min(dp[i], dp[i-6**six_count]+1)

    # 1 yen
    if i>=1:
        dp[i] = min(dp[i], dp[i-1]+1)

# output
print(dp[N])
