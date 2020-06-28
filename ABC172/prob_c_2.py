# Problem C - Tsundoku

# input
N, M, K = map(int, input().split())
a_nums = list(map(int, input().split()))
b_nums = list(map(int, input().split()))

# initialization
max_count = 0
b_i = M
a_cums = [0]*(N+1)
b_cums = [0]*(M+1)
for i in range(1, N+1):
    if i>1:
        a_cums[i] = a_cums[i-1] + a_nums[i-1]
    else:
        a_cums[i] = a_nums[i-1]
for i in range(1, M+1):
    if i>1:
        b_cums[i] = b_cums[i-1] + b_nums[i-1]
    else:
        b_cums[i] = b_nums[i-1]

for i in range(N+1):
    if a_cums[i]<=K:
        while b_i>0 and a_cums[i]+b_cums[b_i]>K:
            b_i -= 1
        if i+b_i>max_count:
            max_count = i+b_i

# output
print(max_count)
