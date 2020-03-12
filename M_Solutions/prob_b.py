# Problem B - Sumo

# input process
S = input()

# initilization
win_num = 0
rest_num = 15 - len(S)

# count process
for s in S:
    if s=='o':
        win_num+=1

if win_num+rest_num>=8:
    print("YES")
else:
    print("NO")
