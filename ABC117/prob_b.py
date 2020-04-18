# Problem B - Polygon

# input
N = int(input())
l_nums = list(map(int, input().split()))

# initialization
is_ok = True

# check
for i in range(N):
    check_sum = 0
    for j in range(N):
        if i==j:
            continue
        check_sum += l_nums[j]
    if l_nums[i]>=check_sum:
        is_ok = False

# output
if is_ok:
    print("Yes")
else:
    print("No")
