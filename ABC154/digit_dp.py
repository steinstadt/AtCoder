N = input() # 数字を文字列として受け取る

keta = len(N)

dp = [[0]*2 for i in range(keta+1)]

dp[0][0] = 1 # 初期化処理
for i in range(keta):
    for smaller in range(2):
        x = 0
        if smaller:
            x = 9
        else:
            x = int(N[i])
        # 遷移処理
        for num in range(x+1):
            dp[i+1][smaller or num<int(N[i])] += dp[i][smaller]

ans = dp[keta][0] + dp[keta][1]

print(ans-1)
