# Problem A - Shik and Stone (幅優先探索は難しい> <)

# input
H, W = map(int, input().split())
board = [['.']*W for i in range(H)]
v_board = [[True]*W for i in range(H)]
for i in range(H):
    s = input()
    for j in range(W):
        board[i][j] = s[j]

# initialization
is_ok = True
search_queue = []

# search
search_queue.append([0, 0])
while len(search_queue)>0:
    s = search_queue.pop(0)
    x = s[0]
    y = s[1]
    v_board[x][y] = False

    # left
    if y-1>=0 and board[x][y-1]=='#' and v_board[x][y-1]:
        is_ok = False
        search_queue.append([x, y-1])

    # up
    if x-1>=0 and board[x-1][y]=='#' and v_board[x-1][y]:
        is_ok = False
        search_queue.append([x-1, y])

    # right
    if y+1<W and board[x][y+1]=='#' and v_board[x][y+1]:
        search_queue.append([x, y+1])

    # down
    if x+1<H and board[x+1][y]=='#' and v_board[x+1][y]:
        search_queue.append([x+1, y])

# output
if is_ok:
    print("Possible")
else:
    print("Impossible")
