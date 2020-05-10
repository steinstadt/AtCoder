# Problem C - Synthetic Kadomatsu

# input
N, A, B, C = map(int, input().split())
l_list = [0]*N
for i in range(N):
    l = int(input())
    l_list[i] = l

# dfs search
class DFS:

    def __init__(self, l_list, N, A, B, C):
        self.l_list = l_list
        self.N = N
        self.A = A
        self.B = B
        self.C = C
        self.INF = float('INF')
        self.ans = float('INF')

    def get_ans(self):
        return self.ans

    def dfs(self, n, a, b, c):
        if n==self.N:
            if not a==0 and not b==0 and not c==0:
                return abs(a-self.A) + abs(b-self.B) + abs(c-self.C)
            else:
                return self.INF

        # 今ある竹を利用しない場合
        self.ans = min(self.ans, self.dfs(n+1, a, b, c))

        # A, B, C を利用する場合
        if a==0:
            self.ans = min(self.ans, self.dfs(n+1, a+self.l_list[n], b, c))
        else:
            self.ans = min(self.ans, self.dfs(n+1, a+self.l_list[n], b, c) + 10)

        if b==0:
            self.ans = min(self.ans, self.dfs(n+1, a, b+self.l_list[n], c))
        else:
            self.ans = min(self.ans, self.dfs(n+1, a, b+self.l_list[n], c) + 10)

        if c==0:
            self.ans = min(self.ans, self.dfs(n+1, a, b, c+self.l_list[n]))
        else:
            self.ans = min(self.ans, self.dfs(n+1, a, b, c+self.l_list[n]) + 10)

        return self.ans

# calc
dfs_obj = DFS(l_list, N, A, B, C)
dfs_obj.dfs(0, 0, 0, 0)

# output
print(dfs_obj.get_ans())
