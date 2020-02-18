S = input()

ans_count = 0
b_count = 0
for s in S:
    if s=="B":
        b_count = b_count + 1
    if s=="W":
        ans_count = ans_count + b_count

print(ans_count)
