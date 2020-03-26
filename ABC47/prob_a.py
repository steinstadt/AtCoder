# Problem A - キャンディーと2人の子供

# input
a, b, c = map(int, input().split())

# initialization
is_ok = False

# check
if a+b==c:
    is_ok = True
elif a+c==b:
    is_ok = True
elif b+c==a:
    is_ok = True

# output
if is_ok:
    print("Yes")
else:
    print("No")
