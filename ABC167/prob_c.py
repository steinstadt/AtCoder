# Problem C - Skill Up

# input
N, M, X = map(int, input().split())
book_list = []
for i in range(N):
    book = list(map(int, input().split()))
    book_list.append(book)

# initialization
min_cost = float("INF")
is_ok = False
pattern = []
for i in range(2**N):
    p = [0]*N
    for j in range(N):
        if (i>>j)&1==1:
            p[j] = 1
    pattern.append(p)

# check
for p in pattern:
    tmp_cost = 0
    tmp_list = [0] * M
    tmp_ok = True
    for i in range(N):
        if p[i]==0:
            continue

        tmp_cost += book_list[i][0]
        for j in range(1, M+1):
            tmp_list[j-1] += book_list[i][j]
    for t in tmp_list:
        if t<X:
            tmp_ok = False
            break
    if tmp_ok:
        is_ok = True
        min_cost = min(min_cost, tmp_cost)

# output
if is_ok:
    print(min_cost)
else:
    print(-1)
