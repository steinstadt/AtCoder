# Problem C - Skill Up

# input
N, M, X = map(int, input().split())
book_list = []
for i in range(N):
    book = list(map(int, input().split()))
    book_list.append(book)

# initialization
price = float('INF')
is_ok = False

# pattern
pattern = []
for i in range(2**N):
    p = [0]*N
    for j in range(N):
        if (i>>j)&1==1:
            p[j] = 1
    pattern.append(p)

for p in pattern:
    tmp_sum = [0]*(M+1)
    is_finish = True
    for i in range(N):
        if p[i]==1:
            for j in range(M+1):
                tmp_sum[j] += book_list[i][j]
    # check
    for i in range(1, M+1):
        if not tmp_sum[i]>=X:
            is_finish = False
            break

    if is_finish:
        is_ok = True
        price = min(price, tmp_sum[0])

# output
if is_ok:
    print(price)
else:
    print(-1)
