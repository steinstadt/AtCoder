# Problem C - Candies

# input
N = int(input())
candie_board = [[0]*N for i in range(2)]
for i in range(2):
    a_list = list(map(int, input().split()))
    for j in range(len(a_list)):
        candie_board[i][j] = a_list[j]

# initialization
cost_board = [[0]*N for i in range(2)]
cost_board[0][0] = candie_board[0][0]
visit_queue = []
visit_queue.append([0, 0])

# search
while len(visit_queue)>0:
    v = visit_queue.pop(0)
    x = v[0]
    y = v[1]

    # right
    if y+1<N:
        cost_board[x][y+1] = max(cost_board[x][y+1], cost_board[x][y] + candie_board[x][y+1])
        visit_queue.append([x, y+1])

    # down
    if x+1<2:
        cost_board[x+1][y] = max(cost_board[x+1][y], cost_board[x][y] + candie_board[x+1][y])
        visit_queue.append([x+1, y])

# output
print(cost_board[1][N-1])
