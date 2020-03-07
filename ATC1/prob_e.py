# Problem E - 数

# input process
D = int(input()) # multiple number
N = input() # positive number str
keta = len(N)

INF = 10**9 + 7 # **には気をつけよう

# digit dp
dp = [[[0]*D for j in range(2)] for i in range(keta+1)] # リストは内包表記で作成しよう
dp[0][0][0] = 1
for k in range(keta): # keta loop 0~N
    for s in range(2): # smaller loop 0~1
        for d in range(D): # sum_position loop
            d_num = (9 if s else int(N[k]))

            for i in range(d_num+1): # num_sum loop 0~limit
                sum_position = (d + i) % D
                dp[k+1][s or i < d_num][sum_position]  += dp[k][s][d]
                dp[k+1][s or i < d_num][sum_position] %= INF

print((dp[keta][0][0] + dp[keta][1][0] - 1)%INF)
