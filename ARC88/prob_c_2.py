# Problem C - Multiple Gift

# input
X, Y = map(int, input().split())

# initialization
ans = 0

# count
while X<=Y:
    X *= 2
    ans += 1

# output
print(ans)
