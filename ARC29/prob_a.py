N = int(input())
t_list = []
for i in range(N):
    t_list.append(int(input()))

t_list = sorted(t_list, reverse=True)

cost_list = [[0]*2 for i in range(N+1)]
for i in range(N):
    conro_1, conro_2 = cost_list[i][0]+t_list[i], cost_list[i][1]+t_list[i]
    if conro_1 < conro_2:
        cost_list[i+1][0] = conro_1
        cost_list[i+1][1] = cost_list[i][1]
    elif conro_1 > conro_2:
        cost_list[i+1][0] = cost_list[i][0]
        cost_list[i+1][1] = conro_2
    else:
        cost_list[i+1][0] = conro_1
        cost_list[i+1][1] = cost_list[i][1]

print(max(cost_list[N]))
