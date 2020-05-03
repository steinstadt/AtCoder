# Problem C - HonestOrUnkind2

# input
N = int(input())
shogen_list = []
for i in range(N):
    A = int(input())
    tmp = []
    for j in range(A):
        x, y = map(int, input().split())
        tmp.append([x, y])
    shogen_list.append(tmp)

# initialization
pattern = []
for i in range(2**N):
    p = [0]*N
    for j in range(N):
        if (i>>j)&1==1:
            p[j] = 1
    pattern.append(p)
max_count = 0

# count
for p in pattern:
    is_ok = True
    num_count = 0
    for i in range(N):
        # 正直者であればチェック
        if p[i]==1:
            num_count += 1
            shogen = shogen_list[i]
            if len(shogen)==0:
                continue
            else:
                for s in shogen:
                    x = s[0]
                    y = s[1]
                    if not p[x-1]==y:
                        is_ok = False
                        break
    if is_ok:
        max_count = max(max_count, num_count)

# output
print(max_count)
