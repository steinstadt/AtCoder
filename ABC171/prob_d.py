# Problem D - Replacing

# input
N = int(input())
a_nums = list(map(int, input().split()))
Q = int(input())

# initialization
nums = [0] * (10**5 + 1)
cur_sum = sum(a_nums)
for a in a_nums:
    nums[a] += 1

# count
for i in range(Q):
    b, c = map(int, input().split())
    b_count = nums[b]
    cur_sum = cur_sum - b_count*b + b_count*c
    print(cur_sum)
    nums[b] = 0
    nums[c] += b_count
