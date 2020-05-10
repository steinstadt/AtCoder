# Problem D - I hate Factorization

# input
X = int(input())

# initialization
ans_list = [0, 0]

# count
for a in range(-500, 501):
    for b in range(-500, 501):
        if a**5-b**5==X:
            ans_list[0] = a
            ans_list[1] = b
            break

# output
print(" ".join(map(str, ans_list)))
