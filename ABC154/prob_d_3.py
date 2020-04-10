# Problem D - Dice in Line

# input
N, K = map(int, input().split())
p_list = list(map(int, input().split()))

# initialization
kitai_list = [0]*N
for i in range(N):
    p = p_list[i]
    p_sum = (1 + p)*p / 2
    p_ave = p_sum / p
    kitai_list[i] = p_ave
max_score = -1

# count
tmp = 0
for i in range(N):
    if i-K<0:
        tmp += kitai_list[i]
        max_score = max(max_score, tmp)
    else:
        tmp -= kitai_list[i-K]
        tmp += kitai_list[i]
        max_score = max(max_score, tmp)

# output
print(max_score)
