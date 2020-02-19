H, W = map(int, input().split())
maze_list = [[""]*W for i in range(H)]
for i in range(H):
    maze_pattern = input()
    for j in range(W):
        maze_list[i][j]=maze_pattern[j]

maze_count = 0
def maze_search(maze_point):
    
