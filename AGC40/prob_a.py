# Problem A - ><

S = input()
N = len(S) + 1

num_list = [0]*N
ans_sum = 0

# < process
for i in range(len(S)):
    s = S[i]
    if s=="<":
        num_list[i+1] = num_list[i] + 1

# > process
for i in range(len(S)-1, -1, -1):
    s = S[i]
    if s==">":
        num_list[i] = max(num_list[i], num_list[i+1]+1)

# sum process
for i in range(N):
    ans_sum = ans_sum + num_list[i]

print(ans_sum)
