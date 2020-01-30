# ダイナミック・プログラミング
# PythonではTLEを起こしてしまう例

INF = float('inf')

H, N = map(int, input().split())
A = []
B = []

for i in range(N):
    a_i, b_i = map(int, input().split())
    A.append(a_i)
    B.append(b_i)

dp = [[INF]*(H+1) for i in range(N+1)] # DP用配列
dp[0][0] = 0 # 初期化処理
for i in range(0,N):
    for j in range(0,H+1):
        a, b = j+A[i], H
        min_h = a
        if a>b:
            min_h = b
        a, b = dp[i+1][j], dp[i][j]
        if a>b:
            dp[i+1][j] = b
        a, b = dp[i+1][min_h], dp[i+1][j]+B[i]
        if a>b:
            dp[i+1][min_h] = b

print(dp[N][H])
