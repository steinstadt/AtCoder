# Problem B - AcCepted

# input process
S = input()

# initialization
is_a_ok = False
is_s_ok = False
s_len = len(S)
count = 0

# count process
for i in range(s_len):
    if i==0 and S[i]=='A':
        is_a_ok = True
        count += 1
        continue

    if i+1>=3 and (i+1)<=(s_len-1):
        if S[i]=='C':
            is_s_ok = True
            count += 1
            continue

    if S[i].isupper():
        count += 1

if count==2 and is_a_ok and is_s_ok:
    print("AC")
else:
    print("WA")
