# Problem B - Easy Linear Programming

# input
A, B, C, K = map(int, input().split())

# initialization
ans = 0
# calc a
nokori = K
if nokori>=A:
    ans += 1 * A
    nokori -= A
else:
    ans += 1 * nokori
    nokori = 0

# calc b
if nokori>=B:
    nokori -= B
else:
    nokori = 0

# calc c
ans -= 1 * nokori

# output
print(ans)
