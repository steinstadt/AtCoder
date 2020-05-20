# Problem Triple Dots
# input
K = int(input())
S = list(input())
s_len = len(S)

if s_len<=K:
    print("".join(S))
else:
    tmp = S[:K]
    ans = "".join(tmp) + "..."
    print(ans)
