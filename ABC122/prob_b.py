# Problem B - ATCoder

# input
S = list(input())

# initialization
max_count = 0
atgc_list = ['A', 'T', 'G', 'C']

# count
tmp = 0
for i in range(len(S)):
    if S[i] in atgc_list:
        tmp += 1
    else:
        max_count = max(max_count, tmp)
        tmp = 0
max_count = max(max_count, tmp)
# output
print(max_count)
