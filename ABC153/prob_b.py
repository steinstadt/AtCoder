H, N = map(int, input().split())
A_list = list(map(int, input().split()))

for i in range(0,N):
    H = H - A_list[i]

if H<=0:
    print("Yes")
else:
    print("No")
