# Problem A - Security

# input process
S = input()
S_len = len(S)

# initialization
is_ok = True

# count process
for i in range(S_len-1):
    if S[i]==S[i+1]:
        is_ok = False
        break

# output process
if is_ok:
    print("Good")
else:
    print("Bad")
