# Problem D - Disjoint Set of Common Divisors

import fractions

# 約数を列挙する関数
def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    divisors.sort()
    return divisors

# 素因数分解
def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr

# input
A, B = map(int, input().split())
C = fractions.gcd(A, B)
if A==1 or B==1:
    print(1)
elif C==1:
    print(1)
else:
    arr = factorization(C)
    print(len(arr) + 1)
