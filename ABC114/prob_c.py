# Problem C - 755

from collections import deque

# input
N = input()
n_keta = len(N)
N = int(N)

# initialization
class Search:
    def __init__(self, n, keta):
        self.ans = 0
        self.n = n
        self.keta = keta

    def get_ans(self):
        return self.ans

    def check_str(self, check_num, check_str):
        return check_num<=self.n and '3' in check_str and '5' in check_str and '7' in check_str

    # dfs search
    # num_str is deque
    def dfs(self, num_str):
        if len(num_str)==self.keta:
            check_num = int("".join(num_str))
            if self.check_str(check_num, num_str):
                self.ans += 1
        else:
            for s in ['3', '5', '7']:
                num_str.append(s)
                check_num = int("".join(num_str))
                if len(num_str)<self.keta:
                    if self.check_str(check_num, num_str):
                        self.ans += 1
                self.dfs(num_str)
                num_str.pop()

# calc
dfs_search = Search(N, n_keta)
num_str = deque([])
dfs_search.dfs(num_str)

# output
print(dfs_search.get_ans())
