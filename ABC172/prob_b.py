# Problem B - Minor Change

# input
S = list(input())
T = list(input())

# initialization
str_len = len(S)
count = 0

# count
for i in range(str_len):
    if S[i]!=T[i]:
        count += 1

# output
print(count)
