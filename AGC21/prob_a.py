# Problem A - Digit Sum 2

# input process
N = input()

# initizalization
keta_len = len(N)
keta_list = [[0]*2 for i in range(keta_len+1)] # keta_list[keta][smaller]
keta_list[0][0] = int(N[0])
keta_list[0][1] = int(N[0]) - 1

for i in range(1, keta_len): # keta loop 2桁目から
    for j in range(2): # smaller loop
        n_lim = 0
        if j==1:
            n_lim = 9
        else:
            n_lim = int(N[i])
        cost = keta_list[i-1][j] + n_lim
        keta_list[i][j] = max(keta_list[i][j], cost)

# output process
max_ans = max(keta_list[keta_len-1])
print(max_ans)
