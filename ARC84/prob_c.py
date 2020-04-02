# Problem C - Snuke Festival

import bisect

# input
N = int(input())
A_list = list(map(int, input().split()))
B_list = list(map(int, input().split()))
C_list = list(map(int, input().split()))

# initialization
A_list = sorted(A_list)
B_list = sorted(B_list)
C_list = sorted(C_list)
ans = 0

# b search
for i in range(N):
    b = B_list[i]
    a_nums = bisect.bisect_left(A_list, b)
    c_nums = N - bisect.bisect_right(C_list, b)
    ans += a_nums * c_nums

# output
print(ans)
