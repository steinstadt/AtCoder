# input
N = int(input())
S = list(input())

# initialization
ans = 0

for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            if not S[i]==S[j] and not S[i]==S[k] and not S[k]==S[j] and not j-i==k-j:
                ans += 1

# output
print(ans)
