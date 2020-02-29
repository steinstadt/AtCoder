# C - Candies

N = int(input())
A_list = []
# input process
for i in range(2):
    A_list.append(list(map(int, input().split())))

search_queue = [] # queue for the path search [x, y]
cost_list = [[0]*N for i in range(2)] # max cost list

# initialization
search_queue.append([0, 0])
cost_list[0][0] = A_list[0][0]

while len(search_queue)>0:
    # visit process
    pos = search_queue.pop(0)
    x = pos[0]
    y = pos[1]

    # right search
    if y+1<N:
        # cost calculation
        cost_list[x][y+1] = max(cost_list[x][y+1], cost_list[x][y]+A_list[x][y+1])
        if not [x, y] in search_queue:
            search_queue.append([x, y+1])

    # down search
    if x+1<2:
        # cost calculation
        cost_list[x+1][y] = max(cost_list[x+1][y], cost_list[x][y]+A_list[x+1][y])
        if not [x, y] in search_queue:
            search_queue.append([x+1, y])

# output process
print(cost_list[1][N-1])
