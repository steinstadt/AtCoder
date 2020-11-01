# Problem C - Sum of product of pairs

# input
N = int(input())
a_list = list(map(int, input().split()))

# initialization
MOD = 10**9 + 7
s_list = [0] * (N + 1)
for i in range(N):
    if i==0:
        s_list[N] = a_list[N-1]
        s_list[N] %= MOD
    else:
        s_list[N-i] = ((s_list[N-i+1])%MOD + (a_list[N-i-1])%MOD) % MOD
ans = 0

for i in range(N-1):
    tmp = ((a_list[i]%MOD) * (s_list[i+2]%MOD)) % MOD
    ans += tmp
    ans %= MOD

# output
print(ans%MOD)
