# Problem C - Collinewrity

# input
N = int(input())
points = []
for i in range(N):
    x, y = map(int, input().split())
    points.append([x, y])

# initialization
is_exists = False

# check
for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            line_1 = [points[j][0]-points[i][0], points[j][1]-points[i][1]]
            line_2 = [points[k][0]-points[j][0], points[k][1]-points[j][1]]
            tmp = line_1[0]*line_2[1] - line_1[1]*line_2[0]
            if tmp==0:
                is_exists = True

# output
if is_exists:
    print("Yes")
else:
    print("No")
