# Problem C - Traveling Salesman around Lake

# input
K, N = map(int, input().split())
A_list = list(map(int, input().split()))
list_len = len(A_list)

# initialization
min_ans = 10**18

# search
for i in range(list_len):
    mae_i = 0
    if i==list_len-1:
        mae_i = 0
    else:
        mae_i = i + 1

    kyori = 0
    if A_list[mae_i]-A_list[i]<0:
        kyori = K - (A_list[mae_i] - A_list[i] + K)
    else:
        kyori = K - (A_list[mae_i] - A_list[i])
    min_ans = min(min_ans, kyori)

# output
print(min_ans)
