# Problem C - To3

# input
N_list = list(input())
N_len = len(N_list)


# initialization
is_ok = False
ok_num = float("inf")
# bit search
pattern = []
for i in range(2**N_len):
    p = [0] * N_len
    for j in range(N_len):
        if ((i>>j)&1):
            p[j] = 1
    pattern.append(p)

# bit search
for p in pattern:
    tmp = 0
    zero_count = 0
    for i in range(N_len):
        if p[i]==1:
            tmp += int(N_list[i])
        else:
            zero_count += 1
    if tmp==0:
        continue
    if tmp%3==0:
        is_ok = True
        ok_num = min(ok_num, zero_count)

# output
if is_ok:
    print(ok_num)
else:
    print(-1)
