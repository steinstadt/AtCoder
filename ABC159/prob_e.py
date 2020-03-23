# Problem E - Dividing Chocolate

# input
H, W, K = map(int, input().split())
s_board = [['.']*W for i in range(H)]
c_board = [[0]*W for i in range(H)]
for i in range(H):
    s = list(input())
    for j in range(W):
        s_board[i][j] = s[j]
        c_board[i][j] = int(s[j])

# initialization
divide_count = 0

# count
for i in range(H-1):
    tmp_sum = 0
    if sum(c_board[i])>K:
        divide_count = sum(c_board[i]) // K
        c_board[i][0] = 0
    for j in range(W):
        s = s_board[i][j]
        c_board[i+1][j] += c_board[i][j]

# output
print(divide_count)
