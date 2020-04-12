# Problem C - Bugged

# input
N = int(input())

# initialization
max_score = 0
score_list = []
for i in range(N):
    tmp = int(input())
    score_list.append(tmp)
score_list = sorted(score_list, reverse=True)

# score update
min_score = 10**4 + 1
for score in score_list:
    max_score += score
    if score%10!=0 and min_score>score:
        min_score = score

# output
ans = max_score
if max_score%10==0:
    ans = max(0, max_score-min_score)
print(ans)
