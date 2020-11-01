# Problem D - Wizard in Maze
from collections import deque

# input
H, W = map(int, input().split())
c_h, c_w = map(int, input().split())
d_h, d_w = map(int, input().split())
board = [[""]*W for i in range(H)]
for i in range(H):
    line = list(input())
    for j in range(W):
        board[i][j] = line[j]

# initialization
visited = [[-1]*W for i in range(H)]
visited[c_h-1][c_w-1] = 1
dp_board = [[float("inf")]*W for i in range(H)]
dp_board[c_h-1][c_w-1] = 0
visited_queue = deque([[c_h-1, c_w-1]])
visited_queue_b = deque([[c_h-1, c_w-1]])
queue_count = 1
queue_count_b = 1


# bfs a
# (x, y)から移動Aで行ける箇所を列挙する
def bfs_a(x, y, n):
    global H
    global W
    global board
    global dp_board
    global visited
    global visited_queue
    global queue_count
    global queue_count_b

    for i in range(-1, 2):
        for j in range(-1, 2):
            if i==0 and j==0:
                visited_queue_b.append([x, y])
                queue_count_b += 1
                continue
            elif -1<=i<=1 and j==0:
                tmp_h = x + i
                tmp_w = y
                if 0<=tmp_h<H and 0<=tmp_w<W:
                    if visited[tmp_h][tmp_w]==-1 and board[tmp_h][tmp_w]==".":
                        if dp_board[x][y]<dp_board[tmp_h][tmp_w]:
                            dp_board[tmp_h][tmp_w] = dp_board[x][y]
                            visited[tmp_h][tmp_w] = 1
                            visited_queue.append([tmp_h, tmp_w])
                            visited_queue_b.append([tmp_h, tmp_w])
                            queue_count += 1
                            queue_count_b += 1
            elif i==0 and -1<=j<=1:
                tmp_h = x
                tmp_w = y + j
                if 0<=tmp_h<H and 0<=tmp_w<W:
                    if visited[tmp_h][tmp_w]==-1 and board[tmp_h][tmp_w]==".":
                        if dp_board[x][y]<dp_board[tmp_h][tmp_w]:
                            dp_board[tmp_h][tmp_w] = dp_board[x][y]
                            visited[tmp_h][tmp_w] = 1
                            visited_queue.append([tmp_h, tmp_w])
                            visited_queue_b.append([tmp_h, tmp_w])
                            queue_count += 1
                            queue_count_b += 1

# bfs b
# visited_queueから移動Bを行う。移動する必要のないものはvisited_queueにappendしない。
def bfs_b():
    global H
    global W
    global dp_board
    global visited
    global visited_queue
    global visited_queue_b
    global queue_count
    global queue_count_b

    while queue_count_b>0:
        pos = visited_queue_b.popleft()
        queue_count_b -= 1
        pos_h = pos[0]
        pos_w = pos[1]

        for i in range(-2, 3):
            for j in range(-2, 3):
                tmp_h = pos_h + i
                tmp_w = pos_w + j
                if not (0<=tmp_h<H and 0<=tmp_w<W):
                    continue
                if board[tmp_h][tmp_w]==".":
                    if dp_board[pos_h][pos_w]+1<dp_board[tmp_h][tmp_w]:
                        dp_board[tmp_h][tmp_w] = dp_board[pos_h][pos_w] + 1
                        visited_queue.append([tmp_h, tmp_w])
                        queue_count += 1
                    if visited[tmp_h][tmp_w]==-1:
                        visited[tmp_h][tmp_w] = 1

# main
search_count = 0
while queue_count>0:
    # move a
    while queue_count>0:
        pos = visited_queue.popleft()
        queue_count -= 1
        pos_h = pos[0]
        pos_w = pos[1]
        bfs_a(pos_h, pos_w, search_count)
    # move b
    bfs_b()

    search_count += 1

# output
if visited[d_h-1][d_w-1]==-1:
    print(-1)
else:
    print(dp_board[d_h-1][d_w-1])
