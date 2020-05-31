# Problem D - Boring Sequence

# input
N, K = map(int, input().split())
a_nums = list(map(int, input().split()))

# initialization
left = 0
right = 2 * 10**5 + 1

# binary search
while right-left>1:
    mid = (right + left) // 2

    is_ok = True
    swap_count = 0
    check_count = 0
    i = 1
    while i<N:
        if a_nums[i-1]==a_nums[i]:
            check_count += 1
            if check_count==mid:
                swap_count += 1
                i += 2
                check_count = 0
                continue
        else:
            check_count = 0

        i += 1

    # update
    if swap_count<=K:
        right = mid
    else:
        left = mid

# output
print(right)
