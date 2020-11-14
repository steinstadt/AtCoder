# Problem E - Akari

# input
H, W, N, M = map(int, input().split())

# initialization
board = [[0]*W for i in range(H)]
ans = 0
for i in range(N):
    A, B = map(int, input().split())
    board[A-1][B-1] = 2
    ans += 1
for i in range(M):
    C, D = map(int, input().split())
    board[C-1][D-1] = -1

# go from left and right
for i in range(H):
    is_on = False
    is_on_2 = False
    for j in range(W):
        # from left
        if board[i][j]==2:
            is_on = True
        elif board[i][j]==-1:
            is_on = False
        elif is_on and board[i][j]==0:
            board[i][j] = 1
            ans += 1

        # from right
        if board[i][W-j-1]==2:
            is_on_2 = True
        elif board[i][W-j-1]==-1:
            is_on_2 = False
        elif is_on_2 and board[i][W-j-1]==0:
            board[i][W-j-1] = 1
            ans += 1

# go from up and below
for j in range(W):
    is_on = False
    is_on_2 = False
    for i in range(H):
        # from up
        if board[i][j]==2:
            is_on = True
        elif board[i][j]==-1:
            is_on = False
        elif is_on and board[i][j]==0:
            board[i][j] = 1
            ans += 1

        # from below
        if board[H-i-1][j]==2:
            is_on_2 = True
        elif board[H-i-1][j]==-1:
            is_on_2 = False
        elif is_on_2 and board[H-i-1][j]==0:
            board[H-i-1][j] = 1
            ans += 1

# output
print(ans)
