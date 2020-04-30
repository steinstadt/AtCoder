# Problem C - Grid Repainting 2

# input
H, W = map(int, input().split())
board = [[0]*W for i in range(H)]
for i in range(H):
    s_list = list(input())
    for j in range(W):
        board[i][j] = s_list[j]

# initialization
is_ok = True

# check
for i in range(H):
    for j in range(W):
        s = board[i][j]
        if s=='.':
            continue

        # right
        if j+1<W:
            if s=='#' and board[i][j+1]=='#':
                continue

        # left
        if j-1>=0:
            if s=='#' and board[i][j-1]=='#':
                continue

        # up
        if i-1>=0:
            if s=='#' and board[i-1][j]=='#':
                continue

        # down
        if i+1<H:
            if s=='#' and board[i+1][j]=='#':
                continue

        is_ok = False
        break

# output
if is_ok:
    print("Yes")
else:
    print("No")
