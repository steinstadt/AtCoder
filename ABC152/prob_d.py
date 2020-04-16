# Problem D - Hand

# input
N = int(input())

# initialization
nums = [[0]*10 for i in range(10)]
ans = 0

# count check
for n in range(1, N+1):
    tmp = list(str(n))
    tmp = list(map(int, tmp))
    sento = tmp[0]
    ichi = tmp[-1]
    nums[sento][ichi] += 1

# count
for i in range(1, 10):
    for j in range(1, 10):
        ans += nums[i][j] * nums[j][i]

# output
print(ans)
