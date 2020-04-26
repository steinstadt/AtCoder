# Problem C - City Savers

# input
N = int(input())
a_nums = list(map(int, input().split()))
b_nums = list(map(int, input().split()))

# initialization
ans_monsters = 0

# count
for i in range(len(b_nums)):
    # round 1
    if b_nums[i]>=a_nums[i]:
        ans_monsters += a_nums[i]
        b_nums[i] -= a_nums[i]
    else:
        ans_monsters += b_nums[i]
        b_nums[i] = 0

    # round 2
    if b_nums[i]>0:
        if b_nums[i]>=a_nums[i+1]:
            ans_monsters += a_nums[i+1]
            a_nums[i+1] = 0
        else:
            ans_monsters += b_nums[i]
            a_nums[i+1] -= b_nums[i]

# output
print(ans_monsters)
