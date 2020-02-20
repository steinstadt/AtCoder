# Problem - D Partition

def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    divisors.sort()
    return divisors

N, M = map(int, input().split())
gcd_max = 0 # 最大公約数の最大値
a_list = [[0]*N]
# 約数の列挙
divisor_list = make_divisors(M)

for d in divisor_list:
    check_sum = N * d
    if check_sum<=M:
        gcd_max = max(gcd_max, d)

print(gcd_max)
