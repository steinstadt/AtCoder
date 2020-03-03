# Problem A - Colorful Transceivers

a, b, c, d = map(int, input().split())
d_1 = abs(a - c)
d_2 = abs(b - a)
d_3 = abs(c - b)

if d_1<=d or (d_2<=d and d_3<=d):
    print("Yes")
else:
    print("No")
