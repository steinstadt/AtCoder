# Problem B - あみだくじ

# input process
N, L = map(int, input().split())
amida_list = [[' ']*(2*N-1) for i in range(L)]

# initialization
for i in range(L):
    amida_in = input()
    for j in range(2*N-1):
        amida_list[i][j] = amida_in[j]
goal_list = input()
goal_pos = 0
for i in range(len(goal_list)):
    if goal_list[i]=='o':
        goal_pos = i
        break

# search process
for i in range(L-1, -1, -1):
    # right process
    if goal_pos+1<(2*N-1):
        if amida_list[i][goal_pos+1]=='-':
            goal_pos = goal_pos + 2
            continue
    # left process
    if goal_pos-1>=0:
        if amida_list[i][goal_pos-1]=='-':
            goal_pos = goal_pos - 2
            continue

print(goal_pos//2 + 1)
