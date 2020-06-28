# Problem D - Sum of Divisors

# input
N = int(input())

# initialization
ans = 0

# count
for j in range(1, N+1):
    Y = N // j
    ans += ((Y * (Y + 1))*j) // 2

# output
print(ans)
