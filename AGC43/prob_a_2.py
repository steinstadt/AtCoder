# Problem A - Range Flip Find Route

# input
h, w = map(int, input().split())
s_board = [['']*w for i in range(h)]
for i in range(h):
    s = list(input())
    for j in range(w):
        s_board[i][j] = s[j]

# initialization
INF = 10**5
dp = [[INF]*w for i in range(h)]
if s_board[0][0]=='#':
    dp[0][0] = 1
else:
    dp[0][0] = 0

# count
for i in range(h):
    for j in range(w):
        # skip
        if i==0 and j==0:
            continue

        # left
        if j-1>=0:
            if s_board[i][j]=='#' and s_board[i][j-1]=='.':
                dp[i][j] = min(dp[i][j], dp[i][j-1] + 1)
            else:
                dp[i][j] = min(dp[i][j], dp[i][j-1])

        # up
        if i-1>=0:
            if s_board[i][j]=='#' and s_board[i-1][j]=='.':
                dp[i][j] = min(dp[i][j], dp[i-1][j] + 1)
            else:
                dp[i][j] = min(dp[i][j], dp[i-1][j])

# output
print(dp[-1][-1])
