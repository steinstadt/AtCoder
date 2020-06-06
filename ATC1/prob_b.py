# Problem B - Union Find

class UnionFind:
    # n要素で初期化
    def __init__(self, n):
        self.par = [0]*n
        for i in range(n):
            self.par[i] = i

    # 木の根を求める
    def root(self, x):
        if self.par[x]==x: # 根
            return x
        else: # 経路圧縮
            self.par[x] = self.root(self.par[x])
            return self.par[x]

    # xとyが同じ集合に属するか否かを判定
    def same(self, x, y):
        return self.root(x)==self.root(y)

    # xとyの属する集合を併合
    def unite(self, x, y):
        x = self.root(x)
        y = self.root(y)
        if x==y:
            return

        if x<y:
            self.par[y] = x
        else:
            self.par[x] = y

# input
N, Q = map(int, input().split())

# initialization
union_find_obj = UnionFind(N)

# query
for i in range(Q):
    p, a, b = map(int, input().split())
    if p==0: # 連結クエリ
        union_find_obj.unite(a, b)
    else:
        result = union_find_obj.same(a, b)
        if result:
            print("Yes")
        else:
            print("No")
