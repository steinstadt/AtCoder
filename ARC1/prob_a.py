# Problem C - パズルのお手伝い (バックトラック法)

class Queen:
    def __init__(self, board):
        self.board = board
        self.vertical = [True] * 9
        self.major = [True] * 17
        self.minor = [True] * 16
        self.is_ok = True
        self.ans_list = []

        # 最初のQによる配置
        for i in range(1, 9):
            for j in range(1, 9):
                if board[i-1][j-1]=="Q":
                    if self.vertical[j] and self.major[i+j] and self.minor[i-j+8]:
                        self.vertical[j] = False
                        self.major[i+j] = False
                        self.minor[i-j+8] = False
                    else:
                        self.is_ok = False

    def add_queen(self, row, col):
        self.board[row-1][col-1] = 'Q'

    def remove_queen(self,row, col):
        self.board[row-1][col-1] = '.'

    def print_board(self):
        for i in range(8):
            for j in range(8):
                print(self.board[i][j], end="")
            print()
        print()

    def result_out(self):

        if self.is_ok and len(self.ans_list)>0:
            a = self.ans_list[0]
            for i in range(8):
                for j in range(8):
                    print(a[i][j], end="")
                print()
        else:
            print("No Answer")

    # バックトラック開始
    def backtrack(self, level, col_num):
        if not self.is_ok:
            return

        # 停止条件
        if level>=8:

            if "Q" in self.board[level - 1]:
                if self.board[level - 1][col_num-1]=="Q":
                    self.is_ok = True
                    # 答えのコピー
                    tmp = [['.']*8 for i in range(8)]
                    for i in range(8):
                        for j in range(8):
                            tmp[i][j] = self.board[i][j]
                    self.ans_list.append(tmp)
                return
            else:
                self.is_ok = True
                # ボードのコピー
                tmp = [['.']*8 for i in range(8)]
                for i in range(8):
                    for j in range(8):
                        tmp[i][j] = self.board[i][j]
                self.ans_list.append(tmp)
                return

        # Qがすでに配置されていた時の処理
        row = level + 1
        if "Q" in self.board[row - 1]:
            # Qがある列の位置をcol_numにする
            tmp = 0
            for i in range(8):
                if self.board[row-1][i]=="Q":
                    tmp = i + 1
            self.backtrack(row, tmp)
            return

        for i in range(1, 9):
            if self.vertical[i] and self.major[row + i] and self.minor[row - i + 8]:
                # 局面の変更
                self.vertical[i] = False
                self.major[row + i] = False
                self.minor[row - i + 8] = False
                self.add_queen(row, i)
                # 再帰呼び出し
                self.backtrack(row, i)
                # 局面の戻し
                self.remove_queen(row, i)
                self.vertical[i] = True
                self.major[row + i] = True
                self.minor[row - i + 8] = True


# input
board = [] # チェス盤
for i in range(8):
    board.append(list(input()))


# initialization
queen = Queen(board)
queen.backtrack(0, 0)
queen.result_out()
