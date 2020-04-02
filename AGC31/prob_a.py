# Problem A - Colorful Subsequence

# input
N = int(input())
S = list(input())

# initialization
word_dic = {}
ans = 1
INF = 10**9 + 7

# word count
for s in S:
    if not s in word_dic:
        word_dic[s] = 1
    else:
        word_dic[s] += 1

# output
for w in word_dic:
    tmp = word_dic[w]
    ans = (ans * (tmp + 1))%INF
ans -= 1
print(ans % INF)
