# Problem C - Many Requirements

# input
N, M, Q = map(int, input().split())
query = []
for i in range(Q):
    a, b, c, d = map(int, input().split())
    query.append([a, b, c, d])

# dfs search
def dfs(nums, score, ini_num, keta):
    if keta==N+1:
        tmp_score = 0
        for q in query:
            if nums[q[1]]-nums[q[0]]==q[2]:
                tmp_score += q[3]
        score = max(score, tmp_score)
    else:
        for i in range(ini_num, M+1):
            nums[keta] = ini_num
            score = max(score, dfs(nums, score, i, keta+1))
    return score

# initialization
nums = [0]*(N+1)
max_score = 0

max_score = dfs(nums, 0, 1, 1)
# output
print(max_score)
