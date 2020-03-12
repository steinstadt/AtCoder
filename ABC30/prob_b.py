# Problem B - 時計盤

# input process
n, m = map(int, input().split())

sa_1 = abs((n%12)*30 + 0.5*m - m*6)
sa_2 = 360-sa_1

ans = min(sa_1, sa_2)

print(ans)
