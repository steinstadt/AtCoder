# Problem C - Divide the Problem

# input process
N = int(input())
d_nums = map(int, input().split())

# initialization
d_nums = sorted(d_nums)
d_len = len(d_nums)
median_1 = d_nums[d_len//2-1]
median_2 = d_nums[d_len//2]

# process
if d_len%2==0:
    ans = median_2 - median_1
    print(ans)
else:
    print(0)
