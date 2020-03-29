# Problem - Count ABC

# input
N = int(input())
S = list(input())

# initialization
abc_count = 0

# abc count
for i in range(1, N-1):
    if S[i]=='B' and S[i-1]=='A' and S[i+1]=='C':
        abc_count += 1

# output
print(abc_count)
