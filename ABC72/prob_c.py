# Problem C - Together

# input
N = int(input())
a_nums = list(map(int, input().split()))

# initialization
nums = [0]*(10**5 + 1)
max_count = 0

# count
for a in a_nums:
    nums[a] += 1

# max count
for i in range(10**5 + 1):
    if i==0 or i==10**5:
        continue

    tmp_count = nums[i-1] + nums[i] + nums[i+1]
    max_count = max(max_count, tmp_count)

# output
print(max_count)
