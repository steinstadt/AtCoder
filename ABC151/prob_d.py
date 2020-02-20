H, W = map(int, input().split())
cost_list = [[0]*W for i in range(H)]
cost_check = [[0]*W for i in range(H)]
path_list = [] # path content
max_cost = 0 # max path cost

def path_cost(x, y):
    if path_list[x][y]=="#":
        return -1
    # cost check clear
    for i in range(H):
        for j in range(W):
            cost_check[i][j] = 0
            cost_list[i][j] = 0
    # cost calculation
    path_queue = [[x,y]]
    cost_check[x][y] = 1
    # path cost process
    while len(path_queue)>0:
        # path queue pop
        path = path_queue.pop(0)
        next_x, next_y = path[0], path[1]
        # right cost process
        if next_x+1<H:
            if path_list[next_x+1][next_y]=="." and cost_check[next_x+1][next_y]==0:
                cost_list[next_x+1][next_y] = max(cost_list[next_x+1][next_y], cost_list[next_x][next_y]+1)
                path_queue.append([next_x+1, next_y])
                cost_check[next_x+1][next_y] = 1

        # bottom cost process
        if next_y+1<W:
            if path_list[next_x][next_y+1]=="." and cost_check[next_x][next_y+1]==0:
                cost_list[next_x][next_y+1] = max(cost_list[next_x][next_y+1], cost_list[next_x][next_y]+1)
                path_queue.append([next_x, next_y+1])
                cost_check[next_x][next_y+1] = 1

        # left cost process
        if next_x-1>=0:
            if path_list[next_x-1][next_y]=="." and cost_check[next_x-1][next_y]==0:
                cost_list[next_x-1][next_y] = max(cost_list[next_x-1][next_y], cost_list[next_x][next_y]+1)
                path_queue.append([next_x-1, next_y])
                cost_check[next_x-1][next_y] = 1

        # up cost process
        if next_y-1>=0:
            if path_list[next_x][next_y-1]=="." and cost_check[next_x][next_y-1]==0:
                cost_list[next_x][next_y-1] = max(cost_list[next_x][next_y-1], cost_list[next_x][next_y]+1)
                path_queue.append([next_x, next_y-1])
                cost_check[next_x][next_y-1] = 1

    tmp_max_cost = max(sum(cost_list,[]))
    return tmp_max_cost

# input path
for i in range(H):
    path_in = input()
    path = []
    for j in range(W):
        path.append(path_in[j])
    path_list.append(path)

# cost calculation
for i in range(H):
    for j in range(W):
        max_cost = max(max_cost,path_cost(i, j))

print(max_cost)
