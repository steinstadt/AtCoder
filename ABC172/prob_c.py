# Problem C - Tsundoku

# input
N, M, K = map(int, input().split())
a_nums = list(map(int, input().split()))
b_nums = list(map(int, input().split()))

# initialization
a_start = -1
b_start = -1
max_count = 0
cur_count = 0

# dfs search
def dfs(a_i, b_i):
    global max_count
    global cur_count
    global K
    global N
    global M

    if a_i>=N or b_i>=M:
        if cur_count>max_count:
            max_count = cur_count
        return

    # right check
    if a_i+1<N:
        if K - a_nums[a_i+1]>=0:
            K -= a_nums[a_i + 1]
            cur_count += 1
            dfs(a_i+1, b_i)
            cur_count -= 1
            K += a_nums[a_i + 1]
        else:
            if cur_count>max_count:
                max_count = cur_count
    else:
        if cur_count>max_count:
            max_count = cur_count

    # left check
    if b_i+1<M:
        if K - b_nums[b_i+1]>=0:
            K -= b_nums[b_i + 1]
            cur_count += 1
            dfs(a_i, b_i+1)
            cur_count -= 1
            K += b_nums[b_i + 1]
        else:
            if cur_count>max_count:
                max_count = cur_count
    else:
        if cur_count>max_count:
            max_count = cur_count

dfs(a_start, b_start)

# output
print(max_count)
