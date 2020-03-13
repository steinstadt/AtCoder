# Problem B - Increment Decrement

# input process
N = int(input())
S = input()

# initialization
max_score = 0
tmp = 0

# count process
for i in range(N):
    if S[i]=='I':
        tmp += 1
    else:
        tmp -= 1
    max_score = max(max_score, tmp)

print(max_score)
