# Problem A - ><

# input
S = input()

# initialization
N = len(S) + 1
num_list = [0]*N
ans = 0

# count
for i in range(N-1):
    if S[i]=='<':
        num_list[i+1] = num_list[i] + 1

for i in range(N-2, -1, -1):
    if S[i]=='>':
        num_list[i] = max(num_list[i], num_list[i+1]+1)

# output
ans = sum(num_list)
print(ans)
