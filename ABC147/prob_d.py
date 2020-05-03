# Problem D - Xor Sum 4

# input
N = int(input())
a_nums = list(map(int, input().split()))

# initialization
ans = 0
MOD = 10**9 + 7

# count
two_factor = 1
for i in range(60):
    tmp_count = 0
    one_count = 0
    zero_count = 0
    for j in range(N):
        if (a_nums[j]>>i)&1==1:
            one_count += 1
        else:
            zero_count += 1
    tmp_count = (one_count * zero_count)%MOD
    ans += (tmp_count * two_factor)%MOD
    two_factor = (two_factor * 2)%MOD

# output
print(ans%MOD)
