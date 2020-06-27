# Problem B - Crane and Turtle

# input
X, Y = map(int, input().split())

# initialization
is_ok = False

# count
for a in range(X+1):
    b = X - a
    if (2*a + 4*b)==Y:
        is_ok = True

# output
if is_ok:
    print("Yes")
else:
    print("No")
