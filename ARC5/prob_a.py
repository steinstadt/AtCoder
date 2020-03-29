# Problem A - 大好き高橋君

# input
N = int(input())
w_list = input().split()

# initialization
word_count = 0

# word count
for i in range(N):
    w = list(w_list[i])

    if w[-1]=='.' or w[-1]==',':
        w.pop(-1);

    w = ''.join(w)

    if w=="TAKAHASHIKUN" or w=="Takahashikun" or w=="takahashikun":
        word_count += 1

# output
print(word_count)
