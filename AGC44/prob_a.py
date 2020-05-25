T = int(input())
K = []
for i in range(T):
    a = list(map(int,input().split()))
    K.append(a)

def pay(N):
    if N == 0:
        return 0
    if N == 1:
        return D
    if N in memo:
        return memo[N]

    m = float("inf")
    if N % 2 == 0:
        m = min(m, A + pay(N // 2))
    else:
        m = min(m, A + pay(N // 2) + D)
        m = min(m, A + pay(N // 2 + 1) + D)

    if N % 3 == 0:
        m = min(m, B + pay(N // 3))
    else:
        m = min(m, B + pay(N // 3) + D*(N%3))
        m = min(m, B + pay(N // 3 + 1) + D*(3 - N%3))

    if N % 5 == 0:
        m = min(m, C + pay(N // 5))
    else:
        m = min(m, C + pay(N // 5) + D*(N%5))
        m = min(m, C + pay(N // 5 + 1) + D*(5 - N%5))

    m = min(m, D*N)
    memo[N] = m
    return m

for i in range(T):
    memo = {}
    N, A, B, C, D = K[i]
    print(pay(N))
