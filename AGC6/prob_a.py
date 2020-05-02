# Problem A - Prefix and Suffix

# input
N = int(input())
s = list(input())
t = list(input())

# initialization
ans_str = 't'*3*N

# count
for i in range(N+1):
    is_ok = True
    tmp_str = ['']*2*N
    for j in range(N):
        tmp_str[j] = s[j]
    for j in range(N):
        if tmp_str[i+j]=='':
            tmp_str[i+j] = t[j]
        elif not tmp_str[i+j]==t[j]:
            is_ok = False
            break
    if is_ok:
        if len(tmp_str)<len(ans_str):
            ans_str = "".join(tmp_str)

# output
print(len(ans_str))
