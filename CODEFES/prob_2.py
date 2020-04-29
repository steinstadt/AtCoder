# Problem C - 旅館

# input
N, M = map(int, input().split())
a_rooms = list(map(int, input().split()))
b_peoples = list(map(int, input().split()))

# initialization
a_rooms = sorted(a_rooms, reverse=True)
b_peoples = sorted(b_peoples, reverse=True)

# room check
if N<M:
    print("NO")
else:
    is_ok = True
    for i in range(M):
        a = a_rooms[i]
        b = b_peoples[i]
        if b>a:
            is_ok = False
            break
    if is_ok:
        print("YES")
    else:
        print("NO")
