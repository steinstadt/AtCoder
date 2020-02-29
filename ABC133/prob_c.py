L, R = map(int, input().split())

count_limit = 0 # count limit is 2019
min_num = 2020
for i in range(L, R+1):

    count_limit_j = 0
    for j in range(i+1, R+1):
        min_num = min(min_num, (i*j)%2019)
        count_limit_j = count_limit_j + 1
        if count_limit_j>2020:
            break

    # limit process
    count_limit = count_limit + 1
    if count_limit>2020:
        break

print(min_num)
