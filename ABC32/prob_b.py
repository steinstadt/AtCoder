# Problem B - 高橋君とパスワード

# input process
s = input()
k = int(input())

# initialization
s_length = len(s)
word_dic = {}

# kによって条件分岐
if k==0 or k>s_length:
    print(0)
else:
    for i in range(s_length-k+1):
        s_tmp = s[i:i+k] # string slice
        # dictionary process
        if not s_tmp in word_dic:
            word_dic[s_tmp] = 1
    # output process
    print(len(word_dic))
