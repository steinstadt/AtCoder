# Problem Triple Dots

# input
K = int(input())
S = input()

# output
if len(S)<=K:
    print(S)
else:
    ans = S[:K] + '...'
    print(ans)
