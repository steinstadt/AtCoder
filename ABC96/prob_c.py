# Problem C - Grid Repainting

# input process
H, W = map(int, input().split())
s_list = [[0]*W for i in range(H)]
for i in range(H):
    tmp = input()
    for j in range(W):
        s_list[i][j] = tmp[j]

# search process
is_ok = True
for i in range(H):
    for j in range(W):
        if s_list[i][j]==".":
            continue
        # right process
        if j+1<W:
            if s_list[i][j+1]=="#":
                continue
        # left process
        if j-1>=0:
            if s_list[i][j-1]=="#":
                continue
        # down process
        if i+1<H:
            if s_list[i+1][j]=="#":
                continue
        # up process
        if i-1>=0:
            if s_list[i-1][j]=="#":
                continue
        # stop process
        is_ok = False
        break

if is_ok:
    print("Yes")
else:
    print("No")
