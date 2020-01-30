import fractions

N = int(input())
A_list = list(map(int, input().split()))

mod = 10**9+7

R = 1 # 最小公倍数
# 最小公倍数を求める
for A in A_list:
    R *= A // fractions.gcd(R, A)

# Bの合計を求める
ans = 0
for A in A_list:
    ans = ans + R // A # 計算は小数として出してはダメだから//を使う

ans %= mod

print(ans)
