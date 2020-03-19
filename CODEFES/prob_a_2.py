# Problem A - CF

# input process
S = input()

# initialization
is_ok_1 = False
is_ok_2 = False

# str count process
for s in S:
    if s=="C":
        is_ok_1 = True

    if is_ok_1 and s=="F":
        is_ok_2 = True

# output process
if is_ok_2:
    print("Yes")
else:
    print("No")
