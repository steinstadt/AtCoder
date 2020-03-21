# Problem C - パズルのお手伝い

class Queen:

    def __init__(self, n):
        n1 = n - 1
        n2 = n * 2

        self.pattern_num = 0
        self.n = n
        self.horizontal = [True] * (n + 1) # 水平方向のチェック 1~n
        self.major = [True] * (n2 + 1) # 対角線方向のチェックその１ 2~n2
        self.minor = [True] * n2 # 対角線方向のチェックその２ -n1~n1 -> -n1+n~n1+n

        self.ans_list = []
        self.pattern_list = []

    def add_queen(self, a):
        self.ans_list.append(a)

    def remove_queen(self):
        self.ans_list.pop(-1)

    def print_board(self):
        print(" - "*self.n)
        print("現在の配置%d"%(self.pattern_num))
        for a in self.ans_list:
            for i in range(1, self.n+1):
                if i==a:
                    print(" #", end = "")
                else:
                    print(" .", end= "")
            print()
        print(" - "*self.n)

    def queen_num(self):
        print("クイーン配置の組み合わせは %d 個あります。"%(self.pattern_num))

    def get_pattern(self):
        return self.pattern_list

    def backtrack(self, level):
        if level>=self.n:
            # 答えの出力
            self.pattern_num += 1
            p = []
            for a in self.ans_list:
                p.append(a)
            self.pattern_list.append(p)
        else:
            # 次の局面の探索
            col = level + 1
            for i in range(1, self.n + 1):
                if self.horizontal[i] and self.major[col + i] and self.minor[col - i + self.n]:
                    # 局面の変更
                    self.horizontal[i] = False
                    self.major[col + i] = False
                    self.minor[col - i + self.n] = False
                    self.add_queen(i)
                    # 再帰呼び出し
                    self.backtrack(level + 1)
                    # 局面の戻し
                    self.remove_queen()
                    self.horizontal[i] = True
                    self.major[col + i] = True
                    self.minor[col - i + self.n] = True


queen = Queen(8)
queen.backtrack(0) # バックトラック開始
pattern_list = queen.get_pattern()

# input
board = []
for i in range(8):
    board.append(list(input()))

# initialization
ans_list = []

# search
for p in pattern_list:
    is_ok = True
    for i in range(8):
        if "Q" in board[i] and not board[i][p[i]-1]=="Q":
            is_ok = False
            break
    if is_ok:
        ans_list.append(p)

# output
if len(ans_list)>0:
    print(ans_list)
    p = ans_list[0]
    for i in range(8):
        p_num = p[i]
        for j in range(8):
            if j==p_num-1:
                print("Q", end="")
            else:
                print(".", end="")
        print()
else:
    print("No Answer")
