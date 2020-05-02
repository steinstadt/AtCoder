# Problem C - Monsters Battle Royale

# input
N = int(input())
a_nums = list(map(int, input().split()))

# initialization
count = 0
is_finished = True

# count
while is_finished:
    min_hp = float('INF')
    min_index = 0
    for i in range(N):
        if a_nums[i]==0:
            continue
        if min_hp>a_nums[i]:
            min_hp = a_nums[i]
            min_index = i
    for i in range(N):
        if i==min_index:
            continue
        a_nums[i] = a_nums[i] - min_hp*(a_nums[i]//min_hp)
        if a_nums[i]<0:
            a_nums[i] = 0
    if len(set(a_nums))==2 and 0 in set(a_nums):
        is_finished = False

# output
ans = max(a_nums)
print(ans)
