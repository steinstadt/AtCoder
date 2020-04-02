# Problem A - Eating Symbols Easy

# input
S = list(input())
S_len = len(S)

# initialization
ans = 0

# count
for i in range(S_len):
    if S[i]=='+':
        ans += 1
    else:
        ans -= 1

# output
print(ans)
