L, X, Y, S, D = map(int, input().split())

K = 0
# kの計算
if S<=D:
    if X<Y:
        K = min(D-S, S+L-D)
    else:
        K = D - S
else:
    if X<Y:
        K = min(D+L-S, S-D)
    else:
        K = D + L - S

ans = 0
if X<Y:
    ans = min(K/(X+Y), K/(Y-X))
else:
    ans = K/(X+Y)

print(ans)
