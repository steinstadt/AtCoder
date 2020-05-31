# Problem C - Many Requirements

# input
N, M, Q = map(int, input().split())
rules = []
for i in range(Q):
    a, b, c, d = map(int, input().split())
    rules.append([a, b, c, d])

# initialization
ans_score = 0
num_list = []

# calc func
def dfs(num_list, keta, c):
    global ans_score
    global N
    if keta==N:
        # check
        tmp = 0
        for r in rules:
            if num_list[r[1]-1]-num_list[r[0]-1]==r[2]:
                tmp += r[3]
        ans_score = max(ans_score, tmp)
        return

    for n in range(c, M+1):
        num_list.append(n)
        dfs(num_list, keta+1, n)
        num_list.pop(-1)

# calc
dfs(num_list, 0, 1)

# output
print(ans_score)
