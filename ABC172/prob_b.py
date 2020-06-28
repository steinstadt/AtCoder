# Problem B - Minor Change

# input
S = list(input())
T = list(input())

# initialization
count = 0
s_len = len(S)

# count
for i in range(s_len):
    if S[i]!=T[i]:
        count += 1

# output
print(count)
