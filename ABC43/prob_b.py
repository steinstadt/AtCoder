# Problem B - バイナリックイージー
# input
s = list(input())

# initialization
result = []

# count
for c in s:
    if c=='B':
        if len(result)>0:
            result.pop(-1)
    elif c=='0':
        result.append(c)
    elif c=='1':
        result.append(c)

# output
print("".join(result))
