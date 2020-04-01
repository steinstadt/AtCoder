# Problem B - 直方体

# input
A, B, C = map(int, input().split())

# initialization
MOD = 10**9 + 7

tmp_1 = (A * B) % MOD
tmp_2 = (tmp_1 * C) % MOD

# output
print(tmp_2)
