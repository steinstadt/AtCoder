# Problem C - Rectangle Cutting

# input
W, H, x, y = map(int, input().split())

# initialization
ans = (W * H) / 2
is_ok = (x*2==W) and (y*2==H)

if is_ok:
    print("%f %d"%(ans, 1))
else:
    print("%f %d"%(ans, 0))
