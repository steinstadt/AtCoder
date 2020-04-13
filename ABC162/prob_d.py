# Problem D - RGB Triplets

# input
N = int(input())
S = list(input())

# initialization
r_count = 0
g_count = 0
b_count = 0
exception_count = 0

# a, b, c count
for i in range(N):
    if S[i]=='R':
        r_count += 1
    elif S[i]=='G':
        g_count += 1
    elif S[i]=='B':
        b_count += 1
ans_1 = r_count * g_count * b_count

# exception count
for i in range(N-2):
    for j in range(i+1,N-1):
        k = 2 * j - i
        if k>=N:
            continue
        if not S[i]==S[j] and not S[j]==S[k] and not S[i]==S[k]:
            exception_count += 1

# output
ans = ans_1 - exception_count
print(ans)
