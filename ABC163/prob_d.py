# Problem D - Sum of Large Numbers

# input
N, K = map(int, input().split())

# initialization
up_list = [i for i in range(N+1)] # 昇順リスト
up_sums = [0]*(N+1)
for i in range(N+1):
    if i==0:
        up_sums[i] = up_list[i]
    else:
        up_sums[i] = up_sums[i-1] + up_list[i]
down_list = [i for i in range(N, -1, -1)] # 降順リスト
down_sums = [0]*(N+1)
for i in range(N+1):
    if i==0:
        down_sums[i] = down_list[i]
    else:
        down_sums[i] = down_sums[i-1] + down_list[i]
ans = 0
MOD = 10**9 + 7

# count
tmp_k = K
while tmp_k<=(N+1):
    test_up = up_sums[tmp_k-1]
    test_down = down_sums[tmp_k-1]
    tmp = (test_down - test_up + 1)%MOD
    ans += tmp
    ans = ans % MOD
    tmp_k += 1

# output
print(ans)
