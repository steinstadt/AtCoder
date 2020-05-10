# Problem E - This Message Will Self-Destruct in 5s

# input
N = int(input())
a_nums = list(map(int, input().split()))

# initialization
tmp_1 = {}
ans = 0

# count
for i in range(1, N+1):
    if i+a_nums[i-1] in tmp_1:
        tmp_1[i + a_nums[i-1]] += 1
    else:
        tmp_1[i + a_nums[i-1]] = 1

# count 2
for j in range(1, N+1):
    if j-a_nums[j-1] in tmp_1:
        ans += tmp_1[j-a_nums[j-1]]

# output
print(ans)
