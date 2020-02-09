N = int(input())
N_list = list(map(int, input().split()))

N_set = set(N_list)

list_num = len(N_list)
set_num = len(N_set)

if list_num==set_num:
    print("YES")
else:
    print("NO")
