# Problem A - 首席

# input process
N = int(input())
score_list = []
score_max = 0

# calc process
for i in range(N):
    a, b, c, d, e = map(int, input().split())
    score = a+b+c+d+(e*110/900)
    score_list.append(score)

score_max = max(score_list)
print(score_max)
