# Problem C - One Quadrillion and One Dalmatians

# input
N = int(input())

# initialization
alphabet = "zabcdefghijklmnopqrstuvwxy"
ans = ""

# check
if N>=1 and N<=26:
    ans = alphabet[N%26]
else:
    while N>0:
        if N%26==0:
            ans += alphabet[0]
            N = N // 26 -1
        else:
            ans += alphabet[N%26]
            N = N // 26

# output
ans = ans[::-1]
print(ans)
