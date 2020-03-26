# Problem B - 高橋くんと文字列圧縮

# input
s = list(input())

# initialization
c = s[0]
s_count = 1

# count
for i in range(1, len(s)):
    if s[i]==c:
        s_count += 1
    else:
        print("%s%d"%(c, s_count), end="")
        c = s[i]
        s_count = 1
# last output
print("%s%d"%(c, s_count), end="")
print()
