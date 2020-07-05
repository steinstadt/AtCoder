# Problem D - Sum of Divisors

# input
N = int(input())

# initialization
count = 0

# count
for j in range(1, N+1):
    M = N // j
    count += j * ((M * (M+1)) // 2)

# output
print(count)
