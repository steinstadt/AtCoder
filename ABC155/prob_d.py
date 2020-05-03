# Problem D - Pairs（Pythonだと間に合わない）

# input
N, K = map(int, input().split())
a_nums = list(map(int, input().split()))

# initialization
a_nums = sorted(a_nums)
left = -10**18
right = 10**18

# binary search
while right-left>1:
    x = (right + left) // 2
    S = 0
    T = 0
    # 判定部分
    for a in a_nums:
        if a>0:
            r2 = N
            l2 = -1
            while r2-l2>1:
                mid = (r2 + l2) // 2
                if a*a_nums[mid]<=x:
                    l2 = mid
                else:
                    r2 = mid
            S += r2
        elif a<0:
            r2 = N
            l2 = -1
            while r2-l2>1:
                mid = (r2 + l2) // 2
                if a*a_nums[mid]<=x:
                    r2 = mid
                else:
                    l2 = mid
            S += N - r2
        elif x>=0: # a==0の時
            S += N
        # 重複を数える
        if a*a<=x:
            T += 1
    # 判定部分（大元）
    check_nums = (S - T) // 2
    if check_nums>=K:
        right = x
    else:
        left = x

# output
print(right)
