# Problem D - Partition

# 公約数を列挙する関数
def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    divisors.sort()
    return divisors

# input process
N, M = map(int, input().split())
common_divisors = make_divisors(M)

# initialization
max_cd = 1

for c in common_divisors:
    if c*N<=M:
        max_cd = max(max_cd, c)

print(max_cd)
