# Problem A - Shik and Stone

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

# search
class DfsSearch:
    def __init__(self):
        self.is_ok = True

    def get_is_ok(self):
        return self.is_ok

    def dfs(self, pos):
        x = pos[0]
        y = pos[1]
        v_board[x][y] = False
        # left
        if y-1>=0 and board[x][y-1]=='#' and v_board[x][y-1]:
            self.is_ok = False
            self.dfs([x, y-1])

        # up
        if x-1>=0 and board[x-1][y]=='#' and v_board[x-1][y]:
            self.is_ok = False
            self.dfs([x-1, y])

        # right
        if y+1<W and board[x][y+1]=='#' and v_board[x][y+1]:
            self.dfs([x, y+1])

        # down
        if x+1<H and board[x+1][y]=='#' and v_board[x+1][y]:
            self.dfs([x+1, y])

        v_board[x][y] = True

# output
dfs = DfsSearch()
dfs.dfs([0, 0])
if dfs.get_is_ok():
    print("Possible")
else:
    print("Impossible")
