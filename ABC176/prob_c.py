# Problem C - Step

# input
N = int(input())
a_nums = list(map(int, input().split()))

# initialization
ans = 0

# calc
tmp_cost = a_nums[0]
for i in range(N):
    if tmp_cost-a_nums[i]>0:
        ans += tmp_cost - a_nums[i]
    else:
        tmp_cost = a_nums[i]

# output
print(ans)
