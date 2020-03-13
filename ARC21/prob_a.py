# Problem A - DEAD END

# input process
A_list = []
for i in range(4):
    in_list = list(map(int, input().split()))
    A_list.append(in_list)

# initialization
is_ok = False

# search process
for i in range(4):
    for j in range(4):
        # right search
        if j+1<4:
            if A_list[i][j]==A_list[i][j+1]:
                is_ok = True
                break
        # left search
        if j-1>=0:
            if A_list[i][j]==A_list[i][j-1]:
                is_ok = True
                break

        # up search
        if i-1>=0:
            if A_list[i][j]==A_list[i-1][j]:
                is_ok = True
                break

        # down search
        if i+1<4:
            if A_list[i][j]==A_list[i+1][j]:
                is_ok = True
                break

# output process
if is_ok:
    print("CONTINUE")
else:
    print("GAMEOVER")
