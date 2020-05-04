# Problem D - I hate Factorization

# input
X = int(input())

# count
ans = [0, 0]
for a in range(-500, 500):
    for b in range(-500, 500):
        if a**5 - b**5 == X:
            ans[0] = a
            ans[1] = b
            break

# output
print(" ".join(list(map(str , ans))))
