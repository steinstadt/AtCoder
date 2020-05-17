# Problem C - To Infinity

# input
S = list(input())
s_len = len(S)
K = int(input())

# initialization
pos = 0
while K>0:
    K -= 1
    if int(S[pos])==1:
        pos += 1
    else:
        K += 1
        break
    if pos==s_len:
        pos -= 1
        break

# output
if K==0:
    print(S[pos-1])
else:
    print(S[pos])
