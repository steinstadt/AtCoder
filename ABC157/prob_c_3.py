# Problem C - Guess The Number

# input
N, M = map(int, input().split())

# initialization
input_ok = True
num_list = [-1]*N
for i in range(M):
    s, c = map(int, input().split())
    if N>=2 and s==1:
        if c==0:
            input_ok = False
            break

    if num_list[s-1]==-1:
        num_list[s-1] = c
    else:
        if not c==num_list[s-1]:
            input_ok = False
            break

# min_search
if input_ok:
    min_num = 1000
    for n in range(1000):
        n_str = str(n)
        is_ok = True
        if len(n_str)==N:
            for i in range(N):
                if not num_list[i]==-1:
                    if not int(n_str[i])==num_list[i]:
                        is_ok = False
            if is_ok:
                min_num = min(min_num, int(n_str))
        else:
            continue
    # output
    print(min_num)
else:
    print(-1)
