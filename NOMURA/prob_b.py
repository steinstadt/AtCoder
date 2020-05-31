# Problem B - Postdocs

# input
T = list(input())
T_len = len(T)

# swap
for i in range(T_len):
    if T[i]=='?':
        T[i] = 'D'

# output
print("".join(T))
