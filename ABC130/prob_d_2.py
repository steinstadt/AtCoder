# Problem D - Enough Array

# input
N, K = map(int, input().split())
a_nums = list(map(int, input().split()))

# initialization
ans_count = 0
tmp_sum = 0

# shakutori count
right = 0
for left in range(N):
    while right<N and tmp_sum+a_nums[right]<K:
        tmp_sum += a_nums[right]
        right += 1

    ans_count += N - right

    # left update
    if left==right:
        right += 1
    else:
        tmp_sum -= a_nums[left]

# output
print(ans_count)
