# Problem C - パズルのお手伝い (順列による解)

from itertools import permutations

# input
board = []
for i in range(8):
    board.append(list(input()))

# initialization
perm_list = []
for v in permutations(list(range(1, 9))):
    perm_list.append(v)
vertical = [True] * 9
major = [True] * 17
minor = [True] * 16
ans_list = []
is_ok = True

# search process
for p in perm_list:
    tmp_ok = True
    # clear
    vertical = [True] * 9
    major = [True] * 17
    minor = [True] * 16

    for i in range(8):
        if "Q" in board[i]:
            if board[i][p[i]-1]=="Q":
                if vertical[p[i]] and major[i+1 + p[i]] and minor[i+1 - p[i] + 8]:
                    vertical[p[i]] = False
                    major[i+1 + p[i]] = False
                    minor[i+1 - p[i] + 8] = False
                else:
                    tmp_ok = False
                    break
                continue
            else:
                tmp_ok = False
                break
        else:
            if vertical[p[i]] and major[i+1 + p[i]] and minor[i+1 - p[i] + 8]:
                vertical[p[i]] = False
                major[i+1 + p[i]] = False
                minor[i+1 - p[i] + 8] = False
            else:
                tmp_ok = False
                break

    if tmp_ok:
        ans_list.append(p)

# output
if len(ans_list)>0:
    p = ans_list[0]
    for i in range(8):
        p_num = p[i]
        for j in range(8):
            if j==p_num-1:
                print("Q", end="")
            else:
                print(".", end="")
        print()
else:
    print("No Answer")
