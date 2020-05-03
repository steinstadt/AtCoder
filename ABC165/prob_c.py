# Problem C - Many Requirements

# input
N, M, Q = map(int, input().split())
q_list = []
for i in range(Q):
    a, b, c, d = map(int, input().split())
    q_list.append([a, b, c, d])

# initialization
max_ans = 0

# dfs search
def dfs_score(a_list, p, n, max_ans):
    if p==N:
        tmp_score = 0
        for q in q_list:
            if a_list[q[1]-1]-a_list[q[0]-1]==q[2]:
                tmp_score += q[3]
        max_ans = max(max_ans, tmp_score)
    else:
        for i in range(n, M+1):
            a_list[p] = i
            max_ans = dfs_score(a_list, p+1, i, max_ans)
    return max_ans

# output
a_list = [0]*N
max_ans = dfs_score(a_list, 0, 1, max_ans)
print(max_ans)
