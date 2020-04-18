# Problem D - 射撃王

# input
N = int(input())
H = [0]*N
S = [0]*N
for i in range(N):
    h, s = map(int, input().split())
    H[i] = h
    S[i] = s

# initialization
left = 0
right = 10**18

# binary search
while not abs(right-left)<=1:
    mid = (right + left) // 2
    time_list = [0] * N
    for i in range(N):
        time_list[i] = (mid - H[i]) // S[i]
    time_list = sorted(time_list)
    is_ok = True
    for i in range(N):
        if time_list[i]<i:
            is_ok = False
    if is_ok:
        right = mid
    else:
        left = mid

# output
print(right)
