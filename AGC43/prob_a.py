# Problem A - Range Flip Find Route

# input
h, w = map(int, input().split())
s_board = [['.']*w for i in range(h)]
c_board = [[100000]*w for i in range(h)]
for i in range(h):
    w_line = list(input())
    for j in range(w):
        s_board[i][j] = w_line[j]

# initialization
visit_queue = []

# count step
visit_queue.append([0, 0])
c_board[0][0] = 0
while len(visit_queue)>0:
    q = visit_queue.pop(0)
    r = q[0]
    c = q[1]
    # right
    if c+1<w:
        if s_board[r][c]=='.' and s_board[r][c+1]=='#':
            c_board[r][c+1] = min(c_board[r][c+1], c_board[r][c]+1)
        else:
            c_board[r][c+1] = min(c_board[r][c+1], c_board[r][c])
        visit_queue.append([r, c+1])
    # down
    if r+1<h:
        if s_board[r][c]=='.' and s_board[r+1][c]=='#':
            c_board[r+1][c] = min(c_board[r+1][c], c_board[r][c]+1)
        else:
            c_board[r+1][c] = min(c_board[r+1][c], c_board[r][c])
        visit_queue.append([r+1, c])

# start adjust
if s_board[0][0]=='#':
    c_board[h-1][w-1] += 1

# output
print(c_board[h-1][w-1])
