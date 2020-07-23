# Problem C - Dice and Coin
# input
N, K = map(int, input().split())

# initialization
ans = 0

def calc_count(n, K):
    tmp = 0
    while n<K:
        tmp += 1
        n *= 2
    return tmp

# count
for i in range(1, N+1):
    count = calc_count(i, K)
    ans += (1 / 2)**count

# output
ans = ans / N
print(ans)
