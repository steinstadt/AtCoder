# Problem A - Registration

# input
S = list(input())
T = list(input())

# initialization
is_ok = True

# check
for i in range(len(S)):
    if not S[i]==T[i]:
        is_ok = False
        break

# output
if is_ok:
    print("Yes")
else:
    print("No")
