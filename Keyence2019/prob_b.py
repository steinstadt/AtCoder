# Problem B - KEYENCE String

# input
s = input()
s_l = len(s)

# initialization
is_ok = False

# check
for i in range(s_l):
    for j in range(i, s_l):
        tmp_s = s[:i] + s[j:]
        if tmp_s=='keyence':
            is_ok = True
            break

# output
if is_ok:
    print("YES")
else:
    print("NO")
