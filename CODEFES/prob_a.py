# Snuke's favorite YAKINIKU

# input process
S = input()

# initialization
s_len = len(S)

# output process
if s_len<4:
    print("No")
elif S[:4]=="YAKI":
    print("Yes")
else:
    print("No")
