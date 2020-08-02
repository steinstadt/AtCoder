# Problem C - Build Stairs

# input
N = int(input())
h_list = list(map(int, input().split()))

# initialization
is_ok = True

if N>1:
    tmp_height = h_list[-1]
    for i in range(N-2, -1, -1):
        if h_list[i]>tmp_height:
            h_list[i] -= 1
        if not h_list[i]<=tmp_height:
            is_ok = False
            break
        tmp_height = h_list[i]

# output
if is_ok:
    print("Yes")
else:
    print("No")
