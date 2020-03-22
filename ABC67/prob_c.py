# Problem C - Splitting Pile

# input
n = int(input())
a_list = list(map(int, input().split()))

# initialization
min_cost = 10**15
arai_score = sum(a_list)
snuke_score = 0

# 累積和による解
for i in range(len(a_list)-1):
    a = a_list[i]
    snuke_score += a
    arai_score = arai_score - a
    min_cost = min(min_cost, abs(snuke_score - arai_score))

# output
print(min_cost)
