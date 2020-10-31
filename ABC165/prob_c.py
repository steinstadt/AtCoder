# Problem C - Many Requirements

# input
n, m, q = map(int, input().split())
pattern_list = []
for i in range(q):
    a, b, c, d = map(int, input().split())
    pattern_list.append([a, b, c, d])

# initialization
a_list = [0] * n
ans_point = 0

def dfs(a_c, n_c):
    global a_list
    global n
    global m
    global ans_point

    if n_c-1==n:
        tmp_point = 0
        for p in pattern_list:
            if a_list[p[1]-1]-a_list[p[0]-1]==p[2]:
                tmp_point += p[3]
        ans_point = max(ans_point, tmp_point)
    else:
        for i in range(a_c, m+1):
            a_list[n_c-1] = i
            dfs(i, n_c+1)

# calc
dfs(1, 1)

# output
print(ans_point)
