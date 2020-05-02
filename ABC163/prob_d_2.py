# Problem D - Sum of Large Numbers

# input
N, K = map(int, input().split())

# initialization
mae_list = [i for i in range(N+1)]
ushiro_list = [i for i in range(N, -1, -1)]
ans = 0
MOD = 10**9 + 7

# count
for i in range(1, N+1):
    mae_list[i] += mae_list[i-1]
    ushiro_list[i] += ushiro_list[i-1]

for k in range(K-1, N+1):
    ans += (ushiro_list[k] - mae_list[k] + 1)%MOD

# output
print(ans%MOD)
