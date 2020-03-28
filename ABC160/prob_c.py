# Problem C - Traveling Salesman around Lake

K, N = map(int, input().split())
a_list = list(map(int, input().split()))

# initialization
min_cost = 10**8
a_len = len(a_list)

for i in range(len(a_list)):
    a = a_list[i]
    ushiro_i = 0
    mae_i = 0
    # 1つ後ろを取る
    if i-1<0:
        ushiro_i = a_len - 1
    else:
        ushiro_i = i - 1

    # 1つ前を取る
    if i+1>=a_len:
        mae_i = 0
    else:
        mae_i = i + 1

    # update
    kouho_1 = 0
    kouho_2 = 0
    if a_list[mae_i]-a_list[i]<0:
        kouho_1 = K - (a_list[mae_i] - a_list[i] + K)
    else:
        kouho_1 = K - (a_list[mae_i] - a_list[i])
    if a_list[i]-a_list[ushiro_i]<0:
        kouho_2 = K - (a_list[i] - a_list[ushiro_i] + K)
    else:
        kouho_2 = K - (a_list[i] - a_list[ushiro_i])
        
    min_cost = min(min_cost, kouho_1, kouho_2)

# output
print(min_cost)
