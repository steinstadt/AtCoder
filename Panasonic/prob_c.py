# Problem C - Sqrt Inequality

# input
a, b, c = map(int, input().split())

# check
is_ok = (a * b)*4 < (c - a - b)**2 and (c-a-b)>0

# output
if is_ok:
    print("Yes")
else:
    print("No")
