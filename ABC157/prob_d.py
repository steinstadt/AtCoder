# Problem D - Friend Suggestions

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())

# input
N, M, K = map(int, input().split())

# initialization
friend_uf = UnionFind(N)
not_list = [[] for i in range(N+1)]
ans_list = [0] * (N)

# friend relation union
for i in range(M):
    a, b = map(int, input().split())
    friend_uf.union(a-1, b-1)
    not_list[a].append(b)
    not_list[b].append(a)

# block relation union
for i in range(K):
    c, d = map(int, input().split())
    if friend_uf.same(c-1, d-1):
        not_list[c].append(d)
        not_list[d].append(c)

# output
for i in range(1, N+1):
    group_size = friend_uf.size(i-1)
    not_size = not_list[i]
    ans = group_size - len(set(not_size)) - 1
    ans_list[i-1] = ans
ans_list = list(map(str, ans_list))
print(" ".join(ans_list))
